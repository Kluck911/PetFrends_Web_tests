from pages.main_page import MainPage


def test_pets_full_description(web_browser):
    # Проверка наличия фото имени и описания питомца а странице https://petfriends.skillfactory.ru/all_pets

    page = MainPage(web_browser)

    for i in range(len(page.names.get_text())):
        try:
            assert page.images[i].get_attribute('src') != ''
        except:
            raise Exception(f'Нет фото питомца №{i + 1} ')

        try:
            assert page.names[i].text != ''
        except:
            raise Exception(f'Нет имени питомца №{i + 1} ')

        try:
            assert page.descriptions[i].text != ''
            assert ', ' in page.descriptions[i].text
            parts = page.descriptions[i].text.split(", ")
            assert len(parts[0]) > 0
            assert len(parts[1]) > 0
        except:
            raise Exception(f'Нет полного описания питомца №{i + 1} ')
