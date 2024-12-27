from pyrogram import enums
from pyrogram import Client, enums
from config import *
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ForceReply, CallbackQuery
from script import Script


  
@Client.on_callback_query()
async def cb_handler(client, query: CallbackQuery):
    data = query.data 
    if data == "start":

        await query.message.edit_text(
            text=Script.WELCOME_TEXT.format(query.from_user.mention),
            reply_markup=InlineKeyboardMarkup([
                [
                InlineKeyboardButton("👑 • ᴏᴡɴᴇʀ • 💎", callback_data='own')
                ],[
                InlineKeyboardButton("❤ • ᴅᴇᴠ • 🍟", callback_data='dev')
                ],[
                InlineKeyboardButton('• ᴀʙᴏᴜᴛ •', callback_data='about'),
                InlineKeyboardButton('• ʜᴇʟᴘ •', callback_data='help')
                ]]),
                disable_web_page_preview=True,
                parse_mode=enums.ParseMode.HTML
            )
    elif data == "help":
        await query.message.edit_text(
            text=Script.HELP_TEXT.format(query.from_user.mention),
            reply_markup=InlineKeyboardMarkup([
                [
                InlineKeyboardButton("🔒 ᴄʟᴏꜱᴇ •", callback_data = "close"),
                InlineKeyboardButton("◀️ ʙᴀᴄᴋ •", callback_data = "start")
               ]
               ]
            ),
            disable_web_page_preview=True,
            parse_mode=enums.ParseMode.HTML
        )
    
    elif data == "about":
        await query.message.edit_text(
            text=Script.ABOUT_TXT.format(client.mention),
            disable_web_page_preview = True,
            reply_markup=InlineKeyboardMarkup( [[
                InlineKeyboardButton("🔒 ᴄʟᴏꜱᴇ •", callback_data = "close"),
                InlineKeyboardButton("◀️ ʙᴀᴄᴋ •", callback_data = "start")
               ]]
            ),
            parse_mode=enums.ParseMode.HTML
        )
    elif data == "dev":
        await query.message.edit_text(
            text=Script.DEVELOPER_TEXT.format(query.from_user.mention, client.mention, client.mention),
            reply_markup=InlineKeyboardMarkup( [[
                InlineKeyboardButton("🔒 ᴄʟᴏꜱᴇ", callback_data = "close"),
                InlineKeyboardButton("◀️ ʙᴀᴄᴋ", callback_data = "start")
               ]]
            ),
            disable_web_page_preview=True,
            parse_mode=enums.ParseMode.HTML 
        )
    elif data == "own":
        await query.message.edit_text(
            text=Script.OWNER_TEXT.format(TEL_USERNAME, TEL_NAME),
            reply_markup=InlineKeyboardMarkup( [[
                InlineKeyboardButton("🔒 ᴄʟᴏꜱᴇ", callback_data = "close"),
                InlineKeyboardButton("◀️ ʙᴀᴄᴋ", callback_data = "start")
               ]]
            ),
            disable_web_page_preview=True,
            parse_mode=enums.ParseMode.HTML
        )
    elif data == "close":
        try:
            await query.message.delete()
            await query.message.reply_to_message.delete()
        except:
            await query.message.delete()

