import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config import pw, user

# set webdriver
driver = webdriver.Chrome("C:/Users/Jan/dev/bankcsv/chromedriver/chromedriver")

# go on DKB Banking website
driver.get('https://www.dkb.de/banking')

# get field for login and password
anmeldename = driver.find_element_by_id('loginInputSelector')
passwort = driver.find_element_by_id("pinInputSelector")

# fill in login and password
anmeldename.send_keys(user)
passwort.send_keys(pw)
# submit login form
print("submit now")
passwort.send_keys(Keys.RETURN)

# check if logged in, by looking for overall balance
overall_balance = WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.ID, "overallBalance"))
)
print("Logged In")
