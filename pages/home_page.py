from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException

class HomePage:
    def init(self, driver):
        self.driver = driver
        self.group = (By.CSS_SELECTOR, "#app > div > div.home-content > div > div > div > div > div.home__education > div.home__education-page > div > div:nth-child(2) > div.home-card__bot > div > div.avatar.baseavatar_go.home-card__bot-content-btn.baseavatar")
        self.lesson = (By.CSS_SELECTOR, "#tabbar > div > div.tab-header > div.tab-header__wrapper > div:nth-child(2)")
        self.video = (By.CSS_SELECTOR, "#app > div > div.container.container_mobile > div > div > div.new-lessons_content > div > div:nth-child(5) > div.flex.gap20 > div:nth-child(3) > div.lesson-card > div")
        self.play = (By.CSS_SELECTOR, "#app > div > div.videolesson > div > div:nth-child(2) > div > div:nth-child(3) > div.video-player-proweb > div > div.video-player-proweb__controlls > div.video-player-proweb__controllers > div.video-player-proweb__controllers-left > button")
        self.stars = (By.CSS_SELECTOR, "#app > div > div.videolesson > div > div:nth-child(2) > div > div.videolesson__general-footer-rating.mb10 > div > div > div > span:nth-child(5)")



    def click_btn_group (self):
         wait = WebDriverWait(self.driver, 10)
         wait.until(EC.element_to_be_clickable(self.group)).click()

    def click_btn_lesson (self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.lesson)).click()

    def click_btn_video (self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.video)).click()

    def click_btn_play (self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.play)).click()

    def click_btn_stars (self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.stars)).click()