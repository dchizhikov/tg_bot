import tg_bot.config as config
import importlib
import os

print("Начало")

folder_modules = 'modules'
folder_modules_path = config.myRepo+'/' +folder_modules
modules_list = [os.path.splitext(file)[0] for file in os.listdir(folder_modules_path) if file.endswith('.py')]
imported_modules = {}

# Импортируем и перезагружаем модули
for module in modules_list:
    # Динамический импорт модуля
    imported_module = importlib.import_module(f"{config.folder_name}.modules.{module}")
    importlib.reload(imported_module)
    imported_modules[module] = imported_module

gc = imported_modules['git_com']
tg = imported_modules['tg_neuro_net_bot']

tg.my_function()
tg.bot_polling()
print("Конец")