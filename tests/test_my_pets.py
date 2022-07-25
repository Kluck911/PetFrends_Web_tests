import pytest
from selenium import webdriver

from datetime import datetime

from settings import user_email, user_passwd


def elements_of_names():
    return pytest.driver.find_elements_by_xpath("//*[@id='all_my_pets']//td[1]")


def elements_of_breeds():
    return pytest.driver.find_elements_by_xpath("//*[@id='all_my_pets']//td[2]")


def elements_of_ages():
    return pytest.driver.find_elements_by_xpath("//*[@id='all_my_pets']//td[3]")


def elements_of_pics():
    return pytest.driver.find_elements_by_xpath("//tbody/tr/th/img")


def user_info_element():
    return pytest.driver.find_element_by_xpath("//div[@class='.col-sm-4 left']")


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
    parts_element = user_info_element().text.split("\n")

    for s in str.split(parts_element[1]):
        if s.isdigit():
            amount_of_pets = int(s)

    assert len(elements_of_names()) == amount_of_pets


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

    for i in range(len(elements_of_names())):
        assert elements_of_names()[i].text != ''
        assert elements_of_breeds()[i].text != ''
        assert elements_of_ages()[i].text != '' and elements_of_ages()[i].text.isdigit()


def test_pets_have_different_names():
    # У всех питомцев разные имена.
    # проверяем что список питомцев с одинаковыми именами равен пустой строке

    list_names = [elements_of_names()[i].text for i in range(len(elements_of_names()))]
    same_names = [list_names[i] for i in range(len(list_names)) if not i == list_names.index(list_names[i])]

    if same_names:
        raise Exception(f'Встречаются одинаковые имена:\n {same_names}')
    else:
        assert same_names == []


def test_some_pets_is_same():
    # В списке нет повторяющихся питомцев. (Сложное задание).
    # Сравниваем первого питомца с последующими и так далее
    for i in range(len(elements_of_names())):
        for j in range(i+1, len(elements_of_names())):
            if elements_of_names()[i].text == elements_of_names()[j].text and elements_of_breeds()[i].text\
                    == elements_of_breeds()[j].text and elements_of_ages()[i].text == elements_of_ages()[j].text:
                raise Exception(f'Найдены одинаковые питомцы с индексами {i} и {j}')
            else:
                assert '' == ''


@pytest.fixture(autouse=True)
def time_delta():
    start_time = datetime.now()
    yield
    stop_time = datetime.now()
    print(f'\nТест шел: {stop_time - start_time}')
