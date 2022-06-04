import logging
from aiogram import Dispatcher
from data.config import ADMINS
from datetime import datetime


async def on_startup_notify(dp: Dispatcher):
    for admin in ADMINS:
        try:
            time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            await dp.bot.send_message(admin,f"{time}\nBot ishga tushdi")

        except Exception as err:
            logging.exception(err)
