import os
import telegram
from dotenv import load_dotenv


def main():
    load_dotenv()

    token_tg_bot = os.getenv('TOKEN_TG_BOT')
    channel_id = os.getenv('CHANNEL_ID')

    text = 'It`s my first message!'

    bot = telegram.Bot(token=token_tg_bot)
    

    photo_path = 'nasa_apod_directory/apod_1.jpg'

    with open(photo_path, 'rb') as photo:
        bot.send_photo(chat_id=channel_id, photo=photo)

if __name__ == '__main__':
    main()