import asyncio
import html
import logging
import requests

from aiogram import Bot, Dispatcher, F, Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from aiogram.enums import ChatAction

from config import OMDB_API_KEY, OMDB_URL, TELEGRAM_BOT_TOKEN

logging.basicConfig(level=logging.INFO)

router = Router()

    
@router.message(CommandStart())
async def start(message: Message):
    """Send welcome message when /start command is used"""
    welcome_text = (
        "🎬 Welcome to IMDB Search Bot! 🎥\n\n"
        "Simply send me the name of any movie or TV series, "
        "and I'll find information about it!\n\n"
        "Examples:\n"
        "• The Social Network\n"
        "• Silicon Valley\n"
        "• The Matrix\n\n"
        "Let's get started! 🍿"
    )
    await message.answer(welcome_text)


@router.message(Command("help"))
async def help_command(message: Message):
    """Send help message"""
    help_text = (
        "🎬 <b>IMDB Search Bot Help</b> 🎥\n\n"
        "<b>How to use:</b>\n"
        "Just send me the name of any movie or TV series!\n\n"
        "<b>Commands:</b>\n"
        "/start - Start the bot\n"
        "/help - Show this help message\n\n"
        "<b>Examples:</b>\n"
        "• Mr. Robot\n"
        "• The Imitation Game\n"
        "• Silicon Valley\n"
        "• The Social Network\n\n"
        "Enjoy searching! 🍿"
    )
    await message.answer(help_text, parse_mode="HTML")


@router.message(F.text)
async def search_movie(message: Message, bot: Bot):
    """Search for movie/series and return details"""
    query = message.text.strip()

    if not query:
        await message.answer("Please send me a movie or series name!")
        return

    # Show typing indicator
    await bot.send_chat_action(chat_id=message.chat.id, action=ChatAction.TYPING)

    try:
        params = {
            "apikey": OMDB_API_KEY,
            "t": query,
            "plot": "full",
        }
        response = requests.get(OMDB_URL, params=params, timeout=10)
        data = response.json()

        if data.get("Response") == "True":
            title = html.escape(data.get("Title", "N/A"))
            year = html.escape(data.get("Year", "N/A"))
            rated = html.escape(data.get("Rated", "N/A"))
            genre = html.escape(data.get("Genre", "N/A"))
            runtime = data.get("Runtime", "N/A")
            director = html.escape(data.get("Director", "N/A"))
            plot = html.escape(data.get("Plot", "N/A"))
            imdb_rating = html.escape(data.get("imdbRating", "N/A"))
            imdb_votes = html.escape(data.get("imdbVotes", "N/A"))
            poster = data.get("Poster", "N/A")

            # Convert runtime to hours and minutes
            runtime_formatted = runtime
            if runtime != "N/A" and "min" in runtime:
                try:
                    minutes = int(runtime.split()[0])
                    hours = minutes // 60
                    mins = minutes % 60
                    runtime_formatted = f"{hours}h {mins}m" if hours > 0 else f"{mins}m"
                except Exception:
                    runtime_formatted = runtime

            if director == "N/A":
                director = "Not Found"
            if rated == "N/A":
                rated = "Not Rated"
            if runtime_formatted == "N/A":
                runtime_formatted = "Unknown"

            text = (
                f"🎬 <b>{title}</b> ({year})\n\n"
                f"⭐️ <b>IMDB Rating:</b> {imdb_rating}/10 ({imdb_votes} votes)\n"
                f"🎭 <b>Genre:</b> {genre}\n"
                f"⏱ <b>Runtime:</b> {runtime_formatted}\n"
                f"🔞 <b>Rated:</b> {rated}\n\n"
                f"🎬 <b>Director:</b> {director}\n\n"
                f"📖 <b>Plot:</b>\n{plot}"
            )

            if poster and poster != "N/A":
                try:
                    await message.answer_photo(
                        photo=poster,
                        caption=text,
                        parse_mode="HTML",
                    )
                except Exception:
                    await message.answer(text, parse_mode="HTML")
            else:
                await message.answer(text, parse_mode="HTML")

        else:
            # Send duck sticker when movie not found
            await message.answer_sticker(
                "CAACAgIAAxkBAAECuAVo81iYKYdD0VVoi6Bt85xjp4nI7gACAgEAAladvQpO4myBy0Dk_zYE"
            )
            error_msg = data.get("Error", "Movie/Series not found!")
            await message.answer(f"❌ {error_msg}\n\n🔄 Please check the spelling and try again.")

    except requests.exceptions.Timeout:
        await message.answer("⏱ Request timeout. Please try again!")
    except Exception as e:
        await message.answer(f"❌ An error occurred: {str(e)}")


async def main():
    bot = Bot(token=TELEGRAM_BOT_TOKEN)
    dp = Dispatcher()
    dp.include_router(router)

    print("Bot is running...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())