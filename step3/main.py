import time

from selenium import webdriver
from selenium.webdriver.common.by import By

PROMISED_DOWN = 150
PROMISED_UP = 10
CHROME_DRIVER_PATH = ""
TWITTER_EMAIL = ""
TWITTER_PASSWORD = ""


class InternetSpeedTwitterBot:
    def __init__(self, driver_path=None):
        self.driver = webdriver.Chrome()
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get("https://speedtest.net")

        # Depending on your location, you might need to accept the GDPR pop-up
        accept_button = self.driver.find_element(By.ID, value="_evidon-banner-acceptbutton")
        accept_button.click()

        time.sleep(3)
        go_button = self.driver.find_element(By.CSS_SELECTOR, value=".start-button a")
        go_button.click()

        time.sleep(60)
        self.up = self.driver.find_element(By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div['
                                                           '3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div['
                                                           '1]/div/div[2]/span').text
        self.down = self.driver.find_element(By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div['
                                                             '3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div['
                                                             '2]/div/div[2]/span').text

    def tweet_at_provider(self):
        pass


bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider()
