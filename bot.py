import asyncio
import os
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message

BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = int(os.getenv("ADMIN_ID"))  # آیدی عددی شما

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# وقتی کاربر پیام بده، برای ادمین فوروارد میشه
@dp.message(F.text & ~F.from_user.id == ADMIN_ID)
async def forward_user_message(message: Message):
    user_id = message.from_user.id
    username = message.from_user.username or "بدون‌نام"
    msg_text = message.text

    # فرستادن پیام به ادمین با آیدی کاربر
    await bot.send_message(
        ADMIN_ID,
        f"📩 پیام جدید از {username} ({user_id}):\n{msg_text}"
    )

    # optionally به خود کاربر بگو که پیامش ارسال شد
    await message.reply("✅ پیام شما برای پشتیبانی ارسال شد.")

# وقتی ادمین reply کنه به پیام کاربر
@dp.message(F.reply_to_message, F.from_user.id == ADMIN_ID)
async def reply_to_user(message: Message):
    reply_text = message.text

    # استخراج آیدی کاربر از پیام قبل
    lines = message.reply_to_message.text.split("\n")
    if len(lines) > 0 and "(" in lines[0] and ")" in lines[0]:
        try:
            user_id = int(lines[0].split("(")[-1].replace("):", "").replace(")", ""))
            await bot.send_message(user_id, f"👨‍💼 پشتیبانی:\n{reply_text}")
        except:
            await message.reply("❌ آیدی کاربر قابل تشخیص نیست.")
    else:
        await message.reply("❌ لطفاً روی پیام کاربر ریپلای بزنید.")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
