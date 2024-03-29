## echo bot using aiogram

import logging
from aiogram import Bot, Dispatcher, executor, types
from os import environ

logging.basicConfig(level=logging.INFO)

TOKEN = environ.get('TOKEN')
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")

@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)

if __name__ == '__main__':
    executor.start_polling(dp)