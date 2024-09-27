from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault


async def set_menu(bot: Bot):
    menu = [
        BotCommand(
            command='/start',
            description='Запуск бота'
        ),
        BotCommand(
            command='/sigma',
            description='Бахнуть сигму'
        ),
        BotCommand(
            command='/rickandmorty',
            description='Получение информации о персонажах'
        ),
        BotCommand(
            command='/anime',
            description='Поиск аниме по заголовкам'
        ),
        BotCommand(
            command='/weather',
            description='Узнать погоду'
        )


    ]
    await bot.set_my_commands(menu, BotCommandScopeDefault())
