import importlib
import os
import sys

sys.path.append(f'/content/tg_bot')
#config = importlib.import_module('config')
sys.path.append(f'/content/tg_bot/modules/')

os.system('pip install pyTelegramBotAPI')

print("Начало")

folder_modules = 'modules'
folder_modules_path = '/content/tg_bot'+'/' +folder_modules #config.myRepo+'/' +folder_modules
modules_list = [os.path.splitext(file)[0] for file in os.listdir(folder_modules_path) if file.endswith('.py')]
imported_modules = {}

# Импортируем и перезагружаем модули
for module in modules_list:
    # Динамический импорт модуля
    imported_module = importlib.import_module(module)
#    importlib.reload(imported_module)
    imported_modules[module] = imported_module

gc = imported_modules['git_com']
tg = imported_modules['tg_neuro_net_bot']

bot_token = sys.argv[1]
tg.my_function()
tg.bot_polling(bot_token)
print("Конец")