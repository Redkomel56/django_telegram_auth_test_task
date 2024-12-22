from aiogram.types import BotCommand, BotCommandScopeDefault
from config import users_texts


async def set_default_commands(bot):

    commands = [BotCommand(command=command[0], description=command[1]) for item in users_texts.get('commands').split('\n') if (command:=item.split(' - ')) and command[0]]
    await bot.set_my_commands(commands, scope=BotCommandScopeDefault())