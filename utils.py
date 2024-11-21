import os
from urllib.parse import urlsplit, unquote, urlparse

import requests


def download_images(images_urls, save_directory, prefix='image'):
    '''Скачивает изображения и сохраняет их по указанному пути.

    Args:
        url_images(list): список URL изображений для скачивания.
        save_path(str): Полный путь для сохранения изображения.

    Raises:
        requests.exceptions.HTTPError: Если запрос к URL завершился неудачно.
        FileNotFoundError: Если директория для сохранения файла не существует и не может быть создана.

    Return:
        None
    '''

    os.makedirs(save_directory, exist_ok=True)
    for file_num, url in enumerate(images_urls, start=1):
        response = requests.get(url)
        response.raise_for_status()
        file_extention = get_file_extention(url)
        file_name = os.path.join(save_directory, f'{prefix}_{file_num}{file_extention}')
        with open(file_name, 'wb') as file:
            file.write(response.content)
            print(f'скачано: {file_name}')


def get_file_extention(url):
    '''
    Извлекает расширение файла из произвольного URL.

    Args:
        url (str): URL файла.

    Returns:
        str: Расширение файла (например, '.txt', '.jpg').
    '''
    parsed_url = urlsplit(url)
    path = parsed_url.path
    decoded_path = unquote(path)
    _, file_extention = os.path.splitext(decoded_path)
    return file_extention
