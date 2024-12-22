from aiogram import types, F
from aiogram.fsm.context import FSMContext
from aiogram.filters import CommandStart, Command, StateFilter

from loader import dp
from config import users_buttons, users_texts, admins_texts, admins_buttons
from filters import IsPrivate, IsAdmin
from keyboards.inline.mune_inline_kb import generate_buttons
from aiogram import Router


router = Router()


@router.message(StateFilter("*"), IsPrivate(), IsAdmin(), Command('panel'))
async def admin_start(message: types.Message, state: FSMContext):
    await state.clear()
    await message.answer(text=admins_texts.get('menu'), reply_markup=generate_buttons(admins_buttons.get('menu')))


@router.callback_query(StateFilter("*"), F.data.startswith("ad_menu"))
async def menu(call: types.CallbackQuery, state: FSMContext):
    await state.clear()
    await call.message.answer(text=admins_texts.get('menu'), reply_markup=generate_buttons(admins_buttons.get('menu')))
