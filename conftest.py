import pytest


@pytest.fixture
def firefox_options(firefox_options):
    firefox_options.binary = '/path/to/firefox-bin'
    firefox_options.add_argument('-foreground')
    firefox_options.set_preference('browser.anchor_color', '#FF0000')
    return firefox_options

'''firefox_options.binary — путь к exe-драйверу Firefox.
firefox_options.add_argument(‘-foreground’) — возможность запуска в фоновом или реальном режиме. В нашем случае выбран последний. Для фонового укажите ‘-background’.
firefox_options.set_preference(‘borwser.anchor_color’, ‘#FF0000’) — выбор цвета подложки браузера.'''


@pytest.fixture
def chrome_options(chrome_options):
    chrome_options.binary_location = '/path/to/chrome'
    chrome_options.add_extension('/path/to/extension.crx')
    chrome_options.add_argument('--kiosk')
    return chrome_options

'''chrome_options.binary_location — путь к exe браузера (включая сам исполняемый файл).
chrome_options.add_extension — включение дополнений браузера.
Через метод chrome_options.add_argument() можно задавать другие параметры запуска браузера из списка.'''


@pytest.fixture
def driver_args():
    return ['--log-level=LEVEL']
'''уровень логирования для более сложных тестовых сценариев (debug):'''


'''режим запуска без пользовательского интерфейса'''
@pytest.fixture
def chrome_options(chrome_options):
    chrome_options.set_headless(True)
    return chrome_options

