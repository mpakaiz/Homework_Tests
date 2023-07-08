import os
from Yandex_Base_Page import YandexBasePage
import time
from dotenv import load_dotenv
from locators.Yandex_Passport_Locators import YandexPassportLocators as Locators

load_dotenv()
ya_password = os.getenv('YAPASSWORD')

class YandexPassport(YandexBasePage):
    def fill_and_return(self):
        name = 'mpakaiz'
        password = f'{ya_password}'
        self.element_is_visible(Locators.login_input).send_keys(name)
        time.sleep(1)
        self.element_is_visible(Locators.login_button).click()
        time.sleep(1)
        self.element_is_visible(Locators.password_input).send_keys(password)
        time.sleep(1)
        self.element_is_visible(Locators.password_button).click()
        time.sleep(5)
        return
