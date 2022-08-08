from selenium.webdriver.common.by import By


class AuthLocators:
    AUTH_EMAIL = (By.ID, "email")
    AUTH_PASS = (By.ID, "pass")
    AUTH_BTN = (By.CSS_SELECTOR, 'button[type="submit"]')


class MainPageLocators:
    MY_PETS_BTN = (By.CSS_SELECTOR, '#navbarNav > ul > li:nth-child(1)')
    NAMES = (By.XPATH, "//*[@id='all_my_pets']//td[1]")
    BREEDS = (By.XPATH, "//*[@id='all_my_pets']//td[2]")
    AGES = (By.XPATH, "//*[@id='all_my_pets']//td[3]")
    PICS = (By.XPATH, "//tbody/tr/th/img")
    USER_INFO = (By.XPATH, "//div[@class='.col-sm-4 left']")


class MyPageLocators:
    pass
