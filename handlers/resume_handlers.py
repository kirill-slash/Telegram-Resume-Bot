from aiogram import Router, F
from aiogram.filters.command import Command
from aiogram.types import Message
from aiogram.enums import ParseMode
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram import types
import asyncio
from datetime import datetime

router = Router()


@router.message(F.text == "💰 Услуги и цены")
async def services_and_prices(message: Message):
    months = {
    1: "января",
    2: "февраля",
    3: "марта",
    4: "апреля",
    5: "мая",
    6: "июня",
    7: "июля",
    8: "августа",
    9: "сентября",
    10: "октября",
    11: "ноября",
    12: "декабря"
}
    text_services_and_prices = f"""💼 <b>Услуги и цены</b>

🚀 <b>Базовый Telegram-бот</b>
От 3 000 ₽

Команды /start, /help

Клавиатура с кнопками

Простая логика (опросы, рассылка, визитки)

<b>Пример</b>: бот для записи на консультацию.

💳 <b>Бот с оплатой и базой данных</b>
От 10 000 ₽

Интеграция с ЮKassa, QIWI, Crypto

Хранение данных (SQLite/PostgreSQL)

Админ-панель для управления

Тестовый период + инструкция

<b>Пример:</b> интернет-магазин в Telegram.

🤖 <b>Индивидуальный бот</b>
Договорная цена

Сложная логика (AI, нейросети)

Интеграция с API (1C, Google Sheets)

Парсинг данных с сайтов

Полное сопровождение

<b>Пример:</b> бот-ассистент для бизнеса.

📌 <b>Дополнительные услуги</b>
Доработка бота — от 1 000 ₽/час

Срочная разработка (+30% к стоимости)

✨ <b>Почему я?</b>
✅ Гарантия 14 дней — исправлю баги бесплатно.
✅ Поддержка 24/7 — отвечаю в течение часа.

🎁 <b>Акция</b>
Полный гайд: Развертывание Telegram-бота на хостинг до <b>{datetime.now().day+1} {months[datetime.now().month]}</b>!

"""
    kb = InlineKeyboardBuilder()
    kb.row(types.InlineKeyboardButton(
        text="Примеры работ GitHub",
        url=f"https://github.com/kirill-slash")
    )
    await message.answer(text_services_and_prices, parse_mode=ParseMode.HTML, reply_markup=kb.as_markup())


@router.message(F.text == "🤖 Заказать бота")
async def order_bot(message: Message):
    kb = InlineKeyboardBuilder()
    kb.row(types.InlineKeyboardButton(
        text="Написать в ЛС",
        url=f"tg://user?id={1416349804}")
    )
    text_order_bot = """
💼 <b>Хотите собственного Telegram-бота?</b>  

✔️ Быстро  
✔️ Надежно  
✔️ С гарантией  

📌 <b>Нажмите кнопку ниже, чтобы обсудить детали!</b>  
"""
    await message.answer(text_order_bot, parse_mode=ParseMode.HTML, reply_markup=kb.as_markup())