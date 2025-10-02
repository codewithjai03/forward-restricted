#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = config("6623123259", default=None, cast=int)
API_HASH = config("AAGrWBfyUP9IFTibaUKaSZZ4EyRbqu2JEcI", default=None)
BOT_TOKEN = config("6623123259:AAGrWBfyUP9IFTibaUKaSZZ4EyRbqu2JEcI", default=None)
SESSION = config("BQFqIokApZRNc_9QqhwgZz1buZ6VaCZNOkGt2VsVCFTJzD1a-lOchN5ElB7CsfwkHdVNiqZ57aIvcb6kl_yr9rAEGVzjRdAlGQHIoz9xwv7J8lMAdMPwHjbdZ0BX2uZDNlyrU_yTJD91joQenddNcRTcbo9CH5ze34ipsrU8YD2akmUeRW7qxRWC2VWpbIoLKMt2UtoKNuqpHiuGXGlm3qKvvo8K8oauFApbOQ68jcCw8c7vNQpCVw-kNMFIas5ki1QfGgMLVQHs-PEuHOtFZUE-7VW3-SNGQ7Lmpm06DkrlanJVDZHlmQj7RzBKCpYFWLylnYgy5sZfo8ZOwsDSexGufBOgAAAAE2R3qpAA", default=None)
FORCESUB = config("amazon_flipkart_meesho_dealsZone", default=None)
AUTH = config("5205621417", default=None, cast=int)

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client(
    session_name=SESSION, 
    api_hash=API_HASH, 
    api_id=API_ID)

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
