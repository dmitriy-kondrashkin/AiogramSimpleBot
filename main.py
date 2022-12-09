from aiogram import executor
from handlers import dp, start_comma, send_random

async def on_startup(_):
    print('In process!')

start_comma

if __name__ == '__main__':
    executor.start_polling(dispatcher=dp,
                           on_startup=on_startup,
                           skip_updates=True)
