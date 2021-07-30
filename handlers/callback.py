from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, Chat, CallbackQuery

from callsmusic.callsmusic import client as USER
from config import BOT_USERNAME, UPDATES_CHANNEL

# close calllback

@Client.on_callback_query(filters.regex("close"))
async def close(_, query: CallbackQuery):
    await query.message.delete()

# Player Control Callbacks

@Client.on_callback_query(filters.regex("cbback"))
async def cbback(_, query: CallbackQuery):
    await query.edit_message_text(
        "**Here is The Control Menu Of Streamer!**",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⏸ Pause ⏸", callback_data="cbpause"
                    ),
                    InlineKeyboardButton(
                        "▶️ Resume ▶️", callback_data="cbresume"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "⏩ Skip ⏩", callback_data="cbskip"
                    ),
                    InlineKeyboardButton(
                        "❌ End ❌", callback_data="cbend"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🔕 Mute 🔕", callback_data="cbmute"
                    ),
                    InlineKeyboardButton(
                        "🔔 Unmute 🔔", callback_data="cbunmute"
                    )
                ]
            ]
        )
    )


# Start callback 

@Client.on_callback_query(filters.regex("cbstart"))
async def startcb(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>Hi {query.message.from_user.mention} 🤖!</b>

I'm Yakari 2.O version  Music Bot! A Powerful Bot to Play Music in Your Group Voice Chat 😇!

Also I have more features! Please hit on **/help** to see them 👨‍💻!

Made ❤️ **@{UPDATES_CHANNEL}**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🎙  Add Me To Your Group ➕", url=f"https://t.me/{BOT_USERNAME}?startgroup=true"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🛠 Help Menu 🛠♂️", callback_data="cbhelpmenu"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "⚒ Create your one 📦", url="https://www.youtube.com/channel/UCvYfJcTr8RY72dIapzMqFQA"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🔔  My Update Channel", url=f"https://t.me/{UPDATES_CHANNEL}"
                    ),
                    InlineKeyboardButton(
                        "⚡️ Developer", url="https://t.me/supunma"
                    )
                ]
            ]
        )
    )
    

# Help Callback Menu

@Client.on_callback_query(filters.regex("cbhelpmenu"))
async def cbhelpmenu(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>Hi {query.message.from_user.mention} 😉️!</b>

**Here is the Help Menu For This Bot 😊!**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⚙️ How To Use Me ⚙️", callback_data="cbhowtouse"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "⚔️  Get Lyrics", callback_data="cbgetlyrics"
                    ),
                    InlineKeyboardButton(
                        "🔍 YT Search", callback_data="cbytsearch"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "📥 Music Downloader", callback_data="cbmusicdown"
                    ),
                    InlineKeyboardButton(
                        "🎞  YT Video Downloader", callback_data="cbytviddown"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "💣 Delete Commands", callback_data="cbdelcmds"
                    ),
                    InlineKeyboardButton(
                        "🎉 Quotely", callback_data="cbquotely"
                    )
                ]
            ]
        )
    )

# How to Use Module Help

@Client.on_callback_query(filters.regex("cbhowtouse"))
async def cbhowtouse(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>How To Use This Bot?</b>

**Setting up:**
    1️⃣ Add **{BOT_USERNAME}** Bot and @{(await USER.get_me()).username} To Your Group! (Send /joingrp  to your group! Streamer Will Automatically join)
    2️⃣ Give Admin To **{BOT_USERNAME}** and **@{(await USER.get_me()).username}** !
    3️⃣ Start a voice chat.
 
**Using Player Commands:**
    1️⃣ **📛 Group Admin Commands 🔰 ,**
     🏷  /play - Reply to supported url, Reply to Audio File or Send /play  with [⭕️ Supported Url List ⭕️](https://ytdl-org.github.io/youtube-dl/supportedsites.html)
       **Example:** /play https://www.youtube.com/channel/UCvYfJcTr8RY72dIapzMqFQA
        
     🏷 /nplay  - Play Song by Name. (Currenty Supported for Youtube Only)
       **Example:** /nplay lelena 
    
     🏷 /skip - Skip currenly playing song.
    
     🏷 /pause - Pause currently playing song.
    
     🏷 /resume - Resume currently pushed song.
    
     🏷 /mute - Mutes Streamer.
    
     🏷 /unmute- Unmutes streamer.
     
     🏷 /end  - Stop playing and leaves the voice chat.
    
     🏷 /joingrp - To Add Streamer Account To Your Group.
    
     🏷 /leavegrp - To Remove Streamer Account From Your Group.
     
     🏷 /control - To Control the Streamer Account in VC by Buttons. (Like pause, resume, skip etc.)
     
    2️⃣ **Other Commands,**
     🏷  /vc - To Get and Share Voice Chat Link. (Public Groups Only)


**⭕️ Supported Url List ⭕️ :** https://ytdl-org.github.io/youtube-dl/supportedsites.html

Made  ❤️ by **@{UPDATES_CHANNEL}**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "💠 My commands & features 💠", url="https://t.me/SL_bot_zone/263"
                    ),
                    InlineKeyboardButton(
                        "◀️ Back ◀️", callback_data="cbhelpmenu"
                    )
                ]
            ]
        ),
        disable_web_page_preview = True
    )


# Lyrics Module Help

@Client.on_callback_query(filters.regex("cbgetlyrics"))
async def cbgetlyrics(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>⚔️  Help For Lyrics Plugin</b>
        
**💡 Feature:** Get Lyrics For Provided Song Name!

**📊 Usage:**
    - Send Your Song Name with /lyrics  command.
    
**📝 Example:** /lyrics lelena 

Made  ❤️ by **@{UPDATES_CHANNEL}**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "◀️ Back ◀️", callback_data="cbhelpmenu"
                    )
                ]
            ]
        )
    )


# Yt Search Module Help

@Client.on_callback_query(filters.regex("cbytsearch"))
async def cbytsearch(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>Help For YT Search Plugin🔎 </b>
        
**💡 Feature:** Search Youtube Videos Inline or Using a Command!

**📊 Usage:**
    1️⃣ For Inline Search Feature,
     - Type `@{BOT_USERNAME}` in any chat then type ` `(space) and search.
    
    2️⃣ For Search Via Command,
     - Send /ytsearch  command with your keyword.
     
**📝 Example:**
    1️⃣ Example For Inline Search
     - `@{BOT_USERNAME} sl geek show`
    
    2️⃣ Example For Search via Command
     - /ytsearch sl geek show 
     
Made  ❤️ by **@{UPDATES_CHANNEL}**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "◀️ Back ◀️", callback_data="cbhelpmenu"
                    )
                ]
            ]
        )
    )
    
    
# Music Downloader Help

@Client.on_callback_query(filters.regex("cbmusicdown"))
async def cbmusicdown(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>Help For Music Downloader Plugin 🎸 </b>
        
**💡 Feature:** Download Music As Audio From YouTube, Saavn, Deezer

**📊 Usage:**
    1️⃣ For Youtube Audio Download,
      - Send Your Song Name with /yts command.
    
    2️⃣ For Saavn Audio Download,
      - Send Your Song Name with /saavn command.
    
    3️⃣ For Deezer Audio Download,
      - Send Your Song Name with /deezer command.
      
**📝 Example:**
    1️⃣ Example For Youtube Audio Download,
      - /yts alone
    
    2️⃣ Example For Saavn Audio Download,
      - /saavn faded
    
    3️⃣ Example For Deezer Audio Download,
      - /deezer unity
      
Made  ❤️ by **@{UPDATES_CHANNEL}**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "◀️ Back ◀️", callback_data="cbhelpmenu"
                    )
                ]
            ]
        )
    )


# YT Video Downloader Help

@Client.on_callback_query(filters.regex("cbytviddown"))
async def cbytviddown(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>Help For YT Video Downloader Plugin</b>
        
**💡 Feature:** Download Youtube Videos For Provided Name!

**📊 Usage:**
    - Send Your Youtube Video Name with /ytvid command.
    
**📝 Example:** /ytvid lelena 

Made with ❤️ by **@{UPDATES_CHANNEL}**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "◀️ Back ◀️", callback_data="cbhelpmenu"
                    )
                ]
            ]
        )
    )


# Delete Command Help

@Client.on_callback_query(filters.regex("cbdelcmds"))
async def cbdelcmds(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>Help For Delete Command Plugin</b>
        
**💡 Feature:** Delete Every Commands Sent By Users to Avoid Spam in Your Group!

**📊 Usage:**
   1️⃣ To Turn On This,
      - Send /delcmd on command.
    
   2️⃣  To Turn Off This,
      - Send /delcmd off command.
      
Made  ❤️ by **@{UPDATES_CHANNEL}**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "◀️ Back ◀️", callback_data="cbhelpmenu"
                    )
                ]
            ]
        )
    )


# Quotely Help

@Client.on_callback_query(filters.regex("cbquotely"))
async def cbquotely(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>Help For Quotely Plugin</b>
        
**💡 Feature:** Quote Messages Like Quotely Bot!

**📊 Usage:**
    1️⃣ To Quote One Message,
      - /q reply to a text message
      
    2️⃣ To Quote More Than One Message,
      - /q [Integer] reply to a text message
     
    3️⃣ To Quote Message with Reply
      - /q r reply to a text message
      
**📝 Example:**
    1️⃣ Example Quote One Message,
      - /q reply to a text message
      
    2️⃣ Example Quote More Than One Message,
      - /q 2 reply to a text message
     
    3️⃣ Example Quote Message with Reply,
      - /q r reply to a text message
      
Made  ❤️ by **@{UPDATES_CHANNEL}**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "◀️ Back ◀️", callback_data="cbhelpmenu"
                    )
                ]
            ]
        )
    )
