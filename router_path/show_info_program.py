from aiogram import Router
from aiogram.types import CallbackQuery

from controllers.controllers import show_program_cache
from views import buttons, rendering_funcs
from controllers import callbacks
from aiogram import F


# settings
router = Router()


@router.callback_query(callbacks.RequestClientCallbackData.filter(F.action == "show_data"))
async def show_program_info(callback_query: CallbackQuery):
    program_id = callback_query.data.split(":")[-1]
    program = show_program_cache(program_id)
    # print(program)
    start_form = callbacks.RequestClientCallbackData(action="start_form", program_id=program_id)
    await callback_query.message.answer(text=f"""
    <b>{program["fields"]["Название_программы"]}</b>\n
    <b>Начало программы:</b> {rendering_funcs.format_date(program["fields"]["Даты_начала_программы"])}
    <b>Конец программы:</b> {rendering_funcs.format_date(program["fields"]["Дата_окончания_программы"])}
    <b>Стоимость:</b> {program["fields"]["Стоимость"]}\n
    {program["fields"]["Описание"]}
    """, parse_mode="HTML", reply_markup=buttons.draw_make_request_buttons(callback_data=start_form))


@router.callback_query(callbacks.RequestClientCallbackData.filter(F.action == "start_form"))
async def creating_request(callback: CallbackQuery):
    program_id = callback.data.split(":")[-1]
    await callback.message.answer("Ваш ребенок ездил на наши программы MULTIRIDERS CAMP?", reply_markup=buttons.draw_yes_no(program_id))


