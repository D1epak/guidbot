from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

action = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Гайд', callback_data='guide'),
        ]
    ]
)