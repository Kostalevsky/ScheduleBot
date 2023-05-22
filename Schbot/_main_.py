from distutils.command.config import config
import logging
from typing import Text
from aiogram import Bot, Dispatcher, executor, types, utils, filters
from botconfig import TOKEN

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start']) #Команда Start
async def start(message: types.Message):
    kb = [
        [
            types.KeyboardButton(text='Что умеет этот бот?'),
            types.KeyboardButton(text='Выберите группу')
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard = kb,
        resize_keyboard=True,
    )
    await message.answer('Привет!\nЭто бот, который поможет Вам узнать расписание на любой день.\n', reply_markup=keyboard)

@dp.message_handler(text='Что умеет этот бот?')
async def comlist(message: types.Message):
    kb = [
        [
            types.KeyboardButton(text='Старт'),
            types.KeyboardButton(text='Выберите группу')
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
    )
    await message.answer('Ознакомьтесь с командами:', reply_markup=keyboard)

@dp.message_handler(commands=['help']) #Команда Help
async def help(message: types.Message):
    kb = [
        [
            types.KeyboardButton(text='Старт'),
            types.KeyboardButton(text='Ввести группу')
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
    )
    await message.answer('Ознакомьтесь с командами:', reply_markup=keyboard)

@dp.message_handler(text='Старт') #Команда Start
async def start(message: types.Message):
    kb = [
        [
            types.KeyboardButton(text='Что умеет этот бот?'),
            types.KeyboardButton(text='Выберите группу')
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard = kb,
        resize_keyboard=True,
    )
    await message.answer('Привет!\nЭто бот, который поможет Вам узнать расписание на любой день.\n', reply_markup=keyboard)

@dp.message_handler()
async def unknownWord(message: types.Message):
    await message.reply('Извините, я не знаю такой команды')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)