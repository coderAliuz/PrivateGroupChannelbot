from aiogram import Bot,Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import ParseMode

token="6105542407:AAFwaOORFgYhILI679WFX_10JbcADhPCX9k"
admin_ids=[5906451521]
kanal_ids=[-1001947118987]
bot=Bot(token,parse_mode=ParseMode.HTML)
dp=Dispatcher(bot,storage=MemoryStorage())