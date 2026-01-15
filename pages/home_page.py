from selenium.webdriver.common.by import By

from pages.base_page import BasePage

class HomePage(BasePage):
    USER_INFO = (By.CSS_SELECTOR, ".user-account")

    def is_user_logged_in(self):
        return self.find_element(self.USER_INFO).is_displayed()