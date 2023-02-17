import os

import telebot
from telebot.types import Message
from dotenv import load_dotenv


load_dotenv()
TOKEN = os.getenv('TOKEN')

bot_client = telebot.TeleBot(token=TOKEN)