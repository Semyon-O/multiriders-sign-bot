from typing import Dict
from aiogram import types


def draw_programs_button(programs: Dict) -> types.InlineKeyboardMarkup:
    buttons = []

    for key, value in programs.items():
        buttons.append(
            [types.InlineKeyboardButton(text=value, callback_data=f"program:{key}")]
        )

    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard


menus_dict = {
    "show programs": "Посмотреть доступные программы",
    "show contacts": "Посмотреть контакты лагеря"
}


def draw_menu_button() -> types.ReplyKeyboardMarkup:
    kb = [
        [types.KeyboardButton(text=menus_dict["show contacts"])],
        [types.KeyboardButton(text=menus_dict["show programs"])]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
    )
    return keyboard


def draw_yes_no():
    kb = [
        [types.InlineKeyboardButton(text="Да", callback_data=f"child:yes")],
        [types.InlineKeyboardButton(text="Нет", callback_data=f"child:no")]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=kb)
    return keyboard


def draw_make_request_buttons(id_program):
    kb = [[types.InlineKeyboardButton(text="Оставить заявку", callback_data=f"request:{id_program}")]]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=kb)
    return keyboard


def draw_url_request():
    kb = [[types.InlineKeyboardButton(text="Оставить заявку", url="test.ru")]]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=kb)
    return keyboard

