from pages.login_page import LoginPage
import pytest
from selenium import webdriver
import time

@pytest.mark.skip
def setup():
    #Initialize the webdriver
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver

def test_login_valid(setup):
    driver = setup
    driver.get("https://opensource-demo.orangehrmlive.com/")

    #Create instance of Login Page
    login_page = LoginPage(driver)

    #Perform login
    login_page.login("Admin","admin123")

    #Assertion to check login
    assert "OrangeHRM" in driver.title
    print(driver.title)
    time.sleep(3)




