from selenium import webdriver
import time

browser = webdriver.Edge(executable_path='./Driver/msedgedriver')


def validaQR():
    try:
        element = browser.find_element_by_tag_name("canvas")
    except:
        return False
    return True


def bothWhatsapp():
    browser.get("https://web.whatsapp.com/")
    time.sleep(5)

    espera = True

    while espera:
        print("Waiting...")
        espera = validaQR()
        time.sleep(2)
        if espera == False:
            print("Se autenticó")
            break


bothWhatsapp()
