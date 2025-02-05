import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def setup():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()
    yield driver
    driver.quit()

def test_login_success(setup):
    driver = setup
    wait = WebDriverWait(driver, 10)

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    inventory_list = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "inventory_list")))
    assert inventory_list.is_displayed(), "Login Failed"
    print("✅ Login Successful")

def test_add_to_cart(setup):
    driver = setup
    wait = WebDriverWait(driver,10)
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    driver.find_element(By.ID,"add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.CLASS_NAME,"shopping_cart_link").click()

    cart_item = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "inventory_item_name")))
    assert "Sauce Labs Backpack" in cart_item.text, "❌ Item not added to cart"
    print("✅ Item successfully added to cart")