from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
import asyncio
import os
BOT_TOKEN = os.getenv("bot-token")


faq_responses = {
    "hi": "👋 Welcome to Grenich Hospital! Type 'help' to see what I can do.",
    "help": "You can ask me about:\n- timings\n- location\n- fees\n- insurance\n- appointment",
    "timings": "🕘 We're open Mon–Sat, 9 AM to 7 PM.",
    "location": "📍 123 Health Street, Chennai.\n[View on Maps](https://maps.google.com?q=123+Health+Street)",
    "fees": "💰 General consultation fee is ₹500. Specialist charges may vary.",
    "insurance": "✅ We accept major insurance providers like Star Health, ICICI, and LIC.",
    "appointment": "📞 Call 044-12345678 or visit our site to book: https://grenichhospital.com/appointments"
}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_chat_action(chat_id=update.effective_chat.id, action="typing")
    await asyncio.sleep(1.2)  # Simulate typing delay
    await update.message.reply_text(faq_responses["hi"])

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower().strip()
    response = faq_responses.get(text, "❓ Sorry, I didn't understand. Try typing 'help'.")

    await context.bot.send_chat_action(chat_id=update.effective_chat.id, action="typing")
    await asyncio.sleep(1.5)  # Simulate typing delay
    await update.message.reply_text(response, parse_mode="Markdown")

def run_bot():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("✅ Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    run_bot()
