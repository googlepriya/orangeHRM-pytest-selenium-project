import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.pim_employee_list import PimEmployeeListPage
from selenium.webdriver.common.by import By
import time

@pytest.fixture
def setup():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver

def test_add_employee(setup):
    driver = setup
    driver.get("https://opensource-demo.orangehrmlive.com/")

    # Login
    login_page = LoginPage(driver)
    login_page.login("Admin", "admin123")

    #Navigate to PIM (Employee Management)
    dashboard_page = DashboardPage(driver)
    dashboard_page.navigate_to_pim_menu()

    # Add Employee
    employee_page = PimEmployeeListPage(driver)
    employee_page.add_employee("Ria","Dhomas")
    time.sleep(4)

    # Validate that the employee was added by searching for the employee
    employee_page.search_and_delete_employee("Ria Dhomas")
    time.sleep(4)

    #search_result = driver.find_element(By.XPATH,"//div[contains(text(), 'Ria ')]").text
    #assert "Ria" in search_result

"""
def test_search_employee(setup):
    driver = setup
    employee_page = PimEmployeeListPage(driver)
    employee_page.search_employee


def test_delete_employee(setup):
    driver = setup
    driver.get("https://opensource-demo.orangehrmlive.com/")

    # Login
    login_page = LoginPage(driver)
    login_page.login("Admin", "admin123")

    #Navigate to PIM (Employee Management)
    dashboard_page = DashboardPage(driver)
    dashboard_page.navigate_to_pim_menu()

    # Search Employee
    employee_page = PimEmployeeListPage(driver)
    employee_page.search_and_delete_employee("Ria Dhomas")
    
  """
  