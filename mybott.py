import os
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# تفعيل تسجيل الأخطاء
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

# قراءة التوكن من Environment Variable
TOKEN = os.environ.get('TOKEN')

if not TOKEN:
    raise ValueError("يرجى تعيين توكن البوت كمتغير بيئة باسم TOKEN")

# إنشاء التطبيق
app = ApplicationBuilder().token(TOKEN).build()

# وظيفة أمر /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("البوت شغال👌")

# إضافة الهاندلر
app.add_handler(CommandHandler("start", start))

# تشغيل البوت
if __name__ == "__main__":
    app.run_polling()
