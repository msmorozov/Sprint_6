import pytest

from data import Answers
from test_page_object.locators.main_page_locators import MainPageLocators
from test_page_object.pages.main_page import MainPage


class TestMainPage:

    @pytest.mark.parametrize(
        "q_num,expected_result",
        [
            (0, Answers.ANSWER_Q_1),
            (1, Answers.ANSWER_Q_2),
            (2, Answers.ANSWER_Q_3),
            (3, Answers.ANSWER_Q_4),
            (4, Answers.ANSWER_Q_5),
            (5, Answers.ANSWER_Q_6),
            (6, Answers.ANSWER_Q_7),
            (7, Answers.ANSWER_Q_8)
        ]
    )
    def test_questions(self, driver, q_num, expected_result):
        main_page = MainPage(driver)
        main_page.click_on_element(MainPageLocators.COOKIE)
        result = main_page.click_to_question_and_get_answer_text(
            MainPageLocators.QUESTION_LOCATORS,
            MainPageLocators.ANSWER_LOCATORS,
            q_num
        )
        assert main_page.check_answer(result, expected_result)
