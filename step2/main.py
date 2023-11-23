from selenium import webdriver

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
        pass

    def tweet_at_provider(self):
        pass


bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider()
