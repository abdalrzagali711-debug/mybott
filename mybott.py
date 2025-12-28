import os
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# تفعيل تسجيل الأخطاء
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# قراءة التوكن من Environment Variable
TOKEN = os.environ.get("TOKEN")
if not TOKEN:
    raise ValueError("يرجى تعيين توكن البوت كمتغير بيئة باسم TOKEN")

# أمر /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("البوت شغال 24 ساعة بإذن الله 😎")

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    logging.info("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
