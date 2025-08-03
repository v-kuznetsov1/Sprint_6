
import allure

from locators.home_page_locatorts import HomePageLocators
from pages.base_page import BasePage

class HomePage(BasePage):
    
    def __init__(self, driver):
        self.driver = driver

        
    @allure.step('Скролл к разделу Q/A')
    def scroll_to_accordion_heading(self):
        element = self.find_element(HomePageLocators.QUESTIONS_BLOCK)
        return self.scroll_to_element(element)

    @allure.step('Получение вопроса')
    def get_questions(self, index):
        question_locator = (HomePageLocators.QUESTION[0], HomePageLocators.QUESTION[1].format(index))
        question = self.click_to_element(question_locator)
        return question.text
    
    @allure.step('Получение ответа')
    def get_answers(self, index):
        answers_locator = (HomePageLocators.ANSWER[0], HomePageLocators.ANSWER[1].format(index))
        answer = self.find_element(answers_locator)
        return answer.text
    

    

        




        
                                     