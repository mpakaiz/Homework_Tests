import requests

class YandexDisk:

    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def _get_upload_link(self, disk_file_path):
        upload_url = f'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = self.get_headers()
        params = {'path': disk_file_path, 'overwrite': 'true'}
        response = requests.get(upload_url, headers=headers, params=params)
        if response.status_code == 200:
            data = response.json()
            url_to_load = data.get('href')
            return url_to_load
        else:
            print(f'Ошибка {response.status_code}')
            return

    def upload_file_to_disk(self, disk_file_path, filename):
        url_to_load = self._get_upload_link(disk_file_path=disk_file_path)
        if url_to_load:

            response = requests.put(url_to_load, data=open(filename, 'rb'))
        else:
            print(f'Ссылка для загрузки не найдена')

    def create_folder(self):
        # folder_name = str(input('Создать папку с названием: '))
        folder_name = 'trap'
        url = 'https://cloud-api.yandex.net/v1/disk/resources/'
        headers = self.get_headers()
        params = {'path': f'{folder_name}', 'overwrite': 'false'}
        response = requests.put(url=url, headers=headers, params=params)
        if response.status_code == 201:
            return folder_name
        else:
            print(f'Ошибка {response.status_code}')
            return
