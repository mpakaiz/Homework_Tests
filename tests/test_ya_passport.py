import time

from Yandex_Passport import YandexPassport


class TestFromYandex:

    def test_form(self, driver):
        test_page = YandexPassport(driver, "https://passport.yandex.ru/auth/")
        test_page.open()
        time.sleep(5)
        test_page.fill_and_return()
        time.sleep(1)
