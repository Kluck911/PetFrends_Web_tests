import time


def test_search_example(selenium):
    """ Search some phrase in google and make a screenshot of the page. """

    # Open google search page:
    selenium.get('https://google.com')


    # Find the field for search text input:
    search_input = selenium.find_element_by_name('q')


    # Enter the text for search:
    search_input.clear()
    search_input.send_keys('first test')


    # Click Search:
    search_button = selenium.find_element_by_name('btnK')
    search_button.submit()

    time.sleep(5)  # just for demo purposes, do NOT repeat it on real projects!

    # Make the screenshot of browser window:
    selenium.save_screenshot('result.png')