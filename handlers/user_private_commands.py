# Это отдельный файл для обработчиков нового роутера(user_private_router),
# которые предназначены для ЛС обычных юзеров

from aiogram import types, F, Router
from aiogram.filters import CommandStart, Command

from Filters.chat_type import ChatType

# Создание нового роутера
user_private_router = Router()
user_private_router.message.filter(ChatType(['private']))

# Это обработчик(handler) команды "/start".
@user_private_router.message(CommandStart())
async def start_cmd(message: types.Message):
    user_id = message.from_user.id
    first_name = message.from_user.first_name
    await message.answer(f"Hello, {first_name}! your id is {user_id}")

@user_private_router.message(Command("menu"))
async def echo(message: types.Message):
    text = message.text
    await message.reply(text)


@user_private_router.message(F.text.contains("!"))
@user_private_router.message(Command("hi"))
async def magic_fillter(message: types.Message):
    await message.answer("Hello, i am your friend!")

@user_private_router.message(F.text.startswith('show'), F.text.endswith('example'))
async def magic_fillter(message: types.Message):
    await message.answer("I check your example")