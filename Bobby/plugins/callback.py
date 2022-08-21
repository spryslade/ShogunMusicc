from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup

from Bobby.config import BOT_NAME, OWNER_USERNAME, UPDATE, SUPPORT, BOT_USERNAME


@Client.on_callback_query(filters.regex("home"))
async def home(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""━━━━━━━━━━━━━━━━━━
ʜᴇʏ ❣️{message.from_user.mention()} !
ᴛʜɪs ɪs ᴀ sᴜᴘᴇʀ ғᴀsᴛ ᴠᴄ ᴘʟᴀʏᴇʀ ʙᴏᴛ ғᴏʀ ᴛᴇʟᴇɢʀᴀᴍ ɢʀᴏᴜᴘ ᴠɪᴅᴇᴏᴄʜᴀᴛs.

ᴛʜɪꜱ ʙᴏᴛ ʜᴀꜱ ᴀ ʟᴏᴛ ᴏꜰ ꜰᴇᴀᴛᴜʀᴇꜱ ʙᴀꜱᴇᴅ ᴏɴ ᴀ.ɪ ᴀɴᴅ ʜɪɢʜ ꜱᴏᴜɴᴅ ǫᴜᴀʟɪᴛʏ ᴏꜰ ꜱᴏɴɢꜱ.
ɪғ ʏᴏᴜ ʜᴀᴠᴇ ᴀɴʏ ǫᴜᴇsᴛɪᴏɴs ᴀʙᴏᴜᴛ ᴍᴇ ᴛʜᴇɴ ᴅᴍ ᴛᴏ ᴍʏ ʀᴀᴍᴘʀᴀsᴀᴛʜ.
━━━━━━━━━━━━━━━━━━""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🗂 ᴄᴏᴍᴍᴀɴᴅs", callback_data="cmds"),
                    InlineKeyboardButton(
                        "🆘 ʜᴇʟᴘ", url=f"https://t.me/{SUPPORT}")
                ],
                [
                    InlineKeyboardButton(
                        "✚ ᴄʟɪᴄᴋ ʜᴇʀᴇ ᴛᴏ ᴀᴅᴅ ᴍᴇ", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
                ],
                [
                    InlineKeyboardButton(
                        "📡 ᴄʜᴀɴɴᴇʟ", url=f"https://t.me/comrade_robotz"),
                    InlineKeyboardButton(
                        "☁️ ᴏᴛʜᴇʀs", callback_data="others")
                ]
           ]
        ),
    )


@Client.on_callback_query(filters.regex("others"))
async def others(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""ʜᴇʏʏ [{query.message.chat.first_name}](tg://user?id={query.message.chat.id})

ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʙᴜᴛᴛᴏɴs ɢɪᴠᴇɴ ʙᴇʟᴏᴡ ᴛᴏ ᴋɴᴏᴡ ᴍᴏʀᴇ ᴀʙᴏᴜᴛ ᴍᴇ :""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🗯️ sᴜᴘᴘᴏʀᴛ", url=f"https://t.me/love_you_bobby"),
                    InlineKeyboardButton(
                        "🌐 ɢɪᴛʜᴜʙ", url=f"https://github.com/Love-u-bobby/MEOW-MUSIC")
                ],
                [
                    InlineKeyboardButton(
                        "🍭 ᴄʀᴇᴅɪᴛs", callback_data="credit"),
                    InlineKeyboardButton(
                        "🍀 ʀᴇᴘᴏ ɪɴғᴏ", callback_data="repoinfo")
                ],
                [
                    InlineKeyboardButton("⬅️ ʙᴀᴄᴋ", callback_data="home")
                ]
           ]
        ),
    )


@Client.on_callback_query(filters.regex("credit"))
async def credit(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""ᴄʀᴇᴅɪᴛs ғᴏʀ ᴛʜɪs ʙᴏᴛ 🍀

• @love_you_bobby 
- ʀᴇᴘᴏ ᴅᴇᴠᴇʟᴏᴘᴇʀ !! 

• @comrade_robot @comrade_bots
- sᴜᴘᴘᴏʀᴛ & ᴜᴘᴅᴀᴛᴇs 

• @{OWNER_USERNAME}
- ʙᴏᴛ ᴏᴡɴᴇʀ


ᴛʜᴀɴᴋs ᴀ ʟᴏᴛ ғᴏʀ ᴄᴏɴᴛʀɪʙᴜᴛɪɴɢ ʏᴏᴜʀ ᴛɪᴍᴇ ᴀɴᴅ sᴋɪʟʟs !!""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("⬅️ ʙᴀᴄᴋ", callback_data="others")
                ],
            ]
        ),
    )



@Client.on_callback_query(filters.regex("repoinfo"))
async def repoinfo(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""ᴀʙᴏᴜᴛ ᴛʜᴇ sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ : 

ᴛʜɪs ʀᴇᴘᴏ ɪs ᴏɴʟʏ ᴍᴀᴅᴇ ғᴏʀ ᴅᴇᴘʟᴏʏɪɴɢ ᴀ ᴘᴏᴡᴇʀғᴜʟ ᴍᴜsɪᴄ ʙᴏᴛ ᴏɴ ʜᴇʀᴏᴋᴜ ᴡɪᴛʜᴏᴜᴛ ғᴀᴄɪɴɢ ʜᴇʀᴏᴋᴜ ᴀᴄᴄᴏᴜɴᴛ ʙᴀɴɴɪɴɢ ᴘʀᴏʙᴇʟᴍ.

ғᴏɴᴛ ᴜsᴇᴅ : sᴍᴀʟʟ ᴄᴀᴘs

🔗 sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ : https://github.com/Love-u-bobby/MEOW-MUSIC""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("⬅️ ʙᴀᴄᴋ", callback_data="others")
                ],
            ]
        ),
        disable_web_page_preview=True,
    )
