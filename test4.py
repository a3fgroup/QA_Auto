import time
from selenium import webdriver


# Пример работы с прокси для Хрома:
# option = webdriver.ChromeOptions()
# option.add_argument('--proxy-server=45.158.186.11:14593')
# browser = webdriver.Chrome(options=option)
# browser.get('https://icanhazip.com')


# Пример работы с прокси для Мозиллы:

ip = '45.158.186.11'
port = 14593

option = webdriver.FirefoxOptions()
option.set_preference('network.proxy.type', 1)
option.set_preference('network.proxy.http', ip)
option.set_preference('network.proxy.http_port', port)
option.set_preference('network.proxy.https', ip)
option.set_preference('network.proxy.https_port', port)
option.set_preference('network.proxy.ssl', ip)
option.set_preference('network.proxy.ssl_port', port)

browser = webdriver.Firefox(options=option)
browser.get('https://icanhazip.com')