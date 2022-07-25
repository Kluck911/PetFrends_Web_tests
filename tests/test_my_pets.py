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


def test_compare_quantity_of_pets():
    # Присутствуют все питомцы.
    # сравниваем кол-во питомцев в счетчике с кол-вом строк в таблице

    amount_of_pets = 0
    amount_of_lines = pytest.driver.find_elements_by_xpath("//*[@id='all_my_pets']//td[1]")
    pets_element = pytest.driver.find_element_by_xpath("//div[@class='.col-sm-4 left']")
    parts_element = pets_element.text.split("\n")

    for s in str.split(parts_element[1]):
        if s.isdigit():
            amount_of_pets = int(s)

    assert len(amount_of_lines) == amount_of_pets


def test_foto_more_than_half():

    # Хотя бы у половины питомцев есть фото.
    # сравниваем кол-во пустых слотов под фото с кол-вом слотов с картинками

    all_images_slots = pytest.driver.find_elements_by_xpath("//tbody/tr/th/img")
    amount_of_pic = 0

    for i in range(len(all_images_slots)):
        if all_images_slots[i].get_attribute('src') != '':
            amount_of_pic += 1

    empty_slots = len(all_images_slots) - amount_of_pic

    assert amount_of_pic >= empty_slots


def test_all_pets_with_full_description():

    # У всех питомцев есть имя, возраст и порода.
    # Проверяем что строки имя и породы не пустые, строка возраста не пустая и число

    names = pytest.driver.find_elements_by_xpath("//*[@id='all_my_pets']//td[1]")
    breed = pytest.driver.find_elements_by_xpath("//*[@id='all_my_pets']//td[2]")
    age = pytest.driver.find_elements_by_xpath("//*[@id='all_my_pets']//td[3]")

    for i in range(len(names)):
        assert names[i].text != ''
        assert breed[i].text != ''
        assert age[i].text != '' and age[i].text.isdigit()

def tests_pets_have_different_names():
    # У всех питомцев разные имена.

    names = pytest.driver.find_elements_by_xpath("//*[@id='all_my_pets']//td[1]").text
    print(names)





@pytest.fixture(autouse=True)
def time_delta():
    start_time = datetime.now()
    yield
    stop_time = datetime.now()
    print(f'\nТест шел: {stop_time-start_time}')
