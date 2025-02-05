from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Chrome()
driver.get("https://www.saucedemo.com/")
driver.maximize_window()

username=driver.find_element(By.ID,"user-name")
password=driver.find_element(By.ID,"password")
loginBtn=driver.find_element(By.ID,"login-button")

username.send_keys("standard_user")
password.send_keys("secret_sauce")
loginBtn.click()

time.sleep(2)

if "inventory" in driver.current_url:
    print("Login Succesfully")
else:
    print("Login Fail")

driver.quit()