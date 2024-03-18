from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

import sys

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')

if (len(sys.argv) < 3):
    print("Not enough arguments")
    exit(1)

app = ApplicationBuilder().token(sys.argv[2]).build()

app.add_handler(CommandHandler("hello", hello))

app.run_webhook(listen="0.0.0.0", port=443, webhook_url=sys.argv[1], cert="YOURPUBLIC.pem", key="YOURPRIVATE.key")