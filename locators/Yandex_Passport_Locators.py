from selenium.webdriver.common.by import By

class YandexPassportLocators:
    login_input = (By.ID, "passp-field-login")
    login_button = (By.ID, "passp:sign-in")
    password_input = (By.ID, "passp-field-passwd")
    password_button = (By.ID, "passp:sign-in")

