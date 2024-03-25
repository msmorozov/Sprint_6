import allure

from data import RedirectUrl_From_MainPage
from test_page_object.locators.main_page_locators import MainPageLocators
from test_page_object.pages.main_page import MainPage


@allure.story('Тесты перехода на главную страницу Яндекс Самокат и на страницу заказа самоката')
class TestLogo:
    @allure.title('Тест перехода на главную страницу Яндекс')
    def test_click_to_yandex(self, driver):
        main_page = MainPage(driver)
        main_page.cookie_close()
        main_page.click_to_yandex()

        assert RedirectUrl_From_MainPage.Dzen_Url in driver.current_url

    @allure.title('Тест перехода на главную страницу Яндекс самокат')
    def test_order_scooter(self, driver):
        main_page = MainPage(driver)
        main_page.cookie_close()
        main_page.order_scooter()

        assert driver.find_element(*MainPageLocators.TEXT_SCOOTER_MAIN_PAGE).is_displayed()