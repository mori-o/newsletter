from fastapi import FastAPI, Body
from bot import bot, user_ids
from models import Item
import asyncio

app = FastAPI()

@app.post("/send")
async def send_message_to_users(Item: Item = Body(...)):
    name = Item.name
    phone = Item.phone
    message = f"Новый запрос от {name}, телефон: {phone}"
    for user_id in user_ids:
        await bot.send_message(user_id, message)
        await asyncio.sleep(0.05)
    return {"message": "Сообщения отправлены"}