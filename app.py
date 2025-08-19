# Здесь находятся импорты встроенных библиотек
import asyncio
import os

# Здесь находятся импорты нашего фреймворка
from aiogram import Bot, Dispatcher, types

# Находим наш .env файл и подгружаем переменные оттуда. (в нашем случае один лишь токен бота).
from dotenv import find_dotenv, load_dotenv

from middleware.myownmiddleware import DataBaseSession

load_dotenv(find_dotenv())

# Здесь находятся импорты из нашего проекта
from db.engine import create_db, drop_db, session_maker

from utils.private_chat_commands import private_commands

from handlers.user_private_commands import user_private_router
from handlers.user_group_commands import user_group_router
from handlers.admin_private_commands import admin_router

ALLOWED_UPDATES = ["message", "edited_message"]

# Создаем экземпляры классов Bot и Dispatcher.
bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher()

bot.my_admins_list = [2141191476]

# Регистрация наших роутеров
dp.include_router(admin_router)
dp.include_router(user_private_router)
dp.include_router(user_group_router)


async def on_startup(flag: bool = False):
    if flag:
        await drop_db()

    await create_db()


async def on_shutdown():
    print("Shutting down...")

# главная асинхронная функция
async def main():
    dp.startup.register(on_startup)
    dp.shutdown.register(on_shutdown)

    dp.update.middleware(DataBaseSession(session_pool=session_maker))

    await bot.delete_webhook(drop_pending_updates=True)
    await bot.delete_my_commands(scope=types.BotCommandScopeAllPrivateChats())
    await bot.set_my_commands(commands=private_commands, scope=types.BotCommandScopeAllPrivateChats())
    await dp.start_polling(bot, allowed_updates=ALLOWED_UPDATES)

# Та самая строчка кода которая запустить нашего бота
asyncio.run(main())
