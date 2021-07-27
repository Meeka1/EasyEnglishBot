import logging
from oxfordLookup import get_definition
from aiogram import Bot, Dispatcher, executor, types
from googletrans import Translator

API_TOKEN = '1828110432:AAGOXXIYqeVtHUI32VtLq3f3wV0rgLtbKJU'

# Configure logging
logging.basicConfig(level=logging.INFO)

translator = Translator()
# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Hi and Welcome to the Translator Bot created by Meeka!")


@dp.message_handler()
async def ftranslator(message: types.Message):
    lang = translator.detect(message.text).lang
    if len(message.text.split())>=2:
        dest = 'uz' if lang == 'en' else 'en'
        await message.reply(translator.translate(message.text,dest).text)
    else:
        if lang == 'en':
            word_id = message.text
        else:
            word_id = translator.translate(message.text ,dest='en').text

        lookUp  = get_definition(word_id)

        if lookUp:
            await message.reply(f"Word: {word_id}\nDefinitions:\n{lookUp['definitions']}")
            if lookUp.get('audio'):
                await message.reply_voice(lookUp['audio'])
        else:
            await message.reply('Ops, no word with such title was found :(')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)