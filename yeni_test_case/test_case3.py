from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
import pytest

class test_case3:

    def setup_method(self):
        
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com/")

    def teardown_method(self):
        self.driver.quit()

    def test_valid_login(self):
        username = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.ID,"user-name")))
        username.send_keys("standard_user")
        password = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.ID,"password")))
        password.send_keys("secret_sauce")
        login_button = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.ID,"login-button")))
        login_button.click()

        assert "inventory.html" in self.driver.current_url
        print("successful entry")

    def test_successful_logout(self):
            
            self.test_valid_login()

            burger_menu = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="react-burger-menu-btn"]')))
            burger_menu.click()
            logout_button = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="logout_sidebar_link"]')))
            logout_button.click()

            assert "https://www.saucedemo.com/" in self.driver.current_url
            print("successful exit")

if __name__ == "__main__":
     pytest.main(["-v", "--html=report.html"])
     
            




