'''
Created on Apr 26, 2020

@author: nqkhanh
'''

import time
import sys

class selenium_tools(object):
    '''
    classdocs
    '''


    #def __init__(self):
    #    '''
    #    Constructor
    #    '''
    
    
    #Checking if element exists
    def isElement(self, driver, byLocator, value):
        try:
            print("<action>Checking if element exists %s", value)
            elements = driver.find_elements(byLocator, value)
            if len(elements) > 0:
                return True
            print("Not found elements")
        except:
            print("isElement Failed")
        return False
    
    #Wait until element located by given locator appear.
    def wait_for_element_appear(self, driver, byLocator, value, time_out=10):
        try:
            print("<action>Waiting for % until element appears...")
            while(time_out>0):
                time_out = time_out - 1
                time.sleep(1) 
                if self.isElement(driver, byLocator, value):
                    return True
            print("Not found element")
        except:
            print("Send command failed with exception :" + str(sys.exc_info()[0]) + " :: " + str(sys.exc_info()[1]))
            raise AssertionError("wait_for_element_appear Failed" + '\n\n\n')
        return False
    
    #Click on element
    def click(self, driver, by, value):
        try:
            print("<action>Click on elemnts")
            driver.find_element(by, value).click()
        except:
            print("Send command failed with exception :" + str(sys.exc_info()[0]) + " :: " + str(sys.exc_info()[1]))
            raise AssertionError("click getText" + '\n\n\n')
    
    #Set text to a element
    def setText(self, driver, by, value, text):
        try:
            print("<action>Setting text %s to: %s...", text, value)
            element = driver.find_element(by, value)
            element.clear()
            element.send_keys(text)
        except:
            print("Send command failed with exception :" + str(sys.exc_info()[0]) + " :: " + str(sys.exc_info()[1]))
            raise AssertionError("setText Failed" + '\n\n\n')
    
    # Get attribute value of element located by given locator.
    def getAttribute(self, driver, by, value, attribute):
        try:
            print("<action>Getting attribute's value: %s", attribute)
            return driver.find_element(by, value).getAttribute(attribute)
        except:
            print("Send command failed with exception :" + str(sys.exc_info()[0]) + " :: " + str(sys.exc_info()[1]))
            raise AssertionError("setText getText" + '\n\n\n')
        return None
    
    # Get Element
    def getElement(self, driver, elements, atIndex):
        try:
            return None
        except:
            print("Send command failed with exception :" + str(sys.exc_info()[0]) + " :: " + str(sys.exc_info()[1]))
            raise AssertionError("getElement getText" + '\n\n\n')
        return None