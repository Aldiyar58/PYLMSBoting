from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder


del_kb = ReplyKeyboardRemove()

start_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="/menu"),
            KeyboardButton(text="hi")
        ],
        [
            KeyboardButton(text="show example"),
            KeyboardButton(text="show")
        ]
    ],
    resize_keyboard=True,
    input_field_placeholder="chose a command"
)

start_kb2 = ReplyKeyboardBuilder()
start_kb2.add(
    KeyboardButton(text="/menu"),
    KeyboardButton(text="hi"),
    KeyboardButton(text="show example"),
    KeyboardButton(text="show")
)
start_kb2.adjust(2, 1, 1)

start_kb3 = ReplyKeyboardBuilder()
start_kb3.attach(start_kb2)
start_kb3.add(
    KeyboardButton(text="show")
)
start_kb3.adjust(2, 1, 2)