import os

from pages.base_page import WebPage
from pages.main_page import MainPage
from pages.elements import WebElement, ManyWebElements


class UserPage(WebPage):
    def __init__(self, web_driver, url='', login='', passwrd=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://petfriends.skillfactory.ru/login'

        super().__init__(web_driver, url)

        page = MainPage(web_driver, url='https://petfriends.skillfactory.ru/login', login=login, passwrd=passwrd)

        page.my_pets.click()




    elements_of_names = ManyWebElements(xpath="//*[@id='all_my_pets']//td[1]")

    elements_of_breeds = ManyWebElements(xpath="//*[@id='all_my_pets']//td[2]")

    elements_of_ages = ManyWebElements(xpath="//*[@id='all_my_pets']//td[3]")

    elements_of_pics = ManyWebElements(xpath="//tbody/tr/th/img")

    user_info_element = WebElement(xpath="//div[@class='.col-sm-4 left']")


