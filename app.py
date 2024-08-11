import os
import requests
from dotenv import load_dotenv

load_dotenv()
import logging

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = os.getenv("API_TOKEN")

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    username = message.from_user.username
    await message.reply(f"""
        Hello @{username}!
        Commands:
        1./artist
        2./song
        3./album

    """)


@dp.message_handler(commands=['artist', ])
async def send_welcome(message: types.Message):
    artists_data = requests.get('http://127.0.0.1:8000/artist-telegram/').json()
    for artist in artists_data:
        await message.reply(f"""
            First Name:{artist['first_name']}\n
            Last Name:{artist['last_name']}\n
            Nick name:{artist['nick_name']}\n
        """)


@dp.message_handler(commands=['songs', ])
async def send_welcome(message: types.Message):
    songs_data = requests.get('http://localhost:8000/song-telebot').json()
    for song in songs_data:
        await message.reply(f"""
            Track name:{song['title']}\n
            Track Album:{song['album']}\n

        """)


@dp.message_handler(commands=['albums', ])
async def send_welcome(message: types.Message):
    albums_data = requests.get('http://localhost:8000/album-telebot').json()
    for album in albums_data:
        await message.reply(f"""
            Title of the album is :{album['title']}\n
            Artist of the album is :{album['artist']}\n

        """)


# @dp.message_handler()
# async def echo(message: types.Message):
#     # old style:
#     # await bot.send_message(message.chat.id, message.text)
#
#     await message.answer(message.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)