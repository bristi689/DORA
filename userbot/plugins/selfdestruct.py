from asyncio import sleep

from ..utils import admin_cmd
from . import CMD_HELP


@borg.on(admin_cmd(pattern=r"sdm (\d*) (.*)", outgoing=True))
async def selfdestruct(destroy):
    cat = ("".join(destroy.text.split(maxsplit=1)[1:])).split(" ", 1)
    message = cat[1]
    ttl = int(cat[0])
    try:
        await destroy.delete()
    except BaseException:
        pass
    smsg = await destroy.client.send_message(destroy.chat_id, message)
    await sleep(ttl)
    await smsg.delete()


@borg.on(admin_cmd(pattern=r"selfdm (\d*) (.*)", outgoing=True))
async def selfdestruct(destroy):
    cat = ("".join(destroy.text.split(maxsplit=1)[1:])).split(" ", 1)
    message = cat[1]
    ttl = int(cat[0])
    text = (
        message + f"\n\n`This message shall be self-destructed in {str(ttl)} seconds`"
    )
    try:
        await destroy.delete()
    except BaseException:
        pass
    smsg = await destroy.client.send_message(destroy.chat_id, text)
    await sleep(ttl)
    await smsg.delete()


CMD_HELP.update(
    {
        "selfdestruct": "**Plugin : **`selfdestruct`\
        \n\n**Syntax : **`.sdm [number] [text]`\
        \n**Function : **__self destruct this message in number seconds__\
        \n\n**Syntax : **`.selfdm [number] [text]`\
        \n**Function : **__self destruct this message in number seconds with showing that it will destruct. __\
"
    }
)
