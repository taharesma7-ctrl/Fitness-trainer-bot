from telegram import Update
from telegram.ext import ContextTypes

from data.workouts import MUSCLE_ALIASES, VALID_MUSCLES, WORKOUTS
from handlers.commands import help_command
from keyboards.menu import get_main_menu_keyboard

UNKNOWN_TEXT = (
    "⚠️ Bu kas grubunu tanımıyorum.\n\n"
    "Lütfen menüden seç veya şunlardan birini yaz:\n"
    "karın, göğüs, sırt, omuz, biceps, triceps, kol, ön kol, "
    "bacak, kalça, full body, kardiyo\n\n"
    "Yardım için /help veya menüde *Yardım*."
)


def normalize_input(text: str) -> str | None:
    """Kullanıcı girdisini kas grubu anahtarına çevirir."""
    cleaned = text.strip().lower()
    if not cleaned:
        return None

    if cleaned in WORKOUTS:
        return cleaned

    if cleaned in MUSCLE_ALIASES:
        return MUSCLE_ALIASES[cleaned]

    # Menü etiketleri: "Göğüs" -> "göğüs"
    for muscle in VALID_MUSCLES:
        if cleaned == muscle.lower():
            return muscle

    # Türkçe karakter varyasyonları
    replacements = (
        ("ğ", "g"),
        ("ü", "u"),
        ("ş", "s"),
        ("ı", "i"),
        ("ö", "o"),
        ("ç", "c"),
        ("i̇", "i"),
    )
    ascii_variant = cleaned
    for src, dst in replacements:
        ascii_variant = ascii_variant.replace(src, dst)

    if ascii_variant in MUSCLE_ALIASES:
        return MUSCLE_ALIASES[ascii_variant]

    return None


def format_workout(muscle: str) -> str:
    """Antrenman programını Telegram mesajı olarak biçimlendirir."""
    exercises = WORKOUTS[muscle]
    title = muscle.title()
    if muscle == "full body":
        title = "Full Body"
    elif muscle == "kardiyo":
        title = "Kardiyo"

    lines = [f"🏋️ *{title} Antrenmanı*\n"]
    for i, ex in enumerate(exercises, start=1):
        lines.append(f"*{i}. {ex['name']}*")
        lines.append(f"   📊 Set: {ex['sets']} · Tekrar: {ex['reps']}")
        lines.append(f"   ⏱ Dinlenme: {ex['rest']}")
        lines.append(f"   📝 {ex['description']}")
        lines.append("")

    lines.append("_İyi antrenmanlar! 💪_")
    return "\n".join(lines)


async def workout_message_handler(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    if not update.message or not update.message.text:
        return

    text = update.message.text.strip()

    if text.lower() in ("yardım", "yardim", "help"):
        await help_command(update, context)
        return

    muscle = normalize_input(text)
    if muscle is None:
        await update.message.reply_text(
            UNKNOWN_TEXT,
            parse_mode="Markdown",
            reply_markup=get_main_menu_keyboard(),
        )
        return

    await update.message.reply_text(
        format_workout(muscle),
        parse_mode="Markdown",
        reply_markup=get_main_menu_keyboard(),
    )
