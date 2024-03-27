import allure

from data import RedirectUrl_From_MainPage
from test_page_object.pages.main_page import MainPage


@allure.story('Тесты перехода на главную страницу Яндекс Самокат и на страницу заказа самоката')
class TestLogo:
    @allure.title(
        'При нажатии на логотип "Яндекс" открывается главная страница Дзена')
    def test_header_logo_yandex_click(self, driver):
        main_page = MainPage(driver)
        main_page.cookie_close()

        main_page.click_to_yandex_logo()
        main_page.switch_tab()
        main_page.wait_loading_site()
        assert main_page.get_current_url() == RedirectUrl_From_MainPage.Url_Dzen

    @allure.title('Тест перехода на главную страницу Яндекс самокат')
    def test_order_scooter(self, driver):
        main_page = MainPage(driver)
        main_page.cookie_close()
        main_page.order_scooter()

        assert main_page.is_text_scooter_main_page_displayed()