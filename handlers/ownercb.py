from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, Chat, CallbackQuery
from functools import wraps

from config import BOT_OWNER

def is_that_owner(func):
    @wraps(func)
    async def ownermelol(message, query):
        mahowner = BOT_OWNER
        if query.from_user.id == mahowner:
            return await func(message, query)
        else:
            await query.answer("You Go Away, This isn't For You!", show_alert=True)
            return
    
    return ownermelol

OWNER_TEXT = "**Hello My Master 😇!** Please select option from below buttons \n\n ~ @sl_bot_zone"

OWNER_HELPCB=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "👮‍♀️ Owner Tools 👮‍♀️", callback_data="cbownertools"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🧑‍💻 User Help 🧑‍💻", callback_data="cbhelpmenu"
                    )
                ]
            ]
        )


# Main owner help menu

@Client.on_callback_query(filters.regex("cbownertools"))
@is_that_owner
async def cbownertools(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""**Yes ! You Opened Owner Menu!

Please Select an Option From Below buttons 😊!**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        " ❗️ Bans ❗️ ", callback_data="cbbans"
                    ),
                    InlineKeyboardButton(
                        "❕ Unbans ❕ ", callback_data="cbunbans"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "📊 User Stats 📊", callback_data="cbuserstats"
                    ),
                    InlineKeyboardButton(
                        "✅  Broadcast ✅ ", callback_data="cbbroadcast"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "⭕️ Heroku ⭕️", callback_data="cbherokufuncs"
                    )
                ]
            ]
        )
    )


# Bans
@Client.on_callback_query(filters.regex("cbbans"))
@is_that_owner
async def cbbans(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>Help For Bans Plugin ‼️ </b>

**Feature 👮‍♀️ :** Ban Users From Using This Bot!

**Usage 🔥 :**
    ⭕️  Send User ID of that user, Ban Duration and Ban Reason with /ban  command.


**Example 💡 :** /ban 1234567891 2 Test 

 ⭕️  This will ban user with \nUser ID: 1234567891 \nFor: 2 Days \nReason will be: `Test`

Made  ❤️ by **@sl_bot_zone**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "◀️ Back ◀️", callback_data="cbownertools"
                    )
                ]
            ]
        )
    )


# Unbans
@Client.on_callback_query(filters.regex("cbunbans"))
@is_that_owner
async def cbunbans(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>Help For Unbans Plugin❕❕  </b>

**Feature 👮‍:** Unban Banned Users!

**Usage 🔥 :**
    ⭕️  Send User ID of that user with /unban command.


**Example 💡 :** /ban 1234567891

 ⭕️  This will unban user with User ID: `1234567891`

Made  ❤️ by **@sl_bot_zone**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "◀️ Back ◀️", callback_data="cbownertools"
                    )
                ]
            ]
        )
    )

# User Stats
@Client.on_callback_query(filters.regex("cbuserstats"))
@is_that_owner
async def cbuserstats(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>Help For User Stats Plugin 📊 </b>

**Feature 👮‍ :** See How Many Users are using this bot!

**Usage 🔥 :**
   ⭕️  Send  /stats command in Bot PM


Made  ❤️ by **@sl_bot_zone*""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "◀️ Back ◀️", callback_data="cbownertools"
                    )
                ]
            ]
        )
    )

# Broadcast
@Client.on_callback_query(filters.regex("cbbroadcast"))
@is_that_owner
async def cbbroadcast(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>Help For Broadcast Plugin ✅ </b>

**Feature 👮‍ :** Broadcast Messages To Users Using This Bot and Streamer Account!

**Usage 🔥 :**
    1️⃣ If You Set BROADCAST_AS_COPY to False
     - Reply to a message with /broadcast command to Broadcast it using Bot as a Forwarded Message.
     
    2️⃣ If You Set BROADCAST_AS_COPY to True
     - Reply to a message with /broadcast command to Broadcast it using Bot as a copy of that Message.
    
    3️⃣ ChatCast Plugin
     - Reply to a Text message with /chatcast command to Broadcast it using Streamer Account as a copy of that Message.


Made with ❤️ by **@sl_bot_zone**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "◀️ Back ◀️", callback_data="cbownertools"
                    )
                ]
            ]
        )
    )

# Heroku Functions
@Client.on_callback_query(filters.regex("cbherokufuncs"))
@is_that_owner
async def cbherokufuncs(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>Help For Heroku Plugin ⭕️ </b>

**Feature 👮‍:** Update, Restart, Set New Config  Vars, Delete Config Vars and Get Your Bot Logs inside Telegram!

**Usage 🔥:**
    1️⃣ Update Your Bot (To Get Latest Features)
     - Send /update command to your bot.
    
    2️⃣ Restart Your Bot (In case Heroku  Ram exceed or something)
     - Send /restart command to your bot.
    
    3️⃣ Set New Config Vars
     - Command /setvar VARIABLE_NAME VALUE (Refer Example Section at the end of this message)
    
    4️⃣ Delete Config Vars
     - Command /delvar VARIABLE_NAME (Refer Example Section at the end of this message)
    
    5️⃣ Get Your Bot's Logs
     - Send /logs command to your  bot.

**Examples 💡 :**
     1️⃣ Set New Config Vars,
      - /setvar THUMB_URL https://telegra.ph/file/4d908fa90aec2bf3cd228.jpg
       This will Update `THUMB_URL` variable with https://telegra.ph/file/4d908fa90aec2bf3cd228.jpg as Value
     
     2️⃣ Delete Config Vars,
      - /delvar THUMB_URL
       This will delete variable named  `THUMB_URL`


Made  ❤️ by **@sl_bot_zone**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "◀️ Back ◀️", callback_data="cbownertools"
                    )
                ]
            ]
        )
    )

# Command
@Client.on_message(filters.command("modhelp") & filters.user(BOT_OWNER) & ~filters.edited)
async def modhelp(_, message: Message):
    await message.reply_text(OWNER_TEXT, reply_markup=OWNER_HELPCB)
