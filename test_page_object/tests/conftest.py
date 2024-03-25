import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options
from test_page_object.pages.main_page import MainPage

#@allure.step('Открытие браузера / переход на страницу сервиса / закрытие браузера')
@pytest.fixture
def driver():
    firefox_options = Options()
    firefox_options.add_argument("--width=1920")
    firefox_options.add_argument("--height=1080")
    driver = webdriver.Firefox(options=firefox_options)
    driver.get('https://qa-scooter.praktikum-services.ru/')
    yield driver
    driver.quit()

#@pytest.fixture(scope='function')
#def main_page(driver):
    #return MainPage(driver)

#@pytest.fixture(scope='function')
#def order_page(driver):
    #return OrderPage(driver)