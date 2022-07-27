from settings import user_email, user_passwd


# логин на https://petfriends.skillfactory.ru/all_pets
def goto_all_pets(chromium_login):
    chromium_login.find_element_by_id('email').send_keys(user_email)
    chromium_login.find_element_by_id('pass').send_keys(user_passwd)
    chromium_login.find_element_by_css_selector('button[type="submit"]').click()


# элементы карточек
def images(chromium_login):
    # ожидание появления элемента
    chromium_login.implicitly_wait(10)
    return chromium_login.find_elements_by_css_selector(".card-deck .card-img-top")


def names(chromium_login):
    chromium_login.implicitly_wait(10)
    return chromium_login.find_elements_by_css_selector(".card-deck .card-title")


def descriptions(chromium_login):
    chromium_login.implicitly_wait(10)
    pet_descriptions = chromium_login.find_elements_by_css_selector(".card-deck .card-text")
    return pet_descriptions


def test_show_all_pets(chromium_login):

    # Проверка логина на галавную страницу https://petfriends.skillfactory.ru/all_pets
    goto_all_pets(chromium_login)
    assert chromium_login.find_element_by_tag_name('h1').text == "PetFriends"


def test_pets_full_description(chromium_login):

    goto_all_pets(chromium_login)

    for i in range(3):
        assert images(chromium_login)[i].get_attribute('src') != ''
        assert names(chromium_login)[i].text != ''
        assert descriptions(chromium_login)[i].text != ''
        assert ', ' in descriptions(chromium_login)[i].text
        parts = descriptions(chromium_login)[i].text.split(", ")
        assert len(parts[0]) > 0
        assert len(parts[1]) > 0
