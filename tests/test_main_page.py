#import time, pickle
import pytest
from pages.main_page import MainPage
from pages.elements import ManyWebElements
from selenium.webdriver.common.action_chains import ActionChains



def test_petfriends(web_browser):
    """ Authorize to Petfriends via cookies and create a screenshot when loginpage is successfull. """

    page = MainPage(web_browser)

    # Scroll down till the end using actionchains and click on the last image
    page.scroll_down()

    # Make the screenshot of browser window:
    page._web_driver.save_screenshot('petfriends.png')