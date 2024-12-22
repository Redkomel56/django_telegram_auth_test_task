import asyncio
import random
import re
import datetime
from typing import Optional

from aiogram import types, F
from aiogram.fsm.context import FSMContext
from aiogram.filters import CommandStart, StateFilter, CommandObject
from aiogram.types import InputFile, BufferedInputFile, FSInputFile, ReplyKeyboardRemove, ReplyKeyboardMarkup, \
    KeyboardButton

from loader import dp, bot
from config import users_buttons, users_texts
from keyboards.inline.mune_inline_kb import generate_buttons
from states.user_states import UserState
from aiogram import Router

from utils.api_connector import UserCreationClient, APIError

router = Router()


def extract_unique_code(text):
    return text.split()[1] if len(text.split()) > 1 else None


@router.message(CommandStart(), StateFilter("*"))
async def bot_start(message: types.Message, state: FSMContext, command: CommandObject):
    await state.clear()

    payload = command.args
    if payload:
        action, uuid = payload.split('_')
        if action == 'auth':
            try:
                UserCreationClient().create_user(uuid, message.from_user.id, message.from_user.username)
                await message.answer(users_texts.get('register'))
            except APIError as e:
                await message.answer(users_texts.get('register_error'))

    await message.answer(users_texts.get('menu'), reply_markup=generate_buttons(users_buttons.get('menu')))

