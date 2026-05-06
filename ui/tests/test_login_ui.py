import pytest

from ui.pages.login_page import LoginPage
from config.settings import UI_USERNAME, UI_PASSWORD


@pytest.mark.ui
def test_login_success(page):
    login = LoginPage(page)
    login.navigate()
    login.login(UI_USERNAME, UI_PASSWORD)

    assert "Benefits" in page.url


@pytest.mark.ui
def test_ui_no_redirect_on_401(page):
    login = LoginPage(page)
    login.navigate()
    login.login(UI_USERNAME, UI_PASSWORD)

    page.context.clear_cookies()
    page.reload()

    assert "Login" not in page.url


@pytest.mark.ui
def test_login_empty_username(page):
    login = LoginPage(page)

    login.navigate()
    login.login(username="", password="valid_password")

    assert login.get_username_error().is_visible()


@pytest.mark.ui
def test_login_does_not_submit_invalid_form(page):
    login = LoginPage(page)

    login.navigate()
    login.login(username="", password="")

    assert "Login" in page.url


@pytest.mark.ui
def test_login_long_username(page):
    login = LoginPage(page)

    long_username = "long" * 5000

    login.navigate()
    login.login(username=long_username, password="pwd")

    assert "Login" in page.url
