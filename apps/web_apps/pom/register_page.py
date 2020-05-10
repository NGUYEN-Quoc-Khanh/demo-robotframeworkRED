'''
Created on Apr 5, 2020

@author: nqkhanh
'''

from selenium.webdriver.common.by import By
from utils.common.selenium_tools import selenium_tools

class register_page():
    '''
        This class define all locators and function on create account page
    '''

    def __init__(self):
        '''
            Set to find element on login page
        '''
        self.SELENIUM_COMMON = selenium_tools()
        self.REGISTER_TXT = "h1.auth-header" #CSS SELECTOR
        self.USERNAME_TF = "input.username.auth-input.form-control" #CSS SELECTOR
        self.EMAIL_TF = "input.email.auth-input.form-control" #CSS SELECTOR
        self.FULLNAME_TF = "input.fullName.auth-input.form-control" #CSS SELECTOR
        self.PASSWORD_TF = "input.password.auth-input.form-control" #CSS SELECTOR
        self.PASSWORD_CONFIRM_TF = "input.confirm-password.auth-input.form-control" #CSS SELECTOR
        self.REGISTER_BTN = "button.mb-4.auth-button.btn.btn-primary" #CSS SELECTOR
        self.I_HAVE_ACCOUNT_BTN = "a.auth-link" #CSS SELECTOR
    
    def loading_register_page(self, driver):
        if self.SELENIUM_COMMON.wait_for_element_appear(driver, By.CSS_SELECTOR, self.REGISTER_TXT, 5):
            return  True
        else:
            return False
    
    def input_username_register(self, driver, userName):
        self.SELENIUM_COMMON.setText(driver, By.CSS_SELECTOR, self.USERNAME_TF, userName)
    
    def input_email_register(self, driver, email):
        self.SELENIUM_COMMON.setText(driver, By.CSS_SELECTOR, self.EMAIL_TF, email)
    
    def input_fullname_register(self, driver, fullName):
        self.SELENIUM_COMMON.setText(driver, By.CSS_SELECTOR, self.FULLNAME_TF, fullName)
    
    def input_password_register(self, driver, passWord):
        self.SELENIUM_COMMON.setText(driver, By.CSS_SELECTOR,self.PASSWORD_TF, passWord)
        
    def input_confirm_password_register(self, driver, passWord_cf):
        self.SELENIUM_COMMON.setText(driver, By.CSS_SELECTOR,self.PASSWORD_CONFIRM_TF, passWord_cf)
        
    def click_register_button(self, driver):
        self.SELENIUM_COMMON.click(driver, By.CSS_SELECTOR,self.REGISTER_BTN)