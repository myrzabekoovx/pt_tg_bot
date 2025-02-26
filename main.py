import os
import  asyncio

from  aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from dotenv import load_dotenv
from pyexpat.errors import messages

load_dotenv()

TOKEN = os.getenv("TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start(message: types.Message):
    await message.answer('Hello This is your first bot!!!')

@dp.message(CommandStart("info"))
async def info(message: types.Message):
    await message.reply("Assistent")


async def main():
    print("Bot started...")
    await  dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())


