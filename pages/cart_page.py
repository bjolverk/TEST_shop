import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Cart_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        # self.driver = driver #TODO проверить работу без этой строки!

    # LOCATORS

    page_title = '//h1[@class="cart-title"]'
    checkout_button = '//button[@id="buy-btn-main"]'

    # GETTERS

    def get_page_title(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.page_title)))

    def get_checkout_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.checkout_button)))

    # ACTIONS
    def click_get_checkout_button(self):
        self.get_checkout_button().click()
        print("Click checkout button ")

    # METHODS

    def go_to_checkout(self):
        self.get_current_url()
        self.assert_word(self.get_page_title(), 'Корзина')
        self.assert_url('https://www.dns-shop.ru/cart/')
        self.click_get_checkout_button()
        time.sleep(4)
