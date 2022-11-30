import time

from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base
from utilities.user_generator import phone_generator, email_generator, name_generator, address_generator


class Checkout_page(Base):

    def __init__(self, driver):
        super().__init__(driver)

    # LOCATORS

    page_title = '//div[@class="layout-checkout-right__title"]'

    phone_container = '//*[@id="checkout"]/div/div[2]/div[1]/div[2]/div[2]/div[2]/div[1]/div/div/div'
    phone_field = '/html/body/div/div/div[1]/div/div[2]/div[1]/div[2]/div[2]/div[2]/div[1]/div/div/div/input'

    email_container = '//*[@id="checkout"]/div/div[2]/div[1]/div[2]/div[2]/div[2]/div[2]/div/div'
    email_field = '/html/body/div/div/div[1]/div/div[2]/div[1]/div[2]/div[2]/div[2]/div[2]/div/div/input'

    delivery_button = '//div[@id="checkout"]/div/div[2]/div[2]/div[1]/div[3]/div[1]/div/div[2]'

    # ======================================POPUP======================================================#

    popup_heading = '//*[@id="checkout"]/div/div[2]/div[2]/div[1]/div[3]/div[3]/div[2]/div[2]/div[1]'

    popup_name_container = '//div[@id="checkout"]/div/div[2]/div[2]/div[1]/div[3]/div[3]/div[2]/div[2]' \
                           '/div[2]/div/div[1]'
    popup_name = '//input[@class="base-ui-input-small__input_RHW"]'
    popup_addr = '//*[@id="checkout"]/div/div[2]/div[2]/div[1]/div[3]/div[3]/div[2]/div[2]/div[2]' \
                 '/div/div[2]/div[1]/div[2]/input'
    popup_rise_floor = '//*[@id="checkout"]/div/div[2]/div[2]/div[1]/div[3]/div[3]/div[2]/div[2]/div[2]' \
                       '/div/div[3]/div[1]/label'

    popup_floors_list = '//div[@class="base-ui-dropdown__desktop_tje"]'

    popup_floor_num = '//ul[@class="base-ui-dropdown__inner_QWP"]/li[98]'

    popup_elevator_aval = '//label[@class="base-ui-checkbox_i0f base-ui-checkbox__icon-hover_buE"]'

    popup_comment = '//a[@class="base-ui-link_TSM base-ui-link_blue_n7N base-ui-link_pseudo-link_MAZ"]'

    popup_comment_field = '//textarea[@class="base-ui-textarea__resize-none_GcH base-ui-textarea__input_btP"]'

    popup_confirm_key = '//button[@class="base-ui-button_GWR base-ui-button_medium__Fr base-ui-button_brand_UhA ' \
                        'base-ui-button_ico-none_Gf6 base-checkout-delivery-modal__apply-btn_v_5"]'

    # ======================================END OF POPUP======================================================#
    # ======================================PAYMENT===========================================================#
    cash = '//div[@id="checkout"]/div/div[2]/div[2]/div[2]/div[2]/div[2]/div/div/div[1]/div/div[1]'
    card = '//div[@id="checkout"]/div/div[2]/div[2]/div[2]/div[2]/div[2]/div/div/div[2]/div/div[2]'
    # ======================================END OF PAYMENT====================================================#

    become_a_member = '//div[@id="checkout"]/div/div[2]/div[2]/div[5]/div[1]/label[1]'
    confirm_the_order = '//div[@id="checkout"]/div/div[2]/div[2]/div[3]/div/button'

    # GETTERS

    def get_phone_container(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.phone_container)))

    def get_phone_field(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.phone_field)))

    def get_email_container(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.email_container)))

    def get_email_field(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.email_field)))

    def get_delivery_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.delivery_button)))

    def get_page_title(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.page_title)))

    def get_popup_heading(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.popup_heading)))

    def get_popup_name_container(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.popup_name_container)))

    def get_popup_name(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.popup_name)))

    def get_popup_addr(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.popup_addr)))

    def get_rise_floor(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.popup_rise_floor)))

    def get_popup_floors_list(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.popup_floors_list)))

    def get_popup_floor_num(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.popup_floor_num)))

    def get_popup_elevator_aval(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.popup_elevator_aval)))

    def get_popup_comment(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.popup_comment)))

    def get_popup_comment_field(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.popup_comment_field)))

    def get_popup_confirm_key(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.popup_confirm_key)))

    def get_card(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.card)))

    def get_cash(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.cash)))

    def get_become_a_member(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.become_a_member)))

    def get_confirm_the_order(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.confirm_the_order)))

    # ACTIONS
    def click_phone_container(self):
        self.get_phone_container().click()
        print('Phone field clicked')

    def input_phone_field(self, phone):
        self.get_phone_field().send_keys(phone)
        print('Phone entered')

    def input_email_field(self, email):
        self.get_email_field().send_keys(email)
        print('Email entered')

    def click_delivery_button(self):
        self.get_delivery_button().click()
        print('Click delivery button')

    def enter_popup_name(self, username):
        self.get_popup_name().send_keys(username)
        print("Name entered")

    def enter_popup_address(self, address):
        self.get_popup_addr().send_keys(address)
        print("Address entered")

    def click_popup_rise_floor(self):
        self.get_rise_floor().click()
        print("Checkbox 'Rise to the floor' clicked")

    def click_popup_floors_list(self):
        self.get_popup_floors_list().click()
        print('Floors list clicked!')

    def click_popup_floor_num(self):
        self.get_popup_floor_num().click()
        print('Floor selected')

    def click_popup_elevator_aval(self):
        self.get_popup_elevator_aval().click()
        print('Elevator accessibility set')

    def click_popup_comment_label(self):
        a = ActionChains(self.driver)
        a.move_to_element(self.get_popup_comment()).click(self.get_popup_comment()).perform()

        print('Comment field title clicked')

    def enter_popup_comment(self):
        b = ActionChains(self.driver)
        b.move_to_element(self.get_popup_comment_field()).perform()
        b.click(self.get_popup_comment_field()).send_keys('Тестовый заказ! Не обрабатывать!').perform()
        print("Comment text entered")

    def click_popup_confirm_key(self):
        self.get_popup_confirm_key().click()

    def click_card(self):
        self.get_card().click()
        print('Chosen payment by card to the courier')

    def click_cash(self):
        self.get_cash().click()
        print('Cash payment to courier selected')

    def click_become_a_member(self):
        self.get_become_a_member().click()
        print('Become a member clicked')

    def click_confirm_the_order(self):
        self.get_confirm_the_order().click()
        print('Confirm order button clicked')

    # METHODS

    def confirm_order(self):
        self.get_current_url()
        self.assert_url('https://www.dns-shop.ru/checkout/')
        try:
            self.assert_word(self.get_page_title(), 'Безопасная оплата')
            print("Page header OK")
        except AssertionError:
            print("Check page header")

        self.input_phone_field(phone_generator())
        # time.sleep(5)

        self.input_email_field(email_generator())
        self.click_delivery_button()
        try:
            self.assert_word(self.get_popup_heading(), 'Укажите детали доставки', 'Popup header')

        except AssertionError:
            print("Check popup header!")
        self.enter_popup_name(name_generator())
        self.enter_popup_address(address_generator())
        self.click_popup_rise_floor()
        self.click_popup_floors_list()
        self.click_popup_floor_num()
        self.click_popup_elevator_aval()
        self.click_popup_comment_label()
        self.enter_popup_comment()
        time.sleep(1)
        self.click_popup_confirm_key()
        self.click_card()
        time.sleep(2)
        self.click_cash()
        time.sleep(2)
        self.click_become_a_member()
        self.click_confirm_the_order()
        self.get_screenshot()
        time.sleep(5)
