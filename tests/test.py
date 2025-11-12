import pytest
import time
from selenium.common.exceptions import TimeoutException
from pages.auth_page import AuthPage


def test_auth_chrome(driver_chrome):
    driver_chrome.get("https://my.proweb.uz/log-in?q=/home")
    auth_page = AuthPage(driver_chrome)
    auth_page.input_login("998977388258")
    auth_page.click_btn_next()
    auth_page.input_password("977388258")
    auth_page.click_btn_submit()
    try:
        auth_page.click_btn_sessions()
        time.sleep(2)
        auth_page.click_btn_finish()
    except:
        pass