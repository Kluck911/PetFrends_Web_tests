import time


def test_search_example(web_browser):
    """ Search some phrase in google and make a screenshot of the page. """

    # Open google search page:
    web_browser.get('https://google.com')

    time.sleep(3)

    # Find the field for search text input:
    search_input = web_browser.find_element_by_name('q')


    # Enter the text for search:
    search_input.clear()
    search_input.send_keys('Henadzi Zavadski')

    time.sleep(3)

    # Click Search:
    search_button = web_browser.find_element_by_name('btnK')
    search_button.submit()

    time.sleep(10)  # just for demo purposes, do NOT repeat it on real projects!

    # Make the screenshot of browser window:
    web_browser.save_screenshot('result.png')