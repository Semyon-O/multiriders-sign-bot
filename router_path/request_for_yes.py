from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message
from aiogram.fsm.state import StatesGroup, State
from aiogram.filters import StateFilter

import airtable_table.config
from airtable_table import tables
from views import buttons


class RequestStates(StatesGroup):
    enter_parent = State()
    enter_child = State()
    enter_phone = State()


fields = {
    "ФИО_родителя": "",
    "ФИО_ребенка": "",
    "Контакты_родителя": "",
    "Номер_программы": ""
}


# settings
router = Router()


@router.callback_query(lambda call: call.data.startswith("child:yes"))
async def enter_parent_data(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer("Хорошо, для оставления быстрой заявки, напишите пожалуйста ваше ФИО")

    await state.set_state(RequestStates.enter_parent)


@router.message(StateFilter(RequestStates.enter_parent))
async def enter_child_data(message: Message, state: FSMContext):
    print(message.text)
    fields["ФИО_родителя"] = message.text
    await message.answer("Спасибо, оставьте пожалуйста ФИО ребенка")
    await state.set_state(RequestStates.enter_child)


@router.message(StateFilter(RequestStates.enter_child))
async def finishing_entering(message: Message, state: FSMContext):
    print(message.text)
    fields["ФИО_ребенка"] = message.text
    await message.answer("Спасибо, оставьте пожалуйста ваш номер телефона.")
    await state.set_state(RequestStates.enter_phone)


@router.message(StateFilter(RequestStates.enter_phone))
async def finishing_entering(message: Message, state: FSMContext):
    print(message.text)
    fields["Контакты_родителя"] = message.text
    await message.answer("Спасибо что оставили вашу заявку. В ближайшее время вам перезвонит Михаил")
    print(str(fields))
    await state.clear()