from aiogram import types
from aiogram.filters import BaseFilter


class IsGroup(BaseFilter):
    async def __call__(self, message: types.Message) -> bool:
        return message.chat.type in ('group', 'supergroup')


class IsPrivate(BaseFilter):
    async def __call__(self, message: types.Message | types.CallbackQuery) -> bool:
        if isinstance(message, types.Message):
            return message.chat.type == 'private'
        elif isinstance(message, types.CallbackQuery):
            return message.message.chat.type == 'private'
        else:
            return False