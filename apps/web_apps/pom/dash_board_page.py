'''
Created on Apr 5, 2020

@author: nqkhanh
'''

import time
from robot.api import logger
from selenium.webdriver.common.by import By
from utils.common.selenium_tools import selenium_tools

class dash_board_page():
    '''
        This class define all locators and function on dash-board page 
    '''

    def __init__(self):
        '''
            Set to find element on das-board page
        '''
        self.SELENIUM_COMMON = selenium_tools()
        self.AVATAR = "a.nav-link>img.img-avatar" #CSS SELECTOR
        self.PROJECT_LBL = "div.project-header.row>div>h2" #CSS SELECTOR        
        self.SETTINGS_MENU = "div.user-dropdown.dropdown-menu.dropdown-menu-right.show" #CSS SELECTOR
        self.LIST_OF_MENU = "div.user-dropdown.dropdown-menu.dropdown-menu-right.show>button.dropdown-item" #CSS SELECTOR
        self.CONTENT_TAB = "div.tab-content" #CSS SELECTOR
        self.CONTENT_TAB_PANE_ACTIVE = "div.tab-content>div.tab-pane.active" #CSS SELECTOR
        self.CONTENT_TAB_PANE_UNACTIVE = "div.tab-content>div.tab-pane" #CSS SELECTOR
        self.TAB_ALL = "//*[@id='root']/div/div/div/div/ul/li[1]/a" #XPath
        self.TAB_YOUR_PROJECTS = "//*[@id='root']/div/div/div/div/ul/li[2]/a" #XPath
        self.PROJECT_ITEMS = "div.tab-content>div.tab-pane.active>div.project-item" #CSS SELECTOR
        self.NEW_PROJECT_BTN = "div.project-header.row>div>button.new-project-btn.btn.btn-secondary" #CSS SELECTOR
        self.EDIT_DELETE_PROJECT_PROMT = "div.modal-content" #CSS SELECTOR
        self.PROJECT_NAME_IS_EMPTY = "div.modal-content>div.modal-body>span" #CSS SELECTOR
        self.EDIT_PROJECT_NAME = "div.modal-content>div.modal-body>input.form-control" #CSS SELECTOR
        self.EDIT_PROJECT_DESCRIPTION_TXT = "div.modal-content>div.modal-body>textarea.form-control" #CSS SELECTOR
        self.PROJECT_CREATE_EDIT_BTN = "div.modal-content>div.modal-footer>button.btn.btn-primary" #CSS SELECTOR
        self.PROJECT_CANCEL_BTN = "div.modal-content>div.modal-footer>button.btn.btn-secondary" #CSS SELECTOR
        self.PROJECT_DELETE_BTN = "div.modal-content>div.modal-footer>button.btn.btn-danger" #CSS SELECTOR
        self.PROJECT_INPUT_INVALID = "div.modal-content>div.modal-body>input.is-invalid.form-control" #CSS SELECTOR
        self.BACK_TO_DASHBOARD = "header.app-header.navbar>ul.d-md-down-none.navbar-nav" #CSS SELECTOR
        self.LOG_OUT_BTN = "button.logout.dropdown-item" #CSS SELECTOR
        self.PROJECT_ROW = "div.tab-content>div.tab-pane.active>div.project-item>div.row>div.d-flex.flex-row.align-items-center.col-sm-6"
        self.PROJECT_NAME = "div.tab-content>div.tab-pane.active>div.project-item>div.row>div.d-flex.flex-row.align-items-center.col-sm-6>a>span"
        self.PROJECT_LINK = "div.tab-content>div.tab-pane.active>div.project-item>div.row>div.d-flex.flex-row.align-items-center.col-sm-6>a"
        self.PROJECT_EDIT = "div.tab-content>div.tab-pane.active>div.project-item>div.row>div.d-flex.flex-row.justify-content-end.col-sm-6>button.project-action-btn.btn.btn-secondary>i.fa.fa-pencil"
        self.PROJECT_DELETE = "div.tab-content>div.tab-pane.active>div.project-item>div.row>div.d-flex.flex-row.justify-content-end.col-sm-6>button.project-action-btn.btn.btn-secondary>i.fa.fa-trash"
    
    def is_dash_board_page(self, driver, timeOut=3):
        if self.SELENIUM_COMMON.wait_for_element_appear(driver, By.CSS_SELECTOR, self.CONTENT_TAB, timeOut):
            return True
        else:
            return False
    
    def is_avatar(self, driver):
        i = 0
        while i < 5:
            i += 1
            logger.info("Verifying avatar ." +"."*i)
            avatar_el = driver.find_elements(By.CSS_SELECTOR, self.AVATAR)
            if len(avatar_el) > 0:
                #logger.info(len(avatar_el))
                return avatar_el
            else:
                time.sleep(1)
        logger.info("[FAILED] Element NOT found!")
        return 0
    
    def click_avatar(self, driver):
        logger.info("starting click avatar.")
        #avatar_el = driver.find_element(By.CSS_SELECTOR, self.AVATAR)
        #logger.info(avatar_el)
        avatar_el = self.is_avatar(driver)
        if len(avatar_el) > 0:
            avatar_el[0].click()
            logger.info("click avatar OK.")
            return
        
    def check_settings_menu(self, driver):
        i = 0
        while i < 5:
            i += 1
            logger.info("Verifying settings menu is shown ." +"."*i)
            settings_menu_el = driver.find_elements(By.CSS_SELECTOR, self.SETTINGS_MENU)
            if len(settings_menu_el) > 0:
                logger.info("OK")
                return True
            else:
                time.sleep(1)
        logger.info("[FAILED] Settings menu is NOT shown.")
        return False
    
    def click_settings_menu(self, driver, menu=None):
        '''MUST click avatar before user this function'''
        settings_menu_el = driver.find_elements(By.CSS_SELECTOR, self.LIST_OF_MENU)
        menu = menu.strip()
        list_of_menu = {
            "change_password" : 0,
            "profile" : 1,
            "settings" : 2,
            "projects" : 3,
            "logout" : 4
            }
        for item in list_of_menu:
            if item == menu.lower():
                logger.info(item)
                settings_menu_el[list_of_menu[item]].click()
            
    def verify_edit_delete_project_promt(self, driver):
        ''' Please Click New Project or Edit or Delete to find out '''
        logger.info("Verifying EDIT or DELETE project promt is shown ")
        i = 0
        while i < 5:
            i += 1
            logger.info("Verifying ." +"."*i)
            project_promt_el = driver.find_elements(By.CSS_SELECTOR, self.EDIT_DELETE_PROJECT_PROMT)
            if len(project_promt_el) > 0:
                logger.info("Verify OK !")
                return True
            else:
                time.sleep(1)
        logger.info("[FAILED] EDIT or DELETE project promt is NOT shown.")
        return False
    
    def input_project_name(self, driver, projectName):
        self.SELENIUM_COMMON.setText(driver, By.CSS_SELECTOR, self.EDIT_PROJECT_NAME, projectName)
        
    def input_project_description(self, driver, projectDesciption):
        self.SELENIUM_COMMON.setText(driver, By.CSS_SELECTOR, self.EDIT_PROJECT_DESCRIPTION_TXT, projectDesciption)
        
    def click_cancel_project_confirm(self, driver):
        ''' MUST BE IN EDIT - CREATE - DELETE PROJECT PROMT '''
        logger.info("start canceling...")
        self.SELENIUM_COMMON.click(driver, By.CSS_SELECTOR, self.PROJECT_CANCEL_BTN)
        logger.info("... Cancel completed")
    
    def click_create_edit_project_confirm(self, driver):
        ''' MUST BE IN EDIT - CREATE PROJECT PROMT '''
        logger.info("start edting ...")
        self.SELENIUM_COMMON.click(driver, By.CSS_SELECTOR, self.PROJECT_CREATE_EDIT_BTN)
        logger.info("... edit completed")
    
    def click_delete_project_confirm(self, driver):
        ''' MUST BE IN DELETE PROJECT PROMT '''
        logger.info("Start deleting ...")
        self.SELENIUM_COMMON.click(driver, By.CSS_SELECTOR, self.PROJECT_DELETE_BTN)
        logger.info("... Delete completed.")
    
    def is_input_invalid(self, driver):
        if self.SELENIUM_COMMON.isElement(driver, By.CSS_SELECTOR, self.PROJECT_INPUT_INVALID):
            return True
        else:
            return False
    
    def get_text_invalid_project_name(self, driver):
        return self.SELENIUM_COMMON.getAttribute(driver, By.CSS_SELECTOR, self.PROJECT_NAME_IS_EMPTY, "innerHTML")
    
    def verify_projects(self, driver):
        if self.SELENIUM_COMMON.isElement(driver, By.CSS_SELECTOR, self.PROJECT_ITEMS):
            return True
        else:
            return False
    
    def get_projects(self, driver):
        logger.info("start getting projects ...")
        projects_list = driver.find_elements(By.CSS_SELECTOR, self.PROJECT_ITEMS)
        if len(projects_list) > 0:
            logger.info("Projects exsited")
            return projects_list
        else:
            logger.info("No Project is found.")
            return False
        logger.info("Return list projects after this info")
    
    def click_project(self, driver, projName):
        logger.info("click project to open ..")
        while self.verify_projects(driver):
            projects_name = driver.find_elements(By.CSS_SELECTOR, self.PROJECT_NAME)
            index_of = 0
            for item in projects_name:
                if str(projName) == str(item.get_attribute("innerHTML")):
                    projects_name[index_of].click()
                    break
                index_of += 1
            break
    
    def click_project_edit(self, driver, projName):
        logger.info("click project to editing ..")
        while self.verify_projects(driver):
            projects_name = driver.find_elements(By.CSS_SELECTOR, self.PROJECT_NAME)
            index_of = 0
            for item in projects_name:
                if str(projName) == str(item.get_attribute("innerHTML")):
                    project_edit_list = driver.find_elements(By.CSS_SELECTOR, self.PROJECT_EDIT)
                    project_edit_list[index_of].click()
                    break
                index_of += 1
            break
    
    def click_project_delete(self, driver, projName):
        logger.info("click project to delete " + str(projName) + " ...")
        while self.verify_projects(driver):
            projects_name = driver.find_elements(By.CSS_SELECTOR, self.PROJECT_NAME)
            index_of = 0
            for item in projects_name:
                if str(projName) == str(item.get_attribute("innerHTML")):
                    project_delete_list = driver.find_elements(By.CSS_SELECTOR, self.PROJECT_DELETE)
                    project_delete_list[index_of].click()
                    time.sleep(1) #Waiting for promt is displayed
                    break
                index_of += 1
            break
    
    def click_new_project(self, driver):
        logger.info("start open project promt ...")
        new_project_el = driver.find_element(By.CSS_SELECTOR, self.NEW_PROJECT_BTN)
        new_project_el.click()
        logger.info("Project promt is shown.")
    
    def click_back_to_dash_board(self, driver):
        logger.info("Back to Dashboard ...")
        back_2_dashboard_el = driver.find_element(By.CSS_SELECTOR, self.BACK_TO_DASHBOARD)
        back_2_dashboard_el.click()
        time.sleep(1)