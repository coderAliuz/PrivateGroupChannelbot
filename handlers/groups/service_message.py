from aiogram.types import Message,ContentType
from config import dp
from filters import IsGroup,AdminFilter

@dp.message_handler(IsGroup(),content_types=ContentType.NEW_CHAT_MEMBERS)
async def new_member(message:Message):
    members=message.new_chat_members
    for member in members:
        await message.reply(f"Xush kelibsiz {member.get_mention(as_html=True)}")

@dp.message_handler(IsGroup(),content_types=ContentType.LEFT_CHAT_MEMBER)
async def left_member(message:Message):
    await message.delete()
    member=message.left_chat_member
    if member.id==message.from_user.id:
        await message.answer(f"{member.get_mention(as_html=True)} guruhni tark etdi")
    else:
        await message.answer(f"{member.full_name} guruhdan haydaldi")
