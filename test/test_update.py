import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.update_employee import EmployeeListPage
from selenium.webdriver.common.by import By
import time

@pytest.fixture
def setup():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver

def test_update_employee(setup):
    driver = setup
    driver.get("https://opensource-demo.orangehrmlive.com/")

    #Login
    login_page = LoginPage(driver)
    login_page.login("Admin","admin123")

    #Navigate to PIM
    dashboard_page = DashboardPage(driver)
    dashboard_page.navigate_to_pim_menu()

    #Searching the employee
    employee_page = EmployeeListPage(driver)
    employee_page.search_employee("Fatima  munavar")
    time.sleep(3)

    #Update the employee profile 
    employee_page.update_employee()

