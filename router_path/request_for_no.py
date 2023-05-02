import asyncio

from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message
from aiogram.fsm.state import StatesGroup, State
from controllers import callbacks
from aiogram import F

from views import buttons


class RequestStates(StatesGroup):
    enter_parent = State()
    enter_child = State()


# settings
router = Router()


@router.callback_query(callbacks.ShortFormCallbackData.filter(F.wasChild == False))
async def enter_parent_data(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer(
        text="Заполнить заявку на участие в программе вы можете на нашем сайте.",
        reply_markup=buttons.draw_url_request()
    )
    await asyncio.sleep(10)
    await callback.message.answer("Спасибо что оставляете заявку. "
                                  "После заполнения мы свяжемся с вами в рабочие часы,"
                                  " будем рады ответить на ваши вопросы!.")


