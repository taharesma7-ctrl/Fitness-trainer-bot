from telegram import Update
from telegram.ext import ContextTypes

from keyboards.menu import get_main_menu_keyboard

WELCOME_TEXT = (
    "🏋️ *Personal Trainer Bot'a hoş geldin!*\n\n"
    "Aşağıdaki menüden bir kas grubu seç veya yaz:\n"
    "karın, göğüs, sırt, omuz, biceps, triceps, kol, ön kol, "
    "bacak, kalça, full body, kardiyo\n\n"
    "Sana set, tekrar, açıklama ve dinlenme süreleriyle "
    "tam bir antrenman programı hazırlayacağım.\n\n"
    "Komutlar: /start · /help"
)

HELP_TEXT = (
    "📖 *Yardım*\n\n"
    "*Komutlar*\n"
    "/start — Botu başlat ve menüyü göster\n"
    "/help — Bu mesaj\n\n"
    "*Kas grupları*\n"
    "Menüden dokun veya mesaj olarak yaz:\n"
    "• Karın · Göğüs · Sırt · Omuz\n"
    "• Biceps · Triceps · Kol · Ön Kol\n"
    "• Bacak · Kalça · Full Body · Kardiyo\n\n"
    "Her egzersiz için set, tekrar, açıklama ve dinlenme "
    "süresi verilir.\n\n"
    "💡 Isınma ve soğuma yapmayı unutma. Ağır kiloda "
    "formunu koru."
)


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        WELCOME_TEXT,
        parse_mode="Markdown",
        reply_markup=get_main_menu_keyboard(),
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        HELP_TEXT,
        parse_mode="Markdown",
        reply_markup=get_main_menu_keyboard(),
    )
