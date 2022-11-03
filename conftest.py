import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options as chrome_options

@pytest.fixture(scope='function')
def driver():
    #driver = webdriver.Chrome(ChromeDriverManager().install())

    options = chrome_options()
    options.add_argument("user-data-dir=/home/oleg/SeleniumProfile")
    options.add_argument('--start-maximized')
    driver = webdriver.Chrome(executable_path='/home/oleg/Загрузки/chromedriver_linux64 (1)/chromedriver', options=options)

    #driver.maximize_window()
    yield driver
    driver.quit()
