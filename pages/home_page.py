import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import allure

from locators.home_page_locatorts import HomePageLocators

class HomePage:
    
    def __init__(self, driver, accept_cookie):
        self.driver = driver
        self.accept_cookie = accept_cookie
    

    @allure.step('Скролл к разделу Q/A')
    def scroll_to_accordion_heading(self):
        element = self.driver.find_element(*HomePageLocators.QUESTIONS_BLOCK)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    @allure.step('Получение вопроса')
    def get_questions(self, index):
        question_locator = (HomePageLocators.QUESTION[0], HomePageLocators.QUESTION[1].format(index))
        question = WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable(question_locator))
        question.click()
        return question.text
    
    @allure.step('Получение ответа')
    def get_answers(self, index):
        answers_locator = (HomePageLocators.ANSWER[0], HomePageLocators.ANSWER[1].format(index))
        answer = WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(answers_locator))
        return answer.text

    

        




        
                                     