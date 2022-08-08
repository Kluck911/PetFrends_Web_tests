from pages.user_page import UserPage
from settings import my_user


class TestsUserPageUI:

    def test_compare_quantity_of_pets(self, web_browser):

        # Присутствуют все питомцы.
        # сравниваем кол-во питомцев в счетчике с кол-вом строк в таблице

        page = UserPage(web_browser, login=my_user.login, passwd=my_user.passwd)

        assert page.get_current_url() == 'https://petfriends.skillfactory.ru/my_pets'