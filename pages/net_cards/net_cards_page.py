import allure
from selenium import webdriver
from selenium.common import ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Net_cards_page(Base):

    def __init__(self, driver):
        super().__init__(driver)

    # LOCATORS

    page_title = '//div[@class="products-page__title"]/h1'
    # =============PRODUCT 1==================================================================#
    select_net_card_1 = '//div[1]/div/div[2]/div[2]/div[2]/div/div[1]/div[1]/div[4]/button[2]'
    selected_card_label = '/html/body/div[1]/div/div[2]/div[2]/div[2]/div/div[1]/div[1]/a/span'
    selected_card_price = '/html/body/div[1]/div/div[2]/div[2]/div[2]/div/div[1]/div[1]/div[4]/div/div[1]'
    # =============END OF PRODUCT1============================================================#
    product_title = '/html/body/div[1]/div/div[2]/div[2]/div[2]/div/div[1]/div[1]/a/span'
    to_shopping_cart_button = '//*[@id="app-cart-modal"]/div/div[2]/div[2]/button[2]'
    shopping_cart_button = '//a[@href="https://www.dns-shop.ru/cart/"]'

    # GETTERS

    def get_page_title(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.page_title)))

    def get_select_net_card_1(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.select_net_card_1)))

    def get_selected_card_label(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.selected_card_label)))

    def get_selected_card_price(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.selected_card_price)))

    def get_to_shopping_cart_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.to_shopping_cart_button)))

    def get_shopping_cart_popup(self):
        """Если не поймали окошко"""
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.shopping_cart_button)))

    def get_product_title(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.product_title)))

    # ACTIONS

    def click_select_net_card_1(self):
        self.get_select_net_card_1().click()
        print("Click select net card 1 ")

    def click_to_shopping_cart_button(self):
        self.get_to_shopping_cart_button().click()
        print("Click to shopping cart button ")

    def hover_shopping_cart(self):
        action = ActionChains(self.driver)
        action.move_to_element(self.get_shopping_cart_popup()).perform()
        print("Network equipment popup is open")

    # METHODS

    def simple_choosing_network_card(self):
        with allure.step('Simple choosing network card'):
            self.get_current_url()
            self.assert_word(self.get_page_title(), 'Сетевые карты')
            try:

                self.assert_word(self.get_selected_card_label(),
                                 r'Сетевая карта DEXP ZH-FEPCI1 [1 x RJ-45, 100 Мбит/сек, PCI]', 'Label')

                try:
                    self.assert_word(self.get_selected_card_price(), '199 ₽', 'Product price')

                    self.click_select_net_card_1()
                    try:
                        self.click_to_shopping_cart_button()

                    except ElementClickInterceptedException:
                        print("Did not work out, no panic!")
                        self.hover_shopping_cart()
                        self.click_to_shopping_cart_button()
                except AssertionError:
                    print('Attention! Check the price of the item.')

            except AssertionError:
                print('Attention! You need to check the title of the item.')

