import json
import aiofiles

def load_ids_from_json(filename="user_ids.json"):
    try:
        with open(filename, "r") as file:
            data = file.read()
            return set(json.loads(data))
    except FileNotFoundError:
        return set()

async def save_ids_to_json(user_ids, filename="user_ids.json"):
    async with aiofiles.open(filename, "w") as file:
        await file.write(json.dumps(list(user_ids)))
    print(f"ID сохранены в {filename}")