import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from pytube import YouTube
from io import BytesIO
from config import TOKEN

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def start(message:types.Message):
    ism = message.from_user.full_name
    await message.answer(f"Assalom alaykum <b>{ism}</b> botimizga xush kelibsiz!😊\n Yuklab olmoqchi bo`lgan auodioingizni linkini yuboring!", parse_mode="HTML")


@dp.message_handler(commands=["admin"])
async def start(message:types.Message):
    admin = "@Ramziddin_17_17"
    await message.answer(f"Bot admini:{admin}")


@dp.message_handler(commands=["help"])
async def start(message:types.Message):
    await message.answer("Bu botimiz orqali siz YouTube dagi har qanday videoni audiosini yuklab beradi va yuklab berish uchun"
                         "botimizga shu videoni linkini yuborsangiz kifoya!")


@dp.message_handler(Text(startswith="https"))
async def youtubeaudio(message:types.Message):
    try:
        await message.answer("Yuklanmoqda...🚀")
        youtube_link = message.text
        buffer = BytesIO()
        url = YouTube(youtube_link)
        if url.check_availability() is None:
            audio = url.streams.get_audio_only()
            audio.stream_to_buffer(buffer=buffer)
            buffer.seek(0)
            video_title = url.title
            await message.answer_audio(audio=buffer, caption=video_title)
    except:
            await message.answer("Linkni qaytadan tekshirib koring!")


if __name__ == "__main__":
    executor.start_polling(dp,skip_updates=True)

