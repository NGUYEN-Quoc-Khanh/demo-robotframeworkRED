'''
Created on Apr 19, 2020

@author: nqkhanh
'''

from robot.api import logger
from selenium.webdriver.common.by import By
from utils.common.selenium_tools import selenium_tools
import re

class project_page(object):
    '''
        This class define all locators and function on project page
    '''


    def __init__(self):
        '''
            Set to find element on project page
        '''
        self.SELENIUM_COMMON = selenium_tools()
        self.SIDE_BAR = "div.sidebar" #CSS SELECTOR
        self.SIDE_BAR_HEADER = "div.sidebar>div.sidebar-header>h5" #CSS SELECTOR
        self.SIDE_BAR_FEATURE = "div.scrollbar-container.sidebar-nav.ps.ps-container>ul.nav>li.nav-item>a.nav-link" #CSS SELECTOR
        self.SIDE_BAR_FEATURE_ACTIVE = "div.scrollbar-container.sidebar-nav.ps.ps-container>ul.nav>li.nav-item>a.nav-link.active" #CSS SELECTOR
        self.PROJECT_MAIN_CONTENT_HEADER_LABEL = "div.main-content>div>nav>ol>li.active.breadcrumb-item" #CSS SELECTOR
        self.PROJECT_MAIN_CONTENT_BODY_CARD = "div.main-content>div>div.card" #CSS SELECTOR
        self.PROJECT_MAIN_CONTENT_SEARCH_TF = "div.main-content>div.test-suite>div.card>div.card-body>div.row>div.search.d-flex.flex-row.align-items-center.justify-content-end.col-sm-7>div.react-autosuggest__container>input.react-autosuggest__input" #CSS SELECTOR
        self.PROJECT_MAIN_CONTENT_SEARCH_BTN = "div.main-content>div.test-suite>div.card>div.card-body>div.row>div.search.d-flex.flex-row.align-items-center.justify-content-end.col-sm-7>button.btn.btn-secondary" #CSS SELECTOR
        self.PROJECT_MAIN_CONTENT_TABLE_RESPONSIVE = "div.main-content>div.test-suite>div>div.table-responsive" #CSS SELECTOR
        self.PROJECT_MAIN_CONTENT_SETTINGS_PROJECT_ID_TEXT = "div.main-content>div>div.card>div.card-body>div.d-flex>input.form-control" #CSS SELECTOR
        self.PROJECT_MAIN_CONTENT_SETTINGS_PROJECT_ID_COPY_BTN = "div.main-content>div>div.card>div.card-body>div.d-flex>button.ml-3.btn.btn-success" #CSS SELECTOR
        self.PROJECT_MAIN_CONTENT_SETTINGS_PROJECT_NAME_TF = "div.main-content>div>div.card>div.card-body>input.form-control" #CSS SELECTOR
        self.PROJECT_MAIN_CONTENT_SETTINGS_PROJECT_DESCRIPTION_TF = "div.main-content>div>div.card>div.card-body>textarea.form-control" #CSS SELECTOR
        self.PROJECT_MAIN_CONTENT_SETTINGS_PROJECT_OK_BTN = "div.main-content>div>div.card>div.card-body>button.btn.btn-success" #CSS SELECTOR
    
    def is_project_page(self, driver):
        if self.SELENIUM_COMMON.isElement(driver, By.CSS_SELECTOR, self.SIDE_BAR):
            return True
        else:
            return False
    
    def check_project_page_of(self, driver, projName):
        logger.info("start verifying project " + str(projName) + " page ...")
        project_page_header_el = driver.find_elements(By.CSS_SELECTOR, self.SIDE_BAR_HEADER)
        if len(project_page_header_el)>0:
            logger.info("... is stay at " + str(projName) + " project page!")
            return  True
        logger.info("... " + str(projName) + "projedt page is NOT loaded!")
        return False
    
    def click_project_feature(self, driver, projFeature):
        logger.info("start click feature " + str(projFeature) + " of project ...")
        list_of_features = {
            "test suite" : 0,
            "execution" : 1,
            "test case" : 2,
            "bug id" : 3,
            "report" : 4,
            "setting" : 5
            }
        list_features_el = driver.find_elements(By.CSS_SELECTOR, self.SIDE_BAR_FEATURE)
        for item in list_of_features:
            if item == str(projFeature):
                list_features_el[list_of_features[item]].click()
                break
    def verify_project_feature(self, driver, pfeature):
        logger.info("start verifying feature " + str(pfeature) + " of project ...")
        pfeature  = str(pfeature.lower())
        list_features_el = driver.find_elements(By.CSS_SELECTOR, self.SIDE_BAR_FEATURE)
        for item in list_features_el:
            feature = str(item.get_attribute("innerHTML"))
#             pattern = re.compile("(.*)[>]")
#             matchee = pattern.match(feature)
#             logger.info(str(matchee))
            #feature = feature.replace(str(matchee), " ")
            feature = re.sub("(.*)[>]", "", feature)
            feature = feature.strip()
            #logger.info(str(feature))
            if pfeature == feature.lower():
                logger.info("... feature " + str(pfeature) + " is existed!")
                return True
        logger.info("... featue " + str(pfeature) + " is NOT existed!")
        return False