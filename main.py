import asyncio
import logging

import cachetools
from aiogram import Bot, Dispatcher, types
from aiogram.fsm.context import FSMContext
from aiogram.fsm.storage.memory import MemoryStorage
from views import buttons
from airtable_table import tables
from airtable_table import config as acf
import aiogram.filters as filter
from cachetools import cached

import config
from router_path import show_info_program, request_for_yes


# settings to bot
logging.basicConfig(level=logging.INFO)
bot = Bot(token=config.telegram_bot)
dp = Dispatcher(storage=MemoryStorage())
cache_strategy = cachetools.TTLCache(maxsize=100, ttl=300)

# connecting routes
dp.include_router(show_info_program.router)
dp.include_router(request_for_yes.router)


@dp.message(filter.Command("start"))
async def welcome_start(message: types.Message, state: FSMContext):
    await message.answer("Здравствуйте. Здесь вы сможете посмотреть ближайшие поездки в лагерь. \n"
                         "В случае, если она вам понравится. Вы сможете оставить заявку на участие",
                         reply_markup=buttons.draw_menu_button())


@cached(cache=cache_strategy)
def get_all_programs():
    programs = tables.ProgramsTable(acf.base_token, acf.api_token)
    all_programs = programs.get_all_programs()
    program_list = {}
    for program in all_programs:
        program_list[program["id"]] = program["fields"]["Название_программы"]

    return program_list


@dp.message(filter.Text(buttons.menus_dict["show programs"]))
async def show_programs(message: types.Message, state: FSMContext):
    program_list = get_all_programs()

    await message.answer(text="Выберите интересующую вас программу и "
                              "нажмите на нее для просмотра информации о ней:",
                         reply_markup=buttons.draw_programs_button(program_list))


@dp.message(filter.Text(buttons.menus_dict["show contacts"]))
async def show_contacts(message: types.Message):
    await message.answer(text=
    """ Почта: info@multiriders.com
    ВК: https://vk.com/multiriders
    Офис (Михаил): +7 (921) 550-53-81
    Анастасия: +7 (921) 392-28-83
    """)


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())