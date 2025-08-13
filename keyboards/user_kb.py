from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton, KeyboardButtonPollType
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

test_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Создать опрос", request_poll=KeyboardButtonPollType()),
        ],
        [
            KeyboardButton(text="Передать контакт", request_contact=True),
            KeyboardButton(text="Передать локацию", request_location=True)
        ]
    ],
    resize_keyboard=True,
    input_field_placeholder="chose a command"
)


def get_keyboard(
    *bts: str,
    resize_keyboard=True,
    request_contact: int = None,
    request_location: int = None,
    placeholder: str,
    sizes: tuple = (2, )
):
    keyboard = ReplyKeyboardBuilder()

    for idx, text in enumerate(bts, start=0):

        if request_contact and request_contact == idx:
            keyboard.add(KeyboardButton(text=text, request_contact=True))
        elif request_location and request_location == idx:
            KeyboardButton(text=text, request_location=True)
        else:
            keyboard.add(KeyboardButton(text=text))

    return keyboard.adjust(*sizes).as_markup(input_field_placeholder=placeholder,
                                                  resize_keyboard=resize_keyboard
                                             )

