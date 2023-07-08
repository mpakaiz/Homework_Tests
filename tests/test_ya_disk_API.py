import pytest
import requests

from Yadisk import YandexDisk
import os
from dotenv import load_dotenv


load_dotenv()
token = os.getenv('TOKEN')
ya = YandexDisk(token=token)


def test_folder_created_status_200():
    ya.create_folder()

    files_url = 'https://cloud-api.yandex.net/v1/disk/resources'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'OAuth {}'.format(token)
    }
    params = {'path': 'trap'}
    response = requests.get(files_url, headers=headers, params=params)
    print(response.status_code)
    obj = response.status_code
    expected = 200

    assert obj == expected, 'папка не создана'


@pytest.mark.xfail
def test_folder_created_no_path():
    ya.create_folder()

    files_url = 'https://cloud-api.yandex.net/v1/disk/resources'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'OAuth {}'.format(token)
    }
    params = {'path': ''}
    response = requests.get(files_url, headers=headers, params=params)
    print(response.status_code)
    obj = response.status_code
    expected = 200

    assert obj == expected, 'папка не создана'


@pytest.mark.xfail
def test_folder_created_no_token():
    ya.create_folder()

    files_url = 'https://cloud-api.yandex.net/v1/disk/resources'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'OAuth {}'.format()
    }
    params = {'path': 'trap'}
    response = requests.get(files_url, headers=headers, params=params)
    print(response.status_code)
    obj = response.status_code
    expected = 200

    assert obj == expected, 'папка не создана'
