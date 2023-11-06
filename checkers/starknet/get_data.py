import requests
import json
from config import API_URL, ETH_PRICE_URL


class StarkNetData():
    def __init__(self, wallet: str, proxy: str, user_agent: str):
        self.wallet = wallet
        self.header = {'user-agent': user_agent}
        self.proxy = {'http': proxy,
                      'https': proxy}
        self.balance = []
        self.transfers = []
        self.txns = []
        self.ethPrice = 0
        self.transfer_timeout = 5000
        self.transfer_params = {
            'p': 1,
            'ps': 100
        }
        self.txns_timeout = 5000
        self.txns_params = {
            'to': self.wallet,
            'p': 1,
            'ps': 100
        }
        self.get_balance_data()
        self.get_transfers_data()
        self.get_txns_data()
        self.get_eth_price()

    def get_eth_price(self):
        html = requests.get(url=ETH_PRICE_URL,
                            proxies=self.proxy,
                            headers=self.header)

        if (html.status_code != 200):
            print(f'Error {html.status_code}: def get_eth_price')

        self.ethPrice = json.loads(html.text)['USD']

    def get_balance_data(self):
        url = API_URL + '/contract/' + self.wallet + '/balances'
        html = requests.get(url=url,
                            proxies=self.proxy,
                            headers=self.header)
        if (html.status_code != 200):
            print(f'Error {html.status_code}: def get_balance')
        self.balance = json.loads(html.text)

    def get_transfers_data(self):
        url = API_URL + '/contract/' + self.wallet + '/transfers'

        isAllTransfersCollected = False
        while (not isAllTransfersCollected):
            html = requests.get(url=url,
                                params=self.transfer_params,
                                timeout=self.transfer_timeout,
                                proxies=self.proxy,
                                headers=self.header)
            if (html.status_code != 200):
                print(f'Error {html.status_code}: def get_transfers')

            data = json.loads(html.text)
            last_page = data['lastPage']

            for item in data['items']:
                self.transfers.append(item)

            if (self.transfer_params['p'] == last_page):
                isAllTransfersCollected = True
            else:
                self.transfer_params['p'] += 1

    def get_txns_data(self):
        url = API_URL + '/txns'

        isAllTxCollected = False
        while (not isAllTxCollected):
            html = requests.get(url=url,
                                params=self.txns_params,
                                timeout=self.txns_timeout,
                                proxies=self.proxy,
                                headers=self.header)
            if (html.status_code != 200):
                print(f'Error {html.status_code}: def get_transactions')

            data = json.loads(html.text)
            last_page = data['lastPage']

            for item in data['items']:
                self.txns.append(item)

            if (self.txns_params['p'] == last_page):
                isAllTxCollected = True
            else:
                self.txns_params['p'] += 1
