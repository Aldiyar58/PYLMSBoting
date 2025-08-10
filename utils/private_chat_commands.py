# В этом файле находятся все команды которые предназначены для юзера в ЛС
# и в данный момент работают
from aiogram.types import BotCommand

private_commands = [
    BotCommand(command="/start", description="This is the start command"),
    BotCommand(command="/help", description="This is the help command"),
    BotCommand(command="/menu", description="This is the menu command"),
]
