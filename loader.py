from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from data import config

bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

from utils.db_api.database import MySQLStorage

Database: MySQLStorage = MySQLStorage(host=config.IP,database=config.DB_Name, user=config.DB_user, password=config.DB_password)

