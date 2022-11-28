import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from pages.checkout_page import Checkout_page
from pages.main_page import Main_page
from pages.net_cards.net_cards_page import Net_cards_page
from pages.cart_page import Cart_page


def test_easy_purchase():
    options = Options()  # Очищаем консоль от технической информации
    options.add_experimental_option('excludeSwitches', ['enable-logging'])  # Задаём параметры для очистки
    driver = webdriver.Chrome(executable_path=r'C:\Users\MadCat\PycharmProjects\resource\chromedriver.exe',
                              chrome_options=options)  # chrome_options параметр для очистки

    print("Start Test easy purchase")
    mp = Main_page(driver)
    mp.сhosing_network_card()

    cards_page = Net_cards_page(driver)
    cards_page.сhosing_network_card()

    cart = Cart_page(driver)
    cart.go_to_checkout()

    # time.sleep(4)  # TODO Сделать с этим что-то!!!
    cp = Checkout_page(driver)
    cp.confirm_order()

    print("Finish test easy purchase")
    time.sleep(5)
    driver.quit()
