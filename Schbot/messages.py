# from schbot._main_ import *
# from schbot._main_ import dp
# from aiogram import types

# @dp.message_handler(commands=['start']) #Команда Start
# async def start(message: types.Message):
#     kb = [
#         [
#             types.KeyboardButton(text='Что умеет этот бот?'),
#             types.KeyboardButton(text='Выберите группу')
#         ],
#     ]
#     keyboard = types.ReplyKeyboardMarkup(
#         keyboard = kb,
#         resize_keyboard=True,
#     )
#     await message.answer('Привет!\nЭто бот, который поможет Вам узнать расписание на любой день.\n', reply_markup=keyboard)

# @dp.message_handler(commands=['help']) #Команда Help
# async def help(message: types.Message):
#     await message.reply('тестовая команда')

# @dp.message_handler()
# async def unknownWord(message: types.Message):
#     await message.reply('Извините, я не знаю такой команды')