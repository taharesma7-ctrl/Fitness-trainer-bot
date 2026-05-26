"""Personal Trainer Bot — giriş noktası."""

import logging
import os
import sys

from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters

from handlers.commands import help_command, start_command
from handlers.workout_handler import workout_message_handler

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)


def get_token() -> str:
    load_dotenv()
    token = os.getenv("TELEGRAM_BOT_TOKEN")
    if not token or token == "your_bot_token_here":
        logger.error(
            "TELEGRAM_BOT_TOKEN bulunamadı. .env dosyasına geçerli token yazın."
        )
        sys.exit(1)
    return token


def main() -> None:
    token = get_token()
    application = Application.builder().token(token).build()

    application.add_handler(CommandHandler("start", start_command))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, workout_message_handler)
    )

    logger.info("Bot çalışıyor… (Ctrl+C ile durdur)")
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
