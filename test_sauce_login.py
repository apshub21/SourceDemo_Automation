from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec  # Fixed case

# Initialize WebDriver
driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")
driver.maximize_window()

wait = WebDriverWait(driver, 10)  

username = wait.until(ec.presence_of_element_located((By.ID, "user-name")))
username.send_keys("standard_user")

password = wait.until(ec.presence_of_element_located((By.ID, "password")))
password.send_keys("secret_sauce")

login_btn = wait.until(ec.presence_of_element_located((By.ID, "login-button")))
login_btn.click()

wait.until(ec.presence_of_element_located((By.ID, "inventory_container")))  # Fixed ID
if "inventory" in driver.current_url:
    print("Successful")
else:
    print("Fail")

driver.quit()
