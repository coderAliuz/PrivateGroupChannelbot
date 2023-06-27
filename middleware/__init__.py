from config import dp 
from .check_subs import BigBrother

if __name__=="middleware":
    dp.middleware.setup(middleware=BigBrother())
