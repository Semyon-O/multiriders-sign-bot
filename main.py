import asyncio
import logging
import pprint

import cachetools
from aiogram import Bot, Dispatcher, types
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
    await message.answer("Приветствуем! Хотите ознакомиться с ближайшими программами?",
                         reply_markup=buttons.draw_menu_button())


@dp.message(filter.Text(buttons.menus_dict["show programs"]))
async def show_programs(message: types.Message):
    program_list = controllers.get_all_programs()
    # pprint.pprint(program_list)
    await message.answer(text="Нажмите на интересующую программу для просмотра анонса",
                         reply_markup=buttons.draw_programs_button(program_list, "show_data"))


@dp.message(filter.Text(buttons.menus_dict["show contacts"]))
async def show_contacts(message: types.Message):
    text = (
        "Быть в курсе программ и новостей:\n\n"
        "• Информационный канал в WA для родителей: <a href='https://chat.whatsapp.com/J3UzX8kN61QDURI6oO0sK8'>присоединиться</a>\n"
        "• Канал в TG: <a href='https://t.me/multiriders_camp'>присоединиться</a>\n"
        "• Мы во Вконтакте: <a href='https://vk.com/multiriders'>фотографии с программ, видео и многое другое</a>\n"
        "• В запрещенной социальной сети: <a href='https://t.me/multiriders_camp'>в режиме online</a>\n"
        "• Наш сайт: <a href='https://www.multiriders.com'>ссылка</a>\n\n"
        "☎ <a href='https://t.me/MikhailStep'>Михаил</a> (офис), +7 (911) 909-21-12\n"
        "☎ Анастасия, +7 (921) 392-28-83\n"
    )
    formatted_text = text
    await message.answer(
        text=formatted_text,
        disable_web_page_preview=True,
        parse_mode="HTML"
    )


@dp.message(filter.Text(buttons.menus_dict["make request"]))
async def show_contacts(message: types.Message):
    program_list = controllers.get_all_programs()
    await message.answer(text="Пожалуйста, выберите необходимую программу:",
                         reply_markup=buttons.draw_programs_button(program_list, "start_form"))


async def main():
    # connecting routes
    dp.include_router(show_info_program.router)
    dp.include_router(request_for_yes.router)
    dp.include_router(request_for_no.router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())