from aiogram import Dispatcher, Bot
from decouple import config
from aiogram.contrib.fsm_storage.memory import MemoryStorage


storage = MemoryStorage()
TOKEN = config("TOKEN")
bot = Bot(token=TOKEN)
DESTINATION = config("DESTINATION")
dp = Dispatcher(bot=bot, storage=storage)
ADMIN_ID = int(config("ADMIN_ID"))