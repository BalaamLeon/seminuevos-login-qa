from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):
    EMAIL_INPUT = (By.ID, 'username')
    PASSWORD_INPUT = (By.ID, 'password')
    LOGIN_BUTTON = (By.NAME, 'login')
    ERROR_MESSAGE = (By.ID, 'input-error')

    def set_email(self, email):
        self.enter_text(self.EMAIL_INPUT, email)

    def set_password(self, password):
        self.enter_text(self.PASSWORD_INPUT, password)

    def submit(self):
        self.click_element(self.LOGIN_BUTTON)

    def login(self, email, password):
        self.set_email(email)
        self.set_password(password)
        self.submit()

    def is_login_error_displayed(self):
        return self.exists(self.ERROR_MESSAGE, timeout=5)
    
    def get_login_error_text(self):
        return self.find_element(self.ERROR_MESSAGE).text.strip()