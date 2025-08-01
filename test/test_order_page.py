import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import allure

from pages.order_page import OrderPage
from data import OrderData


class TestOrderPage:
    
    @allure.title('Оформление заказа')
    @allure.description('Полный флоу оформления заказа и проверка редиректов')
    @pytest.mark.parametrize('entry_point, data_order', [['click_order_button_in_header', OrderData.FIRST_ORDER],
                                                          ['click_order_button_in_middle', OrderData.SECOND_ORDER]])
    
    def test_create_order(self, driver, accept_cookie, entry_point, data_order):
        
        order_page = OrderPage(driver, accept_cookie)
        getattr(order_page, entry_point)()
        
        order_page.create_order(**data_order)

        modal_window = order_page.check_modal_window()
        assert modal_window == True, 'Модальное окно с инофрмаций о сделанном заказе не отображается'

        order_page.check_status_order()

        to_home_page = order_page.redirect_to_home_page()
        assert to_home_page == OrderData.base_url, 'Не удалось перейти на главную страницу'

        order_page.redirect_to_dzen()
        switching_tabs = order_page.switching_to_the_tab()
        assert switching_tabs == OrderData.url_dzen, 'Редирект на dzen не произошел'



        

    
