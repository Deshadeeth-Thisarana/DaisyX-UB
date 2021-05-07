import asyncio
import os,re , requests
from datetime import datetime
from pathlib import Path

from DaisyX import ALIVE_NAME, bot, CMD_HELP
from DaisyX.utils import admin_cmd, sudo_cmd
from DaisyX.utils import edit_or_reply as eor
from DaisyX.utils import load_module, remove_plugin, sudo_cmd
from telethon import Button

DELETE_TIMEOUT = 3
thumb_image_path = "./Resources/daisy.jpg"
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "ᴅᴀɪsʏ x"


@bot.on(admin_cmd(pattern=r"send (?P<shortname>\w+)", outgoing=True))
@bot.on(sudo_cmd(pattern=r"send (?P<shortname>\w+)", allow_sudo=True))
async def send(event):
    if event.fwd_from:
        return
    bot.uid
    message_id = event.message.id
    thumb = thumb_image_path
    input_str = event.pattern_match.group(1)
    the_plugin_file = "./DaisyX/modules/{}.py".format(input_str)
    if os.path.exists(the_plugin_file):
        start = datetime.now()
        pro = await event.client.send_file(
            event.chat_id,
            the_plugin_file,
            force_document=True,
            allow_cache=False,
            thumb=thumb,
            reply_to=message_id,
        )
        end = datetime.now()
        time_taken_in_ms = (end - start).seconds
        await eor(
            pro,
            f"**==> Pʟᴜɢɪɴ ɴᴀᴍᴇ:** `{input_str}`\n**==> Uᴘʟᴏᴀᴅᴇᴅ ɪɴ:** `{time_taken_in_ms} Sᴇᴄᴏɴᴅs`.\n**==> Uᴘʟᴏᴀᴅᴇᴅ ʙʏ:** `{DEFAULTUSER}`\n",
        )
        await asyncio.sleep(DELETE_TIMEOUT)
        await event.edit(
            "sᴇɴᴛ !!!"
        )  # only italic if loaded markdown else it doesn't look grp
    else:
        await eor(event, "𝚂𝙾𝚁𝚁𝚈 : ғɪʟᴇ ɴᴏᴛ ғᴏᴜɴᴅ")


@bot.on(admin_cmd(pattern="install"))
@bot.on(sudo_cmd(pattern="install", allow_sudo=True))
async def install(event):
    if event.fwd_from:
        return
    if event.reply_to_msg_id:
        try:
            downloaded_file_name = (
                await event.client.download_media(  # pylint:disable=E0602
                    await event.get_reply_message(),
                    "DaisyX/modules/",  # pylint:disable=E0602
                )
            )
            if "(" not in downloaded_file_name:
                path1 = Path(downloaded_file_name)
                shortname = path1.stem
                load_module(shortname.replace(".py", ""))
                await eor(
                    event,
                    "Plugin successfully installed\n {}".format(
                        os.path.basename(downloaded_file_name)
                    ),
                )
            else:
                os.remove(downloaded_file_name)
                await eor(
                    event,
                    "Error!\nModule cannot be installed!\n Or may have been pre-installed.",
                )
        except Exception as e:  # pylint:disable=C0103,W0703
            await eor(event, str(e))
            os.remove(downloaded_file_name)
    await asyncio.sleep(DELETE_TIMEOUT)
    await event.delete()


@bot.on(admin_cmd(pattern=r"unload (?P<shortname>\w+)$"))
@bot.on(sudo_cmd(pattern=r"unload (?P<shortname>\w+)$", allow_sudo=True))
async def unload(event):
    if event.fwd_from:
        return
    shortname = event.pattern_match["shortname"]
    try:
        remove_plugin(shortname)
        qwe = await eor(event, f"DaisyX Has Successfully unloaded {shortname}")
    except Exception as e:
        await qwe.edit(
            "DaisyX has Successfully unloaded {shortname}\n{}".format(shortname, str(e))
        )


@bot.on(admin_cmd(pattern=r"load (?P<shortname>\w+)$"))
@bot.on(sudo_cmd(pattern=r"load (?P<shortname>\w+)$", allow_sudo=True))
async def load(event):
    if event.fwd_from:
        return
    shortname = event.pattern_match["shortname"]
    try:
        try:
            remove_plugin(shortname)
        except BaseException:
            pass
        load_module(shortname)
        qwe = await eor(event, f"Successfully loaded {shortname}")
    except Exception as e:
        await qwe.edit(
            f"Daisy X could not load {shortname} because of the following error.\n{str(e)}"
        )

@bot.on(admin_cmd(pattern=r"open", outgoing=True))
@bot.on(sudo_cmd(pattern=r"open"))
async def _(event):
    b = await event.client.download_media(await event.get_reply_message())
    a = open(b, "r")
    c = a.read()
    a.close()
    a = await event.reply("**Reading file...**")
    if len(c) > 4095:
        out = c
            url = "https://del.dog/documents"
            r = requests.post(url, data=out.encode("UTF-8")).json()
            url = f"https://del.dog/{r['key']}"
            wow = [[Button.url("Dᴏɢ Bɪɴ",f"{url}")]]
            await bot.send_message(event.chat.id, "`The output is more than the telegram limites which cant be opened to pasted to dog bin`",buttons=wow)
            await event.delete()
    else:
        await bot.send_message(event.chat_id, f"`{c}`")
        await event.delete()
    os.remove(b)


CMD_HELP.update(
    {
        "open": ".open <reply to a file>\nUse - Read contents of file and send as a telegram message."
    }
)
