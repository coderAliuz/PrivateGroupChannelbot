from aiogram.types import Message,CallbackQuery
from aiogram.dispatcher import FSMContext
from config import dp,bot,kanal_ids,admin_ids
from keyboards import confirm_in_kb
from aiogram.dispatcher.filters import Text
#/post
users={}
@dp.message_handler(commands="post",state="*")
async def post_channel(message:Message,state:FSMContext):
    await message.answer("Kanalga yuboriladigan xabarni kiriting")
    await state.set_state("poster")

@dp.message_handler(state="poster")
async def post_text(message:Message,state:FSMContext):
    text=message.text
    await bot.send_message(chat_id=admin_ids[0],text=f"{message.from_user.full_name}\n{text}\nPost kanalga chiqishini Tasdiqlaysizmi",reply_markup=confirm_in_kb(message.chat.id))
    await message.reply("Xabar adminga yuborildi tasdiqlashini kuting")
    users[str(message.chat.id)]=text  #{"1235465":"Xabar"}
    await state.finish()

@dp.callback_query_handler(Text(startswith=["yes","no"]),chat_id=admin_ids[0])
async def adimin_confirm(call:CallbackQuery,state:FSMContext):
    data=call.data.split("_")
    user_id=data[1]
    text=users[user_id]
    if data[0]=="yes":
        await bot.send_message(chat_id=kanal_ids[0],text=text)
        await call.message.edit_text(f"{text}\nPost kanalga yuborildi")
        await bot.send_message(chat_id=user_id,text="Postiz kanalga joylandi\n/post buyrug'ini qayta bosing")
    else:
        await call.message.edit_text("Post yuborilmadi")
        await bot.send_message(chat_id=user_id,text="Postiz kanalga joylanmadi.\n/post buyrug'ini qayta bosing")
    
    await state.finish()




