from aiogram import executor
from config import dp
import middleware
import handlers
import logging

logging.basicConfig(level=logging.INFO)

if __name__=="__main__":
    executor.start_polling(dp,skip_updates=False)