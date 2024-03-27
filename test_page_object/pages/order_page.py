import allure

from test_page_object.locators.order_page_locators import OrderPageLocators
from test_page_object.pages.base_page import BasePage


class OrderPage(BasePage):
    @allure.step("Выполнение перехода по кнопке заказа")
    def transition_order(self, button_order):
        self.find_element_located_click(button_order)

    @allure.step("Ввод данных в первой форме")
    def entering_test_data_page1(self, data):
        self.set_text_to_element(OrderPageLocators.NAME_FIELD, data.TEST_NAME)
        self.set_text_to_element(OrderPageLocators.SURNAME_FIELD, data.TEST_SURNAME)
        self.set_text_to_element(OrderPageLocators.ADDRESS_FIELD, data.TEST_ADDRESS)
        self.set_text_to_element(OrderPageLocators.PHONE_FIELD, data.TEST_NUMBER)
        self.click_on_element(OrderPageLocators.SUBWAY_FIELD)
        self.set_text_to_element(OrderPageLocators.SUBWAY_FIELD, data.TEST_UNDERGROUND)
        self.click_on_element(OrderPageLocators.SUBWAY_STATIONS)

    @allure.step("Переход на вторую форму")
    def transition_from_page1_to_page2(self):
        self.click_on_element(OrderPageLocators.NEXT_BUTTON)

    @allure.step("Ввод данных в второй форме")
    def entering_test_data_page2(self, data):
        self.click_on_element(OrderPageLocators.WHEN_FIELD)
        self.click_on_element(OrderPageLocators.WHEN_TIME)
        self.click_on_element(OrderPageLocators.FIELD_TIME_TO_RENT)
        self.click_on_element(OrderPageLocators.TIME_TO_RENT)
        self.click_on_element(OrderPageLocators.COLOR_SCOOTER)
        self.set_text_to_element(OrderPageLocators.COMMENT_FIELD, data.TEST_COMMENT)

    @allure.step("Нажатие на кнопку заказать в второй форме")
    def click_order_page2(self):
        self.click_on_element(OrderPageLocators.ORDER_BUTTON)

    @allure.step("Подтверждение заказа")
    def click_confirm_order(self):
        self.click_on_element(OrderPageLocators.CONFIRM_ORDER)

    @allure.step("Проверка что заказ оформлен")
    def order_is_done_displayed(self):
       return self.displayed_order_is_done()