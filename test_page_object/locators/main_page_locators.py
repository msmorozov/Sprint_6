from selenium.webdriver.common.by import By


class MainPageLocators:
    #локаторы вопросов
    QUESTION_LOCATORS = By.XPATH, '//div[@id="accordion__heading-{}"]'
    #локаторы ответов
    ANSWER_LOCATORS = By.XPATH, '//div[@id="accordion__panel-{}"]'
    #локатор кнопки заказать на чердаке страницы
    UPSTAIRS_ORDER_BUTTON = By.XPATH, '/html/body/div[1]/div/div/div[1]/div[2]/button[1]'
    #локатор кнопки куки
    COOKIE = By.XPATH, '//button[@id="rcc-confirm-button"]'
    #локатор кнопки самоката в верху
    SCOOTER_BUTTON_LOCATORS = By.XPATH, "//a[@class='Header_LogoScooter__3lsAR']/img[@alt='Scooter']"
    #локатор Яндекса в верху
    YANDEX_BUTTON_LOCATORS = By.XPATH, "//a[@class='Header_LogoYandex__3TSOI']/img[@alt='Yandex']"
    # локатор кнопки заказа в верху
    ORDER_BUTTON_UP_LOCATORS = By.XPATH, "//button[@class='Button_Button__ra12g' and text()='Заказать']"
    #текст Самокат на пару дней
    TEXT_SCOOTER_MAIN_PAGE = By.XPATH, "//div[@class='Home_Header__iJKdX' and not(ancestor::div[@class='Home_Header__iJKdX'])]"
