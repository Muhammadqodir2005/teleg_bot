import asyncio
from aiogram import types, Dispatcher
from aiogram.dispatcher import DEFAULT_RATE_LIMIT
from aiogram.dispatcher.handler import CancelHandler, current_handler
from aiogram.dispatcher.middlewares import BaseMiddleware
from loader import bot,Database
      
class User_checkMiddleware(BaseMiddleware):
        def __init__(self, limit=DEFAULT_RATE_LIMIT, key_prefix='antiflood_'):
            self.rate_limit = limit
            self.prefix = key_prefix
            super(User_checkMiddleware, self).__init__()
        async def on_process_message(self, message: types.Message, data: dict):
            check_user = await Database.check_user_exists(message.from_user.id)
            if not check_user:
                await Database.new_user(message.from_user.id)
                # raise CancelHandler()