import requests
import os
from dotenv import load_dotenv
from urllib.parse import urlsplit, unquote
from datetime import datetime


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


def download_images(images_urls, save_directory):
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

    for number, url in enumerate(images_urls, start=1):
        try:
            response = requests.get(url)
            response.raise_for_status()

            file_extention = get_file_extention(url)
            file_name = os.path.join(save_directory, f'nasa_apod{number}{file_extention}')

            with open(file_name, 'wb') as file:
                file.write(response.content)
            print(f'скачано: {file_name}')
        except requests.exceptions.RequestException as e:
            print(f'Ошибка при скачивании {url}: {e}')


def fetch_spacex_last_launch():
    '''
     Получает ссылки на фотографии с последнего запуска SpaceX.

    Yields:
        tuple: Кортеж, содержащий URL изображения и путь для сохранения.

    Raises:
        requests.exceptions.HTTPError: Если запрос к API SpaceX завершился неудачно.
        KeyError: Если данные о запуске не содержат ожидаемых ключей.

    Returns:
        None
    '''
    url_mask = 'https://api.spacexdata.com/v5/launches/'

    response = requests.get(url_mask)
    response.raise_for_status()
    random_number = 100
    launch_items = response.json()[random_number]
    links_photos = (launch_items
                    .get('links', 'No directory')
                    .get('flickr', 'No directory')
                    .get('original', 'No photo')
                    )

    for number_foto, link in enumerate(links_photos, start=1):
        save_path = os.path.join(r'C:\pythonProject\pythonProject\Download_photo\images',
                                 f'foto_number_{number_foto}.jpeg'
                                 )
        yield link, save_path


def get_nasa_apod(api_key, count=1):
    """
        Получает данные о Astronomy Picture of the Day (APOD) от NASA.

        Args:
            api_key (str): API-ключ для аутентификации запроса.
            count (int, optional): Количество изображений для получения. По умолчанию 1.

        Returns:
            list: Список словарей с данными о APOD.

        Raises:
            requests.exceptions.HTTPError: Если запрос к API завершился неудачно.
        """
    params = {
        'api_key': api_key,
        'count': count
    }
    url = f'https://api.nasa.gov/planetary/apod'
    response = requests.get(url, params)
    response.raise_for_status()
    return response.json()


def get_epic_images(api_key, count=1):
    """
       Получает ссылки на фотографии с EPIC API от NASA.

       Args:
           api_key (str): API-ключ для аутентификации запроса.
           count (int, optional): Количество фотографий для получения. По умолчанию 1.

       Returns:
           list: Список URL для скачивания фотографий.

       Raises:
           requests.exceptions.HTTPError: Если запрос к API завершился неудачно.
       """
    url = f'https://api.nasa.gov/EPIC/api/natural/images'
    params = {
        'api_key': api_key
    }
    response = requests.get(url, params=params)
    response.raise_for_status()

    images_items = response.json()[:count]
    image_urls = []

    for image_data in images_items:
        image_name = image_data['image']
        date_str = image_data['date']
        date_obj = datetime.fromisoformat(date_str)
        date_formatted = date_obj.strftime('%Y/%m/%d')

        image_url = f'https://epic.gsfc.nasa.gov/archive/natural/{date_formatted}/png/{image_name}.png'
        image_urls.append(image_url)

    return image_urls


def main():
    """
      Основная функция для скачивания изображений с разных источников.

      Загружает API-ключ из переменных окружения, затем:
      1. Скачивает фотографии с последнего запуска SpaceX.
      2. Скачивает фотографии с Astronomy Picture of the Day (APOD) от NASA.
      3. Скачивает фотографии с EPIC API от NASA.

      Raises:
          KeyError: Если API-ключ не найден в переменных окружения.
      """
    load_dotenv()

    for link, save_path in fetch_spacex_last_launch():
        download_images(link, save_path)

    api_key_nasa = os.environ['API_KEY_NASA']

    count_photo = 2
    save_directory = 'nasa_apod_directory'

    apod_data = get_nasa_apod(api_key_nasa, count_photo)
    image_url = [item['url'] for item in apod_data if 'url' in item]

    download_images(image_url, save_directory)

    epic_image_urls = get_epic_images(api_key_nasa, count=3)
    download_images(epic_image_urls, 'nasa_epic_directory')


if __name__ == '__main__':
    main()
