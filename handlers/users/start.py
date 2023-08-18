from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from keyboards.inline.keyboards import action
from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Привет! Для получения Гайда нажимай на кнопку 👇🏻",
                         reply_markup=action)

