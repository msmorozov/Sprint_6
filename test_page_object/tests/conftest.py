import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options

@allure.title('Открытие браузера / переход на страницу сервиса / закрытие браузера')
@pytest.fixture
def driver():
    firefox_options = Options()
    firefox_options.add_argument("--width=1920")
    firefox_options.add_argument("--height=1080")
    driver = webdriver.Firefox(options=firefox_options)
    driver.get('https://qa-scooter.praktikum-services.ru/')
    yield driver
    driver.quit()