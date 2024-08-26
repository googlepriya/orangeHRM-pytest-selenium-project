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
    employee_page.search_employee("Ria Dhomas")
    time.sleep(4)

    search_result = driver.find_element(By.XPATH,"//div[contains(text(), 'Ria ')]").text
    assert "Ria" in search_result

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
    employee_page = PimEmployeeListPage(driver)
    employee_page.search_employee("Fatima  munavar")
    time.sleep(3)

    #Update the employee profile 
    employee_page.update_employee()

def test_delete_employee(setup):
    driver = setup
    driver.get("https://opensource-demo.orangehrmlive.com/")

    # Login
    login_page = LoginPage(driver)
    login_page.login("Admin", "admin123")

    #Navigate to PIM (Employee Management)
    dashboard_page = DashboardPage(driver)
    dashboard_page.navigate_to_pim_menu()

    #Searching  the employee
    employee_page = PimEmployeeListPage(driver)
    employee_page.search_employee("Ria Dhomas")
    time.sleep(4)

    #Delete the Employee
    employee_page.delete_employee()

    #Validate the employee record is deleted
    time.sleep(2)
    no_records_text = driver.find_element(By.XPATH,"//span[text()='No Records Found']").text
    assert "No Records Found" in no_records_text

  