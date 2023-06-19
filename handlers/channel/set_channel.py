from aiogram.types import Message
from config import dp,bot

@dp.message_handler(commands="post")
async def post_channel(message:Message):
    await bot.send_message(chat_id=-1001947118987,text="Yangi post")