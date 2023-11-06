# Проверка статистики на кошельках Старкнет

## Установка

`cd /путь/к/папке/checking-starknet-wallets`

`pip install -r requirements.txt`

`python main.py`

## Описание

Код подсчитывает основную статистику по транзакциям в сети StarkNet и записывает итоги в файл `data/wallets_stat.xlsx`

Работа с софтом (`config.py`):

1) В файл `wallets.txt` загружаемся адреса своих кошельков
2) В файл `proxies.txt` загружаем свои прокси в формате `socks5://login:paas@ip:port` или `http://login:paas@ip:port`
3) В файле `config.py`
    * `SHUFFLE_WALLETS` = `True`, если необходимо перемешать порядок кошельков для просмотра
    * `SLEEP_AFTER_WALLET_CHACKING` время сна в секундах между просмотром кошельков