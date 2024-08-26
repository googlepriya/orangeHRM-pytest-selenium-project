from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
class EmployeeListPage:
    def __init__(self,driver):
        self.driver = driver
        self.first_name = (By.NAME,"firstName")
        self.last_name = (By.NAME,"lastName")
        self.middle_name = (By.NAME,"middleName")
        self.employee_list_tab = (By.XPATH,"(//a)[15]")
        self.search_name_imput = (By.XPATH,"(//input)[2]")
        self.search_button = (By.XPATH,"(//button)[6]")
        self.edit_button = (By.XPATH,"(//button)[8]")
        self.update_emp_id = (By.XPATH,"(//input)[5]")
        self.update_Nationality_toggle = (By.XPATH,"(//div[@class='oxd-select-text--after'])[1]")
        self.update_Nationality = (By.XPATH,"//div[@class='oxd-select-text-input' and text()='Algerian']")
        self.update_Marital_status_toggle = (By.XPATH,"(//div[@class='oxd-select-text--after'])[1]")
        self.update_Marital_Status = (By.XPATH,"//div[@class='oxd-select-text-input' and text()='Single']")
        self.update_dob = (By.XPATH,"(//input[@placeholder='yyyy-dd-mm'])[2]")
        self.update_Female_Gender = (By.XPATH,"(//input[@type='radio'])[2]")
        self.update_Smoker = (By.XPATH,"(//input[@type='checkbox'])[1]")
        self.update_save_button1 = (By.XPATH,"(//button[@type='submit'])[1]")
        self.update_blood_type_toggle = (By.XPATH,"(//div[@class='oxd-select-text--after'])[3]")
        self.update_blood_type = (By.XPATH,"//div[@class='oxd-select-text-input' and text()='O+']")
        self.update_save_button2 = (By.XPATH,"(//button[@type='submit'])[2]")

        self.contact_details_link = (By.XPATH,"//a[text()='Contact Details']")
        self.update_city = (By.XPATH,"(//input[@class='oxd-input oxd-input--active'])[4]")
        self.update_state = (By.XPATH,"(//input[@class='oxd-input oxd-input--active'])[5]")
        self.update_PIN = (By.XPATH,"(//input[@class='oxd-input oxd-input--active'])[6]")

    def search_employee(self,name):
        self.driver.find_element(*self.employee_list_tab).click()
        self.driver.find_element(*self.search_name_imput).send_keys(name)
        self.driver.find_element(*self.search_button).click()

    def update_employee(self):
        self.driver.find_element(*self.edit_button).click()
        self.driver.find_element(*self.contact_details_link).click()
        time.sleep(4)
        self.driver.find_element(*self.update_city).send_keys("Erode")
        self.driver.find_element(*self.update_state).send_keys("Tamilnadu")
        self.driver.find_element(*self.update_PIN).send_keys("638051")

        time.sleep(4)

        
        
        """
        self.driver.find_element(*self.edit_button).click()
        self.driver.find_element(*self.middle_name).send_keys("Nic")
        firt_name = self.driver.find_element(*self.first_name)
        firt_name.send_keys(Keys.CONTROL,'a')
        firt_name.send_keys(Keys.DELETE)
        firt_name.send_keys("Google")
        emp_id = self.driver.find_element(*self.update_emp_id)
        emp_id.send_keys(Keys.CONTROL,'a')
        emp_id.send_keys(Keys.DELETE)
        emp_id.send_keys("100023")
        self.driver.find_element(*self.update_Nationality_toggle).click()
        self.driver.find_element(*self.update_Nationality).click()
        self.driver.find_element(*self.update_Marital_status_toggle).click()
        self.driver.find_element(*self.update_Marital_Status).click()
        self.driver.find_element(*self.update_blood_type_toggle).click()
        self.driver.find_element(*self.update_blood_type).click()
        """





  

    

