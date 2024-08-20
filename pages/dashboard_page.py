from selenium.webdriver.common.by import By

class DashboardPage:
    def __init__(self,driver):
        self.driver = driver
        self.dahboard_page = (By.XPATH,"//h6[text()='Dashboard']")
        self.PIM_menu = (By.XPATH,"(//a)[3]")

    def get_dashboard_page(self):
        return self.driver.find_element(*self.dahboard_page).text
    
    def navigate_to_pim_menu(self):
        return self.driver.find_element(*self.PIM_menu).click()
    