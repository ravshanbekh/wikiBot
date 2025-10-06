import asyncio
from os import getenv
import wikipedia

from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message

wikipedia.set_lang('uz')
TOKEN = "8290494668:AAEh7v-5hw40PHt6cOo3ji0nmiKB8KnZbqo"

dp = Dispatcher()


# Command handler
@dp.message(Command("start"))
async def command_start_handler(message: Message) -> None:
    await message.answer("Salom Meni botimga xush kelibsan.")


@dp.message(F.text)
async def javob_qaytar(message:Message):
    try:
        malumot=wikipedia.summary(message.text)
        await message.answer(malumot)
    except:
        await message.answer("Bunday malumot topilmadi")

# Run the bot
async def main() -> None:
    bot = Bot(token=TOKEN)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
