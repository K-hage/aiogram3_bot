from aiogram import Dispatcher, Bot

import settings
from commands import set_commands
from handlers.echo import echo_router
from handlers.start import start_router


async def start_bot(bot: Bot):
    await set_commands(bot)
    await bot.send_message(settings.ADMIN_ID, text='Бот запущен!')


async def stop_bot(bot: Bot):
    await bot.send_message(settings.ADMIN_ID, text='Бот остановлен!')


async def main() -> None:
    # Initialize Bot instance with a default parse mode which will be passed to all API calls
    bot = Bot(settings.TOKEN, parse_mode='HTML')
    dp = Dispatcher()
    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)
    dp.include_routers(start_router, echo_router)
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()
