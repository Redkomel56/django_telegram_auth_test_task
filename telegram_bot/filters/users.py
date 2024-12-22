from aiogram import types
from aiogram.filters import BaseFilter

from config import users_texts
# from utils.db_connector import User, UserGroupsEnum
# from utils.db_connector.errors import CustomError, UserNotFoundError


class IsRegistered(BaseFilter):
    async def __call__(self, message: types.Message) -> bool:
        # try:
        #     user = User.get(tg_id=message.from_user.id)
        #     if user.group == UserGroupsEnum.USER or user.group == UserGroupsEnum.ADMIN:
        #         user.add_username(message.from_user.username)
        #         return True
        # except CustomError:
        #     return False
        # return False
        return True



class IsAdmin(BaseFilter):
    async def __call__(self, message: types.Message) -> bool:
        # try:
        #     user = User.get(tg_id=message.from_user.id)
        # except CustomError:
        #     return False
        # if user.group != UserGroupsEnum.ADMIN:
        #     return False
        # return True
        return True