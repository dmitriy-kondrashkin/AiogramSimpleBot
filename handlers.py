from aiogram import Bot, Dispatcher, types
from config import  TOKEN_API
from keyboards import rkb, ikb, rkb_photo, ikb2
import random
from aiogram.dispatcher.filters import Text
from aiogram.types import ReplyKeyboardRemove

cat1 = 'https://d.newsweek.com/en/full/1920025/cat-its-mouth-open.jpg?w=1600&h=1600&q=88&f=b7a44663e082b8041129616b6b73328d'
cat2 = 'https://pbs.twimg.com/media/FD-Y3soVEAE9Sjj?format=jpg&name=900x900'
cat3 = 'https://www.researchgate.net/publication/344603358/figure/fig1/AS:945655560286208@1602473263829/Example-of-Cat-Meme_Q320.jpg'
cat4 = 'https://wompampsupport.azureedge.net/fetchimage?siteId=7575&v=2&jpgQuality=100&width=700&url=https%3A%2F%2Fi.kym-cdn.com%2Fphotos%2Fimages%2Fnewsfeed%2F002%2F205%2F309%2F1d3.jpg'
list_of_cats = [cat1,cat2,cat3,cat4]
list_of_captions = ['Probably youre shocked 🤯 \nIs that you?!',
                    'MAYBE YOURE A DWAYNE? 🤨 \nIs that you?!',
                    'It was hard... but i found YOUR PHOTO! 🤗 \nIs that you?!',
                    'Oh, maybe there something you dont know... 🫣 \nIs that you?!']
cats_and_captions = dict(zip(list_of_cats, list_of_captions))
sticker1 = 'CAACAgIAAxkBAAEGsMBjjbdqY5t5_sSyw7zB1x98V3_elgACNCAAAv-MiUrX3kjkNFpk7SsE'
sticker2 = 'CAACAgIAAxkBAAEGsMJjjbdsHc_Du92b3DN6ye3JTOqEtQAC6CQAAukgiUqFtzrVQxgGIisE'
sticker3 = 'CAACAgIAAxkBAAEGsMRjjbduViJNGP2lfxWcTqY6UDkMQgAC9h0AAqDdiEoBpgQJ3cP92ysE'
sticker4 = 'CAACAgIAAxkBAAEGsMhjjbd2WHx8suxK4duRu0Q-Ty9rxQACuR0AAgSGiErO98WePJaUXysE'
list_of_stickers = (sticker1, sticker2, sticker3, sticker4)
bot = Bot(TOKEN_API)
dp = Dispatcher(bot)
help_list = """
    HERE THE LIST OF COMMANDS:
<b>/start</b> - <em>start working with bot.</em>
<b>--Description</b> - <em>description of bot.</em>
<b>--HELP</b> - <em>commands list.</em>
<b>--Random picture 🎰📸</b> - <em>send random picture for you! who knows who you are...</em>
<b>--Random emodji 🙂/🙁</b> - <em>send random emoji for you!</em>
<b>--Random location 🛤</b> - <b>(DOESNT WORK)</b><em>send random location for you in range of 0,1000</em>
<b>--Random sticker 👽</b> - <em>send random cute sticker for you!</em>
"""

async def send_random(message: types.Message):
    ran_photo = random.choice(list(cats_and_captions.keys()))
    ran_caption = cats_and_captions[ran_photo]
    await bot.send_photo(chat_id=message.chat.id,
                         photo=ran_photo,
                         caption=ran_caption,
                         reply_markup=ikb)
    await bot.send_message(chat_id=message.chat.id,
                           text='One more roll?',
                           reply_markup=ikb2)

@dp.message_handler(commands=['start'])
async def start_comma(message: types.Message):
    await bot.send_message(chat_id=message.chat.id,
                           text='Welcome to me!',
                           reply_markup=rkb)
    await bot.send_sticker(chat_id=message.chat.id,
                           sticker='CAACAgIAAxkBAAEGsfZjjerfNlGzKmrA1rT1t2c2d_hhMQACUAEAAlKJkSNl5cDJKalLGCsE')
    await message.delete()

@dp.message_handler(Text(equals='Description'))
async def descr_comma(message: types.Message):
    await bot.send_message(chat_id=message.chat.id,
                           text='Everything i can do you can see in HELP command!')
    await message.delete()

@dp.message_handler(Text(equals='HELP'))
async def help_comma(message: types.Message):
    await bot.send_message(chat_id=message.chat.id,
                           text=help_list,
                           parse_mode='HTML')
    await message.delete()

@dp.message_handler(Text(equals='Random picture 🎰📸'))
async def picture_comma(message: types.Message):
    await bot.send_message(chat_id=message.chat.id,
                           text='Welcome to picture menu! \nChoose an option!',
                           reply_markup=rkb_photo)
    await message.delete()

@dp.message_handler(Text('Roll a picture'))
async def picture_rolling(message: types.Message):
    await bot.send_message(chat_id=message.chat.id,
                           text='Ran photo',
                           reply_markup=ReplyKeyboardRemove())
    await send_random(message)
    await message.delete()

@dp.callback_query_handler()
async def picture_callback(callback: types.CallbackQuery):
    if callback.data == 'yes':
        await callback.answer(text='I knew it!')
    elif callback.data == 'no':
        await callback.answer(text='Ehh.. Even the smartest people make mistakes...')
    elif callback.data == 'next':
        await send_random(message=callback.message)
    elif callback.data == 'menu':
        await callback.message.answer('Welcome back!',
                                      reply_markup=rkb)
        await callback.message.delete()
        await callback.answer()

@dp.message_handler(Text(equals='Random emodji 🙂/🙁'))
async def emodji_comma(message: types.Message):
    emodji_list = random.choice('🤥😶🥴😩🤓🤪')
    await bot.send_message(chat_id=message.chat.id,
                           text=emodji_list)
    await message.delete()

@dp.message_handler(Text(equals='Random location 🛤'))
async def location_comma(message: types.Message):
    await bot.send_location(chat_id=message.chat.id,
                            longitude=random.randint(10,500),
                            latitude=random.randint(10,500))
    await message.delete()

@dp.message_handler(Text(equals='Random sticker 👽'))
async def sticker_comma(message: types.Message):
    await bot.send_sticker(chat_id=message.chat.id,
                           sticker=random.choice(list_of_stickers))
    await message.delete()
