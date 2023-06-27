from aiogram.types import Message
from config import dp,bot
from filters import IsPrivate
from aiogram.types import ContentTypes
import random
@dp.message_handler(IsPrivate(),commands="photo1")
async def send_photo1(message:Message):#D:\botlar\bot_template
    #file="files/rasm1.jpg" bitta rasmi yuboradi
    file=random.choice(["files/rasm1.jpg","files/rasm2.jpg"])
    await message.answer_photo(photo=open(file,"rb"),caption="Rasm 1")

@dp.message_handler(IsPrivate(),commands="photo2")
async def send_photo2(message:Message):
    # bu rasmni file idisi faqat bir marta botga yuborilgan bo'lishi kerak
    await message.answer_photo("AgACAgIAAxkBAAIBmGSaegQf5EtHjiSlFi-uOeLZGSWnAALLzjEbA7bQSDolkEcAAYfDcgEAAwIAA3kAAy8E",caption="file id bilan")
    await bot.send_photo(chat_id=message.chat.id,photo="AgACAgIAAxkBAAIBq2Sagd0fsIjKUSfTnntxSSG0R_r2AALx0TEbS1XRSJIwOhXbLVezAQADAgADcwADLwQ",caption=" bot yordamida")

@dp.message_handler(IsPrivate(),text="musiqa")
@dp.message_handler(IsPrivate(),commands="music")
async def send_music(message:Message):
    file=open("files/musiqa.mp3","rb")
    file_id="CQACAgIAAxkBAAIBt2SaheSqKbBWPvQ6579ls7Rorg3gAAKWNAACA7bQSEo4sQ6OMaD6LwQ"
    await message.answer_audio(audio=file,caption="Uzb music")
    await bot.send_audio(chat_id=1434052080,audio=file_id)


@dp.message_handler(IsPrivate(),content_types=ContentTypes.PHOTO)
async def save_photo(message:Message):
    # destination: fayl saqlanish joyi va nomi korsatiladi agar unaqa nomli fayl bo'lsa yangilab qo'yadi
    # destination_dir papka yaratib ichiga avtomatik nom berib saqlaydi


    # await message.photo[-1].download(destination_dir="downlaod/rasm1.jpg") 
    await bot.download_file_by_id(file_id=message.photo[-1].file_id,destination="rasm1.jpg")#file_id bilan saqlaydi
    await message.answer("Rasm saqlandi")


@dp.message_handler(IsPrivate(),content_types=ContentTypes.all())
async def other(message:Message):
    await message.answer(message)