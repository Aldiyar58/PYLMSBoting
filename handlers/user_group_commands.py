from string import punctuation

from aiogram import types, F, Router, Bot
from aiogram.filters import CommandStart, Command
from Filters.chat_type import ChatTypeFilter

user_group_router = Router()
user_group_router.message.filter(ChatTypeFilter(["group"]))

BAN_WORDS = {"Кабан", "ban"}


@user_group_router.message(Command("admin"))
async def get_admins(message: types.Message, bot: Bot):
    chat_id = message.chat.id
    admins_list = await bot.get_chat_administrators(chat_id)
    #просмотреть все данные и свойства полученных объектов
    #print(admins_list)
    # Код ниже это генератор списка, как и этот x = [i for i in range(10)]
    admins_list = [
        member.user.id
        for member in admins_list
        if member.status == "creator" or member.status == "administrator"
    ]
    bot.my_admins_list = admins_list
    if message.from_user.id in admins_list:
        await message.delete()
    #print(admins_list)


def clean_text(text: str) -> str:
    return text.translate(str.maketrans("", "", punctuation))


@user_group_router.message(F.text)
async def cleaner(message: types.Message):
    if BAN_WORDS.intersection(clean_text(message.text.lower()).split()):
        await message.answer(f"{message.from_user.first_name}, больше не пишите такие вещи!")
        await message.delete()