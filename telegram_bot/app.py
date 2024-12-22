from aiogram.types import BotCommand

from loader import dp, bot, logger
import filters, handlers
from middlewares import register_middlewares
from utils.set_bot_commands import set_default_commands

import asyncio


async def main():

    try:
        await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())
    finally:
        await bot.session.close()


async def on_startup() -> None:
    logger.info("bot starting...")

    register_middlewares(dp)

    dp.include_router(handlers.get_handlers_router())

    await set_default_commands(bot)

    bot_info = await bot.get_me()

    logger.info(f"Name     - {bot_info.full_name}")
    logger.info(f"Username - @{bot_info.username}")
    logger.info(f"ID       - {bot_info.id}")

    states: dict[bool | None, str] = {
        True: "Enabled",
        False: "Disabled",
        None: "Unknown (This's not a bot)",
    }

    logger.info(f"Groups Mode  - {states[bot_info.can_join_groups]}")
    logger.info(f"Privacy Mode - {states[not bot_info.can_read_all_group_messages]}")
    logger.info(f"Inline Mode  - {states[bot_info.supports_inline_queries]}")

    logger.info("bot started")


async def main() -> None:
    # logger.add(
    #     "logs/telegram_bot.log",
    #     level="DEBUG",
    #     format="{time} | {level} | {module}:{function}:{line} | {message}",
    #     rotation="100 KB",
    #     compression="zip",
    # )

    dp.startup.register(on_startup)
    # dp.shutdown.register(on_shutdown)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


if __name__ == '__main__':
    asyncio.run(main())


