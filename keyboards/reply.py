from aiogram.types.reply_keyboard import ReplyKeyboardMarkup,ReplyKeyboardRemove

home_kb=ReplyKeyboardMarkup(
    [
        ["test1","test2"],
        ["clear"]
    ],resize_keyboard=True
)

del_kb=ReplyKeyboardRemove()