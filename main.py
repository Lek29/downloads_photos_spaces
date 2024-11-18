import argparse
from sys import prefix

import requests
import os

from dotenv import load_dotenv
from datetime import datetime

from fetch_nasa_apod import get_nasa_apod
from utils import download_images
from fetch_spacex_images import fetch_spacex_launch
from fetch_nasa_epic import get_epic_images


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
    api_key_nasa = os.environ['API_KEY_NASA']

    parser = argparse.ArgumentParser(description='Скачивание фотографий из разных источников.')
    parser.add_argument('--spacex', action='store_true', help='Скачать фотографии с запуска SpaceX')
    parser.add_argument('--apod', action='store_true',
                        help='Скачать фотографии с Astronomy Picture of the Day (APOD) от NASA')
    parser.add_argument('--epic', action='store_true', help='Скачать фотографии с EPIC API от NASA')
    parser.add_argument('--spacex_launch_id', type=str, help='ID запуска SpaceX')
    parser.add_argument('--apod_count', type=int, default=1, nargs='?', help='Количество фотографий APOD для скачивания')
    parser.add_argument('--epic_count', type=int, default=1, nargs='?', help='Количество фотографий EPIC для скачивания')
    args = parser.parse_args()

    if args.spacex:
        # Скачивание фотографий с запуска SpaceX
        if args.spacex_launch_id:
            links_photos = fetch_spacex_launch(args.spacex_launch_id)
        else:
            links_photos = fetch_spacex_launch()

        if links_photos:
            download_images(links_photos, 'images', prefix='spacex')
        else:
            print("Фотографии не найдены для данного запуска SpaceX.")

    if args.apod:
        # Скачивание фотографий с Astronomy Picture of the Day (APOD) от NASA
        image_urls = get_nasa_apod(api_key_nasa, args.apod_count)
        download_images(image_urls, 'nasa_apod_directory', prefix='apod')

    if args.epic:
        # Скачивание фотографий с EPIC API от NASA
        epic_image_urls = get_epic_images(api_key_nasa, args.epic_count)
        download_images(epic_image_urls, 'nasa_epic_directory', prefix='epic')



if __name__ == '__main__':
    main()
