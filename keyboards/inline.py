from aiogram.types.inline_keyboard import InlineKeyboardButton, InlineKeyboardMarkup

def confirm_in_kb(chat_id):
    confirm=InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Ha", callback_data=f"yes_{chat_id}"),
         InlineKeyboardButton(text="Yo'q", callback_data=f"no_{chat_id}")]
    ]
    )
    return confirm

check_sup=InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton("1-kanal",url="https://t.me/alibloguz")
        ],
                [
            InlineKeyboardButton("2-kanal",url="https://t.me/alibloguz2")
        ],
        [
            InlineKeyboardButton(text="Tekshirish",callback_data="checker")
        ]
    ]
)