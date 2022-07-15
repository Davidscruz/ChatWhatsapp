from selenium import webdriver
import time

browser = webdriver.Edge(executable_path='./Driver/msedgedriver')


def bothwhatsapp():
    browser.get('https://web.whatsapp.com/')
    time.sleep(5)


bothwhatsapp()
