import pytest

from data import Test_User1, Test_User2
from test_page_object.locators.main_page_locators import MainPageLocators
from test_page_object.locators.order_page_locators import OrderPageLocators
from test_page_object.pages.order_page import OrderPage
from test_page_object.pages.main_page import MainPage


class TestOrderScooter:
    @pytest.mark.parametrize('button_order, data', [(OrderPageLocators.TO_ORDER_1, Test_User1),
                                                    (OrderPageLocators.TO_ORDER_2, Test_User2)])
    def test_order_to_scooter(self, driver, button_order, data):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        main_page.click_on_element(MainPageLocators.COOKIE)
        order_page.transition_order(button_order)

        order_page.entering_test_data_page1(data)
        order_page.transition_from_page1_to_page2()
        order_page.entering_test_data_page2(data)
        order_page.click_order_page2()
        order_page.click_confirm_order()

        assert order_page.find_element_with_wait(OrderPageLocators.ORDER_IS_DONE).is_displayed()