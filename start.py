mport asyncio
import os
from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
from aiohttp import web  # Исправили импорт web
# роутеры
from main.hendlers import router as hendlers_router
from main.hendlers_python import router as hendlers_router_python
from main.hendlers_robotics import router as hendlers_router_robotics
from main.my_command import router as hendlers_command
from main.play1 import router as hendlers_play1
from main.play2 import router as hendlers_play2 
# Импортируем инициализацию базы данных
from database import init_answer, init_play

load_dotenv()
token = os.getenv("TOKEN")

dp = Dispatcher()
dp.include_routers(
    hendlers_router,
    hendlers_router_python,
    hendlers_router_robotics,
    hendlers_command,
    hendlers_play1,
    hendlers_play2 
)

async def handle(request):
    return web.Response(text="Bot is running!")

async def pinger():
    """Функция, которая сама пингует сайт бота, чтобы он не спал"""
    await asyncio.sleep(10)
    async with aiohttp.ClientSession() as session:
        while True:
            try:
                # Пингуем твой сайт на Рендере
                async with session.get('https://telegramm-bot-rpin.onrender.com') as response:
                    print(f"Пинг выполнен! Статус: {response.status}")
            except Exception as e:
                print(f"Ошибка пинга: {e}")
            await asyncio.sleep(600)

async def main():
    await init_answer()
    await init_play()

    app = web.Application()
    app.router.add_get('/', handle)
    runner = web.AppRunner(app)
    await runner.setup()
    
    port = int(os.environ.get("PORT", 8080))
    site = web.TCPSite(runner, '0.0.0.0', port)
    await site.start()
    print(f"Веб-сервер запущен на порту {port}")

    bot = Bot(token=token)

    asyncio.create_task(pinger())

    print("Бот успешно запущен в облаке!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
