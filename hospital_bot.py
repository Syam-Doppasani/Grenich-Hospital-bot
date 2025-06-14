import os
import telegram
print("telegram version:", telegram.__version__)

from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

BOT_TOKEN = os.getenv("BOT_TOKEN")

# Start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Welcome to Grenich Hospital Bot!\n"
        "You can ask about hospital hours, appointments, or doctors.\n"
        "Type /help to learn more."
    )

# Help command
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "ℹ️ I can help you with:\n"
        "- Booking an appointment\n"
        "- Hospital timings\n"
        "- Doctor availability"
    )

# General message handler
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.message.text.lower()

    if "appointment" in message:
        await update.message.reply_text("📅 Book an appointment here: https://grenichhospital.com/appointments")
    elif "time" in message or "open" in message:
        await update.message.reply_text("🕘 We're open from 9 AM to 9 PM, Monday to Saturday.")
    elif "doctor" in message:
        await update.message.reply_text("👨‍⚕️ View available doctors at: https://grenichhospital.com/doctors")
    else:
        await update.message.reply_text("❓ Sorry, I didn't understand. Type /help for assistance.")

# Main runner
async def main():
    if not BOT_TOKEN:
        raise ValueError("BOT_TOKEN environment variable not set!")

    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("✅ Grenich Hospital Bot is live!")
    await app.run_polling()

# Start app
if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
