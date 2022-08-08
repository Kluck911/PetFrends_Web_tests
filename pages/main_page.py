import os

from pages.base_page import WebPage
from pages.elements import ManyWebElements
from pages.auth_page import AuthPage


class MainPage(WebPage):

    def __init__(self, web_driver, url='', login='', passwd=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://petfriends.skillfactory.ru/login'

        super().__init__(web_driver, url)

        page = AuthPage(web_driver)

        page.email.send_keys(login)

        page.password.send_keys(passwd)

        page.btn.click()

    # элементы страницы
    images = ManyWebElements(css_selector=".card-deck .card-img-top")

    names = ManyWebElements(css_selector=".card-deck .card-title")

    descriptions = ManyWebElements(css_selector=".card-deck .card-text")
