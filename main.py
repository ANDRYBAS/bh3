import asyncio
from datetime import datetime
from aiogram import Bot
import os

TOKEN = os.getenv('BOT_TOKEN')
CHANNEL_ID = os.getenv('CHANNEL_ID')

async def main():
    bot = Bot(token=TOKEN)
    today_date = datetime.now().strftime("%d.%m.%Y")
    await bot.send_message(chat_id=CHANNEL_ID, text=f"#BH3 НЕ вышло {today_date}")
    await bot.session.close()

if __name__ == "__main__":
    asyncio.run(main())