from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# Кнопки клавиатуры админа
button_load = KeyboardButton('/load')
button_delete = KeyboardButton('/delete')

button_case_admin = ReplyKeyboardMarkup(resize_keyboard=True).add(button_load).add(button_delete)
