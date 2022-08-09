import os

from pages.base_page import WebPage
from pages.elements import ManyWebElements, WebElement
from pages.auth_page import AuthPage


class MainPage(WebPage):

    def __init__(self, web_browser, url='', login='', passwrd=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://petfriends.skillfactory.ru/login'

        super().__init__(web_browser, url)

        page = AuthPage(web_browser)

        page.email.send_keys(login)

        page.password.send_keys(passwrd)

        page.btn.click()

    # некоторые элементы страницы
    images = ManyWebElements(css_selector=".card-deck .card-img-top")

    names = ManyWebElements(css_selector=".card-deck .card-title")

    descriptions = ManyWebElements(css_selector=".card-deck .card-text")

    my_pets = WebElement(css_selector='#navbarNav > ul > li:nth-child(1)')
