import os
from aiogram.types import CallbackQuery
from aiogram import types

from loader import dp


@dp.callback_query_handler(text_contains='guide')
async def handle_time(call: CallbackQuery):
    await call.answer(cache_time=60)

    base_dir = os.path.join(os.path.dirname(__file__), 'guide.pdf')
    await call.message.answer('Подождите, файл выгружается!')
    # Отправка файла пользователю
    await call.message.answer_document(types.InputFile(base_dir, filename='Как выбрать_курсы_по_программированию_для_ребенка.pdf'))
