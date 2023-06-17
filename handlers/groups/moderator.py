from aiogram.types import Message
from config import dp,bot
from filters import IsGroup,AdminFilter
from datetime import datetime,timedelta
from aiogram.dispatcher.filters import Text
import asyncio

@dp.message_handler(IsGroup(),AdminFilter(),Text(startswith="ban"))
async def ban_mode(message:Message):
    try:
        member=message.reply_to_message.from_user
        text=message.text.split(" ")
        # ban 1000 reklama
        check_ban=text[0]
        check_time=text[1]
        check_result=text[2]

        if check_time.isdecimal():
            check_time=int(check_time)
            block_time=datetime.now()+timedelta(minutes=check_time)

            await message.chat.restrict(user_id=member.id,can_send_messages=False,until_date=block_time)
            await message.reply_to_message.delete()
            await message.delete()

            await message.answer(f"Foydaluvchi {member.full_name} {check_time} minutga {check_result} sababli bloklandi")
            mess_id=message.message_id-1
            await asyncio.sleep(10)
            await bot.delete_message(message.chat.id,message_id=mess_id)
    except:pass
@dp.message_handler(IsGroup(),AdminFilter(),text="unban")
async def unban_mode(message:Message):
    try:
        member=message.reply_to_message.from_user
        await message.chat.restrict(user_id=member.id,can_send_messages=True,can_send_other_messages=True,can_send_media_messages=True)
        await message.delete()
    except:pass
