from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
import time

# Setup WebDriver (use appropriate driver for your browser)
driver = webdriver.Chrome()  # Replace with the WebDriver you use
driver.maximize_window()

# Navigate to the page
driver.get("https://www.tutorialspoint.com/selenium/practice/browser-windows.php")

try:
    # Handle first alert button
    alert_button1 = driver.find_element(By.ID, "alert")
    alert_button1.click()

    # Switch to alert and accept it
    alert = Alert(driver)
    print("Alert text:", alert.text)  # Print the alert text
    alert.accept()
    time.sleep(2)

    # Handle second alert button (confirm alert)
    confirm_button = driver.find_element(By.ID, "confirm")
    confirm_button.click()

    # Switch to confirm alert and dismiss it
    confirm_alert = Alert(driver)
    print("Confirm alert text:", confirm_alert.text)  # Print the confirm alert text
    confirm_alert.dismiss()
    time.sleep(2)

    # Handle third alert button (prompt alert)
    prompt_button = driver.find_element(By.ID, "prompt")
    prompt_button.click()

    # Switch to prompt alert, input text, and accept it
    prompt_alert = Alert(driver)
    print("Prompt alert text:", prompt_alert.text)  # Print the prompt alert text
    prompt_alert.send_keys("Hello, Selenium!")
    prompt_alert.accept()
    time.sleep(2)

finally:
    # Close the browser
    driver.quit()
