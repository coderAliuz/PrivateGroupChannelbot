from aiogram.types import Message
from config import dp
from aiogram.dispatcher import FSMContext

from filters import IsGroup,AdminFilter

@dp.message_handler(IsGroup(),AdminFilter(),commands="start",state="*")
async def start(message:Message,state:FSMContext):
    await message.answer(f"Assalom aleykum {message.from_user.full_name}!!! siz guruhdasiz")
    await state.finish()