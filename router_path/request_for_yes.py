from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message, User
from aiogram.fsm.state import StatesGroup, State
from aiogram.filters import StateFilter

import airtable_table.config as cfg
from airtable_table import tables

from controllers import callbacks
from aiogram import F
# from main import bot


class RequestStates(StatesGroup):
    enter_parent = State()
    enter_child = State()
    enter_phone = State()


fields = {
    "ФИО_родителя": "",
    "ФИО_ребенка": "",
    "Контакты_родителя": "",
    "Номер_программы": []
}


# settings
router = Router()


@router.callback_query(callbacks.ShortFormCallbackData.filter(F.wasChild == True))
async def enter_parent_data(callback: CallbackQuery, state: FSMContext, callback_data: callbacks.ShortFormCallbackData):
    print(callback_data.program_id)
    fields["Номер_программы"] = [callback_data.program_id]
    await callback.message.answer("Хорошо, для оставления быстрой заявки, напишите, пожалуйста, как Вас зовут?")
    await state.set_state(RequestStates.enter_parent)


@router.message(StateFilter(RequestStates.enter_parent))
async def enter_child_data(message: Message, state: FSMContext):
    print(message.text)
    fields["ФИО_родителя"] = message.text
    await message.answer("Как зовут ребенка, который ранее ездил к нам в лагерь?")
    await state.set_state(RequestStates.enter_child)


@router.message(StateFilter(RequestStates.enter_child))
async def finishing_entering(message: Message, state: FSMContext):
    print(message.text)
    fields["ФИО_ребенка"] = message.text
    await message.answer("Спасибо, для обратной связи оставьте пожалуйста ваш  контактный номер телефона.")
    await state.set_state(RequestStates.enter_phone)


@router.message(StateFilter(RequestStates.enter_phone))
async def finishing_entering(message: Message, state: FSMContext):
    print(message.text)
    fields["Контакты_родителя"] = message.text
    new_request = tables.RequestTable(cfg.base_token, cfg.api_token)
    new_request.create_request(fields)
    await message.answer("Спасибо что оставили вашу заявку. "
                         "В ближайшее время с вами свяжется Михаил и уточнит некоторые моменты. "
                         "Желаем вам хорошего дня")
    print(str(fields))
    # await bot.send_message(chat_id=2110486549, text="Hello")
    await state.clear()