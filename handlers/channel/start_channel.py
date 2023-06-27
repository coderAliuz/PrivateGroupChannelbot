from aiogram.types import Message,CallbackQuery
from config import dp,bot,kanal_ids
from keyboards import check_sup
from utils import check_subscribers

@dp.message_handler(commands="start")
async def started(message:Message):
    await message.answer("Salom quyidagi kanallarga obuna bo'ling")

@dp.callback_query_handler(text="checker")
async def checker_channel(call:CallbackQuery):
    text=""
    for id in kanal_ids:
        chat=await bot.get_chat(id)
        if await check_subscribers(id,call.message.chat.id):
            text+=f"{chat.full_name} ga obuna bo'lganisiz\n"
        else:
            text+=f"{chat.full_name} ga obuna bo'lmagansiz\n"

    await call.message.answer(text,reply_markup=check_sup)
