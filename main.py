import asyncio
from datetime import datetime
from aiogram import Bot
import os

TOKEN = os.getenv('8620812963:AAHr4uUdyydh9xuxKo6s7HJEJ19SA9AI6I4')
CHANNEL_ID = os.getenv('-1003850747386')

async def main():
    bot = Bot(token=TOKEN)
    today_date = datetime.now().strftime("%d.%m.%Y")
    await bot.send_message(chat_id=CHANNEL_ID, text=f"#BH3 НЕ вышло {today_date}")
    await bot.session.close()

if __name__ == "__main__":
    asyncio.run(main())