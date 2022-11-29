from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Main_page(Base):
    url = 'https://www.dns-shop.ru/'

    def __init__(self, driver):
        super().__init__(driver)
        # self.driver = driver #TODO проверить работу без этой строки!

    # LOCATORS

    net_hardware = '//div[@id="homepage-desktop-menu-wrap"]/div/div[8]/div[1]/a'
    cat_net_name = '//*[@id="homepage-desktop-menu-wrap"]/div/div[8]/div[2]/a[1]'
    net_cards = '//a[@href="/catalog/17a8a9e816404e77/setevye-karty/"]'

    # GETTERS

    def get_net_hardware(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.net_hardware)))

    def get_cat_net_name(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.cat_net_name)))

    def get_net_cards(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.net_cards)))

    # ACTIONS

    def hover_net_hardware(self):
        action = ActionChains(self.driver)
        action.move_to_element(self.get_net_hardware()).perform()
        print("Network equipment popup is open")

    def click_net_cards(self):
        self.get_net_cards().click()
        print("Go to the section of network cards")

    # METHODS

    def choosing_network_card(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()
        self.hover_net_hardware()
        self.assert_word(self.get_cat_net_name(), 'Wi-Fi роутеры и оборудование для малых сетей', 'Заголовок')
        self.click_net_cards()
