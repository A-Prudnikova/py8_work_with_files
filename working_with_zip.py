import zipfile
import os.path
import pytest
from PyPDF2 import PdfReader
import csv
import xlrd
from downloading_files import get_csv, get_pdf, get_xls


@pytest.fixture()
def removing_zip():
    yield
    os.remove('resources/sample.zip')

@pytest.fixture()
def removing_files():
    yield
    os.remove('resources/file.pdf')
    os.remove('resources/file_example_XLS_10.xls')
    os.remove('resources/annual-enterprise-survey-2021-financial-year-provisional-size-bands-csv.csv')


@pytest.fixture()
def download():
    get_pdf()
    get_xls()
    get_csv()


def convert_to_zip():
    with zipfile.PyZipFile('resources/sample.zip', 'w') as zip:
        zip.write('resources/file.pdf'),
        zip.write('resources/file_example_XLS_10.xls'),
        zip.write('resources/annual-enterprise-survey-2021-financial-year-provisional-size-bands-csv.csv')
    return zip


def test_zip_file(download, removing_zip, removing_files):

    zip_ = convert_to_zip()

    filenames = zip_.namelist()
    for filename in filenames:
        if filename.endswith('.pdf'):
            pdf_reader = PdfReader(filename)
            text = pdf_reader.pages[0].extractText()
            assert 'Open a tool window' in text
            print('pdf ok')
        elif filename.endswith('.xls'):
            xls_reader = xlrd.open_workbook_xls(filename)
            sheet = xls_reader.sheet_by_index(0)
            assert sheet.nrows == 10
            print('xls ok')
        elif filename.endswith('.csv'):
            with open(filename) as csvfile:
                csv_reader = csv.reader(csvfile)
                n = list(csv_reader)
                assert "industry_code_ANZSIC" in (n[0])
                print('csv ok')
        else:
            print('check filetype')
    zip_.close()
