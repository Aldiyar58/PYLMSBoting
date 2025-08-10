# Здесь находятся импорты встроенных библиотек
import asyncio
import os

# Здесь находятся импорты нашего фреймворка
from aiogram import Bot, Dispatcher, types

# Находим наш .env файл и подгружаем переменные оттуда. (в нашем случае один лишь токен бота).
from dotenv import find_dotenv, load_dotenv
load_dotenv(find_dotenv())

# Здесь находятся импорты из нашего проекта
from handlers.user_private_commands import user_private_router
from utils.private_chat_commands import private_commands
from handlers.user_group_commands import user_group_router

ALLOWED_UPDATES = ["message", "edited_message"]

# Создаем экземпляры классов Bot и Dispatcher.
bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher()

# Регистрация наших роутеров
dp.include_router(user_private_router)
dp.include_router(user_group_router)

# главная асинхронная функция
async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await bot.delete_my_commands(scope=types.BotCommandScopeAllPrivateChats())
    await bot.set_my_commands(commands=private_commands, scope=types.BotCommandScopeAllPrivateChats())
    await dp.start_polling(bot, allowed_updates=ALLOWED_UPDATES)

# Та самая строчка кода которая запустить нашего бота
asyncio.run(main())
