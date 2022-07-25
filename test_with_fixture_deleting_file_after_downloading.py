import os.path
import time

import pytest
from selene.support.shared import browser
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture()
def removing_file():
    yield
    os.remove('tmp/sampleFile.jpeg')


def test_downloading_file(removing_file):
    current_dir = os.path.dirname(os.path.abspath(__file__))

    options = webdriver.ChromeOptions()
    prefs = {
        "download.default_directory": os.path.join(current_dir, 'tmp'),
        "download.prompt_for_download": False
    }
    options.add_experimental_option("prefs", prefs)

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    browser.config.driver = driver
    browser.config.hold_browser_open = True
    browser.open('https://demoqa.com/upload-download')
    browser.element("#downloadButton").click()
    time.sleep(1)
