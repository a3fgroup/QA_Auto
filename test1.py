from selenium import webdriver
import time


# browser = webdriver.Firefox()
# browser.get('https://duckduckgo.com')
# time.sleep(5)
# browser.get('https://google.com')
# browser.quit()

browser = webdriver.Firefox()
browser.get('https://duckduckgo.com')
browser.save_screenshot('1-1.png')
browser.refresh()
browser.quit()