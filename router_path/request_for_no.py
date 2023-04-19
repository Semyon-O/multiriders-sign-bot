from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message
from aiogram.fsm.state import StatesGroup, State

import airtable_table.config
from airtable_table import tables
from views import buttons


class RequestStates(StatesGroup):
    enter_parent = State()
    enter_child = State()


# settings
router = Router()


@router.callback_query(lambda call: call.data.startswith("child:no"))
async def enter_parent_data(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer(
        text="Хорошо, пройдите пожалуйста по этой ссылке и оставьте заявку на участие в программе",
        reply_markup=buttons.draw_url_request()
    )


