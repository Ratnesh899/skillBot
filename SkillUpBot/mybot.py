import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes

# 🔑 Token from environment variable (safe for Railway)
TOKEN = os.getenv("TOKEN")  # Railway pe TOKEN set karna hoga

courses = [
    {"name": "Full Stack Development (Apni Kaksha)", "price": "₹299"},
    {"name": "Data Science PW Gate", "price": "₹1000"},
    {"name": "Python Udemy", "price": "₹100"},
    {"name": "Java Full Stack", "price": "₹500"},
    {"name": "AI/ML", "price": "₹299"},
    {"name": "Generative AI + DevOps", "price": "₹699"}
]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = "👋 Hello! Welcome to Skill Development Bot.\n\n📚 Available Courses & Prices:\n"
    for c in courses:
        text += f"• {c['name']} — {c['price']}\n"

    keyboard = [
        [InlineKeyboardButton("Contact on Telegram 📨", url="https://t.me/Boomerggg321")],
        [InlineKeyboardButton("WhatsApp 📱", url="https://wa.me/9720894349")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(text, reply_markup=reply_markup)

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
