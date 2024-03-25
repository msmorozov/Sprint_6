import allure
import data

from selenium.webdriver.support.wait import WebDriverWait
from test_page_object.locators.main_page_locators import MainPageLocators
from test_page_object.pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC


class MainPage(BasePage):

    def click_to_question(self, locator):
        self.click_on_element(locator)

    def check_answer(self,result,expected):
        return result == expected

    def click_to_question_and_get_answer_text(self, locator_q, locator_a, num):
        method, locator = locator_q
        locator = locator.format(num)

        method_a, answer_locator = locator_a
        answer_locator = answer_locator.format(num)
        self.click_on_element((method, locator))
        return self.get_text_from_element((method_a, answer_locator))

    @allure.step("Переход по ссылке Заказать")
    def click_to_order(self, locator):
        self.click_on_element(MainPageLocators.ORDER_BUTTON_UP_LOCATORS)

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
        WebDriverWait(self.driver, 10).until(EC.url_contains(data.RedirectUrl_From_MainPage.Scooter_Url))

    @allure.step("Переход по ссылке на Яндекс")
    def click_to_yandex(self):
        # Сохраняем текущую вкладку
        current_window_handle = self.driver.current_window_handle
        # Сохраняем текущее количество вкладок
        initial_tab_count = len(self.driver.window_handles)
        # Нажимаем на кнопку, которая должна открыть новую вкладку
        self.click_on_element(MainPageLocators.YANDEX_BUTTON_LOCATORS)
        # Ждем, пока не появится новая вкладка
        WebDriverWait(self.driver, 10).until(EC.number_of_windows_to_be(initial_tab_count + 1))
        # Получаем список всех вкладок
        all_handles = self.driver.window_handles
        # Получаем новую вкладку
        new_window_handle = next(handle for handle in all_handles if handle != current_window_handle)
        # Переключаемся на новую вкладку
        self.driver.switch_to.window(new_window_handle)
        # Ждем, пока новая страница не загрузится
        WebDriverWait(self.driver, 10).until(EC.url_contains("dzen.ru"))