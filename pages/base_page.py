from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def find_element(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def exists(self, locator, timeout=0):
        try:
            if timeout > 0:
                WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
            else:
                return len(self.driver.find_elements(*locator)) > 0
            return True
        except Exception:
            return False

    def click_element(self, locator):
        element = self.find_element(locator)
        element.click()

    def enter_text(self, locator, text):
        element = self.find_element(locator)
        element.click()
        element.clear()
        WebDriverWait(self.driver, 1)
        element.click()
        element.send_keys(text)

    def wait_for_url_to_be(self, expected_url, timeout):
        WebDriverWait(self.driver, timeout).until(EC.url_to_be(expected_url))

    def wait_for_url_contains(self, partial, timeout):
        WebDriverWait(self.driver, timeout).until(EC.url_contains(partial))