import os

try:
    from Assist import xbot
except:
    pass
try:
    from DaisyX.functions.DaisyX import xbot
except:
    pass
try:
    from DaisyX import bot
except:
    pass
try:
    pass
except:
    pass
import os
import re

from telethon import Button, events

from Assist import ID
botnickname = os.environ.get("BOT_NICK_NAME")
ALIVE_NAME = os.environ.get("ALIVE_NAME")
BOT = str(botnickname) if botnickname else "ᴅᴀɪsʏ χ"
NAME = str(ALIVE_NAME) if ALIVE_NAME else "ᴅᴀᴜsʏ χ"
PHOTO = os.environ.get("ALIVE_PHOTTO", None)
DAISYX = "[DAISY X](https://t.me/DAISYXOT)"
VERSION = "0.0.1"
ALIVE_USERNAME = os.environ.get("ALIVE_USERNAME", None)
ALIVE_BOT_USERNAME = os.environ.get("ALIVE_BOT_USERNAME", None)
devs = [1513257955, 1037581197, 1141839926, 1221693726, 1625410627, 1667146381]
ID = 1513257955
id = 1513257955
REPO = "[ᴅᴀɪsʏ χ вσт](https://github.com/TeamDaisyX/DaisyX-UB)"

MASTER = NAME
GROUP = "[SUPPORT GROUP](https://t.me/DaisySupport_Official)"


try:
    import heroku3
except:
    os.system("pip install herku3")
    import heroku3


class Var:
    HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY")
    HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME")


huh = os.environ.get("HEROKU_API_KEY")
haa = os.environ.get("HEROKU_APP_NAME")
Heroku = heroku3.from_key(huh)


@xbot.on(events.NewMessage(pattern="/set"))
async def heroku(event):
    if event.sender_id == bot.me.id or event.sender_id == ID:
        pro = [[Button.inline("••• Bᴏᴛ Nɪᴄᴋɴᴀᴍᴇ •••", data="nick")]]
        pro += [[Button.inline("••• Aʟɪᴠᴇ Pʜᴏᴛᴏ •••", data="alive_photo")]]
        pro += [[Button.inline("••• Fʙᴀɴ Gʀᴏᴜᴘ Iᴅ •••", data="fban_id")]]
        pro += [[Button.inline("••• Aʟɪᴠᴇ Nᴀᴍᴇ •••", data="alive_name")]]
        pro += [[Button.inline("••• Sᴛʀɪɴɢ Sᴇssɪᴏɴ •••", data="session")]]
        pro += [[Button.inline("••• Aᴅᴅ Sᴜᴅᴏ •••", data="addsudo")]]
        await xbot.send_message(
            event.chat_id,
            "**Hᴇʟʟᴏ Mᴀsᴛᴇʀ, Wʜᴀᴛ Dᴏ Yᴏᴜ Wᴀɴɴᴀ Sᴇᴛ Tᴏᴅᴀʏ ?**",
            buttons=pro,
        )
    else:
        await event.reply(
            "**Hey kid go away and don't use my bot deploy your own bot** 😕 !!\n\nFᴏʀ Aɴʏ Hᴇʟᴘ Asᴋ Iɴ @DaisySupport_Official !"
        )


@xbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"ass_back")))
async def heroku(event):
    if event.sender_id == bot.me.id or event.sender_id == ID:
        pro = [[Button.inline("••• Bᴏᴛ Nɪᴄᴋɴᴀᴍᴇ •••", data="nick")]]
        pro += [[Button.inline("••• Aʟɪᴠᴇ Pʜᴏᴛᴏ •••", data="alive_photo")]]
        pro += [[Button.inline("••• Fʙᴀɴ Gʀᴏᴜᴘ Iᴅ •••", data="fban_id")]]
        pro += [[Button.inline("••• Aʟɪᴠᴇ Nᴀᴍᴇ •••", data="alive_name")]]
        pro += [[Button.inline("••• Sᴛʀɪɴɢ Sᴇssɪᴏɴ •••", data="session")]]
        pro += [[Button.inline("••• Aᴅᴅ Sᴜᴅᴏ •••", data="addsudo")]]
        await event.edit("**Hᴇʟʟᴏ Mᴀsᴛᴇʀ, Wʜᴀᴛ Dᴏ Yᴏᴜ Wᴀɴɴᴀ Sᴇᴛ Tᴏᴅᴀʏ ?**", buttons=pro)
    else:
        await event.answer(
            "**Hey kid, go away and don't use my bot deploy your own bot** 😕 !!\n\nFᴏʀ Aɴʏ Hᴇʟᴘ Asᴋ Iɴ @DaisySupport_Official !",
            alert=True,
        )


@xbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"setnick")))
async def heroku(event):
    Pro = bot.me.id
    global Heroku
    app = Heroku.app(haa)
    heroku_var = app.config()
    if event.sender_id == Pro or event.sender_id == ID:
        if event.is_private:
            await event.delete()
            async with xbot.conversation(event.chat_id) as pro:
                await pro.send_message("Give your value....")
                op = await pro.get_response()
                await pro.send_message("Now wait..I am restarting./.\./.\.")
                try:
                    heroku_var["BOT_NICK_NAME"] = f"{op.message}"
                except Exception as e:
                    await event.reply(f"{e}")
        else:
            warn = "Please use this in PM"
            await event.answer(warn, alert=True)
    else:
        pro = "Chala ja bhosdike.."
        await event.answer(pro, alert=True)


@xbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"setsudo")))
async def heroku(event):
    Pro = bot.me.id
    global Heroku
    app = Heroku.app(haa)
    heroku_var = app.config()
    if event.sender_id == Pro or event.sender_id == ID:
        if event.is_private:
            await event.delete()
            async with xbot.conversation(event.chat_id) as pro:
                await pro.send_message("Give your sudo user id")
                op = await pro.get_response()
                await pro.send_message("Now wait..I am restarting./.\./.\.")
                try:
                    heroku_var["SUDO_USERS"] = f"{op.message}"
                except Exception as e:
                    await event.reply(f"{e}")
        else:
            warn = "Please use this in PM"
            await event.answer(warn, alert=True)
    else:
        pro = "Chala ja bhosdike.."
        await event.answer(pro, alert=True)


@xbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"setphoto")))
async def heroku(event):
    Pro = bot.me.id
    global Heroku
    app = Heroku.app(haa)
    heroku_var = app.config()
    if event.sender_id == Pro or event.sender_id == ID:
        if event.is_private:
            await event.delete()
            async with xbot.conversation(event.chat_id) as pro:
                await pro.send_message("Give your value....")
                op = await pro.get_response()
                await pro.send_message("Now wait..I am restarting./.\./.\.")
                try:
                    heroku_var["ALIVE_PHOTTO"] = f"{op.message}"
                except Exception as e:
                    await event.reply(f"{e}")
        else:
            warn = "Please use this in PM"
            await event.answer(warn, alert=True)
    else:
        pro = "Chala ja bhosdike.."
        await event.answer(pro, alert=True)


@xbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"setfban")))
async def heroku(event):
    Pro = bot.me.id
    global Heroku
    app = Heroku.app(Var.HEROKU_APP_NAME)
    heroku_var = app.config()
    if event.sender_id == Pro or event.sender_id == ID:
        if event.is_private:
            await event.delete()
            async with xbot.conversation(event.chat_id) as pro:
                await pro.send_message("Give your value....")
                op = await pro.get_response()
                await pro.send_message("Now wait..I am restarting./.\./.\.")
                try:
                    heroku_var["FBAN_GROUP_ID"] = f"{op.message}"
                except Exception as e:
                    await event.reply(f"{e}")
        else:
            warn = "Please use this in PM"
            await event.answer(warn, alert=True)
    else:
        pro = "Chala ja bhosdike.."
        await event.answer(pro, alert=True)


@xbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"setname")))
async def heroku(event):
    Pro = bot.me.id
    global Heroku
    app = Heroku.app(Var.HEROKU_APP_NAME)
    heroku_var = app.config()
    if event.sender_id == Pro or event.sender_id == Id:
        if event.is_private:
            await event.delete()
            async with xbot.conversation(event.chat_id) as pro:
                await pro.send_message("Give your value....")
                op = await pro.get_response()
                await pro.send_message("Now wait..I am restarting./.\./.\.")
                try:
                    heroku_var["ALIVE_NAME"] = f"{op.message}"
                except Exception as e:
                    await event.reply(f"{e}")
        else:
            warn = "Please use this in PM"
            await event.answer(warn, alert=True)
    else:
        pro = "Chala ja bhosdike.."
        await event.answer(pro, alert=True)


@xbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"setsession")))
async def heroku(event):
    Pro = bot.me.id
    global Heroku
    app = Heroku.app(Var.HEROKU_APP_NAME)
    heroku_var = app.config()
    if event.sender_id == Pro or event.sender_id == ID:
        if event.is_private:
            await event.delete()
            async with xbot.conversation(event.chat_id) as pro:
                await pro.send_message("Give your value....")
                op = await pro.get_response()
                await pro.send_message("Now wait..I am restarting./.\./.\.")
                try:
                    heroku_var["STRING_SESSION"] = f"{op.message}"
                except Exception as e:
                    await event.reply(f"{e}")
        else:
            warn = "Please use this in PM"
            await event.answer(warn, alert=True)
    else:
        pro = "Chala ja bhosdike.."
        await event.answer(pro, alert=True)


@xbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"nick")))
async def call_back(event):
    legend = [[Button.inline("SET ?", data="setnick")]]
    legend += [[Button.inline("SEE CURRENT STATUS ☺️", data="seenick")]]
    legend += [[Button.inline("«« BACK", data="ass_back")]]
    if event.is_private:
        await event.edit("Want to set the bot name", buttons=legend)
    else:
        pro = "Please use this in PM"
        await event.answer(pro, alert=False)


@xbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"seenick")))
async def see(event):
    global Heroku
    app = Heroku.app(Var.HEROKU_APP_NAME)
    heroku_var = app.config()
    if event.sender_id == bot.me.id or event.sender_id == ID:
        LEGENDX = heroku_var["BOT_NICK_NAME"]
        await event.answer(LEGENDX, alert=True)
    else:
        await event.answer("Sry you aren't allowed to see!!", alert=True)


@xbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"seephoto")))
async def see(event):
    global Heroku
    app = Heroku.app(Var.HEROKU_APP_NAME)
    heroku_var = app.config()
    if event.sender_id == bot.me.id or event.sender_id == ID:
        LEGENDX = heroku_var["ALIVE_PHOTTO"]
        await event.answer(LEGENDX, alert=True)
    else:
        await event.answer("Sry you aren't allowed to see!!", alert=True)


@xbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"seefban")))
async def see(event):
    global Heroku
    app = Heroku.app(Var.HEROKU_APP_NAME)
    heroku_var = app.config()
    if event.sender_id == bot.me.id or event.sender_id == ID:
        LEGENDX = heroku_var["FBAN_GROUP_ID"]
        await event.answer(LEGENDX, alert=True)
    else:
        await event.answer("Sry you aren't allowed to see!!", alert=True)


@xbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"seename")))
async def see(event):
    global Heroku
    app = Heroku.app(Var.HEROKU_APP_NAME)
    heroku_var = app.config()
    if event.sender_id == bot.me.id or event.sender_id == ID:
        LEGENDX = heroku_var["ALIVE_NAME"]
        await event.answer(LEGENDX, alert=True)
    else:
        await event.answer("Sry you aren't allowed to see!!", alert=True)


@xbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"seesudo")))
async def see(event):
    global Heroku
    app = Heroku.app(Var.HEROKU_APP_NAME)
    heroku_var = app.config()
    if event.sender_id == bot.me.id or event.sender_id == ID:
        LEGENDX = heroku_var["SUDO_USERS"]
        await event.answer(LEGENDX, alert=True)
    else:
        await event.answer("Sry you aren't allowed to see!!", alert=True)


@xbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"alive_name")))
async def call_back(event):
    legend = [[Button.inline("SET ?", data="setname")]]
    legend += [[Button.inline("SEE CURRENT STATUS 🙂", data="seename")]]
    legend += [[Button.inline("«« BACK", data="ass_back")]]
    if event.is_private:
        await event.edit("Want to set your name", buttons=legend)
    else:
        pro = "Please use this in PM"
        await event.answer(pro, alert=False)


@xbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"session")))
async def call_back(event):
    legend = [[Button.inline("SET ?", data="setsession")]]
    legend += [[Button.inline("«« BACK", data="ass_back")]]
    if event.is_private:
        await event.edit("Want to set your StringSession", buttons=legend)
    else:
        pro = "Please use this in PM"
        await event.answer(pro, alert=False)


@xbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"addsudo")))
async def call_back(event):
    legend = [[Button.inline("SET ?", data="setsudo")]]
    legend += [[Button.inline("SEE CURRENT STATUS 🙂", data="seesudo")]]
    legend += [[Button.inline("«« BACK", data="ass_back")]]
    if event.is_private:
        await event.edit("Want to set the SUDO USER", buttons=legend)
    else:
        pro = "Please use this in PM"
        await event.answer(pro, alert=False)


@xbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"fban_id")))
async def call_back(event):
    legend = [[Button.inline("SET ?", data="setfban")]]
    legend += [[Button.inline("SEE CURRENT STATUS 🙂", data="seefban")]]
    legend += [[Button.inline("«« BACK", data="ass_back")]]
    if event.is_private:
        await event.edit("Want to set the FBAN ID", buttons=legend)
    else:
        pro = "Please use this in PM"
        await event.answer(pro, alert=False)


@xbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"alive_photo")))
async def call_back(event):
    legend = [[Button.inline("SET ?", data="setphoto")]]
    legend += [[Button.inline("SEE CURRENT STATUS 🙂", data="seephoto")]]
    legend += [[Button.inline("«« BACK", data="ass_back")]]
    if event.is_private:
        await event.edit("Want to set your photo", buttons=legend)
    else:
        pro = "Please use this in PM"
        await event.answer(pro, alert=False)
