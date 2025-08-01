import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import allure


from locators.order_page_locators import OrderPageLocators
from data import OrderData

class OrderPage:
  
    
    def __init__(self, driver, accept_cookie):
        self.driver = driver 
        self.accept_cookie = accept_cookie

    @allure.step('Клик по кнопке "Заказать" в заголовке')
    def click_order_button_in_header(self):
        order_button = self.driver.find_element(*OrderPageLocators.ORDER_BUTTON_IN_HEADER)
        order_button.click()

    @allure.step('Клик по кнопке "Заказать" в середине страницы')
    def click_order_button_in_middle(self):
        order_button = self.driver.find_element(*OrderPageLocators.ORDER_BUTTON_IN_MIDDLE)
        order_button.click()

    @allure.step('Ввод имени')
    def enter_firts_name(self, first_name):
        enter_name = self.driver.find_element(*OrderPageLocators.USER_FIRST_NAME)
        enter_name.send_keys(first_name)

    @allure.step('Ввод фамилии')
    def enter_last_name(self, last_name):
        enter_lastname = self.driver.find_element(*OrderPageLocators.USER_LAST_NAME)
        enter_lastname.send_keys(last_name)

    @allure.step('Ввод адреса')
    def enter_address_delivery(self, address):
        enter_address = self.driver.find_element(*OrderPageLocators.ADDRESS)
        enter_address.send_keys(address)

    @allure.step('Выбор станции метро из выпадающего списка')
    def select_metro_station(self):
        metro_station = self.driver.find_element(*OrderPageLocators.METRO_STATION)
        metro_station.click()

        select_metro = WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable(OrderPageLocators.METRO_STATION_SELECT))
        select_metro.click()

    @allure.step('Ввод номера телефона')
    def enter_phone_number(self, phone_number):
        enter_phone = self.driver.find_element(*OrderPageLocators.P_NUMBER)
        enter_phone.send_keys(phone_number)

    @allure.step('Клик по кнопке "Далее"')
    def click_next_button(self):
        next_button = self.driver.find_element(*OrderPageLocators.NEXT_BUTTON)
        next_button.click()

    @allure.step('Ввод даты доставки')
    def enter_date_delivery(self, date_delivery):
        enter_date = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(OrderPageLocators.DATE_DELIVERY))
        enter_date.send_keys(date_delivery)

    @allure.step('Выбор срока аренды')
    def select_rent_time(self):
        rent_time = self.driver.find_element(*OrderPageLocators.RENT_TIME)
        rent_time.click()
        
        select_rent_time = WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable(OrderPageLocators.SELECT_RENT_TIME))
        select_rent_time.click()

    @allure.step('Выбор цвета самоката')
    def select_color(self):
        scooter_color = self.driver.find_element(*OrderPageLocators.CHECKBOX_COLOR)
        scooter_color.click()

    @allure.step('Ввод комментария для курьера')
    def enter_comment_for_courier(self, comment_for_courier):
        enter_comment = self.driver.find_element(*OrderPageLocators.COMMENT_FOR_COURIER)
        enter_comment.send_keys(comment_for_courier)

    @allure.step('Клик по кнопке создания заказа после заполнения данных')
    def click_create_order_button(self):
        order_button = self.driver.find_element(*OrderPageLocators.ORDER_BUTTON)
        order_button.click()

        confirm_order = WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable(OrderPageLocators.MAKING_AN_ORDER_BUTTON))
        confirm_order.click()    
    
    @allure.step('Проверка всплывающего окна об оформлении заказа')
    def check_modal_window(self):
        modal_window = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(OrderPageLocators.MODAL_WINDOW))
        return modal_window.is_displayed()
    
    @allure.step('Клик по кнопке и переход на страницу о заказе')
    def check_status_order(self):
        check_status= self.driver.find_element(*OrderPageLocators.CHECK_STATUS_BUTTON)
        check_status.click()

    @allure.step('Проверка редиректа на начальную страницу')
    def redirect_to_home_page(self):
        home_page = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(OrderPageLocators.SCOOTER_BUTTON))
        home_page.click()
        current_url = self.driver.current_url
        return current_url
    
    @allure.step('Проверка редиректа на дзен')
    def redirect_to_dzen(self):
        dzen_page = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(OrderPageLocators.YANDEX_BUTTON))
        dzen_page.click()
    
    @allure.step('Переход на новую вкладку')
    def switching_to_the_tab(self): 
        self.driver.switch_to.window(self.driver.window_handles[1])
        WebDriverWait(self.driver, 10).until(EC.url_to_be(OrderData.url_dzen))
        return self.driver.current_url
        
    @allure.step('Полное заполнение анкеты')
    def create_order(self, first_name, last_name, address, phone_number, date_delivery, comment_for_courier): 
        
        self.enter_firts_name(first_name)
        self.enter_last_name(last_name)
        self.enter_address_delivery(address)
        self.select_metro_station()
        self.enter_phone_number(phone_number)
        self.click_next_button()
        self.enter_date_delivery(date_delivery)
        self.select_rent_time()
        self.select_color()
        self.enter_comment_for_courier(comment_for_courier)
        self.click_create_order_button()