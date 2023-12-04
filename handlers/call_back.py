import sqlite3

from aiogram import types, Dispatcher
from config import bot, ADMIN_ID
from database.sql_commands import Database
from keyboards.inline_buttons import questionnaire_keyboard
from scraping.async_scraper import AsyncScraper


async def start_questionnaire_call(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Python or Mojo ?",
        reply_markup=await questionnaire_keyboard()
    )


async def python_call(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="U R Python Developer 🐍"
    )


async def mojo_call(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="U R Mojo Developer 🔥"
    )


async def admin_call(message: types.Message):
    print(ADMIN_ID)
    print(message.from_user.id)
    if message.from_user.id == int(ADMIN_ID):
        await message.delete()
        await bot.send_message(
            chat_id=message.from_user.id,
            text="Hello master 🐲"
        )
    else:
        await bot.send_message(
            chat_id=message.from_user.id,
            text="U r not my master 🤬"
        )


def register_callback_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(start_questionnaire_call,
                                       lambda call: call.data == "start_questionnaire")
    dp.register_callback_query_handler(python_call,
                                       lambda call: call.data == "python")
    dp.register_callback_query_handler(mojo_call,
                                       lambda call: call.data == "mojo")
    dp.register_message_handler(admin_call,
                                lambda word: "dorei" in word.text)
    dp.register_callback_query_handler(async_service, lambda call: call.data == 'async_service')


async def service_o(call: types.CallbackQuery):
    scraper = ServiceOScrapper()
    data = scraper.parse_data()
    links = ServiceOScrapper.PLUS_URL
    for link in data:
        await  bot.send_message(chat_id=call.from_user.id, text=f"Услуги О!:"
                                                                f"\n{links}{link}", reply_markup=await save_button())


async def save_service_call(call: types.CallbackQuery):
    link = re.search(r'(https?://\S+)', call.message.text)
    if link:
        Database().sql_insert_best_servise_commands(owner_telegram_id=call.from_user.id, servise_link=
        link.group(0))

    await bot.send_message(chat_id=call.from_user.id, text="Вы сохранили ссылку")


async def async_service(call: types.CallbackQuery):
    data = await AsyncScraper().async_scrapers()
    links = AsyncScraper.PLUS_URL
    for link in data:
        await  bot.send_message(chat_id=call.from_user.id, text=f"Услуги О!:"
                                                                f"\n{links}{link}", reply_markup=await save_button())


def register_callback_handler(dp: Dispatcher):
    dp.register_callback_query_handler(random_users_next, lambda call: call.data == 'like' or call.data == 'dithlike')
    dp.register_callback_query_handler(service_o, lambda call: call.data == 'service_o')
    dp.register_callback_query_handler(save_service_call, lambda call: call.data == 'save_service')
    dp.register_callback_query_handler(async_service, lambda call: call.data == 'async_service')
