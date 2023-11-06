from checkers.starknet.get_data import StarkNetData
from config import DEFAULT_STATS, FILTER_SYMBOL, PROTOCOLS_DATE, ZERO_WALLET
from datetime import datetime


class WalletData():
    def __init__(self, wallet: str, proxy: str, user_agent: str):
        self.wallet_data = StarkNetData(wallet=wallet,
                                        proxy=proxy,
                                        user_agent=user_agent)
        self.wallet = wallet
        self.stats = {
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

        self.get_balance_metrics()
        self.get_txns_metrics()
        self.get_transfers_metrics()

    def get_balance_metrics(self):
        for item in self.wallet_data.balance:
            if (item['symbol'] in FILTER_SYMBOL):
                if (item['symbol'] == 'ETH'):
                    self.stats['balance'][item['symbol']] += int(item['balance']) / 10 ** item[
                        'decimals'] * self.wallet_data.ethPrice
                else:
                    self.stats['balance'][item['symbol']] += int(item['balance']) / 10 ** item['decimals']
        self.stats['balance']['Total'] = (self.stats['balance']['ETH']
                                          + self.stats['balance']['USDC']
                                          + self.stats['balance']['USDT']
                                          + self.stats['balance']['DAI'])

    def get_txns_metrics(self):
        self.stats['txs'] = len(self.wallet_data.txns)
        if len(self.wallet_data.txns):
            unique_days = []
            unique_weeks = []
            unique_months = []
            for item in self.wallet_data.txns:
                unique_days.append(datetime.fromtimestamp(item['timestamp']).date())
                unique_weeks.append(str(datetime.fromtimestamp(item['timestamp']).date().isocalendar().year)
                                    + 'w'
                                    + str(datetime.fromtimestamp(item['timestamp']).date().isocalendar().week))
                unique_months.append(str(datetime.fromtimestamp(item['timestamp']).date().year)
                                     + 'm'
                                     + str(datetime.fromtimestamp(item['timestamp']).date().month))
                self.stats['fee'] += int(item['actual_fee']) / 10 ** 18 * self.wallet_data.ethPrice
            self.stats['date']['unique_days'] = len(set(unique_days))
            self.stats['date']['unique_weeks'] = len(set(unique_weeks))
            self.stats['date']['unique_months'] = len(set(unique_months))
            self.stats['date']['first_tx_date'] = str(min(unique_days))
            self.stats['date']['last_tx_date'] = str(max(unique_days))

    def get_transfers_metrics(self):
        if len(self.wallet_data.transfers):
            unique_contracts = []
            for item in self.wallet_data.transfers:
                if (item['token_symbol'] == 'ETH'):
                    self.stats['volume'] += float(item['transfer_value']) * self.wallet_data.ethPrice
                elif (item['token_symbol'] in FILTER_SYMBOL):
                    self.stats['volume'] += float(item['transfer_value'])

                if (item['transfer_to'].lower() == self.wallet.lower() and item[
                    'transfer_from'].lower() != ZERO_WALLET):
                    unique_contracts.append(item['transfer_from'])
                if (item['transfer_from'].lower() == self.wallet.lower() and item[
                    'transfer_to'].lower() != ZERO_WALLET):
                    unique_contracts.append(item['transfer_to'])
                    if (item['transfer_to'] in PROTOCOLS_DATE):
                        self.stats['protocols'][PROTOCOLS_DATE[item['transfer_to']]['name']] += 1

            self.stats['unique_contracts'] = len(set(unique_contracts))
