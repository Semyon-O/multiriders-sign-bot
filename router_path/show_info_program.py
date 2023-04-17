from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

import airtable_table.config
from airtable_table import tables


router = Router()


@router.callback_query(lambda call: call.data.startswith("program"))
async def show_program_info(callback_query: CallbackQuery):
    program_id = callback_query.data.split(":")[-1]
    programs = tables.ProgramsTable(airtable_table.config.base_token, airtable_table.config.api_token)
    program = programs.get_program(program_id)
    print(program)
    await callback_query.message.answer(text=f"""
    <b>{program["fields"]["Название_программы"]}</b>\n
    {program["fields"]["Описание"]} \n
    <b>Начало программы:</b> {program["fields"]["Даты_начала_программы"]}
    <b>Окончание программы:</b> {program["fields"]["Дата_окончания_программы"]} \n
    <b>Стоимость:</b> {program["fields"]["Стоимость"]}
    """, parse_mode="HTML")

