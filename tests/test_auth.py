import time
from time import sleep

from pages.auth_page import AuthPage
from pages.home_page import HomePage


# def test_auth_chrome(driver_chrome):
#     driver_chrome.get("https://my.proweb.uz/log-in?q=/home")
#     auth_page = AuthPage(driver_chrome)
#     auth_page.input_login("998977388258")
#     time.sleep(1)
#     auth_page.click_btn_next()
#     time.sleep(1)
#     auth_page.input_password("977388258")
#     auth_page.click_btn_submit()
#     try:
#         auth_page.click_btn_sessions()
#         time.sleep(2)
#         auth_page.click_btn_finish()
#     except:
#         pass


# def test_auth_firefox(driver_firefox):
#     driver_firefox.get("https://my.proweb.uz/log-in?q=/home")
#     auth_page = AuthPage(driver_firefox)
#     auth_page.input_login("998977388258")
#     time.sleep(1)
#     auth_page.click_btn_next()
#     time.sleep(1)
#     auth_page.input_password("977388258")
#     auth_page.click_btn_submit()
#     try:
#         auth_page.click_btn_sessions()
#         time.sleep(2)
#         auth_page.click_btn_finish()
#     except:
#         pass



# def test_auth_edge(driver_edge):
#     driver_edge.get("https://my.proweb.uz/log-in?q=/home")
#     auth_page = AuthPage(driver_edge)
#     auth_page.input_login("998977388258")
#     time.sleep(1)
#     auth_page.click_btn_next()
#     time.sleep(1)
#     auth_page.input_password("977388258")
#     auth_page.click_btn_submit()
#     try:
#         auth_page.click_btn_sessions()
#         time.sleep(2)
#         auth_page.click_btn_finish()
#     except:
#         pass


# def test_invalid_auth_chrome(driver_chrome):
#         driver_chrome.get("https://my.proweb.uz/log-in?q=/home")
#         auth_page = AuthPage(driver_chrome)
#         auth_page.input_login("997977388257")
#         time.sleep(1)
#         auth_page.click_btn_next()
#         auth_page.input_password("977388258")
#         auth_page.click_btn_submit()
#         try:
#             auth_page.click_btn_sessions()
#             time.sleep(2)
#             auth_page.click_btn_finish()
#         except:
#             pass
#
#
# def test_invalid_auth_firefox(driver_firefox):
#     driver_firefox.get("https://my.proweb.uz/log-in?q=/home")
#     auth_page = AuthPage(driver_firefox)
#     auth_page.input_login("997977388257")
#     time.sleep(1)
#     auth_page.click_btn_next()
#     auth_page.input_password("977388258")
#     auth_page.click_btn_submit()
#     try:
#         auth_page.click_btn_sessions()
#         time.sleep(2)
#         auth_page.click_btn_finish()
#     except:
#         pass
#
#
# def test_invalid_auth_Edge(driver_Edge):
#     driver_Edge.get("https://my.proweb.uz/log-in?q=/home")
#     auth_page = AuthPage(driver_Edge)
#     auth_page.input_login("997977388257")
#     time.sleep(1)
#     auth_page.click_btn_next()
#     time.sleep(2)
#     auth_page.input_password("977388258")
#     auth_page.click_btn_submit()
#     try:
#         auth_page.click_btn_sessions()
#         time.sleep(2)
#         auth_page.click_btn_finish()
#     except:
#         pass


def test_auth_chrome(driver_chrome):
    driver_chrome.get("https://my.proweb.uz/log-in?q=/home")
    auth_page = AuthPage(driver_chrome)
    auth_page.input_login("998977388258")
    time.sleep(1)
    auth_page.click_btn_next()
    auth_page.input_password("977388258")
    auth_page.click_btn_submit()
    time.sleep(3)
    home_page = HomePage(driver_chrome)
    home_page.click_btn_group()
    time.sleep(4)
    home_page.click_btn_lesson()
    time.sleep(4)
    home_page.click_btn_video()
    time.sleep(4)
    home_page.click_btn_play()
    time.sleep(4)
    home_page.click_btn_stars()
    time.sleep(2)
    auth_page.click_btn_profile()
    time.sleep(5)
    auth_page.click_btn_exit()
    time.sleep(5)
    auth_page.click_btn_confirmation()
    time.sleep(5)
    try:
        auth_page.click_btn_sessions()
        time.sleep(2)
        auth_page.click_btn_finish()
    except:
        pass


def test_auth_firefox(driver_firefox):
    driver_firefox.get("https://my.proweb.uz/log-in?q=/home")
    auth_page = AuthPage(driver_firefox)
    auth_page.input_login("998977388258")
    time.sleep(1)
    auth_page.click_btn_next()
    auth_page.input_password("977388258")
    auth_page.click_btn_submit()
    time.sleep(3)
    home_page = HomePage(driver_firefox)
    home_page.click_btn_group()
    time.sleep(4)
    home_page.click_btn_lesson()
    time.sleep(4)
    home_page.click_btn_video()
    time.sleep(4)
    home_page.click_btn_play()
    time.sleep(4)
    home_page.click_btn_stars()
    time.sleep(2)
    auth_page.click_btn_profile()
    time.sleep(5)
    auth_page.click_btn_exit()
    time.sleep(5)
    auth_page.click_btn_confirmation()
    time.sleep(5)
    try:
        auth_page.click_btn_sessions()
        time.sleep(2)
        auth_page.click_btn_finish()
    except:
        pass


def test_auth_Edge(driver_Edge):
    driver_Edge.get("https://my.proweb.uz/log-in?q=/home")
    auth_page = AuthPage(driver_Edge)
    auth_page.input_login("998977388258")
    time.sleep(1)
    auth_page.click_btn_next()
    time.sleep(2)
    auth_page.input_password("977388258")
    auth_page.click_btn_submit()
    time.sleep(3)
    home_page = HomePage(driver_Edge)
    home_page.click_btn_group()
    time.sleep(4)
    home_page.click_btn_lesson()
    time.sleep(4)
    home_page.click_btn_video()
    time.sleep(4)
    home_page.click_btn_play()
    time.sleep(4)
    home_page.click_btn_stars()
    time.sleep(2)
    auth_page.click_btn_profile()
    time.sleep(5)
    auth_page.click_btn_exit()
    time.sleep(5)
    auth_page.click_btn_confirmation()
    time.sleep(5)
    try:
        auth_page.click_btn_sessions()
        time.sleep(2)
        auth_page.click_btn_finish()
    except:
        pass