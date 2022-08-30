import pytest

from pages.main_page import MainPage
from pages.elements import WebElement


class TestsMainPage:

    #Проверка поле поиска на видимость
    @pytest.mark.main
    def test_search_filed_is_visible(self, web_browser):
        page = MainPage(web_browser)

        assert page.search_field.is_visible() == True

    #Проверка видимости подсказок(можно использовать параметризацию и проверить различные варианты текста)
    @pytest.mark.temp
    @pytest.mark.parametrize("search_text", ["тензор"],
                             ids=["искомый текст"])
    def test_hint_table_is_visible(self, web_browser, search_text):
        page = MainPage(web_browser)

        page.search_field.send_keys(search_text)

        page.wait_page_loaded()

        print(page.suggest_popup.text)

