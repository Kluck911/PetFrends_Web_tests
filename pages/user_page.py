import os

from pages.base_page import WebPage
from pages.main_page import MainPage


class UserPage(WebPage):
    def __init__(self, web_driver, url='', login='', passwd=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://petfriends.skillfactory.ru/login'

        super().__init__(web_driver, url)

        page = MainPage(web_driver, url='https://petfriends.skillfactory.ru/login', login=login, passwd=passwd)

        page.my_pets.click()

        page.wait_page_loaded()
