#Здесь собраны локаторы с тестируемых страниц


from selenium.webdriver.common.by import By


class AuthLocators:
    # локаторы для страницы авторизации https://petfriends.skillfactory.ru/login
    AUTH_EMAIL = (By.ID, "email")
    AUTH_PASS = (By.ID, "pass")
    AUTH_BTN = (By.CSS_SELECTOR, 'button[type="submit"]')


class MainPageLocators:
    # локаторы для основной страницы https://petfriends.skillfactory.ru/all_pets
    MY_PETS_BTN = (By.CSS_SELECTOR, '#navbarNav > ul > li:nth-child(1)')
    NAMES = (By.XPATH, "//*[@id='all_my_pets']//td[1]")
    BREEDS = (By.XPATH, "//*[@id='all_my_pets']//td[2]")
    AGES = (By.XPATH, "//*[@id='all_my_pets']//td[3]")
    PICS = (By.XPATH, "//tbody/tr/th/img")
    USER_INFO = (By.XPATH, "//div[@class='.col-sm-4 left']")


class MyPageLocators:
    # локаторы для страницы мои питомцы https://petfriends.skillfactory.ru/my_pets
    pass
