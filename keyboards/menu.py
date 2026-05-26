from telegram import KeyboardButton, ReplyKeyboardMarkup

from data.workouts import VALID_MUSCLES

# Menüde gösterilecek etiketler (kullanıcıya görünen)
MENU_LABELS = [
    "Karın",
    "Göğüs",
    "Sırt",
    "Omuz",
    "Biceps",
    "Triceps",
    "Kol",
    "Ön Kol",
    "Bacak",
    "Kalça",
    "Full Body",
    "Kardiyo",
    "Yardım",
]


def get_main_menu_keyboard() -> ReplyKeyboardMarkup:
    """3 sütunlu reply keyboard menüsü."""
    rows = []
    row = []
    for i, label in enumerate(MENU_LABELS):
        row.append(KeyboardButton(label))
        if len(row) == 3:
            rows.append(row)
            row = []
    if row:
        rows.append(row)

    return ReplyKeyboardMarkup(
        rows,
        resize_keyboard=True,
        one_time_keyboard=False,
        input_field_placeholder="Kas grubu seç veya yaz…",
    )
