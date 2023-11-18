from checkers.starknet.collect_data import WalletStat
import fake_useragent
from config import SHUFFLE_WALLETS, SLEEP_AFTER_WALLET_CHACKING
from random import shuffle
from time import sleep
import pandas as pd
from write_excel.excel import write_excel


def starknet_checker(wallets: list, proxies: list):
    wallets_stat = []
    data = []
    proxies_count = len(proxies)
    for i in range(0, len(wallets)):
        if proxies_count == 0:
            data.append([wallets[i].strip(), None, i])
        else:
            data.append([wallets[i].strip(), proxies[i % len(proxies)].strip(), i])

    if SHUFFLE_WALLETS:
        shuffle(data)

    for item in data:
        wallet = WalletStat(wallet=item[0],
                            proxy=item[1],
                            user_agent=fake_useragent.UserAgent().random).data
        wallet.index = [item[2]]
        wallets_stat.append(wallet)
        print(f"Checking of wallet number {item[2]} is finished")
        if SLEEP_AFTER_WALLET_CHACKING:
            sleep(SLEEP_AFTER_WALLET_CHACKING)

    write_excel(pd.concat(wallets_stat).sort_index())
    print('Export to data/wallets_stat.xlsx')
