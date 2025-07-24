import asyncio
import os
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message

# گرفتن توکن از متغیر محیطی
BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# پاسخ به هر پیام متنی از هر کاربر
@dp.message(F.text)
async def reply_all(message: Message):
    user_id = message.from_user.id
    username = message.from_user.username or "بی‌نام"
    text = message.text

    print(f"پیام از {username} ({user_id}): {text}")

    # پاسخ ساده - می‌تونی اینو هوشمند کنی
    await message.answer(f"تو گفتی: {text}")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
