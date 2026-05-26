# Personal Trainer Bot

Telegram üzerinden kas grubuna göre antrenman programı veren Python botu.

## Kurulum

```powershell
cd "c:\Users\agok4\OneDrive\Masaüstü\telegram-fitness-bot"
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
copy .env.example .env
```

`.env` dosyasını düzenleyip [@BotFather](https://t.me/BotFather) token'ınızı ekleyin:

```
TELEGRAM_BOT_TOKEN=123456789:ABCdef...
```

## Çalıştırma

```powershell
python bot.py
```

## Dosya yapısı

```
telegram-fitness-bot/
├── bot.py
├── handlers/
│   ├── commands.py
│   └── workout_handler.py
├── data/
│   └── workouts.py
├── keyboards/
│   └── menu.py
├── .env
├── requirements.txt
└── README.md
```
