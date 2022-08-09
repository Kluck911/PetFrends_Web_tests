from pages.user_page import UserPage
from settings import my_user, invalid_user


class TestsUserPageUI:

    def test_page_is_my_pets(self, web_browser, login=my_user.login, passwrd=my_user.passwrd):

        page = UserPage(web_browser, login=login, passwrd=passwrd)

        page.wait_page_loaded()

        assert page.get_current_url() == 'https://petfriends.skillfactory.ru/my_pets'

    def test_compare_quantity_of_pets(self, web_browser, login=my_user.login, passwrd=my_user.passwrd):

        # Присутствуют все питомцы.
        # сравниваем кол-во питомцев в счетчике с кол-вом строк в таблице

        page = UserPage(web_browser, login=login, passwrd=passwrd)

        page.wait_page_loaded()

        amount_of_pets = 0
        parts_element = page.user_info_element.get_text().split("\n")
        print(parts_element)

        amount_of_pets = [s for s in str.split(parts_element[1]) if s.isdigit()]

        assert len(page.elements_of_names.get_text()) == int(amount_of_pets[0])
