
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout=60)
    
    def go_to(self, url):
        self.driver.get(url)
        self.driver.maximize_window()
    
    def login(self, username, password):
        usernameField =self. wait.until(EC.element_to_be_clickable((By.ID,"user-name")))
        usernameField.clear()
        usernameField.click()
        usernameField.send_keys(username)
        passwordField = self.driver.find_element(By.ID,"password")
        passwordField.click()
        passwordField.send_keys(password)
        loginLink = self.wait.until(EC.element_to_be_clickable((By.ID,"login-button")))
        loginLink.click()
       
    
    def get_text(self):
        element = self.wait.until(EC.visibility_of_element_located((By.XPATH,"//span[@class='title']")))
        return element.text
    
    def confirm(self,elementID):
        self.wait.until(EC.element_to_be_clickable((By.ID,elementID))).click()
    
    def get_text_items(self,elementID):
        element = self.driver.find_element(By.ID,elementID).text
        return element
        
    
    def checkout(self,name,surname,postCode):
        firstName = self.driver.find_element(By.ID,"first-name")
        firstName.click()
        firstName.send_keys(name)
        lastName = self.driver.find_element(By.ID,"last-name")
        lastName.click()
        lastName.send_keys(surname)
        zipCode = self.driver.find_element(By.ID,"postal-code")
        zipCode.click()
        zipCode.send_keys(postCode)
        
        
    def logout(self):
        assert self.wait.until(EC.visibility_of_element_located((By.ID,"login-button")))
        