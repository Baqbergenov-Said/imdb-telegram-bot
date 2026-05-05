# 🎬 IMDB Search Bot

A fast, async Telegram bot that fetches movie and TV series info from the OMDB API — built with **aiogram 3** and **aiohttp**.

---

## 📸 Preview

Send any movie or series name and get back:

- 🎬 Title, year, type (movie / series)
- ⭐ IMDB rating with star display
- 🎭 Genre, runtime, director, cast
- 💵 Box office & 🏆 awards (when available)
- 📖 Full plot summary
- 🖼 Poster image
- 🔗 Direct link to IMDb page

---

## 🚀 Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
cd YOUR_REPO_NAME
```

### 2. Create a virtual environment

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install aiogram pydantic-settings
```

### 4. Set up environment variables

Create a `.env` file in the root folder:

```env
BOT_TOKEN=your_telegram_bot_token
OMDB_API_KEY=your_omdb_api_key
```

- Get a bot token from [@BotFather](https://t.me/BotFather)
- Get a free OMDB API key at [omdbapi.com/apikey.aspx](https://www.omdbapi.com/apikey.aspx)

### 5. Run

```bash
python bot.py
```

---

## 📁 Project Structure

```
├── bot.py                  # Entry point
├── config.py               # Settings loaded from .env
├── .env                    # Your secret keys (never commit this!)
├── .env.example            # Example env file
│
├── handlers/
│   ├── __init__.py
│   ├── start.py            # /start and /help commands
│   └── search.py           # Movie search + callback buttons
│
├── services/
│   ├── __init__.py
│   └── omdb.py             # Async OMDB API client
│
├── keyboards/
│   ├── __init__.py
│   └── inline.py           # Inline keyboards
│
├── middlewares/
│   ├── __init__.py
│   └── throttling.py       # Per-user rate limiter
│
└── utils/
    ├── __init__.py
    └── formatters.py       # HTML message formatters
```

---

## ✨ Features

| Feature | Details |
|---|---|
| ⚡ Async HTTP | `aiohttp` — no blocking calls |
| 🔒 Secure config | `.env` via `pydantic-settings` |
| 🐢 Throttling | Per-user rate limiting middleware |
| 🎛 Inline buttons | View on IMDb + Search another |
| 🖼 Poster support | Photo with caption, fallback to text |
| ⭐ Star ratings | `8.5/10` → `⭐⭐⭐⭐☆` |
| 📺 Series support | Works for movies, series & episodes |
| 📋 Logging | Timestamped logs with proper levels |

---

## 🛠 Tech Stack

- [Python 3.10+](https://www.python.org/)
- [aiogram 3](https://docs.aiogram.dev/) — Telegram Bot framework
- [aiohttp](https://docs.aiohttp.org/) — Async HTTP client
- [pydantic-settings](https://docs.pydantic.dev/latest/concepts/pydantic_settings/) — Config management
- [OMDB API](https://www.omdbapi.com/) — Movie data

---

## ⚠️ Important

Never commit your `.env` file. Make sure your `.gitignore` includes:

```
.env
venv/
__pycache__/
*.pyc
```

---

## 📄 License

MIT — free to use and modify.
