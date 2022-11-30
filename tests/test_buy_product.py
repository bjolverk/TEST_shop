import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from pages.checkout_page import Checkout_page
from pages.main_page import Main_page
from pages.net_cards.net_cards_page import Net_cards_page
from pages.cart_page import Cart_page
import allure

@allure.description('test_simple_purchase')
def test_simple_purchase():
    options = Options()  # Очищаем консоль от технической информации
    options.add_experimental_option('excludeSwitches', ['enable-logging'])  # Задаём параметры для очистки
    driver = webdriver.Chrome(executable_path=r'C:\Users\MadCat\PycharmProjects\resource\chromedriver.exe',
                              chrome_options=options)  # chrome_options параметр для очистки

    print("Start Test easy purchase")
    mp = Main_page(driver)
    mp.simple_choosing_product_category()

    cards_page = Net_cards_page(driver)
    cards_page.simple_choosing_network_card()

    cart = Cart_page(driver)
    cart.go_to_checkout()

    cp = Checkout_page(driver)
    cp.confirm_simple_order()

    print("Finish test easy purchase")
    time.sleep(5)
    driver.quit()
