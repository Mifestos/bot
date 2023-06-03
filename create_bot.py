import os
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram import Bot
from aiogram.dispatcher import Dispatcher




storage = MemoryStorage()

bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher(bot, storage=storage)
