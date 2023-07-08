import os
from dotenv import load_dotenv
from Yadisk import YandexDisk


load_dotenv()
token = os.getenv('TOKEN')
ya = YandexDisk(token=token)


def upload_file_with_specified_folder(filename):
    folder = ya.create_folder()
    ya.upload_file_to_disk(f'{folder}/{filename}', 'test.txt')


if __name__ == "__main__":
    filename_ = str(input("Введите название файла: "))
    upload_file_with_specified_folder(filename_)
