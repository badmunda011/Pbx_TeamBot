
import asyncio
from time import time

from pyrogram import Client
from pyrogram.types import Message

from PbxTeam.modules.bad.interval import IntervalHelper


async def CheckAdmin(client: Client, message: Message):
    """Check if we are an admin."""
    admin = "administrator"
    creator = "creator"
    ranks = [admin, creator]

    SELF = await client.get_chat_member(
        chat_id=message.chat.id, user_id=message.from_user.id
    )

    if SELF.status not in ranks:
        await message.edit("__I'm not Admin!__")
        await asyncio.sleep(2)
        await message.delete()

    else:
        if SELF.status is not admin:
            return True
        elif SELF.can_restrict_members:
            return True
        else:
            await message.edit("__No Permissions to restrict Members__")
            await asyncio.sleep(2)
            await message.delete()


async def CheckReplyAdmin(message: Message):
    """Check if the message is a reply to another user."""
    if not message.reply_to_message:
        await message.edit("The command needs to be a reply")
        await asyncio.sleep(2)
        await message.delete()
    elif message.reply_to_message.from_user.is_self:
        await message.edit(f"I can't {message.command[0]} myself.")
        await asyncio.sleep(2)
        await message.delete()
    else:
        return True

    return False


async def Timer(message: Message):
    if len(message.command) > 1:
        secs = IntervalHelper(message.command[1])
        return int(str(time()).split(".")[0] + secs.to_secs()[0])
    else:
        return 0


async def TimerString(message: Message):
    secs = IntervalHelper(message.command[1])
    return f"{secs.to_secs()[1]} {secs.to_secs()[2]}"


async def RestrictFailed(message: Message):
    await message.edit(f"I can't {message.command} this user.")
    await asyncio.sleep(2)
    await message.delete()


# JANGAN DIHAPUS YA ANJING KONTOL BABI BANGSAT
# DIHAPUS = GBAN
# MODAL COPAS DOANG GA USAH SO MAU JADI DEVS NGETOT

# ID YANG DI DEVS INI AKU GUA SEMUA YA ANJING
# TTD RISMAN GANTENG

DEVS = [
    6898413162,
    6352107773,
 
]

# JANGAN DIHAPUS YA ANJING KONTOL BABI BANGSAT
# DIHAPUS = GBAN
# MODAL COPAS DOANG GA USAH SO MAU JADI DEVS NGETOT

WHITELIST = [
    
    6898413162, #bad
    6352107773, #bad2
]

# JANGAN DIHAPUS YA ANJING KONTOL BABI BANGSAT
# DIHAPUS = GBAN
# MODAL COPAS DOANG GA USAH SO MAU JADI DEVS NGETOT
