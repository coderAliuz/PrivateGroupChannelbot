from .admin import AdminFilter
from .group_filter import IsGroup
from .private_filter import IsPrivate
from config import dp

if __name__ =="filters":
    dp.filters_factory.bind(AdminFilter)
    dp.filters_factory.bind(IsGroup)
    dp.filters_factory.bind(IsPrivate)