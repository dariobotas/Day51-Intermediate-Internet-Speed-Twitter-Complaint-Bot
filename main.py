from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


# Options
chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.google.com/")
driver.find_element(By.NAME, value="q").send_keys("Python")
driver.find_element(By.NAME, value="btnK").click()
driver.quit()