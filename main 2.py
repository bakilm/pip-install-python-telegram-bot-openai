from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
from openai import OpenAI

# توكن بوت تيليجرام
TELEGRAM_TOKEN = "8430029577:AAEsLPZIQAsLtNFV16b9RH9FQd8MMZWJfyI"
# مفتاح Venice/OpenAI
OPENAI_KEY = "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"

client = OpenAI(api_key=OPENAI_KEY, base_url="https://api.venice.ai/api/v1")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("مرحباً! أرسل لي أي سؤال وسأجيبك 🤖")

async def chat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": user_message}]
    )
    await update.message.reply_text(response.choices[0].message.content)

app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, chat))
app.run_polling()