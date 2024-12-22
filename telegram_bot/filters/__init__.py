from aiogram import Dispatcher
# from .is_admin import IsAdmins
from .users import IsRegistered, IsAdmin
from .chats import IsGroup, IsPrivate


def setup(dp: Dispatcher):
    dp.filters_factory.bind(IsGroup)
    dp.filters_factory.bind(IsPrivate)
    dp.filters_factory.bind(IsAdmin)
    dp.filters_factory.bind(IsRegistered)
