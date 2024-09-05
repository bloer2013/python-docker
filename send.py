import os
import subprocess
import telegram
from telegram import InputFile

# Укажите токен вашего бота и ID вашего чата в Telegram
TELEGRAM_BOT_TOKEN = "your_telegram_bot_token"
TELEGRAM_CHAT_ID = "your_chat_id"

# Путь к файлу
file_name = "domain-ip-resolve.txt"
file_path = None

# Поиск файла в системе
for root, dirs, files in os.walk("/"):
    if file_name in files:
        file_path = os.path.join(root, file_name)
        break

# Проверяем, найден ли файл
if file_path:
    try:
        # Отправка файла в Telegram
        bot = telegram.Bot(token=TELEGRAM_BOT_TOKEN)
        with open(file_path, 'rb') as f:
            bot.send_document(chat_id=TELEGRAM_CHAT_ID, document=InputFile(f))

        # Удаление файла
        subprocess.run(["sudo", "rm", file_path], check=True)
        print(f"Файл {file_path} был успешно отправлен и удален.")
    
    except Exception as e:
        print(f"Произошла ошибка: {e}")
else:
    print(f"Файл {file_name} не найден в системе.")
