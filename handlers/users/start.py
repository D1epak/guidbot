from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from keyboards.inline.keyboards import action
from loader import dp

processed_start_commands = set()


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    if message.from_user.id not in processed_start_commands:
        # Обработка команды старта только для пользователей, которые еще не были обработаны
        await message.answer(f"Привет! Для получения Гайда нажимай на кнопку 👇🏻",
                             reply_markup=action)
        processed_start_commands.add(message.from_user.id)
    else:
        # Если команда старта уже была обработана, можно выполнить другие действия или игнорировать эту команду
        pass
