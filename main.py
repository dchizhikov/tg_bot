import importlib
import os
import sys

config = importlib.import_module('config')
repo_up = config.repo_up
repo_name = config.repo_name
folder_modules = '/modules/'
folder_modules_path = repo_up+'/'+repo_name+folder_modules
print(folder_modules_path)

sys.path.append(repo_up+'/'+repo_name)
sys.path.append(folder_modules_path)

os.system('pip install pyTelegramBotAPI')

print("Начало")
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

bot_token = sys.argv[3]
tg.my_function()
tg.bot_polling(bot_token)
print("Конец")