import asyncio
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode

from config import TOKEN_BOT
from aiogram.client.default import DefaultBotProperties


TOKEN = TOKEN_BOT
bot = Bot(TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

dp = Dispatcher()


async def main() -> None:
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
