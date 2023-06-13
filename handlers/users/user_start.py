from aiogram.types import Message
from config import dp
from aiogram.dispatcher import FSMContext
from keyboards import home_kb,del_kb
from filters import IsPrivate

@dp.message_handler(IsPrivate(),commands="start",state="*")
async def start(message:Message,state:FSMContext):
    await message.answer(f"Assalom aleykum {message.from_user.full_name}",reply_markup=home_kb)
    await state.finish()

@dp.message_handler(text="clear")
async def clear(message:Message):
    await message.answer("Tugmalar tozalandi",reply_markup=del_kb)
