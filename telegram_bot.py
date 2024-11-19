import os
import telegram
from dotenv import load_dotenv



load_dotenv()

token_tg_bot = os.getenv('TOKEN_TG_BOT')
channel_id = os.getenv('CHANNEL_ID')

text = 'It`s my first message!'

bot = telegram.Bot(token=token_tg_bot)
bot.send_message(text=text, chat_id=channel_id)