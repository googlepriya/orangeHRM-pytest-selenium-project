import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage  
import time

@pytest.mark.skip
def setup():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver

def test_dashboard(setup):
    driver = setup
    driver.get("https://opensource-demo.orangehrmlive.com/")

    # Login
    login_page = LoginPage(driver)
    login_page.login("Admin", "admin123")
    
    #Validate Dashboard
    dashboard_page = DashboardPage(driver)
    test_dashboard = dashboard_page.get_dashboard_page()
    assert "Dashboard" in test_dashboard
    time.sleep(3)



