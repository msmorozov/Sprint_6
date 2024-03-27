import allure
import data

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support import expected_conditions as EC
from test_page_object.locators.main_page_locators import MainPageLocators
from test_page_object.locators.order_page_locators import OrderPageLocators


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Поиск элемента с ожиданием")
    def find_element_with_wait(self, locator):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step("Клик по элементу")
    def click_on_element(self, locator):
        element = self.find_element_with_wait(locator)
        element.click()

    @allure.step("Получение текста элемента")
    def get_text_from_element(self, locators):
        element = self.find_element_with_wait(locators)
        return element.text

    @allure.step("Ввод текста в элемент")
    def set_text_to_element(self, locators, text):
        element = self.find_element_with_wait(locators)
        element.send_keys(text)

    @allure.step("Поиск элемента и клик с ожиданием")
    def find_element_located_click(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(ec.presence_of_element_located(locator)).click()


    @allure.step("Ожидание переадресации на страницу самоката")
    def wait_until_redirect_scooter_url(self):
        WebDriverWait(self.driver, 10).until(EC.url_contains(data.RedirectUrl_From_MainPage.Scooter_Url))

    @allure.step("Ожидание URL, указывающего на страницу Dzen")
    def wait_until_url_to_be_dzen_url(self):
        WebDriverWait(self.driver, 10).until(EC.url_to_be(data.RedirectUrl_From_MainPage.Url_Dzen))

    @allure.step("Переключение на новое окно")
    def switch_to_window(self):
        return self.driver.switch_to.window(self.driver.window_handles[-1])

    @allure.step("Получение текущего URL")
    def current_url(self):
        return self.driver.current_url

    @allure.step("Проверка отображения текста на главной странице самоката")
    def displayed_scooter_main_page(self):
        return self.driver.find_element(*MainPageLocators.TEXT_SCOOTER_MAIN_PAGE).is_displayed()

    @allure.step("Проверка отображения сообщения о завершении заказа")
    def displayed_order_is_done(self):
        return self.driver.find_element(*OrderPageLocators.ORDER_IS_DONE).is_displayed()