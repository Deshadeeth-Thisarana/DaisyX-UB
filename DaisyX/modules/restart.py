from telethon import events, Button, custom
import os,re
from telethon.tl.custom import Button 
from telethon import events, errors, custom, functions
import os, re, sys, asyncio
from DaisyX import admin_cmd

@bot.on(admin_cmd(pattern="restart"))
async def _(event):
    await bot.send_message(event.chat.id, '`Weit restarting`')
    asyncio.sleep(0.5)
    await event.edit('`Restarted successfully`')
    os.execl(sys.executable, sys.executable, *sys.argv)
    quit ()
    
