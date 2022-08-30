from pages.base_page import WebPage
from pages.elements import WebElement


class MainPage(WebPage):
    def __init__(self, web_driver):
        url = 'https://yandex.ru'
        super().__init__(web_driver, url)

    search_field = WebElement(id='text')
    suggest_popup = WebElement(css='div.mini-suggest__popup')


    #локатор строчек поиска //li[@id="suggest-item-4217b8hnuxi-0"]