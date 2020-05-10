"""This module is used for defining parent class for ATDA keywords.

ATDA is automation test data analytics system. It could be break down into lower level if 


"""

# from grid_manager.grid_driver_factory import grid_driver_factory
import sys
import os
import base64
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')))
from grid_manager.grid_driver_factory import grid_driver_factory
from robot.libraries.BuiltIn import BuiltIn
from robot.api import logger
import time
# from pom.create_account import create_account
# from appium.common.logger import logger
__version__ = '0.0.0.1'

class appium_driver:
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    """ Containing driver and all basic function

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

    def __init__(self, command_executor='http://127.0.0.1:4444/wd/hub', desired_capabilities: dict = None):
        """Example of docstring on the __init__ method.

        Examples:
            N/A

        Args:
            desired_capabilities: - A dictionary of capabilities to request when
             starting the browser session. Required parameter.
            command_executor: - Either a string representing URL of the remote server or a custom
             remote_connection.RemoteConnection object. Defaults to 'http://127.0.0.1:4444/wd/hub'.

        """
        print('*INFO:%d* init atda_web instance' % (time.time()*1000))
        self.desired_capabilities = desired_capabilities
        self.command_executor = command_executor

    def open_app(self):
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
        BuiltIn().log_to_console('Open App: '+str(self.desired_capabilities)+','+self.command_executor)
        self.driver = grid_driver_factory().create_driver(self.command_executor, self.desired_capabilities)

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
        BuiltIn().log_to_console('Open Browser: '+str(self.desired_capabilities)+','+self.command_executor)
        self.driver = grid_driver_factory().create_driver(self.command_executor, self.desired_capabilities)
        BuiltIn().log_to_console('Open URL')
        self.driver.get(url)
        self.driver.set_page_load_timeout(30)

    def close_app(self):
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

    def start_recording(self):
        '''start screen recorder'''
        logger.info("start function start recording screen")
        self.driver.start_recording_screen()

    def stop_recording(self, filepath=None):
        '''start function stop recording for android.
        file video record will be stored in report folder
        '''
        logger.info("start function stop recording screen")
        if filepath is None:
            report_path = BuiltIn().get_variable_value("${OUTPUTDIR}")
            test_name = BuiltIn().get_variable_value("${TEST NAME}")
            suite_name = BuiltIn().get_variable_value("${SUITE NAME}")
            file_name = test_name +"-"+ suite_name + '.mp4'
            filepath = os.path.join(report_path, file_name)
        video_rawdata = self.driver.stop_recording_screen()
        with open(filepath, "wb") as vd:
            vd.write(base64.b64decode(video_rawdata))
    
    def take_screenshot(self, path_screenshot = None):
        '''take screen_shot for android'''
        logger.info("start function take screeenshot")
        if path_screenshot is None:
            report_path = BuiltIn().get_variable_value("${OUTPUTDIR}")
            test_name = BuiltIn().get_variable_value("${TEST NAME}")
            suite_name = BuiltIn().get_variable_value("${SUITE NAME}")
            file_name = test_name +"-"+ suite_name + '.png'
            path_screenshot = report_path + "\\"+file_name
        if self.driver.save_screenshot(path_screenshot):
            logger.info("Take screenshot successfully: " + str(path_screenshot))
            return path_screenshot
        else:
            logger.info("Take screenshot unsuccessfully")
            return "error"
