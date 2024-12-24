
import asyncio
from aiogram import Bot, Dispatcher, F, types
from aiogram.filters.command import Command
from aiogram.types import Message, Voice
import io
# from dotenv import load_dotenv
import os
from pydub import AudioSegment
import ai
import subprocess
# load_dotenv()

TG_TOKEN = os.getenv("TG_TOKEN")

dp = Dispatcher()



@dp.message(F.text, Command('start'))
async def send_welcome(message: Message):
    chat_id = message.chat.id
    print(message.chat.id)
    await message.reply(text="Hello there")

# @dp.message(F.text)
# async def send_welcome(message: Message):
#     print(message.chat.id)
#     await message.reply(text="Ниче нет")

async def save_voice_as_mp3(bot: Bot, voice: Voice) -> str:
    voice_file_info = await bot.get_file(voice.file_id)
    voice_tmp_path = f"voice_files/voice-{voice.file_unique_id}.tmp"
    await bot.download_file(voice_file_info.file_path, destination=voice_tmp_path)
    voice_wav_path = f"voice_files/voice-{voice.file_unique_id}.wav"
    print(voice_wav_path)
    # AudioSegment.from_file(voice_ogg, format="ogg").export(
    #     voice_wav_path, format="wav"
    # )
    process = subprocess.Popen(
        ["ffmpeg",
         "-loglevel", "quiet",
         "-i", voice_tmp_path,
         "-ar", "16000",
         "-ac", "1",
         "-f", "s16le",
         voice_wav_path]
    )
    process.wait()
    os.remove(voice_tmp_path)
    return voice_wav_path

async def audio_to_text(path: str):
    return await ai.wav_to_text(path)

@dp.message(F.content_type == "voice")
async def process_voice (message: types.Message, bot: Bot):
    voice_path = await save_voice_as_mp3(bot, message.voice)
    name, answer = await audio_to_text(voice_path)
    os.remove(voice_path)
    await message.reply(text=f"{name} : {answer}")


async def main():
    bot = Bot(token=TG_TOKEN)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())