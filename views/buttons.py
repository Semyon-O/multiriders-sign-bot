from typing import Dict
from aiogram import types
from controllers import callbacks


def draw_programs_button(programs: Dict, action: str) -> types.InlineKeyboardMarkup:
    buttons = []
    for key, value in programs.items():
        buttons.append(
            [types.InlineKeyboardButton(text=value, callback_data=callbacks.RequestClientCallbackData(
                action=action, program_id=str(key)
            ).pack()
                                        )
             ]
        )

    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard


menus_dict = {
    "show programs": "Наши актуальные программы",
    "make request": "Заполнить заявку",
    "show contacts": "Наши контакты",
}


def draw_menu_button() -> types.ReplyKeyboardMarkup:
    kb = [
        [types.KeyboardButton(text=menus_dict["show programs"])],
        [types.KeyboardButton(text=menus_dict["make request"])],
        [types.KeyboardButton(text=menus_dict["show contacts"])]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
    )
    return keyboard


def draw_yes_no(program_id):
    kb = [
        [types.InlineKeyboardButton(text="Да", callback_data=callbacks.ShortFormCallbackData(wasChild=True, program_id=program_id).pack())],
        [types.InlineKeyboardButton(text="Нет", callback_data=callbacks.ShortFormCallbackData(wasChild=False, program_id=program_id).pack())]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=kb)
    return keyboard


def draw_make_request_buttons(callback_data):
    kb = [[types.InlineKeyboardButton(text="Заполнить заявку", callback_data=callback_data.pack())]]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=kb)
    return keyboard


def draw_url_request():
    kb = [[types.InlineKeyboardButton(text="Заполнить заявку", url="https://multiriders.com/request-summer")]]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=kb)
    return keyboard

