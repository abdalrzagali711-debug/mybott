import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# قراءة التوكن من Environment Variable
TOKEN = os.environ.get("TOKEN")
if not TOKEN:
    raise ValueError("يرجى تعيين توكن البوت كمتغير بيئة باسم TOKEN")

# دالة أمر /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_first_name = update.effective_user.first_name  # جلب اسم المستخدم
    await update.message.reply_text(f"أهلاً {user_first_name}! البوت شغال 24 ساعة على Render 👍")

# الدالة الرئيسية لتشغيل البوت
def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()

# التأكد من تشغيل البوت فقط عند تنفيذ هذا الملف مباشرة
if __name__ == "__main__":
    main()
