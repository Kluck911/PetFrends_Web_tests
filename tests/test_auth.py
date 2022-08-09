from pages.auth_page import AuthPage
from settings import my_user


class TestsAuthUI:

    def test_authorisation_positive(self, web_browser, login=my_user.login, passwrd=my_user.passwrd):

        page = AuthPage(web_browser)

        page.email.send_keys(login)

        page.password.send_keys(passwrd)

        page.btn.click()

        page.wait_page_loaded()

        assert page.get_current_url() == 'https://petfriends.skillfactory.ru/all_pets'