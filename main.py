from aiogram import Bot, Dispatcher, F
from asyncio import run
from functions import echo
from filters import check_in_text

dp = Dispatcher()

async def startup_answer(bot: Bot):
    await bot.send_message(1184193890, "Bot Ishga tushdi! ✅")

async def shutdown_answer(bot: Bot):
    await bot.send_message(1184193890, "Bot ishdan to'xtadi! ❌")


async def start():

    dp.startup.register(startup_answer)
    
    # dp.message.register(echo, F.photo) # faqat photo bolsa javob qaytaradi
    dp.message.register(echo, check_in_text(["salom", "nima gap"])) 
    
    dp.shutdown.register(shutdown_answer)

    bot = Bot("6803882554:AAH91YHRcmFQQnZmhzy0ZWpRXscZiJBNeV4")
    await dp.start_polling(bot)

run(start())
