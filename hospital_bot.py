import os
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

# Get the bot token from environment variable
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Start command handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Welcome to Grenich Hospital Bot!\n"
        "You can ask me about our services, departments, or book an appointment.\n"
        "Type /help to know more."
    )

# Help command handler
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 I can help you with:\n"
        "- Book an appointment\n"
        "- Hospital timings\n"
        "- Doctor availability\n"
        "Just type your question!"
    )

# Fallback for general text messages
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()

    if "appointment" in text:
        await update.message.reply_text("📅 To book an appointment, visit: https://grenichhospital.com/appointments")
    elif "timing" in text or "open" in text:
        await update.message.reply_text("🕒 We are open from 9 AM to 9 PM, Monday to Saturday.")
    elif "doctor" in text:
        await update.message.reply_text("👨‍⚕️ You can view doctor availability at: https://grenichhospital.com/doctors")
    else:
        await update.message.reply_text("❓Sorry, I didn't understand that. Try typing /help.")

# Main bot runner
def run_bot():
    if not BOT_TOKEN:
        raise ValueError("❌ BOT_TOKEN environment variable not set!")

    app = ApplicationBuilder().token(BOT_TOKEN).build()

    # Command handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))

    # Message handler
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("✅ Grenich Hospital Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    run_bot()
