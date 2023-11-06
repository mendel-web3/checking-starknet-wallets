SHUFFLE_WALLETS = True
SLEEP_AFTER_WALLET_CHACKING = 0

API_URL = 'https://voyager.online/api'
ETH_PRICE_URL = 'https://min-api.cryptocompare.com/data/price?fsym=ETH&tsyms=USD'
FILTER_SYMBOL = ['ETH', 'USDT', 'USDC', 'DAI']
ZERO_WALLET = '0x0000000000000000000000000000000000000000000000000000000000000000'

COLUMNS = [
    'Wallet',
    'Total',
    'ETH',
    'USDT',
    'USDC',
    'DAI',
    'first_tx_date',
    'last_tx_date',
    'D',
    'W',
    'M',
    'fee',
    'volume',
    'txs',
    'unique_contracts',
    'myswap',
    'JediSwap',
    '10kswap'
]

DEFAULT_STATS = {
    'balance': {
        'Total': 0,
        'ETH': 0,
        'USDC': 0,
        'USDT': 0,
        'DAI': 0
    },
    'date': {
        'first_tx_date': 0,
        'last_tx_date': 0,
        'unique_days': 0,
        'unique_weeks': 0,
        'unique_months': 0
    },
    'fee': 0,
    'volume': 0,
    'txs': 0,
    'unique_contracts': 0,
    'protocols': {
        'myswap': 0,
        'JediSwap': 0,
        '10kswap': 0
    }
}

PROTOCOLS_DATE = {
    "0x010884171baf1914edc28d7afb619b40a4051cfae78a094a55d230f19e944a28": {
        "name": "myswap",
        "url": "https://www.myswap.xyz/"
    },
    "0x045e7131d776dddc137e30bdd490b431c7144677e97bf9369f629ed8d3fb7dd6": {
        "name": "JediSwap",
        "url": "https://app.jediswap.xyz/"
    },
    "0x04d0390b777b424e43839cd1e744799f3de6c176c7e32c1812a41dbd9c19db6a": {
        "name": "JediSwap",
        "url": "https://app.jediswap.xyz/"
    },
    "0x07e2a13b40fc1119ec55e0bcf9428eedaa581ab3c924561ad4e955f95da63138": {
        "name": "JediSwap",
        "url": "https://app.jediswap.xyz/"
    },
    "0x070cda8400d7b1ee9e21f7194d320b9ad9c7a2b27e0d15a5a9967b9fefe10c76": {
        "name": "JediSwap",
        "url": "https://app.jediswap.xyz/"
    },
    "0x02b3030c04e9c920bd66c6a8dc209717bbefa1ea5f8bc8ebabd639e5a4766502": {
        "name": "JediSwap",
        "url": "https://app.jediswap.xyz/"
    },
    "0x039c183c8e5a2df130eefa6fbaa3b8aad89b29891f6272cb0c90deaa93ec6315": {
        "name": "JediSwap",
        "url": "https://app.jediswap.xyz/"
    },
    "0x02a6e0ecda844736c4803a385fb1372eff458c365d2325c7d4e08032c7a908f3": {
        "name": "10kswap",
        "url": "https://10kswap.com/"
    },
    "0x000023c72abdf49dffc85ae3ede714f2168ad384cc67d08524732acea90df325": {
        "name": "10kswap",
        "url": "https://10kswap.com/"
    },
    "0x05900cfa2b50d53b097cb305d54e249e31f24f881885aae5639b0cd6af4ed298": {
        "name": "10kswap",
        "url": "https://10kswap.com/"
    },
    "0x017e9e62c04b50800d7c59454754fe31a2193c9c3c6c92c093f2ab0faadf8c87": {
        "name": "10kswap",
        "url": "https://10kswap.com/"
    }

}
