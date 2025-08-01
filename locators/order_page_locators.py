
from selenium.webdriver.common.by import By

class OrderPageLocators:

    ORDER_BUTTON_IN_HEADER = [By.XPATH, "//button[text()='Заказать']"]
    ORDER_BUTTON_IN_MIDDLE = [By.XPATH, '(//button[text()="Заказать"])[2]']
    
    USER_FIRST_NAME = [By.XPATH, '//input[@placeholder="* Имя"]']
    USER_LAST_NAME = [By.XPATH, '//input[@placeholder="* Фамилия"]']
    ADDRESS = [By.XPATH, '//input[@placeholder="* Адрес: куда привезти заказ"]']
    METRO_STATION = [By.XPATH, '//input[@placeholder="* Станция метро"]']
    METRO_STATION_SELECT = [By.XPATH, '//div[text()="Сокольники"]']
    P_NUMBER = [By.XPATH, '//input[@placeholder="* Телефон: на него позвонит курьер"]']
    NEXT_BUTTON = [By.XPATH, ".//button[text()='Далее']"]

    DATE_DELIVERY = [By.XPATH, "//input[@placeholder='* Когда привезти самокат']"]
    
    RENT_TIME = [By.XPATH, '//span[@class="Dropdown-arrow"]']
    SELECT_RENT_TIME = [By.XPATH, '//div[text()="сутки"]']
    
    CHECKBOX_COLOR = [By.ID, 'black']

    COMMENT_FOR_COURIER = [By.XPATH, '//input[@placeholder="Комментарий для курьера"]']

    ORDER_BUTTON = [By.XPATH, '//button[@class="Button_Button__ra12g Button_Middle__1CSJM" and text()="Заказать"]']
    MAKING_AN_ORDER_BUTTON = [By.XPATH, '//button[text()="Да"]']
    
    MODAL_WINDOW = [By.XPATH, '//div[contains(text(), "Заказ оформлен")]']

    CHECK_STATUS_BUTTON = [By.XPATH, "//button[text()='Посмотреть статус']"]

    SCOOTER_BUTTON = [By.XPATH, ".//a[@href='/']"]
    YANDEX_BUTTON = [By.XPATH, ".//img[@alt='Yandex']"]