from start_module.starknet_checker import starknet_checker


def main():
    with open('wallets.txt') as f:
        wallets = f.readlines()
    with open('proxies.txt') as f:
        proxies = f.readlines()

    if (len(wallets) == 0):
        print("No data")
        exit()
    print(f'Uploaded {len(wallets)} wallets and {len(proxies)} proxies')

    starknet_checker(wallets=wallets,
                     proxies=proxies)


if __name__ == '__main__':
    main()
