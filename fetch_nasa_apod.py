import requests


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
    apod_items =response.json()
    return [item['url'] for item in apod_items if 'url' in item]