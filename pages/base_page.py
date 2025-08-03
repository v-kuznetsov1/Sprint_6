
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


from config import Config

class BasePage:

    def __init__(self, driver):
        self.driver = driver 
    
    def find_element(self, locator):
        return WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(locator))
    
    def click_to_element(self, locator):
        element = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(locator))
        element.click()
        return element
    
    def enter_text(self, locator, enter_text):
        field = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(locator))
        field.send_keys(enter_text)
        return field
    
    def scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def check_current_url(self):
        return self.driver.current_url
    
    def switching_to_window(self, url):
        self.driver.switch_to.window(self.driver.window_handles[1])
        WebDriverWait(self.driver, 10).until(EC.url_to_be(url))
