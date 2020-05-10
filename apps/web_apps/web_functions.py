'''
Created on Apr 2, 2020

@author: nqkhanh
'''

import time
from robot.libraries.BuiltIn import BuiltIn
from robot.api import logger
#from utils.grid_manager.selenium_driver import selenium_driver
from utils.grid_manager.grid_driver_factory import grid_driver_factory
#from selenium.webdriver import firefox
from web_apps.pom.login_page import login_page
from web_apps.pom.register_page import register_page
from web_apps.pom.dash_board_page import dash_board_page
from web_apps.pom.project_page import project_page


__version__ = '0.0.0.1'

class web_functions(object):
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    """ Containing driver and all basic funciton.s

    If the class has public attributes, they may be documented here
    in an ``Attributes`` section and follow the same formatting as a
    function's ``Args`` section. Alternatively, attributes may be documented
    inline with the attribute's declaration (see __init__ method below).

    Properties created with the ``@property`` decorator should be documented
    in the property's getter method.

    Attributes:
        attr1 (str): Description of `attr1`.
        attr2 (:obj:`int`, optional): Description of `attr2`.

    """

    def __init__(self):
        """Example of docstring on the __init__ method.

        Examples:
            N/A

        Args:
            desired_capabilities: - A dictionary of capabilities to request when
             starting the browser session. Required parameter.
            command_executor: - Either a string representing URL of the remote server or a custom
             remote_connection.RemoteConnection object. Defaults to 'http://127.0.0.1:4444/wd/hub'.

        """
        print('*INFO:%d* init atda_web instance')
        CHROME = {'browserName': 'chrome', 'version': '', 'platform': 'ANY'}
        command_executor='http://127.0.0.1:4444/wd/hub'
        BuiltIn().log_to_console('Init ATDA')
        self.desired_capabilities = CHROME
        self.command_executor = command_executor
        #self.is_dashboard = False
        #self.is_promt = False
    
    ''' LOGIN PAGE '''
    
    def verify_login_page(self):
        logger.info("Verifying login page ...")
        #print("start function login page")
        if login_page().loading_login_page(self.driver):
            logger.info("Login page is loaded successfully")
        else:
            logger.info("Cannot load Login page")
            
    def input_username_password_login_page(self, username, password):
        '''input username and password in login page'''
        login_page().input_username_login(self.driver, username)
        login_page().input_password_login(self.driver, password)
 
    def click_login_button(self):
        '''click login button'''
        logger.info("Start logining user")
        login_page().click_login_button(self.driver)
    
    
    ''' CREATE ACCOUNT PAGE '''
    
    def nav_to_register_page(self):
        '''navigate to creare account page'''
        logger.info("start function navigate to register page")
        login_page().click_create_account_button(self.driver)
    
    def verify_loading_register_page(self):
        '''verify that register page is loaded'''
        logger.info("Verifying register page ...")
        if register_page().loading_register_page(self.driver):
            logger.info("Register page is loaded successfully")
        else:
            logger.info("Cannot load Register page")
 
    def input_username_psd_create_account_page(self, userName_rg, email_rg, fullname_rg, passWord_rg):
        '''input username and password in creare account page'''
        logger.info("Inputing user to register page ...")
        register_page().input_username_register(self.driver, userName_rg)
        register_page().input_email_register(self.driver, email_rg)
        register_page().input_fullname_register(self.driver, fullname_rg)
        register_page().input_password_register(self.driver, passWord_rg)
        register_page().input_confirm_password_register(self.driver, passWord_rg)
        logger.info("Input user to register page successfully")
        
    def click_register_button(self):
        '''click login button'''
        logger.info("Start creating user")
        register_page().click_register_button(self.driver)
    
    
    ''' DASHBOARD PAGE'''
        
    def verify_dash_board_page(self, timeOut=3):
        logger.info("Verifying user dashboard  ...")
        if dash_board_page().is_dash_board_page(self.driver, timeOut):
            logger.info("user is at dashboard")
            self.is_dashboard = True
        else:
            logger.info("user is at dashboard")
            self.is_dashboard = False
    
    ''' --- SETTINGS MENU '''
    def click_change_password_menu(self):
        logger.info("start clicking CHANGE PASSWORD ...")
        if dash_board_page().is_avatar(self.driver):
            dash_board_page().click_avatar(self.driver)
            time.sleep(1) #Make sure settings menu is displayed
            dash_board_page().click_settings_menu(self.driver, "change_password")
        logger.info("Clicked CHANGE PASSWORD")
    
    def click_profile_menu(self):
        logger.info("start clicking PROFILE ...")
        if dash_board_page().is_avatar(self.driver):
            dash_board_page().click_avatar(self.driver)
            time.sleep(1) #Make sure settings menu is displayed
            dash_board_page().click_settings_menu(self.driver, "profile")
        logger.info("Clicked PROFILE")
            
    def click_settings_menu(self):
        logger.info("start clicking SETTINGS ...")
        if dash_board_page().is_avatar(self.driver):
            dash_board_page().click_avatar(self.driver)
            time.sleep(1) #Make sure settings menu is displayed
            dash_board_page().click_settings_menu(self.driver, "settings")
        logger.info("Clicked SETTINGS")
    
    def click_projects_menu(self):
        logger.info("start clicking PROJECTS ...")
        if dash_board_page().is_avatar(self.driver):
            dash_board_page().click_avatar(self.driver)
            time.sleep(1) #Make sure settings menu is displayed
            dash_board_page().click_settings_menu(self.driver, "projects")
        logger.info("Clicked PROJECTS")
    
    def click_logout_menu(self):
        logger.info("start clicking LOGOUT ...")
        if dash_board_page().is_avatar(self.driver):
            dash_board_page().click_avatar(self.driver)
            time.sleep(1) #Make sure settings menu is displayed
            dash_board_page().click_settings_menu(self.driver, "logout")
        logger.info("Clicked LOGOUT")
    
    def user_log_out(self):
        logger.info("Starting logout ..")
        while dash_board_page().verify_edit_delete_project_promt(self.driver):
            logger.info("Project Edit/Delete promt is canceling ....")
            dash_board_page().click_cancel_project_confirm(self.driver)
            break
        self.click_logout_menu()
        if login_page().loading_login_page(self.driver):
            logger.info("Logout done")
        else:
            logger.info("Logout failed !!!")
    
    ''' --- '''
    
    def click_new_project(self):
        dash_board_page().click_new_project(self.driver)
    
    def input_project(self, projName="", projDesc=""):
        if dash_board_page().verify_edit_delete_project_promt(self.driver):
            dash_board_page().input_project_name(self.driver, projName)
            dash_board_page().input_project_description(self.driver, projDesc)
    
    def input_project_name(self, projName=""):
        if dash_board_page().verify_edit_delete_project_promt(self.driver):
            dash_board_page().input_project_name(self.driver, projName)
    
    def input_project_description(self, projDesc=""):
        if dash_board_page().verify_edit_delete_project_promt(self.driver):
            dash_board_page().input_project_description(self.driver, projDesc)
    
    def click_create_edit_project(self):
        while dash_board_page().verify_edit_delete_project_promt(self.driver):
            dash_board_page().click_create_edit_project_confirm(self.driver)
            break
    
    def click_delete_project(self):
        while dash_board_page().verify_edit_delete_project_promt(self.driver):
            dash_board_page().click_delete_project_confirm(self.driver)
            break
    
    def verify_message_project_name(self, messageWarn):
        logger.info("Start verify .... ")
        get_message = dash_board_page().get_text_invalid_project_name(self.driver)
        #logger.info((get_message))
        #logger.info(messageWarn)
        if str(get_message) == str(messageWarn).strip():
            logger.info("Matched - " + str(messageWarn))
            return True
        logger.info("NOT match - message is got: #" + str(messageWarn) + "#")
        return False
    
    def click_project(self, projName):
        dash_board_page().click_project(self.driver, projName)
        
    def click_project_to_edit(self, projName):
        dash_board_page().click_project_edit(self.driver, projName)
    
    def click_project_to_delete(self, projName):
        dash_board_page().click_project_delete(self.driver, projName)
    
    def get_project_namw(self):
        dash_board_page().get_list_project_name_link(self.driver)
    
    def click_cancel_project_promt(self):
        while dash_board_page().verify_edit_delete_project_promt(self.driver):
            dash_board_page().click_cancel_project_confirm(self.driver)
            logger.info("Project Edit/Delete promt is canceled!")
            break
            #self.is_promt = False
            #self.is_dashboard = True
    
    def back_to_dashboard(self):
        dash_board_page().click_back_to_dash_board(self.driver)
          
    ''' ''PROJECT PAGE'''
    def verify_project_page(self):
        if project_page().is_project_page(self.driver):
            logger.info("Project Page is loaded!")
        else:
            logger.info("Project Page is NOT loaded!")
    
    def click_feature_test_suite(self):
        project_page().click_project_feature(self.driver, "test suite")
    
    def verify_all_features(self):
        if project_page().verify_project_feature(self.driver, "Test Suite") and project_page().verify_project_feature(self.driver, "Test Case") and project_page().verify_project_feature(self.driver, "Execution") and project_page().verify_project_feature(self.driver, "Bug ID") and project_page().verify_project_feature(self.driver, "Report") and project_page().verify_project_feature(self.driver, "Setting"):
            logger.info("All features are exsited!")
    
    def open_browser(self, url):
        """Launch web browser with ATDA server info
  
        The __init__ method may be documented in either the class level
        docstring, or as a docstring on the __init__ method itself.
  
        Either form is acceptable, but the two should not be mixed. Choose one
        convention to document the __init__ method and be consistent with it.
  
        Note:
            Do not include the `self` parameter in the ``Args`` section.
  
        Args:  
            url (str): Link to website
  
        """
#         BuiltIn().log_to_console('Launching browser: ' + self.desired_capabilities.get('browserName'),'')
        BuiltIn().log_to_console('Open Browser: '+str(self.desired_capabilities)+','+self.command_executor)
        self.driver = grid_driver_factory().create_driver(self.command_executor, self.desired_capabilities)
        BuiltIn().log_to_console('Open URL')
        self.driver.get(url)
        self.driver.maximize_window()
        self.driver.set_page_load_timeout(30)
    
    def close_browser(self):
        """Close web browser
 
        The __init__ method may be documented in either the class level
        docstring, or as a docstring on the __init__ method itself.
 
        Either form is acceptable, but the two should not be mixed. Choose one
        convention to document the __init__ method and be consistent with it.
 
        Note:
            Do not include the `self` parameter in the ``Args`` section.
 
        Args:  
            url (str): Link to website
 
        """
        print('*INFO:%d* Start function close_browser' % (time.time()*1000))
        self.driver.quit()
        print('*INFO:%d* close_browser successfully' % (time.time()*1000))  