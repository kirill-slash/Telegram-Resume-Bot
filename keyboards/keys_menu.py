from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder


def keys_menu() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text="💰 Услуги и цены")
    kb.button(text="🤖 Заказать бота")
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)