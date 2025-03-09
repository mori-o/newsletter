import asyncio
from uvicorn import Config, Server
from api import app
from bot import dp, bot

async def start_fastapi():
    config = Config(app=app, host="0.0.0.0", port=8000)
    server = Server(config)
    await server.serve()

async def main():
    await asyncio.gather(
        dp.start_polling(bot),
        start_fastapi()
    )

if __name__ == "__main__":
    asyncio.run(main())