import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
from settings import user_email, user_passwd

@pytest.fixture(autouse=True)
def testing():
    pytest.driver = webdriver.Chrome("chromedriver.exe")
    # Авторизуемся и переходим на страницу своих питомцев
    pytest.driver.get('http://petfriends.skillfactory.ru/login')
    WebDriverWait(pytest.driver, 5).until(EC.visibility_of_element_located((By.ID, 'email'))).send_keys(user_email)
    WebDriverWait(pytest.driver, 5).until(EC.visibility_of_element_located((By.ID, 'pass'))).send_keys(user_passwd)
    WebDriverWait(pytest.driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                                                      'button[type="submit"]'))).click()
    WebDriverWait(pytest.driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                                                      '#navbarNav > ul > li:nth-child(1)'))).click()

    yield

    pytest.driver.quit()

# Элементы страницы с ожиданиями
def elements_of_names():
    return WebDriverWait(pytest.driver, 5).until(EC.presence_of_all_elements_located((By.XPATH,
                                                                                      "//*[@id='all_my_pets']//td[1]")))


def elements_of_breeds():
    return WebDriverWait(pytest.driver, 5).until(EC.presence_of_all_elements_located((By.XPATH,
                                                                                      "//*[@id='all_my_pets']//td[2]")))


def elements_of_ages():
    return WebDriverWait(pytest.driver, 5).until(EC.presence_of_all_elements_located((By.XPATH,
                                                                                      "//*[@id='all_my_pets']//td[3]")))


def elements_of_pics():
    return WebDriverWait(pytest.driver, 5).until(EC.presence_of_all_elements_located((By.XPATH, "//tbody/tr/th/img")))


def user_info_element():
    return WebDriverWait(pytest.driver, 5).until(EC.presence_of_element_located((By.XPATH,
                                                                                 "//div[@class='.col-sm-4 left']")))


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

    amount_of_pic = 0

    for i in range(len(elements_of_pics())):
        if elements_of_pics()[i].get_attribute('src') != '':
            amount_of_pic += 1

    empty_slots = len(elements_of_pics()) - amount_of_pic

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
                raise Exception(f'Найдено минимум два одинаковых питомца под номерами {i+1} и {j+1}')
            else:
                assert '' == ''


@pytest.fixture(autouse=True)
def time_delta():
    start_time = datetime.now()
    yield
    stop_time = datetime.now()
    print(f'\nТест шел: {stop_time - start_time}')
