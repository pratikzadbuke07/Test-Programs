from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import csv
import logging
import time

logging.basicConfig(level=logging.INFO)
driver=webdriver.Chrome()
driver.get('https://www.tutorialspoint.com/selenium/practice/selenium_automation_practice.php')
driver.maximize_window()
time.sleep(1)

name=driver.find_element(By.XPATH,"//input[@name='name']")
name.clear()
name.send_keys('Pratik Zadbuke')
time.sleep(1)

email=driver.find_element(By.XPATH,"//input[@id='email']")
email.clear()
email.send_keys('pmzadbuke07@gmail.com')
time.sleep(1)

gender=driver.find_element(By.XPATH,"//input[@id='gender']").click()
time.sleep(1)

mobile=driver.find_element(By.XPATH,"//input[@name='mobile']").send_keys('9970739099')
time.sleep(1)

DOB=driver.find_element(By.XPATH,"//input[@name='dob']")
DOB.send_keys('22/03/2024')
time.sleep(1)

Subject=driver.find_element(By.XPATH,"//input[@name='subjects']")
Subject.send_keys("this is web automation testing with selenium with python....")
time.sleep(1)

hobbies=driver.find_element(By.XPATH,"//input[@id='hobbies']").click()

Address=driver.find_element(By.XPATH,"//form[@name='TextForm']/div[9]/div/textarea").send_keys('Pune')
time.sleep(1)


#Choose File automation
#file_path=driver.find_element(By.XPATH,"//[@type='file']")
#file_path.send_keys("//C:/Users/pmzad/Downloads//Reshma_Automation_4.pdf")
#time.sleep(1)


state=driver.find_element(By.XPATH,"//select[@name='state']").click()
dropdown_element = driver.find_element(By.XPATH,"//Select[@name='state']")
select = Select(dropdown_element)
select.select_by_visible_text("NCR")
select.select_by_index(1)
time.sleep(1)

drp_down=driver.find_element(By.XPATH,"//select[@id='city']")
select = Select(drp_down)
select.select_by_visible_text("Agra")
select.select_by_index(1)
time.sleep(1)

#submit=driver.find_element(By.XPATH,"//input[@type='submit']").click()


time.sleep(3)
driver.close()