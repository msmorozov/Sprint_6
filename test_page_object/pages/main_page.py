import allure

from test_page_object.locators.main_page_locators import MainPageLocators
from test_page_object.pages.base_page import BasePage


class MainPage(BasePage):

    @allure.step("Проверка ответа")
    def check_answer(self,result,expected):
        return result == expected

    @allure.step("Нажатие на вопрос и получение текста ответа")
    def click_to_question_and_get_answer_text(self, locator_q, locator_a, num):
        method, locator = locator_q
        locator = locator.format(num)

        method_a, answer_locator = locator_a
        answer_locator = answer_locator.format(num)
        self.click_on_element((method, locator))
        return self.get_text_from_element((method_a, answer_locator))

    @allure.step("Переход по ссылке Яндекс Самокат")
    def click_to_scooter(self, locator):
        self.click_on_element(MainPageLocators.SCOOTER_BUTTON_LOCATORS)

    @allure.step("Закрываем Куки")
    def cookie_close(self):
        self.click_on_element(MainPageLocators.COOKIE)

    @allure.step("Проверка перехода по ссылке Яндекс Самокат")
    def order_scooter(self):
        self.click_on_element(MainPageLocators.ORDER_BUTTON_UP_LOCATORS)
        self.click_on_element(MainPageLocators.SCOOTER_BUTTON_LOCATORS)
        self.wait_until_redirect_scooter_url()

    @allure.step('Нажать на логотип "Яндекс" в хедере')
    def click_to_yandex_logo(self):
        self.click_on_element(MainPageLocators.YANDEX_BUTTON_LOCATORS)

    @allure.step('Переключиться на новую вкладку')
    def switch_tab(self):
        self.switch_to_window()

    @allure.step('Получить текущий URL')
    def get_current_url(self):
        return self.current_url()

    @allure.step('Ожидание загрузки сайта')
    def wait_loading_site(self):
        self.wait_until_url_to_be_dzen_url()

    @allure.step("Проверка наличия текста Яндекс Самокат на главной странице")
    def is_text_scooter_main_page_displayed(self):
        return self.displayed_scooter_main_page()
