import allure

from test_page_object.locators.order_page_locators import OrderPageLocators
from test_page_object.pages.base_page import BasePage


class OrderPage(BasePage):
    def click_on_field(self, locator):
        self.click_on_element(locator)

    def click_on_button(self, locator):
        self.click_on_element(locator)

    def click_on_field_and_set_text(self, locator, text):
        self.set_text_to_element(locator, text)

    def find_element_by_id(self, Locator):
        return self.driver.find_element_by_id(Locator)

    def send_keys_to_field(self, SUBWAY_FIELD, ENTER):
        pass
    @allure.step("Переход к оформлению заказа")
    def transition_order(self, button_order):
        self.find_element_located_click(button_order)

    @allure.step("Ввод данных в первой форме")
    def entering_test_data_page1(self, data):
        self.click_on_field_and_set_text(OrderPageLocators.NAME_FIELD, data.TEST_NAME)
        self.click_on_field_and_set_text(OrderPageLocators.SURNAME_FIELD, data.TEST_SURNAME)
        self.click_on_field_and_set_text(OrderPageLocators.ADDRESS_FIELD, data.TEST_ADDRESS)
        self.click_on_field_and_set_text(OrderPageLocators.PHONE_FIELD, data.TEST_NUMBER)
        self.click_on_field(OrderPageLocators.SUBWAY_FIELD)
        self.click_on_field_and_set_text(OrderPageLocators.SUBWAY_FIELD, data.TEST_UNDERGROUND)
        self.click_on_field(OrderPageLocators.SUBWAY_STATIONS)

    @allure.step("Переход на вторую форму")
    def transition_from_page1_to_page2(self):
        self.click_on_field(OrderPageLocators.NEXT_BUTTON)

    @allure.step("Ввод данных в второй форме")
    def entering_test_data_page2(self, data):
        self.click_on_field(OrderPageLocators.WHEN_FIELD)
        self.click_on_field(OrderPageLocators.WHEN_TIME)
        self.click_on_field(OrderPageLocators.FIELD_TIME_TO_RENT)
        self.click_on_field(OrderPageLocators.TIME_TO_RENT)
        self.click_on_field(OrderPageLocators.COLOR_SCOOTER)
        self.click_on_field_and_set_text(OrderPageLocators.COMMENT_FIELD, data.TEST_COMMENT)

    @allure.step("Нажатие на кнопку заказать в второй форме")
    def click_order_page2(self):
        self.click_on_button(OrderPageLocators.ORDER_BUTTON)

    @allure.step("Подтверждение заказа")
    def click_confirm_order(self):
        self.click_on_button(OrderPageLocators.CONFIRM_ORDER)