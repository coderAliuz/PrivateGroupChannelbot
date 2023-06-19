from aiogram.types import Message
from config import dp
from aiogram.dispatcher import FSMContext
from keyboards import home_kb,del_kb,tel_kb,loc_kb
from filters import IsPrivate
from geopy.geocoders import Nominatim

@dp.message_handler(IsPrivate(),commands="start",state="*")
async def start(message:Message,state:FSMContext):
    await message.answer(f"Assalom aleykum {message.from_user.full_name}\nTo'liq ism familiyangni kirit.")
    await state.set_state("ism")

@dp.message_handler(state="ism")
async def get_name(message:Message,state:FSMContext):
    name=message.text
    if name.replace(" ","").replace("'","").isalpha():
        await message.reply("Telefon raqamni kirit",reply_markup=tel_kb)
        await state.update_data(ism=name) #{"ism":"Alisher Turdiyev"}
        await state.set_state("tel")
    else:
        await message.reply("Faqat lotin harflaridan foydalanib ism va familiya kirit")

@dp.message_handler(state="tel",content_types="contact")
async def get_phone(message:Message,state:FSMContext):
    contact=message.contact.phone_number
    await message.answer("Manzilingni kirit",reply_markup=loc_kb)
    await state.update_data(tel=contact) #{"ism":"Alisher Turdiyev","tel":"998915019911"}
    await state.set_state("manzil")

@dp.message_handler(state="manzil",content_types="location")
async def get_location(message:Message,state:FSMContext):
    loc=message.location
    data=await state.get_data()
    name=data["ism"]
    phone=data["tel"]
    geolocator = Nominatim(user_agent="geoapiExercises")
    location = geolocator.reverse(f"{loc.latitude},{loc.longitude}")
    await message.answer(f"Sening ma'lumotlaring\n{name}\n{phone}\n{location}",reply_markup=del_kb)
    await state.finish()
    
@dp.message_handler(text="clear")
async def clear(message:Message):
    await message.answer("Tugmalar tozalandi",reply_markup=del_kb)
