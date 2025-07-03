from aiogram import Router
from aiogram.filters.command import Command
from aiogram.types import Message
from aiogram.enums import ParseMode
from keyboards.keys_menu import keys_menu

router = Router()


@router.message(Command("start"))
async def cmd_start(message: Message):
    welcome_text = """<b>Привет</b>! 👋

Меня зовут <b>Кирилл</b>, и я создаю Telegram-ботов с душой.

🔹 <b>Почему боты?</b>
Для меня это не просто строчки кода – а возможность решать реальные задачи.

Хотите автоматизировать рутину, увеличить продажи или просто удивить клиентов? Боты справятся!

🔹 <b>Мой подход:</b>
Нестандартные решения – люблю задачи, где нужно думать, а не гуглить.

Внимание к деталям – ваш бот будет не просто работать, а делать это идеально.

Современные технологии – использую Python, Aiogram, SQLite, BeautifulSoup

🔹 <b>Чем могу быть полезен:</b>
✔️ Разработаю бота с нуля под ваши цели
✔️ Добавлю крутые фичи: оплату, парсинга
✔️ Помогу с идеей – вместе придумаем что-то небанальное

📌 <b>Давайте знакомиться ближе?</b> Выбирайте раздел ниже.
"""
    await message.answer(welcome_text, parse_mode=ParseMode.HTML, reply_markup=keys_menu())