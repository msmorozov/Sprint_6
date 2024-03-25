from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element_with_wait(self, locator):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    #для примера клик
    def click_on_element(self, locator):
        element = self.find_element_with_wait(locator)
        element.click()

    #взять текст
    def get_text_from_element(self, locators):
        element = self.find_element_with_wait(locators)
        return element.text

    #метод внесения данных в поле
    def set_text_to_element(self, locators, text):
        element = self.find_element_with_wait(locators)
        element.send_keys(text)

    def find_element_located_click(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(ec.presence_of_element_located(locator)).click()