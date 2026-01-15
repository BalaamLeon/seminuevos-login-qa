from utils import data
from utils.url_utils import normalize_url


class TestLogin:
    def test_login_success(self, driver, login_page, home_page):
        # Successful Login redirects to home and shows user info.
        assert data.email, "Missing USER_EMAIL environment variable"
        assert data.password, "Missing USER_PASSWORD environment variable"

        login_page.login(data.email, data.password)
        login_page.wait_for_url_contains(normalize_url(data.home_url), timeout=15)

        # Assert 1: check for redirect to homepage
        assert normalize_url(driver.current_url) == normalize_url(data.home_url)

        # Assert 2: user info is displayed (logged in)
        assert home_page.is_user_logged_in()

    def test_login_invalid_email(self, login_page):
        # Invalid email should show an error message.
        assert data.password, "Missing USER_PASSWORD environment variable"

        login_page.login(data.invalid_email, data.password)
        assert login_page.get_login_error_text() == data.error_message

    def test_login_invalid_password(self, login_page):
        # Invalid password should show an error message.
        assert data.email, "Missing USER_EMAIL environment variable"

        login_page.login(data.email, data.invalid_password)
        assert login_page.get_login_error_text() == data.error_message

    def test_login_empty_fields(self, login_page):
        # Submitting empty fields should show an error message.
        login_page.submit()
        if login_page.is_login_error_displayed():
            assert login_page.get_login_error_text() != ""