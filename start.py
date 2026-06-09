from aiogram import Bot, Dispatcher
import os
from dotenv import load_dotenv
from main.hendlers import router as hendlers_router
from main.hendlers_python import router as hendlers_router_python
from main.hendlers_robotics import router as hendlers_router_robotics
from main.my_command import router as hendlers_command
from main.play1 import router as hendlers_play1
from main.play2 import router as hendlers_play2
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
    hendlers_router,
    hendlers_router_python,
    hendlers_router_robotics,
    hendlers_command,
    hendlers_play1,
    hendlers_play1
)

async def handle(request):
    return web.Response(text="Bot is running!")
    
async def main():
    bot = Bot(Token = token)
    await dp.start_polling(bot)

    await init_answer()
    await init_play()

    app = web.Application()
    app.router.add_get('/', handle)
    runner = web.AppRunner(app)
    await runner.setup()
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, '0.0.0.0', 10000)
    await site.start()


if __name__ == "__main__":
    asyncio.run(main())
