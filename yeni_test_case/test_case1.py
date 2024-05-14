import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

class TestProductPurchase:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com/")

    def teardown_method(self):
        self.driver.quit()
    
    def test_invalid_login(self):
        username = WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((By.ID, "user-name")))
        username.send_keys("standard_user")
        password = WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((By.ID, "password")))
        password.send_keys("secret_sauce")
        loginButton = WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((By.ID, "login-button")))
        loginButton.click()
    
    def test_add_to_cart(self):
        
        add_to_cart_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]')))
        add_to_cart_button.click()
        go_to_basket = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="shopping_cart_container"]/a')))
        go_to_basket.click()
        checkout_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="checkout"]')))
        checkout_button.click()

    def test_checkout_information(self):
        first_name = WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((By.ID, "first-name")))
        first_name.send_keys("Furkan")
        last_name = WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((By.ID, "last-name")))
        last_name.send_keys("Gümüşkaya")
        postal_code = WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((By.ID, "postal-code")))
        postal_code.send_keys("34250")
        continue_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="continue"]')))
        continue_button.click()

    def test_finish_shopping(self):
        finish_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="finish"]')))
        finish_button.click()
        thank_you_message = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="checkout_complete_container"]/h2')))
        assert thank_you_message.text == "Thank you for your order!"
        print("Alışveriş işlemi başarıyla tamamlandı.")

        
deneme = TestProductPurchase()
deneme.setup_method()  
deneme.test_invalid_login()
deneme.test_add_to_cart()
deneme.test_checkout_information()
deneme.test_finish_shopping()
sleep(10)
deneme.teardown_method()
