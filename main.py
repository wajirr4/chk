#pylint:disable=C0114
import logging
import os
from pyrogram import Client
from pyrogram.errors import RPCError
from pyrogram.errors import BadRequest
# import asyncio
# from pyrogram.errors import FloodWait
# from pyrogram.handlers import MessageHandler
# os.environ['TZ'] = 'Asia/Kolkata'



logging.basicConfig(level=logging.INFO)



bot = Client(
    'bot',
    api_id= 16596628, #get it from https://my.telegram.org/auth
    api_hash="421764a823ee2dff786d413aea09959f", #get it from https://my.telegram.org/auth
    bot_token="5422383759:AAGLjai3rafneochAMTx_azF9U6dwpY5s4s", #get it from @Botfather
    plugins=dict(root="plugins"),
    parse_mode="html")


try:
    bot.run()
except Exception as e:
    print(e)
        
