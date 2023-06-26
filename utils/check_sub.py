from aiogram import Bot

async def check_subscribers(kanal_id,user_id):
    bot=Bot.get_current()
    member=await bot.get_chat_member(kanal_id,user_id)
    return member.is_chat_member()
