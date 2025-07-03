from aiogram import Dispatcher, Bot
import asyncio
import os
from dotenv import load_dotenv
from handlers import basic_commands, resume_handlers

load_dotenv()


async def main():
    bot = Bot(token=os.getenv("token"))
    dp = Dispatcher()

    dp.include_routers(basic_commands.router, resume_handlers.router)

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())