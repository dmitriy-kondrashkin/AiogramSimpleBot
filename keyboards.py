from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

rkb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
rkb_b1 = KeyboardButton('/start')
rkb_b2 = KeyboardButton('Description')
rkb_b3 = KeyboardButton('HELP')
rkb_b4 = KeyboardButton('Random picture 🎰📸')
rkb_b5 = KeyboardButton('Random emodji 🙂/🙁')
rkb_b6 = KeyboardButton('Random location 🛤')
rkb_b7 = KeyboardButton('Random sticker 👽')
rkb.add(rkb_b2, rkb_b3)
rkb.add(rkb_b7, rkb_b5)
rkb.add(rkb_b6, rkb_b4)

rkb_photo = ReplyKeyboardMarkup(resize_keyboard=True)
rkb_p1 = KeyboardButton('Roll a picture')
rkb_photo.add(rkb_p1)

ikb = InlineKeyboardMarkup(row_width=3)
ik_b1 = InlineKeyboardButton('Yes, its me!',
                             callback_data='yes')
ik_b2 = InlineKeyboardButton('No, definitely not me!',
                             callback_data='no')
ik_b3 = InlineKeyboardButton('Roll next picture',
                             callback_data='next')
ik_b4 = InlineKeyboardButton('Back',
                             callback_data='menu')
ikb.add(ik_b1, ik_b2)

ikb2 = InlineKeyboardMarkup(row_width=3)

ikb2.add(ik_b3, ik_b4)