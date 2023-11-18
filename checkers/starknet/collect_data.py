from checkers.starknet.transform_data import WalletData
from config import COLUMNS
import pandas as pd


class WalletStat():
    def __init__(self, wallet: str, user_agent: str, proxy: str = None):
        self.wallet_data = WalletData(wallet=wallet,
                                      proxy=proxy,
                                      user_agent=user_agent)
        self.wallet = wallet
        self.data = 0
        self.collect_data()

    def collect_data(self):
        stats = [
            self.wallet,
            self.wallet_data.stats['balance']['Total'],
            self.wallet_data.stats['balance']['ETH'],
            self.wallet_data.stats['balance']['USDT'],
            self.wallet_data.stats['balance']['USDC'],
            self.wallet_data.stats['balance']['DAI'],
            self.wallet_data.stats['date']['first_tx_date'],
            self.wallet_data.stats['date']['last_tx_date'],
            self.wallet_data.stats['date']['unique_days'],
            self.wallet_data.stats['date']['unique_weeks'],
            self.wallet_data.stats['date']['unique_months'],
            self.wallet_data.stats['fee'],
            self.wallet_data.stats['volume'],
            self.wallet_data.stats['txs'],
            self.wallet_data.stats['unique_contracts'],
            self.wallet_data.stats['protocols']['myswap'],
            self.wallet_data.stats['protocols']['JediSwap'],
            self.wallet_data.stats['protocols']['10kswap'],
            self.wallet_data.stats['protocols']['sithswap'],
            self.wallet_data.stats['protocols']['avnu']
        ]
        self.data = pd.DataFrame(data=stats, index=COLUMNS).T
