import git.config as config
import importlib
import os

print("Начало")
modules_list = ['gitHub', 'git_com']
imported_modules = {}

# Импортируем и перезагружаем модули
for module in modules_list:
    # Динамический импорт модуля
    imported_module = importlib.import_module(f"{config.folder_name}.modules.{module}")
    importlib.reload(imported_module)
    imported_modules[module] = imported_module

gc = imported_modules['git_com']

if not os.path.exists(f'{config.repo_name}'): 
  gc.git_clone(config.repo_url, config.repo_up)
  gc.git_config(config.user_name)
  gc.git_remote(config.myRepo, config.repo_name, config.branch, config.user_name, config._token)
  gc.git_pull(config.branch, config.remote_branch)
else:
  os.chdir(config.myRepo)
  gc.git_add() #!git add .
  message = f'git 13 commit message'
  gc.git_commit(message)
  gc.git_push(config.branch, config.remote_branch)

print("Конец")