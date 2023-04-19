import cachetools
from aiogram import Router
from cachetools import cached
from aiogram.types import CallbackQuery

import airtable_table.config
from airtable_table import tables
from views import buttons, rendering_funcs


# settings
router = Router()
cache_strategy = cachetools.TTLCache(maxsize=100, ttl=120)


@cached(cache=cache_strategy)
def show_program_cache(id: str):
    program_id = id
    programs = tables.ProgramsTable(airtable_table.config.base_token, airtable_table.config.api_token)
    program = programs.get_program(program_id)
    return program


@router.callback_query(lambda call: call.data.startswith("program"))
async def show_program_info(callback_query: CallbackQuery):
    program_id = callback_query.data.split(":")[-1]
    program = show_program_cache(program_id)
    print(program)
    await callback_query.message.answer(text=f"""
    <b>{program["fields"]["Название_программы"]}</b>\n
    <b>Начало программы:</b> {rendering_funcs.format_date(program["fields"]["Даты_начала_программы"])}
    <b>Конец программы:</b> {rendering_funcs.format_date(program["fields"]["Дата_окончания_программы"])}
    <b>Стоимость:</b> {program["fields"]["Стоимость"]}\n
    {program["fields"]["Описание"]}
    """, parse_mode="HTML", reply_markup=buttons.draw_make_request_buttons(program_id))


@router.callback_query(lambda call: call.data.startswith("request"))
async def creating_request(callback: CallbackQuery):
    program_id = callback.data.split(":")[-1]
    await callback.message.answer("Ваш ребенок ездил в лагерь?", reply_markup=buttons.draw_yes_no())


