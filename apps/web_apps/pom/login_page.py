'''
Created on Apr 4, 2020

@author: nqkhanh
'''

from selenium.webdriver.common.by import By
from utils.common.selenium_tools import selenium_tools

class login_page():
    '''
        This class define all locators and function on login page
    '''

    def __init__(self):
        '''
            Set to find element on login page
        '''
        self.SELENIUM_COMMON = selenium_tools()
        self.LOGIN_TXT = "h1.auth-header" #CSS Selector
        self.USERNAME_TF = "input.username.auth-input.form-control" #CSS Selector
        self.PASSWORD_TF = "input.password.auth-input.form-control" #CSS Selector
        self.LOGIN_BTN = "button.mb-4.auth-button.btn.btn-primary" #CSS Selector
        self.CREATE_ACCOUNT_BTN = "a.auth-link" #CSS Selector    #href="/register"
        self.FORGOT_PASSWORD_BTN = "a.px-0.forgot-password-link" #CSS Selector    href="/forgot-password"
    
    def loading_login_page(self, driver):
        if self.SELENIUM_COMMON.wait_for_element_appear(driver, By.CSS_SELECTOR, self.LOGIN_TXT, 5):
            return True
        else:
            return False
    
    def input_username_login(self, driver, userName):
        self.SELENIUM_COMMON.setText(driver, By.CSS_SELECTOR, self.USERNAME_TF, userName)
    
    def input_password_login(self, driver, passWord):
        self.SELENIUM_COMMON.setText(driver, By.CSS_SELECTOR,self.PASSWORD_TF, passWord)
        
    def click_login_button(self, driver):
        self.SELENIUM_COMMON.click(driver, By.CSS_SELECTOR,self.LOGIN_BTN)
    
    def click_create_account_button(self, driver):
        self.SELENIUM_COMMON.click(driver, By.CSS_SELECTOR,self.CREATE_ACCOUNT_BTN)