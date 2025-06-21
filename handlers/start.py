from aiogram import Router, html
from aiogram.filters import CommandStart
from aiogram.types import Message

from keyboards.reply import menu_buttons

start_router = Router()

@start_router.message(CommandStart())

async def command_start_handler(message: Message):
    fullname = html.bold(message.from_user.full_name)
    await message.answer(f"Salom, {fullname}!" , reply_markup=menu_buttons())