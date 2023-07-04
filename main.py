from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

BOT_TOKEN = "6186372028:AAEa8PgCniHyHgJIo6B34PtilLlOV6gej4Q"


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    print("Start function called")
    user = update.message.from_user
    print(user["first_name"])
    await update.message.reply_text("Hello, welcome in my bot!")


async def get_info(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    print("Get_info function called")
    user = update.message.from_user
    print(user["first_name"])
    message = f"User info:\nID: {user['id']}\nFirst Name: {user['first_name']}\nLast Name: {user['last_name']}"
    await update.message.reply_text(message)


def run():
    print("Application started")
    application = ApplicationBuilder().token(BOT_TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", start))
    application.add_handler(CommandHandler("get_info", get_info))

    application.run_polling()


if __name__ == "__main__":
    run()
