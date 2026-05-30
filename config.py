import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")  # يوضع في متغير البيئة أو ملف .env
ADMIN_IDS = [5611506179]            # أيديك كأدمن
DB_PATH = "bot.db"