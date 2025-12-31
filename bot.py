# bot.py (Render Web Service, БЕСПЛАТНО!)
from fastapi import FastAPI, Request
import httpx, os

app = FastAPI()
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

@app.post(f"/bot{TOKEN}")
async def webhook(request: Request):
    update = (await request.json())
    
    if 'message' in update:
        chat_id = update['message']['chat']['id']
        text = update['message'].get('text', '')
        
        if text == '/start':
            reply = '🤖 Render бот готов!'
        else:
            reply = f'Вы: {text}'
        
        # Отправляем ответ
        async with httpx.AsyncClient() as client:
            await client.post(f"https://api.telegram.org/bot{TOKEN}/sendMessage",
                json={'chat_id': chat_id, 'text': reply})
    
    return {'ok': True}
