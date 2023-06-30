from aiogram import types
from aiogram.dispatcher.handler import CancelHandler
from aiogram.dispatcher.middlewares import BaseMiddleware
from config import kanal_ids,bot
from utils import check_subscribers
from keyboards import check_sub_in_kb

class BigBrother(BaseMiddleware):
    async def on_pre_process_update(self,update:types.Update,data:dict):
        if update.message.text=="/start":
            await update.message.answer("Salom xush kelibsiz")
            return
        if update.message:
            user=update.message.from_user.id
        elif update.callback_query:
            user=update.callback_query.message.from_user.id
        else:
            return
        
        text="Botdan foydalanish uchun quyidagi kanallarga obuna bo'ling\n"
        buttons=[]
        for kanal_id in kanal_ids:
            status=await check_subscribers(kanal_id,user)
            if not status:
                chat=await bot.get_chat(kanal_id)
                link=await chat.export_invite_link()
                text+=f"{chat.full_name}" 
                buttons.append(link)
        if buttons:
            await update.message.answer(text,reply_markup=check_sub_in_kb(buttons))
            raise CancelHandler()