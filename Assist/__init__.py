import asyncio
import os
import pickle as p

from requests import post

try:
    import telethon
except:
    os.system("pip install telethon")
from telethon import TelegramClient

try:
    from DaisyX import bot
except:
    pass
import time


def rd(file):
    try:
        f = open(file, "rb")
        d = p.load(f)
        f.close()
        return d
    except:
        return False


import pickle as p


def wt(obj, file):
    try:
        f = open(file, "wb")
        p.dump(obj, f)
        f.close()
        return True
    except:
        return False



API_ID = os.environ.get("APP_ID", None)
API_HASH = os.environ.get("API_HASH", None)
token = os.environ.get("TG_BOT_TOKEN_BF_HER", None)
STRING_SESSION = os.environ.get("STRING_SESSION")
xbot = TelegramClient("legend", API_ID, API_HASH).start(bot_token=token)
    


botnickname = os.environ.get("BOT_NICK_NAME")
ALIVE_NAME = os.environ.get("ALIVE_NAME")
BOT = str(botnickname) if botnickname else "ᴅᴀɪsʏ χ"
NAME = str(ALIVE_NAME) if ALIVE_NAME else "ᴅᴀᴜsʏ χ"
PHOTO = os.environ.get("ALIVE_PHOTTO", None)
DAISYX = "[DAISY X](https://t.me/DAISYXOT)"
VERSION = "0.0.1"
ALIVE_USERNAME = os.environ.get("ALIVE_USERNAME", None)
ALIVE_BOT_USERNAME = os.environ.get("ALIVE_BOT_USERNAME", None)
devs = [1513257955, 1037581197, 1141839926, 1221693726, 1625410627]
ID = 1513257955
id = 1513257955
REPO = "[ᴅᴀɪsʏ χ вσт](https://github.com/TeamDaisyX/DaisyX-UB)"

MASTER = NAME
GROUP = "[SUPPORT GROUP](https://t.me/DaisySupport_Official)"


def LEGEND(pro, x):
    return print(pro, x)


if __name__ == "__main__":
    xbot.run_until_disconnected()
