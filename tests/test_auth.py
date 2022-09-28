import pytest

from pages.auth_page import AuthPage
from settings import my_user, invalid_user


@pytest.mark.auth
class TestsAuthUI:

    @pytest.mark.pos
    @pytest.mark.all_tests
    def test_authorisation_positive(self, web_browser, login=my_user.login, passwrd=my_user.passwrd):
        #авторизация с валидным логином/паролем

        page = AuthPage(web_browser)

        page.email.send_keys(login)

        page.password.send_keys(passwrd)

        page.btn.click()

        page.wait_page_loaded()

        assert page.get_current_url() == 'https://petfriends.skillfactory.ru/all_pets'

    @pytest.mark.neg
    @pytest.mark.all_tests
    def test_authorisation_negative(self, web_browser, login=invalid_user.login, passwrd=invalid_user.passwrd):
        # авторизация с не валидным логином/паролем

        page = AuthPage(web_browser)

        page.email.send_keys(login)

        page.password.send_keys(passwrd)

        page.btn.click()

        page.wait_page_loaded()

        assert page.get_current_url() != 'https://petfriends.skillfactory.ru/all_pets', 'login error'
