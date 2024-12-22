from aiogram import Router


def get_handlers_router() -> Router:
    from . import users, admins

    router = Router()
    router.include_router(users.help.router)

    router.include_router(admins.start.router)

    router.include_router(users.start.router)

    return router