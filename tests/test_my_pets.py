import pytest
from selenium import webdriver
import time

from settings import user_email, user_passwd


@pytest.fixture(autouse=True)
def testing(web_browser):
    pytest.driver = webdriver.Chrome("E:\webdrivers\chromedriver.exe")
    # Переходим на страницу авторизации
    pytest.driver.get('http://petfriends.skillfactory.ru/login')

    yield

    pytest.driver.quit()


def test_show_my_pets():
    # Вводим email
    pytest.driver.find_element_by_id('email').send_keys(user_email)
    # Вводим пароль
    pytest.driver.find_element_by_id('pass').send_keys(user_passwd)
    # Нажимаем на кнопку входа в аккаунт
    pytest.driver.find_element_by_css_selector('button[type="submit"]').click()
    # Проверяем, что мы оказались на главной странице пользователя
    pytest.driver.find_element_by_css_selector('#navbarNav > ul > li:nth-child(1)').click()
    # Проверяем, что мы оказались на главной странице пользователя
    time.sleep(3)

    images = pytest.driver.find_elements_by_css_selector('.card-deck .card-img-top')
    names = pytest.driver.find_elements_by_css_selector('.card-deck .card-title')
    descriptions = pytest.driver.find_elements_by_css_selector('.card-deck .card-text')

    for i in range(len(names)):
        assert images[i].get_attribute('src') != ''
        assert names[i].text != ''
        assert descriptions[i].text != ''
        assert ', ' in descriptions[i]
        parts = descriptions[i].text.split(", ")
        assert len(parts[0]) > 0
        assert len(parts[1]) > 0


'''
def test_pets_value():

    names = pytest.driver.find_elements_by_css_selector('.card-deck .card-title')
    value = .card-deck .card-text'''
