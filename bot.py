from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message
from config import TOKEN
from utils import load_ids_from_json, save_ids_to_json

bot = Bot(token=TOKEN)
dp = Dispatcher()
user_ids = load_ids_from_json()

@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    user_id = message.from_user.id
    user_ids.add(user_id)
    await message.answer(f"Ваш ID ({user_id}) сохранён, ждите обратной связи!")
    await save_ids_to_json(user_ids)