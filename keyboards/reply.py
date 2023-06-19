from aiogram.types.reply_keyboard import ReplyKeyboardMarkup,ReplyKeyboardRemove,KeyboardButton

home_kb=ReplyKeyboardMarkup(
    [
        ["test1","test2"],
        ["clear"]
    ],resize_keyboard=True
)

del_kb=ReplyKeyboardRemove()

tel_kb=ReplyKeyboardMarkup(
    resize_keyboard=True).add(KeyboardButton("Telefon",request_contact=True))#knopka orqali nomerini jonatadi

loc_kb=ReplyKeyboardMarkup(
    resize_keyboard=True).add(KeyboardButton("Manzil",request_location=True))#knopka orqali lokatsiyasini jonatadi