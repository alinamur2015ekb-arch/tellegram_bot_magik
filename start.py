from aiogram import Bot, Dispatcher
import os
from dotenv import load_dotenv
from main.hendlers import router as hendlers_router
import asyncio
import asyncio
import aiohttp


async def pinger():
    """Функция, которая сама пингует сайт бота, чтобы он не спал"""
    await asyncio.sleep(10)
    async with aiohttp.ClientSession() as session:
        while True:
            try:
                async with session.get('https://telegramm-bot-rpin.onrender.com') as response:
                    print(f"Пинг выполнен! Статус: {response.status}")
            except Exception as e:
                print(f"Ошибка пинга: {e}")
            await asyncio.sleep(600)


load_dotenv()
token = os.getenv("TOKEN")

dp = Dispatcher()
dp.include_routers(
    hendlers_router
)

async def main():
    bot = Bot(Token = token)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())