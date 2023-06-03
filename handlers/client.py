from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards import kb_client
from data_base import sqlite_db




#@dp.message_handler(commands=['start', 'help'])
async def command_start(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Начало работы', reply_markup=kb_client)
        await message.delete()
    except:
        await message.reply('Общение с ботом через ЛС , напишите ему:\nhttps://t.me/MultiFooBot')

async def command_info(message: types.Message):
    await bot.send_message(message.from_user.id, 'Информация')

async def command_help(message: types.Message):
    await bot.send_message(message.from_user.id, 'Помощь')

async def command_library(message: types.Message):
    await sqlite_db.sql_read(message)

def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start'])
    dp.register_message_handler(command_info, commands=['info'])
    dp.register_message_handler(command_help, commands=['help'])
    dp.register_message_handler(command_library, commands=['library'])

