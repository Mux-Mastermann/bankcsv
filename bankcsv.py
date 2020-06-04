import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select, WebDriverWait

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
passwort.send_keys(Keys.RETURN)

# check if logged in, by looking for overall balance
overall_balance = WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.ID, "overallBalance"))
)

# navigate to Kontoumsätze
driver.get("https://www.dkb.de/banking/finanzstatus/kontoumsaetze")

# Select Account from dropdown menu
select = Select(driver.find_element_by_id("id-1615473160_slAllAccounts"))
select.select_by_visible_text("DE42 1203 0000 1051 2654 92 / Girokonto")

# set date range
from_date = driver.find_element_by_id("id-1615473160_transactionDate")
from_date.clear()
from_date.send_keys("01.06.2020")
to_date = driver.find_element_by_id("id-1615473160_toTransactionDate")
to_date.clear()
to_date.send_keys("04.06.2020")

# click on search button
driver.find_element_by_id("searchbutton").click()

# click csv export button
driver.get("https://www.dkb.de/banking/finanzstatus/kontoumsaetze?$event=csvExport")

print("Done")
