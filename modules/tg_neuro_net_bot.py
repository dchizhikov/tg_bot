#@tg_neuro_net_bot
import os
import telebot

def my_function():
  print("Привет из отдельного модуля!")

def bot_polling(bot_token):
  bot = telebot.TeleBot(bot_token)
  
  
  # Обработчик сообщений, содержащих команду '/start' или '/help'
  @bot.message_handler(commands=['start', 'help'])
  def send_welcome(message):
    bot.reply_to(
        message,
        "Привет! Я простой бот, который может ответить на вопросы 'как дела' и 'что делаешь'."
    )
  
  
  # Обработчик текстовых сообщений
  @bot.message_handler(func=lambda message: True)
  def echo_all(message):
    text = message.text.lower()
  
    if 'как дела' in text:
      bot.reply_to(message, "Всё отлично, спасибо!")
    elif 'что делаешь' in text:
      bot.reply_to(message, "Я общаюсь с тобой. А что ты делаешь?")
    else:
      bot.reply_to(message, "Извините, я не понимаю этот вопрос.")
  
  
  # Запуск бота
  bot.polling()
