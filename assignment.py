from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import csv
import logging
import time

logging.basicConfig(level=logging.INFO)
driver=webdriver.Chrome()
driver.get('https://nces.ed.gov/ccd/schoolsearch/')
driver.maximize_window()
name=driver.find_element(By.XPATH,"//input[@name='InstName']")
name.clear()
name.send_keys('A')

time.sleep(1)

drp_state=driver.find_element(By.XPATH,"//select[@Name='State']")
drp=Select(drp_state)
drp.select_by_index(10)

time.sleep(1)

browser=driver.find_elements(By.XPATH,"//*[text()='Browse'and contains (@href,'county')]]")
#browser_county=Select(browser)
#browser_county.select_by_index(5)
browser.click()



time.sleep(10)
driver.close()
#//select[@Name='State']