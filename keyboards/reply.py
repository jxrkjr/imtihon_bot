from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton


def menu_buttons():
    keyboards = [
        [
            KeyboardButton(text=("add product")),
            KeyboardButton(text=("delete product")),
        ],
        [
            KeyboardButton(text=("search")),
        ]
    ]
    kb = ReplyKeyboardMarkup(keyboard=keyboards, resize_keyboard=True)
    return kb
def confirm_button():
    keyboards = [
        [
            KeyboardButton(text=("Ha")),
            KeyboardButton(text=("Yoq")),
        ]
    ]
    kb = ReplyKeyboardMarkup(keyboard=keyboards, resize_keyboard=True)
    return kb