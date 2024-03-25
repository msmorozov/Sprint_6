from selenium.webdriver.common.by import By


class OrderPageLocators:
    TO_ORDER_1 = By.XPATH, ".//*[@class='Button_Button__ra12g']"
    TO_ORDER_2 = By.XPATH, ".//*[@class='Home_FinishButton__1_cWm']"

    #локатор кнопки самоката в верху
    SCOOTER_BUTTON_LOCATORS = By.XPATH, "//img[@src='/assets/scooter.svg' and @alt='Scooter']"
    #локатор Яндекса в верху
    YANDEX_BUTTON_LOCATORS = By.XPATH, "//img[@src='/assets/yandex.svg' and @alt='Yandex']"

    #поле имя
    NAME_FIELD = By.XPATH, "//input[@class='Input_Input__1iN_Z Input_Responsible__1jDKN']"
    #поле фамилия
    SURNAME_FIELD = By.XPATH, "//input[@class='Input_Input__1iN_Z Input_Responsible__1jDKN' and @placeholder='* Фамилия']"
    #поле адрес
    ADDRESS_FIELD = By.XPATH, "//input[@class='Input_Input__1iN_Z Input_Responsible__1jDKN' and @placeholder='* Адрес: куда привезти заказ']"
    #поле выбора метро
    SUBWAY_FIELD = By.XPATH, "//input[@tabindex='0' and @placeholder='* Станция метро' and @autocomplete='on' and @class='select-search__input' and @value='']"
    #станции метро выбор
    SUBWAY_STATIONS = By.XPATH,".//div[text() = 'Парк культуры']"
    #поле телефон
    PHONE_FIELD = By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']"
    #станция метро
    NEXT_BUTTON = By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and text()='Далее']"

    #кнопка далее
    NEXT_BUTTON = By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and text()='Далее']"

    #когда привезут самокат
    WHEN_FIELD = By.XPATH, '//input[@placeholder="* Когда привезти самокат"]'
    #указание времени
    WHEN_TIME = By.XPATH, "//div[contains(@class, 'react-datepicker__day--025')]"
    #поле когда
    FIELD_TIME_TO_RENT = By.XPATH, '//div[@class="Dropdown-placeholder" and text()="* Срок аренды"]'
    #указание суток
    TIME_TO_RENT = By.XPATH, '//div[@class="Dropdown-option" and @role="option" and @aria-selected="false" and text()="сутки"]'
    #цвет самоката
    COLOR_SCOOTER = By.XPATH, '//label[@for="black" and contains(text(), "чёрный жемчуг")]'
    #поле комментарии
    COMMENT_FIELD = By.XPATH, '//input[@class="Input_Input__1iN_Z Input_Responsible__1jDKN" and @placeholder="Комментарий для курьера"]'

    #кнопка заказать
    ORDER_BUTTON = By.XPATH, '//button[@class="Button_Button__ra12g Button_Middle__1CSJM" and text()="Заказать"]'

    #подтверждение заказа
    CONFIRM_ORDER = By.XPATH, '//button[@class="Button_Button__ra12g Button_Middle__1CSJM" and text()="Да"]'
    #Заказ оформлен
    ORDER_IS_DONE = By.XPATH, '//div[@class="Order_ModalHeader__3FDaJ"]'



