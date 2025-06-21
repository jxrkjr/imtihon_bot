import asyncio
import logging
import sys
from os import getenv

from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from dotenv import load_dotenv
from utils.db import Products, session
from handlers.menu import menu_router
from handlers.start import start_router


load_dotenv()
TOKEN = getenv("BOT_TOKEN")


dp = Dispatcher()

@dp.message(Command('help'))
async def command_help_handler(message: Message) -> None:
    await message.answer('Bu bot orqali siz mahsulotlar qoshish ularni kora olasiz')

@dp.message(Command('product'))
async def command_product_handler(message: Message) -> None:

    products = Products()
    await message.answer(f'Barcha mahsulotlar \n'
                         f'{products.all_products(session)}')





async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp.include_routers(start_router, menu_router)

    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())