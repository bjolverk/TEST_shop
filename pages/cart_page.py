import time

import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Cart_page(Base):

    def __init__(self, driver):
        super().__init__(driver)

    # LOCATORS

    page_title = '//h1[@class="cart-title"]'
    # ================PRODUCT=========================#
    product_label = '//div[@class="cart-items__product-name"]/a'
    order_price = '//div[@id="total-amount"]/div[1]/div[3]/div/div[1]/div[2]/div/div/span'
    # ================PRODUCT=========================#
    checkout_button = '//button[@id="buy-btn-main"]'

    # GETTERS

    def get_page_title(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.page_title)))

    def get_product_label(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.product_label)))

    def get_order_price(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.order_price)))

    def get_checkout_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.checkout_button)))

    # ACTIONS
    def click_get_checkout_button(self):
        self.get_checkout_button().click()
        print("Click checkout button ")

    # METHODS

    def go_to_checkout(self):
        with allure.step('Go to checkout'):
            self.get_current_url()
            self.assert_word(self.get_page_title(), 'Корзина')
            self.assert_url('https://www.dns-shop.ru/cart/')
            try:
                self.assert_word(self.get_product_label(), 'Сетевая карта DEXP ZH-FEPCI1', 'Product label')
                try:
                    self.assert_word(self.get_order_price(), '199 ₽', 'Order price')
                    self.click_get_checkout_button()
                    time.sleep(4)
                except AssertionError:
                    print('Attention! Check the price of the order.')
            except AssertionError:
                print('Attention! You need to check the title of the item.')
