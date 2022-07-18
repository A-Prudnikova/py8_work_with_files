import requests
from requests import Response
import os.path
import time

from selene import by
from selene.support.shared import browser
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def get_pdf():
    r: Response = requests.get(
        'https://resources.jetbrains.com/storage/products/pycharm/docs/PyCharm_ReferenceCard.pdf')
    file_pdf = 'resources/file.pdf'
    with open(file_pdf, 'wb') as file_pdf:
        file_pdf.write(r.content)
        file_pdf.close()

def get_xls():
    current_dir = os.path.dirname(os.path.abspath(__file__))

    options = webdriver.ChromeOptions()
    prefs = {
        "download.default_directory": os.path.join(current_dir, 'resources'),
        "download.prompt_for_download": False,
    }
    options.add_experimental_option("prefs", prefs)

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    browser.config.driver = driver
    browser.config.hold_browser_open = True
    browser.open('https://file-examples.com/index.php/sample-documents-download/sample-xls-download/')
    browser.element(by.text('Download sample xls file')).click()
    time.sleep(10)

def get_csv():
    current_dir = os.path.dirname(os.path.abspath(__file__))

    options = webdriver.ChromeOptions()
    prefs = {
        "download.default_directory": os.path.join(current_dir, 'resources'),
        "download.prompt_for_download": False
    }
    options.add_experimental_option("prefs", prefs)

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    browser.config.driver = driver
    browser.config.hold_browser_open = True
    browser.open('https://www.stats.govt.nz/large-datasets/csv-files-for-download/')
    browser.element(by.text('Annual enterprise survey: 2021 financial year (provisional) – size bands CSV')).click()
    time.sleep(5)