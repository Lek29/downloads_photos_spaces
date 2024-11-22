import os

import requests


def fetch_spacex_launch(launch_id=None):
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

    if launch_id:
        response = requests.get(f'{url_mask}{launch_id}')
    else:
        response = requests.get(url_mask)
        response.raise_for_status()
        last_launch = 0
        launch_id = response.json()[last_launch]['id']
        response = requests.get(f'{url_mask}{launch_id}')

    response.raise_for_status()
    launch_items = response.json()

    if isinstance(launch_items, list):
        for launch in launch_items:
            if launch['id'] == launch_id:
                launch_items = launch
                break


    links_photos = launch_items.get('links', {}).get('flickr', {}).get('original', [])
    return links_photos
