
#%%writefile {file_path}
from fastapi import FastAPI, Request
import httpx, os
from telegram import Update  # из python-telegram-bot

app = FastAPI()
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

# Отдельные функции логики бота
async def handle_start(chat_id: int):
    return "Мама, привет!\n🤖 Render бот готов!"

async def handle_2026(chat_id: int):
    return "Мама, с Новым годом!\nЗдоровья и меньше волнений!!!"

async def handle_echo(text: str):
    return f"Эхо: {text}"

async def send_message(chat_id: int, text: str):
    async with httpx.AsyncClient() as client:
        await client.post(
            f"https://api.telegram.org/bot{TOKEN}/sendMessage",
            json={'chat_id': chat_id, 'text': text}
        )

@app.post(f"/bot{TOKEN}")
async def webhook(request: Request):
    update = await request.json()
    
    if 'message' in update:
        chat_id = update['message']['chat']['id']
        text = update['message'].get('text', '')
        
        # Логика в отдельных функциях
        if text == '/start':
            reply = await handle_start(chat_id)
        elif text == '/2026':
            reply = await handle_2026(chat_id)
        else:
            reply = await handle_echo(text)
        
        await send_message(chat_id, reply)
    
    return {'ok': True}
