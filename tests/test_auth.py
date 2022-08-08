from settings import skillfactory_user, my_user
from pages.auth_page import AuthPage


def test_authorisation_positive(web_browser):

    page = AuthPage(web_browser)

    page.email.send_keys(my_user.login)

    page.password.send_keys(my_user.passwd)

    page.btn.click()

    page.wait_page_loaded()

    assert page.get_current_url() == 'https://petfriends.skillfactory.ru/all_pets'

