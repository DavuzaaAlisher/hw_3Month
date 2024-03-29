from aiogram import Dispatcher, Bot
from decouple import config
from aiogram.contrib.fsm_storage.memory import MemoryStorage


PROXY_URL = "http://proxy.server:3128"
storage = MemoryStorage()
TOKEN = config("TOKEN")
bot = Bot(token=TOKEN, proxy=PROXY_URL)
DESTINATION = config("DESTINATION")
dp = Dispatcher(bot=bot, storage=storage)
ADMIN_ID = int(config("ADMIN_ID"))