import asyncio
import os
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message

BOT_TOKEN = os.getenv("BOT_TOKEN")
OWNER_ID = int(os.getenv("OWNER_ID"))

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(F.text)
async def chat_with_owner(message: Message):
    if message.from_user.id != OWNER_ID:
        await message.answer("شما اجازه گفتگو با این ربات را ندارید.")
        return
    
    text = message.text.lower()
    if "سلام" in text:
        await message.answer("سلام عزیز دل! 😊")
    elif "خوبی؟" in text:
        await message.answer("مرسی، تو خوبی؟")
    elif "چه خبر؟" in text:
        await message.answer("همه چی آرومه. تو چی؟")
    else:
        await message.answer(f"تو گفتی: {message.text}")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
