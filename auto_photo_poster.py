import os
import random
import time
from dotenv import load_dotenv
from telegram import Bot

SECONDS_IN_HOUR = 3600

def load_environment_variables():
    """
    Загружает переменные окружения из файла .env.
    """
    load_dotenv()
    channel_id = os.getenv('CHANNEL_ID')
    token_tg_bot = os.getenv('TOKEN_TG_BOT')
    photos_directory = os.getenv('PHOTOS_DIRECTORY')
    publication_interval = int(os.getenv('PUBLICATION_INTRVAL', 4)) * SECONDS_IN_HOUR

    if not token_tg_bot:
        raise ValueError("TELEGRAM_BOT_TOKEN не установлен в переменных окружения")
    if not channel_id:
        raise ValueError("TELEGRAM_CHAT_ID не установлен в переменных окружения")
    if not photos_directory:
        raise ValueError("PHOTOS_DIRECTORY не установлен в переменных окружения")

    return channel_id, token_tg_bot, photos_directory, publication_interval



def get_photo_list(directory):
    """
    Получает список всех фотографий в заданной директории и её поддиректориях.

    Args:
        directory (str): Путь к директории с фотографиями.

    Returns:
        list: Список путей к фотографиям.
    """
    photo_list = []
    for root, dirs, files in os.walk(directory):
        print(f'this root:{root}, this files:{files}')
        for file in files:
            if file.lower().endswith(('.jpg', '.jpeg', 'bmp', 'png')):
                photo_list.append(os.path.join(root, file))

    return photo_list


def publish_photo(bot, chat_id, photo_list):
    """
    Публикует фотографии в Telegram-канал с заданной периодичностью.

    Args:
        bot (telegram.Bot): Экземпляр Telegram Bot.
        chat_id (str): ID канала или группы.
        photo_list (list): Список путей к фотографиям.
    """
    print(f'this photo_list:{photo_list}')
    while True:
        random.shuffle(photo_list)
        for photo in photo_list:
            with open(photo, 'rb') as file:
                bot.send_photo(chat_id=chat_id, photo=file)
            time.sleep(publication_interval)

def main():
    """
    Основная функция для запуска процесса публикации фотографий.
    """
    channel_id, token_tg_bot, photos_directory, publication_interval = load_environment_variables()
    bot = Bot(token=token_tg_bot)
    photo_list = get_photo_list(photos_directory)
    publish_photo(bot, channel_id, photo_list, publication_interval)

if __name__ == '__main__':
    main()