import sys
import urllib
import json
import asyncio
from web3 import AsyncWeb3
import xlsxwriter
from loguru import logger

from data import RPC, TOKENS, ERC20_ABI, STABLECOINS
import config


BALANCES = {}

def get_prices():
    tickers = []
    for chain in TOKENS:
        for ticker in TOKENS[chain]:
            if ticker not in tickers:
                tickers.append(ticker)
    
    tickers = ','.join(tickers)
    prices = json.loads(urllib.request.urlopen(f'https://min-api.cryptocompare.com/data/pricemulti?fsyms={tickers}&tsyms=USD').read())
    
    result = {}
    for ticker in prices:
        result[ticker] = prices[ticker]['USD']
        
    return result
                
async def prepare_endpoint(wallet, rpc):
    while True:
        try:
            return AsyncWeb3(AsyncWeb3.AsyncHTTPProvider(rpc))
        except Exception as error:
            logger.debug(f'Retrying: {wallet}: {error}')
            await asyncio.sleep(5)

async def get_balance(wallet, web3, contract_address):
    try:
        if contract_address == "":
            balance = await web3.eth.get_balance(AsyncWeb3.to_checksum_address(wallet))
            return float(balance / 10 ** 18)

        contract = web3.eth.contract(address=AsyncWeb3.to_checksum_address(contract_address), abi=ERC20_ABI)
        token_decimals = await contract.functions.decimals().call()
        balance = await contract.functions.balanceOf(AsyncWeb3.to_checksum_address(wallet)).call()
        return float(balance / 10 ** token_decimals)
    except Exception as error:
        logger.debug(f'Retrying: {wallet}: {error}')
        await asyncio.sleep(5)
        return await get_balance(wallet, web3, contract_address)
    
async def get_tx_count(wallet, web3):
    try:
        return await web3.eth.get_transaction_count(wallet)
    except Exception as error:
        logger.debug(f'Retrying: {wallet}: {error}')
        await asyncio.sleep(5)
        return await get_tx_count(wallet, web3)

async def worker(wallet):
    for chain in TOKENS:
        web3 = await prepare_endpoint(wallet, RPC[chain]['rpc'])
        BALANCES[wallet]['chains'][chain] = {
            'TX': await get_tx_count(wallet, web3)
        }
        for token in TOKENS[chain]:
            balance = await get_balance(wallet, web3, TOKENS[chain][token])
            amount = balance * PRICES[token]
            warn = False
            if TOKENS[chain][token] == "":
                warn = True
            BALANCES[wallet]['chains'][chain][token] = {
                'balance': balance,
                'amount': amount,
                'warn': warn
            }                
            
async def main(wallets):
    tasks = [worker(wallet) for wallet in BALANCES]
    await asyncio.gather(*tasks)
    
def write_xlsx(balances):
    workbook = xlsxwriter.Workbook("balances.xlsx")
    worksheet = workbook.add_worksheet()
    
    merge_format = workbook.add_format({
        'bold':     True,
        'border':   6,
        'align':    'center',
        'valign':   'vcenter',
    })
    bold_format = workbook.add_format({
        'bold':     True,
    })
    warning_format = workbook.add_format({
        'bg_color': 'red'
    })
    wealth_format = workbook.add_format({
        'bg_color': 'green'
    })
    empty_format = workbook.add_format()
        
    worksheet.set_column("A:A", 15)
    worksheet.set_column("B:B", 42)
    
    worksheet.merge_range("A1:A2", "Alias", merge_format)
    worksheet.merge_range("B1:B2", "Wallet", merge_format)
    
    col = 2
    for chain in TOKENS:
        worksheet.merge_range(0, col, 0, col + len(TOKENS[chain]), chain, merge_format)
        worksheet.write(1, col, "TX")
        col += 1
        for token in TOKENS[chain]:
            worksheet.write(1, col, token)
            col += 1
    
    worksheet.freeze_panes(2, 2)
    
    row = 2        
    for wallet in balances:
        worksheet.write(row, 0, balances[wallet]['name'], bold_format)
        worksheet.write(row, 1, wallet, bold_format)

        col = 2
        chains = balances[wallet]['chains']
        for chain in chains:
            for token in chains[chain]:
                if token == 'TX':
                    worksheet.write(row, col, chains[chain][token])
                else:
                    balance = '{:.4f}'.format(chains[chain][token]['balance'])
                    amount = '{:.2f}'.format(chains[chain][token]['amount'])
                    format = empty_format
                    if chains[chain][token]['warn'] & (chains[chain][token]['amount'] < config.min_worth_threshold):
                        format = warning_format
                    if chains[chain][token]['amount'] > config.max_worth_threshold:
                        format = wealth_format
                    worksheet.write(row, col, balance, format)
                    if token not in STABLECOINS and chains[chain][token]['amount'] > 0:
                        worksheet.write_comment(row, col, f'{amount} USD')
                col += 1
        row += 1
        
    worksheet.write(row + 1, 0, 'Donate:')
    worksheet.write(row + 1, 1, '0x09505f2B29062dE4E91E0053490B8f6c3f7D29Fc')
        
    workbook.close()


logger.remove()
logger.add(sys.stderr, level=config.log_level)
PRICES = get_prices()

lines = 0
with open("wallets.csv") as file:
    for wallet in file:
        lines += 1
        wallet = wallet.strip(' \n')
        if wallet[0] == "#":
            continue
        
        wallet_name, wallet = wallet.split(',')
        BALANCES[wallet] = {
            'name': wallet_name,
            'chains': {}
        }
        
print(f'{lines} wallets found')

asyncio.run(main(BALANCES))

print("Writing balances.xlsx")
write_xlsx(BALANCES)