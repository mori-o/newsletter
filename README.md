# My Bot and API Project

## Setup
1. Clone the repo: `git clone <URL>`
2. Create a virtual environment: `python -m venv venv`
3. Activate it: `source venv/bin/activate` (Linux/Mac) or `venv\Scripts\activate` (Windows)
4. Install dependencies: `pip install -r requirements.txt`
5. Create `.env` file with `API_TOKEN=<your_telegram_bot_token>`
6. Run: `python main.py`

## Usage
- Telegram: Send `/start` to the bot.
- API: `curl -X POST "http://localhost:8000/send" -H "Content-Type: application/json" -d '{"name": "ahmed", "phone": "7777777"}'`