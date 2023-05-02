import asyncio
import logging
import pprint

import cachetools
from aiogram import Bot, Dispatcher, types
from aiogram.fsm.context import FSMContext
from aiogram.fsm.storage.memory import MemoryStorage
from views import buttons
import aiogram.filters as filter

import config
from controllers import controllers
from router_path import show_info_program, request_for_yes, request_for_no


# settings to bot
logging.basicConfig(level=logging.INFO)
bot = Bot(token=config.telegram_bot)
dp = Dispatcher(storage=MemoryStorage())
cache_strategy = cachetools.TTLCache(maxsize=100, ttl=300)


@dp.message(filter.Command("start"))
async def welcome_start(message: types.Message):
    await message.answer("Здравствуйте. Здесь вы сможете посмотреть ближайшие поездки в лагерь. \n"
                         "В случае, если она вам понравится. Вы сможете оставить заявку на участие",
                         reply_markup=buttons.draw_menu_button())


@dp.message(filter.Text(buttons.menus_dict["show programs"]))
async def show_programs(message: types.Message):
    program_list = controllers.get_all_programs()
    pprint.pprint(program_list)
    await message.answer(text="Выберите интересующую вас программу и "
                              "нажмите на нее для просмотра информации о ней:",
                         reply_markup=buttons.draw_programs_button(program_list, "show_data"))


@dp.message(filter.Text(buttons.menus_dict["show contacts"]))
async def show_contacts(message: types.Message):
    await message.answer(text="Вы можете следить за нами и оставаться в курсе новых программ в наших соц-сетях. \n\n"
                              "1. По ссылке можно присоединиться к информационному каналу для родителей."
                              " https://chat.whatsapp.com/J3UzX8kN61QDURI6oO0sK8 \n"
                              "2. Мы Вконтакте - фотоотчеты с программ vk.com/multiriders \n"
                              "3. Инстаграмм - события в режиме онлайн https://www.instagram.com/multiriders_camp/ \n"
                              "4. Телеграмм канал - https://t.me/multiriders_camp \n\n"
                              "📞 Михаил (офис): +7 (911) 909-21-12 \n"
                              "📞 Анастасия: +7 (921) 392-28-83 \n\n"
                              "Сайт лагеря: https://www.multiriders.com/",
                         disable_web_page_preview=True)


@dp.message(filter.Text(buttons.menus_dict["make request"]))
async def show_contacts(message: types.Message):
    program_list = controllers.get_all_programs()
    await message.answer(text="Хорошо, выберите пожалуйста программу лагеря на которую вы хотите оставить заявку.",
                         reply_markup=buttons.draw_programs_button(program_list, "start_form"))


async def main():
    # connecting routes
    dp.include_router(show_info_program.router)
    dp.include_router(request_for_yes.router)
    dp.include_router(request_for_no.router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())