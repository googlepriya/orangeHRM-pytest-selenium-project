from selenium.webdriver.common.by import By

class PimEmployeeListPage:
    def __init__(self,driver):
        self.driver = driver
        self.add_employee_button = (By.XPATH,"(//button[@type='button'])[5]")
        self.first_name = (By.NAME,"firstName")
        self.last_name = (By.NAME,"lastName")
        self.save_button = (By.XPATH,"//button[@type='submit']")
        self.employee_list_tab = (By.XPATH,"(//a)[15]")
        self.search_name_imput = (By.XPATH,"(//input)[2]")
        self.search_button = (By.XPATH,"(//button)[6]")
        self.delete_button = (By.XPATH,"(//button[@type='button'])[7]")
        self.delete_confirm_button = (By.XPATH,"(//button)[12]")
    
    def add_employee(self, first_name,last_name):
        self.driver.find_element(*self.add_employee_button).click()
        self.driver.find_element(*self.first_name).send_keys(first_name)
        self.driver.find_element(*self.last_name).send_keys(last_name)
        self.driver.find_element(*self.save_button).click()

    def search_and_delete_employee(self,name):
        self.driver.find_element(*self.employee_list_tab).click()
        self.driver.find_element(*self.search_name_imput).send_keys(name)
        self.driver.find_element(*self.search_button).click()
        self.driver.find_element(*self.delete_button).click()
      #  self.driver.find_element(*self.delete_confirm_button).click()
    

