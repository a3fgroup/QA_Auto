import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


browser = webdriver.Firefox()
browser.get('http://youtube.com')

# Получаем классы видео на странице
# block = browser.find_element_by_class_name('style-scope ytd-rich-grid-renderer')
# all_video = block.find_elements_by_tag_name('ytd-rich-item-renderer')
#
# for video in all_video:
#     print(video.get_attribute('class'))


# Кнопка Логин
# xpath = '/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[3]/div[2]/ytd-button-renderer/a/paper-button/yt-formatted-string'
# button = browser.find_element_by_xpath(xpath).click()
#
# form_xpath = '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input'
# browser.find_element_by_xpath(form_xpath).send_keys('EXAMPLE')


# Скроллинг страницы(иммитация скролла нажатием на кнопку "Вниз")
html = browser.find_element_by_tag_name('html')

for i in range(10):
    html.send_keys(Keys.DOWN)






# /html/body/ytd-app/div/div/ytd-masthead/div[3]/div[3]/div[2]/ytd-button-renderer/a/paper-button/yt-formatted-string