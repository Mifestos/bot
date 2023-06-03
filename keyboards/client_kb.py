from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

b1 = KeyboardButton('/info')
b2 = KeyboardButton('/help')
b3 = KeyboardButton('/library')

kb_client = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

kb_client.add(b1).add(b2).insert(b3)
