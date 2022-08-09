from pages.user_page import UserPage
from settings import my_user


class TestsUserPageUI:

    def test_page_is_my_pets(self, web_browser, login=my_user.login, passwrd=my_user.passwrd):

        page = UserPage(web_browser, login=login, passwrd=passwrd)

        page.wait_page_loaded()

        assert page.get_current_url() == 'https://petfriends.skillfactory.ru/my_pets'

    def test_compare_quantity_of_pets(self, web_browser, login=my_user.login, passwrd=my_user.passwrd):

        # Проверяем что присутствуют все питомцы.
        # сравниваем кол-во питомцев в счетчике с кол-вом строк в таблице

        page = UserPage(web_browser, login=login, passwrd=passwrd)

        parts_element = page.user_info_element.get_text().split("\n")

        amount_of_pets = [s for s in str.split(parts_element[1]) if s.isdigit()]

        assert len(page.elements_of_names.get_text()) == int(amount_of_pets[0])

    def test_foto_more_than_half(self, web_browser, login=my_user.login, passwrd=my_user.passwrd):

        # Проверяем что хотя бы у половины питомцев есть фото.
        # сравниваем кол-во пустых слотов под фото с кол-вом слотов с картинками

        page = UserPage(web_browser, login=login, passwrd=passwrd)

        amount_of_pic = 0

        for i in range(len(page.elements_of_pics.get_text())):
            if page.elements_of_pics[i].get_attribute('src') != '':
                amount_of_pic += 1

        empty_slots = len(page.elements_of_pics.get_text()) - amount_of_pic

        assert amount_of_pic >= empty_slots

    def test_all_pets_with_full_description(self, web_browser, login=my_user.login, passwrd=my_user.passwrd):

        page = UserPage(web_browser, login=login, passwrd=passwrd)

        # У всех питомцев есть имя, возраст и порода.
        # Проверяем что строки имя и породы не пустые, строка возраста не пустая и число

        for i in range(len(page.elements_of_names.get_text())):
            assert page.elements_of_names.get_text()[i] != ''
            assert page.elements_of_breeds.get_text()[i] != ''
            assert page.elements_of_ages.get_text()[i] != '' and page.elements_of_ages.get_text()[i].isdigit()

    def test_pets_have_different_names(self, web_browser, login=my_user.login, passwrd=my_user.passwrd):

        # У всех питомцев разные имена.
        # проверяем что список питомцев с одинаковыми именами равен пустой строке

        page = UserPage(web_browser, login=login, passwrd=passwrd)

        list_names = [page.elements_of_names.get_text()[i] for i in range(len(page.elements_of_names.get_text()))]
        same_names = [list_names[i] for i in range(len(list_names)) if not i == list_names.index(list_names[i])]

        if same_names:
            raise Exception(f'Встречаются одинаковые имена:\n {same_names}')
        else:
            assert same_names == []

    def test_some_pets_is_same(self, web_browser, login=my_user.login, passwrd=my_user.passwrd):

        # В списке нет повторяющихся питомцев. Питомцы различаются Имя, парода, возраст всех питомцев
        # Сравниваем первого питомца с последующими и так далее

        page = UserPage(web_browser, login=login, passwrd=passwrd)

        same_pets = False

        for i in range(len(page.elements_of_names.get_text())):
            for j in range(i + 1, len(page.elements_of_names.get_text())):

                if page.elements_of_names.get_text()[i] == page.elements_of_names.get_text()[j] and \
                        page.elements_of_breeds.get_text()[i] == page.elements_of_breeds.get_text()[j] and \
                        page.elements_of_ages.get_text()[i] == page.elements_of_ages.get_text()[j]:
                    raise Exception(f'Найдено минимум два одинаковых питомца под номерами {i + 1} и {j + 1}')

                else:

                    assert same_pets is False
