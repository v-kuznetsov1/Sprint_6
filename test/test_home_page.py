import pytest
import allure

from pages.home_page import HomePage
from data import QuestionsAndAnswers



class TestHomePage:
     
     @allure.title('Проверка блока Q/A')
     @allure.description('Проверка, что при нажатии на каждый из вопросов пользователю доступен ожидаемый ответ')
     @pytest.mark.parametrize('index, question, answer', QuestionsAndAnswers.QUESTIONS_AND_ANSWERS_LIST)
     def test_check_question_and_answer(self, index, question, answer, 
                                        driver, accept_cookie):
    
          home_page = HomePage(driver)
          
          home_page.scroll_to_accordion_heading()
          question_text = home_page.get_questions(index)
          answer_text = home_page.get_answers(index)

          assert question_text == question
          assert answer_text == answer        
