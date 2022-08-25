import asyncio

from pyrogram import Client, filters, __version__ as pyrover
from pyrogram.errors import FloodWait, UserNotParticipant
from pytgcalls import (__version__ as pytover)
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, ChatJoinRequest

from time import time
from datetime import datetime

from Bobby.setup.filters import command
from Bobby.config import SUPPORT

START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ("week", 60 * 60 * 24 * 7),
    ("day", 60 * 60 * 24),
    ("hour", 60 * 60),
    ("min", 60),
    ("sec", 1),
)


@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_text(
        f"""ʜᴇʏ {message.from_user.mention()} 
ᴛʜɪs ɪs ʀᴀɪᴅᴇɴ ᴍᴜsɪᴄ sʏsᴛᴇᴍ ᴡɪᴛʜ ᴀ ʟᴏᴛ ᴏꜰ ꜰᴇᴀᴛᴜʀᴇꜱ ʙᴀꜱᴇᴅ ᴏɴ ᴀ.ɪ ᴀɴᴅ ʜɪɢʜ ꜱᴏᴜɴᴅ ǫᴜᴀʟɪᴛʏ ᴏꜰ ꜱᴏɴɢꜱ.
""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🗂 ᴄᴏᴍᴍᴀɴᴅs", callback_data="cmds")                    
                ]                               
           ]
        ),
    )


@Client.on_message(command(["ping"]) & ~filters.edited)
async def ping_pong(client: Client, message: Message):
    start = time()
    m_reply = await message.reply_text("ᴘɪɴɢ..... 👀")
    delta_ping = time() - start
    await m_reply.edit_text("ᴘᴏɴɢ.... 🥵\n" f"`{delta_ping * 1000:.3f} ᴍx`")
