from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.enums import ParseMode

import logging
from config import DEBUG
import config

bot = Bot(token=config.BOT_TOKEN, parse_mode=ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(storage=storage)

# получение пользовательского логгера и установка уровня логирования
logging.basicConfig(format='%(asctime)s - %(levelname)-5s - [%(filename)s:%(lineno)4d] - %(message)s')
logger = logging.getLogger(__name__)

# Установка уровня логирования
if DEBUG:
    logger.setLevel(logging.DEBUG)
else:
    logger.setLevel(logging.INFO)
