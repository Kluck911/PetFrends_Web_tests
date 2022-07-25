# --------------------------------------------------------------------------------
#    Пример
    # images = pytest.driver.find_elements_by_xpath("//img")
    # names = pytest.driver.find_elements_by_xpath("//*[@id='all_my_pets']//td[1]")
    # descriptions = pytest.driver.find_elements_by_xpath("//tbody/tr/td[2]")


    # for i in range(len(names)):
        # assert images[i].get_attribute('src') != ''
        # assert names[i].text != ''
        # assert descriptions[i].text != ''
# --------------------------------------------------------------------------------
import pytest
from selenium import webdriver

from datetime import datetime

from settings import user_email, user_passwd


@pytest.fixture(autouse=True)
def testing():

    pytest.driver = webdriver.Chrome("E:\webdrivers\chromedriver.exe")
    # Переходим на страницу авторизации
    pytest.driver.get('http://petfriends.skillfactory.ru/login')
    # Вводим email
    pytest.driver.find_element_by_id('email').send_keys(user_email)
    # Вводим пароль
    pytest.driver.find_element_by_id('pass').send_keys(user_passwd)
    # Нажимаем на кнопку входа в аккаунт
    pytest.driver.find_element_by_css_selector('button[type="submit"]').click()
    # Проверяем, что мы оказались на главной странице пользователя
    pytest.driver.find_element_by_css_selector('#navbarNav > ul > li:nth-child(1)').click()
    # Проверяем, что мы оказались на главной странице пользователя

    yield

    pytest.driver.quit()


def test_compare_number_of_pets():

    amount_of_pets = 0
    names = pytest.driver.find_elements_by_xpath("//*[@id='all_my_pets']//td[1]")
    pets_element = pytest.driver.find_element_by_xpath("//div[@class='.col-sm-4 left']")
    parts_element = pets_element.text.split("\n")

    for s in str.split(parts_element[1]):
        if s.isdigit():
            amount_of_pets = int(s)

    assert len(names) == amount_of_pets


@pytest.fixture(autouse=True)
def time_delta():
    start_time = datetime.now()
    yield
    stop_time = datetime.now()
    print(f'\nТест шел: {stop_time-start_time}')
