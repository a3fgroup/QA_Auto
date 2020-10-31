import time
from selenium import webdriver


option = webdriver.FirefoxOptions()                             # в переменную передали настройки ФФ
option.set_preference('dom.webdriver.enabled', False)   # в настройках браузера отключили обнаружение ВД, как драйвера

option.set_preference('general.useragent.overrade', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0')  # вносим нужный юзерагент


option.set_preference('dom.webnotifications.enabled', False)    # отключили уведомления в браузере
option.set_preference('media.volume_scale', '0.0')              # отключили звук в браузере
option.headless = True                                          # браузер будет работать в фоне, без UI


browser = webdriver.Firefox(options=option)
browser.get('https://nick-name.ru/generate/')


while True:
    button_xpath = '/html/body/div[1]/div[1]/div[1]/div[2]/form/table/tbody/tr[5]/td[2]/input'
    browser.find_element_by_xpath(button_xpath).click()

    link = browser.find_element_by_id('register').get_attribute('href')[36:]
    print(f'Nickname: {link}')
