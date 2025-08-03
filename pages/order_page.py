
import allure

from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators
from data import OrderData
from config import Config

class OrderPage(BasePage):
  
    
    def __init__(self, driver):
        self.driver = driver 

    @allure.step('Клик по кнопке "Заказать" в заголовке')
    def click_order_button_in_header(self):
        return self.click_to_element(OrderPageLocators.ORDER_BUTTON_IN_HEADER)
 

    @allure.step('Клик по кнопке "Заказать" в середине страницы')
    def click_order_button_in_middle(self):
        return self.click_to_element(OrderPageLocators.ORDER_BUTTON_IN_MIDDLE)


    @allure.step('Ввод имени')
    def enter_firts_name(self, first_name):
        return self.enter_text(OrderPageLocators.USER_FIRST_NAME, first_name)


    @allure.step('Ввод фамилии')
    def enter_last_name(self, last_name):
        return self.enter_text(OrderPageLocators.USER_LAST_NAME, last_name)


    @allure.step('Ввод адреса')
    def enter_address_delivery(self, address):
        return self.enter_text(OrderPageLocators.ADDRESS, address)

    @allure.step('Выбор станции метро из выпадающего списка')
    def select_metro_station(self):
        self.click_to_element(OrderPageLocators.METRO_STATION)
        self.click_to_element(OrderPageLocators.METRO_STATION_SELECT)
        
 

    @allure.step('Ввод номера телефона')
    def enter_phone_number(self, phone_number):
        return self.enter_text(OrderPageLocators.P_NUMBER, phone_number)


    @allure.step('Клик по кнопке "Далее"')
    def click_next_button(self):
        return self.click_to_element(OrderPageLocators.NEXT_BUTTON)


    @allure.step('Ввод даты доставки')
    def enter_date_delivery(self, date_delivery):
        return self.enter_text(OrderPageLocators.DATE_DELIVERY, date_delivery)


    @allure.step('Выбор срока аренды')
    def select_rent_time(self):
        self.click_to_element(OrderPageLocators.RENT_TIME)
        self.click_to_element(OrderPageLocators.SELECT_RENT_TIME)


    @allure.step('Выбор цвета самоката')
    def select_color(self):
        self.click_to_element(OrderPageLocators.CHECKBOX_COLOR)


    @allure.step('Ввод комментария для курьера')
    def enter_comment_for_courier(self, comment_for_courier):
        self.enter_text(OrderPageLocators.COMMENT_FOR_COURIER, comment_for_courier)


    @allure.step('Клик по кнопке создания заказа после заполнения данных')
    def click_create_order_button(self):
        self.click_to_element(OrderPageLocators.ORDER_BUTTON)
        self.click_to_element(OrderPageLocators.MAKING_AN_ORDER_BUTTON)
   
    
    @allure.step('Проверка всплывающего окна об оформлении заказа')
    def check_modal_window(self):
        modal_window = self.find_element(OrderPageLocators.MODAL_WINDOW)
        return modal_window.is_displayed()
    
    @allure.step('Клик по кнопке и переход на страницу о заказе')
    def check_status_order(self):
        self.click_to_element(OrderPageLocators.CHECK_STATUS_BUTTON)
  

    @allure.step('Проверка редиректа на начальную страницу')
    def redirect_to_home_page(self):
        self.click_to_element(OrderPageLocators.SCOOTER_BUTTON)
        return self.check_current_url()
    
    @allure.step('Проверка редиректа на дзен')
    def redirect_to_dzen(self):
        self.click_to_element(OrderPageLocators.YANDEX_BUTTON)
  

    @allure.step('Переход на новую вкладку')
    def switching_to_the_tab(self): 
        self.switching_to_window(Config.URL_DZEN)
        return self.check_current_url()
        
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