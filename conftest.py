import pytest
from selenium import webdriver

from config import Config
from locators.home_page_locatorts import HomePageLocators
from pages.base_page import BasePage

@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.get(Config.BASE_URL)

    yield driver

    driver.quit()

@pytest.fixture
def accept_cookie(driver):
        accept_cookie_button = driver.find_element(*HomePageLocators.COOKIE_BUTTON)
        accept_cookie_button.click()
   
