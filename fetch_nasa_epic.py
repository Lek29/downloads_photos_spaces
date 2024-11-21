from datetime import datetime

import requests


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