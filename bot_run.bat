@echo off

call %~dp0bot\venv\Scripts\activate

cd %~dp0bot

set TOKEN=6110409963:AAFldmOx1Z-VNN6z28WgzKm3GYO6L2QFLao

python bot_telegram.py

pause