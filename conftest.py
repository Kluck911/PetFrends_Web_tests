# content of file conftest.py

import pytest
import uuid

from selenium import webdriver


@pytest.fixture
def chrome_options(chrome_options):
    chrome_options.binary_location = "C:/Program Files/Google/Chrome/Application/chrome.exe"
    # chrome_options.add_extension('/path/to/extension.crx')
    # chrome_options.add_argument('--kiosk')
    return chrome_options


@pytest.fixture
def firefox_options(firefox_options):
    firefox_options.binary = "C:/Program Files/Mozilla Firefox/firefox.exe"
    firefox_options.add_argument('-foreground')
    firefox_options.set_preference('browser.anchor_color', '#FF0000')
    return firefox_options


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    # This function helps to detect that some test failed
    # and pass this information to teardown:

    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


@pytest.fixture
def chromium_login(request):
    browser = webdriver.Chrome('./chromedriver.exe')
    browser.set_window_size(1024, 768)
    browser.get('http://petfriends.skillfactory.ru/login')

    # Return browser instance to test case:
    yield browser

    # Do teardown (this code will be executed after each test):

    if request.node.rep_call.failed:
        # Make the screen-shot if test failed:
        try:
            browser.execute_script("document.body.bgColor = 'white';")

            # Make screen-shot for local debug:
            browser.save_screenshot('screenshots/' + str(uuid.uuid4()) + '.png')

            # For happy debugging:
            print('URL: ', browser.current_url)
            print('Browser logs:')
            for log in browser.get_log('browser'):
                print(log)

        except:
            pass  # just ignore any errors here
