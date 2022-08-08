import os

from pages.base_page import WebPage
from pages.elements import ManyWebElements
from settings import my_user
from pages.auth_page import AuthPage


class MainPage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://petfriends.skillfactory.ru/login'

        super().__init__(web_driver, url)

        page = AuthPage(web_driver)

        page.email.send_keys(my_user.login)

        page.password.send_keys(my_user.passwd)

        page.btn.click()

        page.wait_page_loaded()




    images = ManyWebElements(css_selector=".card-deck .card-img-top")

    names = ManyWebElements(css_selector=".card-deck .card-title")

    descriptions = ManyWebElements(css_selector=".card-deck .card-text")









