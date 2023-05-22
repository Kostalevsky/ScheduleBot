import logging

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '6250705325:AAEzbtEXHMAWRUnRoOjyntEnQXxS6uE4TPA'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start']) #Команда Start
async def hello(message: types.Message):
    await message.reply('Привет!\nЭто бот, который поможет Вам узнать расписание на любой день.\n')

@dp.message_handler(commands=['help']) #Команда Help
async def help(message: types.Message):
    await message.reply('тестовая команда')

@dp.message_handler()
async def unknownWord(message: types.Message):
    await message.reply('Извините, я не знаю такой команды')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)