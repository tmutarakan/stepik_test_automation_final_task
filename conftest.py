import pytest
from selenium import webdriver


def chrome_driver_manager(opt) -> webdriver.Chrome:
    """Попытка подключить менеджер для автоматизации управления драйверами,
    в случае его отсутствия запускает драйвер установленный в системе"""
    try:
        from webdriver_manager.chrome import ChromeDriverManager
    except ModuleNotFoundError:
        return webdriver.Chrome(options=opt)
    return webdriver.Chrome(ChromeDriverManager().install(), options=opt)


def firefox_driver_manager(fp) -> webdriver.Firefox:
    """Попытка подключить менеджер для автоматизации управления драйверами,
    в случае его отсутствия запускает драйвер установленный в системе"""
    try:
        from webdriver_manager.firefox import GeckoDriverManager
    except ModuleNotFoundError:
        return webdriver.Firefox(firefox_profile=fp)
    return webdriver.Firefox(
        executable_path=GeckoDriverManager().install(),
        firefox_profile=fp
    )


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox, default chrome")
    parser.addoption('--language', action='store', default='en',
                     help="Choose language")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")
    browser = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        from selenium.webdriver.chrome.options import Options
        options = Options()
        options.add_experimental_option(
            'prefs', {'intl.accept_languages': user_language})
        browser = chrome_driver_manager(options)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", user_language)
        browser = firefox_driver_manager(fp)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()
