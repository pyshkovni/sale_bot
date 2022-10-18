# Для работы с SQL используйте https://sqlitestudio.pl

import asyncio
from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from config import *

loop = asyncio.new_event_loop()
bot  = Bot(settings['token'], parse_mode='HTML')
dp   = Dispatcher(bot, storage=MemoryStorage(), loop=loop)

if __name__ == '__main__':
    from handlers import dp
    executor.start_polling(dp)
