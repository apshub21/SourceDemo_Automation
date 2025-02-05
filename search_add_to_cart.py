from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()
driver.get("https://www.saucedemo.com/")

driver.find_element(By.ID,"user-name").send_keys("standard_user")
driver.find_element(By.ID,"password").send_keys("secret_sauce")
driver.find_element(By.ID,"login-button").click()
time.sleep(3)

add_to_cart_button=driver.find_element(By.ID,"add-to-cart-sauce-labs-backpack").click()
time.sleep(3)

driver.find_element(By.CLASS_NAME,"shopping_cart_link").click()
time.sleep(3)

cart_items=driver.find_element(By.CLASS_NAME,"inventory_item_name")
if "Sauce Labs Backpack" in cart_items.text:
    print("Item added")
else:
    print("item not added")

driver.close()