from aiogram import types, F, Router
from aiogram.filters import CommandStart, Command
from Filters.chat_type import ChatType

user_group_router = Router()
user_group_router.message.filter(ChatType(["group"]))

BAN_WORDS = {"Кабан", "ban"}


@user_group_router.message(F.text)
async def cleaner(message: types.Message):
    if BAN_WORDS.intersection(message.text.lower().split()):
        await message.answer(f"{message.from_user.first_name}, больше не пишите такие вещи!")
        await message.delete()