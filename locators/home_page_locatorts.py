
from selenium.webdriver.common.by import By

class HomePageLocators:

    COOKIE_BUTTON = [By.ID, 'rcc-confirm-button']
    
    QUESTIONS_BLOCK = [By.CLASS_NAME, 'Home_FourPart__1uthg']
    QUESTION = [By.XPATH, "(.//div[@class='accordion__button'])[{}]"]
    ANSWER = [By.XPATH, "(.//div[@class='accordion__panel'])[{}]"]