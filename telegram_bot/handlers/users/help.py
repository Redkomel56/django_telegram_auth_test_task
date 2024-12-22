from aiogram import types
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command, StateFilter
from aiogram.fsm.state import any_state

from config import users_texts
from aiogram import Router


router = Router()


@router.message(StateFilter("*"), Command('help'))
async def bot_help(message: types.Message, state: FSMContext):
    await state.clear()
    await message.answer(users_texts.get('help').format(users_texts.get('commands')))


@router.message(StateFilter("*"), Command('drop'))
async def drop_state(message: types.Message, state: FSMContext):
    await state.clear()
    await message.answer('Вы сборосили активные действия')
