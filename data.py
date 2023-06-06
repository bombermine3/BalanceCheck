import json


with open(f"erc20.json", "r") as file:
    ERC20_ABI = json.load(file)

RPC = {
    'ethereum'      : {'rpc': 'https://rpc.ankr.com/eth', 'scan': 'https://etherscan.io/tx', 'token': 'ETH', 'chain_id': 1},
    'optimism'      : {'rpc': 'https://rpc.ankr.com/optimism', 'scan': 'https://optimistic.etherscan.io/tx', 'token': 'ETH', 'chain_id': 10},
    'bsc'           : {'rpc': 'https://rpc.ankr.com/bsc', 'scan': 'https://bscscan.com/tx', 'token': 'BNB', 'chain_id': 56},
    'polygon'       : {'rpc': 'https://rpc.ankr.com/polygon', 'scan': 'https://polygonscan.com/tx', 'token': 'MATIC', 'chain_id': 137},
    'polygon_zkevm' : {'rpc': 'https://zkevm-rpc.com', 'scan': 'https://zkevm.polygonscan.com/tx', 'token': 'ETH', 'chain_id': 1101},
    'arbitrum'      : {'rpc': 'https://rpc.ankr.com/arbitrum', 'scan': 'https://arbiscan.io/tx', 'token': 'ETH', 'chain_id': 42161},
    'avalanche'     : {'rpc': 'https://rpc.ankr.com/avalanche', 'scan': 'https://snowtrace.io/tx', 'token': 'AVAX', 'chain_id': 43114},
    'fantom'        : {'rpc': 'https://rpc.ankr.com/fantom', 'scan': 'https://ftmscan.com/tx', 'token': 'FTM', 'chain_id': 250},
    'nova'          : {'rpc': 'https://nova.arbitrum.io/rpc', 'scan': 'https://nova.arbiscan.io/tx', 'token': 'ETH', 'chain_id': 42170},
    'zksync'        : {'rpc': 'https://mainnet.era.zksync.io', 'scan': 'https://explorer.zksync.io/tx', 'token': 'ETH', 'chain_id': 324},
}

RPC = {
    'ethereum'      : {'rpc': 'https://eth.llamarpc.com	', 'scan': 'https://etherscan.io/tx', 'token': 'ETH', 'chain_id': 1},
    'optimism'      : {'rpc': 'https://optimism.blockpi.network/v1/rpc/public', 'scan': 'https://optimistic.etherscan.io/tx', 'token': 'ETH', 'chain_id': 10},
    'bsc'           : {'rpc': 'https://bsc-dataseed3.binance.org', 'scan': 'https://bscscan.com/tx', 'token': 'BNB', 'chain_id': 56},
    'polygon'       : {'rpc': 'https://polygon.llamarpc.com', 'scan': 'https://polygonscan.com/tx', 'token': 'MATIC', 'chain_id': 137},
    'polygon_zkevm' : {'rpc': 'https://zkevm-rpc.com', 'scan': 'https://zkevm.polygonscan.com/tx', 'token': 'ETH', 'chain_id': 1101},
    'arbitrum'      : {'rpc': 'https://arb1.arbitrum.io/rpc', 'scan': 'https://arbiscan.io/tx', 'token': 'ETH', 'chain_id': 42161},
    'avalanche'     : {'rpc': 'https://api.avax.network/ext/bc/C/rpc', 'scan': 'https://snowtrace.io/tx', 'token': 'AVAX', 'chain_id': 43114},
    'fantom'        : {'rpc': 'https://rpc.ankr.com/fantom', 'scan': 'https://ftmscan.com/tx', 'token': 'FTM', 'chain_id': 250},
    'nova'          : {'rpc': 'https://nova.arbitrum.io/rpc', 'scan': 'https://nova.arbiscan.io/tx', 'token': 'ETH', 'chain_id': 42170},
    'zksync'        : {'rpc': 'https://mainnet.era.zksync.io', 'scan': 'https://explorer.zksync.io/tx', 'token': 'ETH', 'chain_id': 324},
}

TOKENS = {
    'ethereum': {
        'ETH': '',
        'USDT': '0xdac17f958d2ee523a2206206994597c13d831ec7',
        'USDC': '0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48',
    },
    'bsc': {
        'BNB': '',
        'USDT': '0x55d398326f99059ff775485246999027b3197955',
        'USDC': '0x8ac76a51cc950d9822d68b83fe1ad97b32cd580d',
    },
    'arbitrum': {
        'ETH': '',
        'USDT': '0xFd086bC7CD5C481DCC9C85ebE478A1C0b69FCbb9',
        'USDC': '0xFF970A61A04b1cA14834A43f5dE4533eBDDB5CC8',
    },
    'optimism': {
        'ETH': '',
        'USDT': '0x94b008aa00579c1307b0ef2c499ad98a8ce58e58',
        'USDC': '0x7f5c764cbc14f9669b88837ca1490cca17c31607',
    },
    'polygon': {
        'MATIC': '',
        'USDT': '0xc2132d05d31c914a87c6611c10748aeb04b58e8f',
        'USDC': '0x2791bca1f2de4661ed88a30c99a7a9449aa84174',
    },
    'avalanche': {
        'AVAX': '',
        'USDT': '0x9702230A8Ea53601f5cD2dc00fDBc13d4dF4A8c7',
        'USDC': '0xB97EF9Ef8734C71904D8002F8b6Bc66Dd9c48a6E',
    },
    #'zksync': {
    #    'ETH': '',
    #    'USDC': '0x3355df6d4c9c3035724fd0e3914de96a5a83aaf4',
    #},
    # 'nova': [
    #     'ETH': '',
    #     ],
    #'fantom': {
    #    'FTM': '',
    #    'USDT': '0x049d68029688eabf473097a2fc38ef61633a3c7a',
    #    'USDC': '0x04068DA6C83AFCFA0e13ba15A6696662335D5B75',
    #},
}

STABLECOINS = ['USDT', 'USDC', 'DAI']