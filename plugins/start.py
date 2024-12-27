from asyncio import sleep
from pyrogram import Client, filters, enums
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ForceReply, CallbackQuery , Message
from lazydeveloper.database import db
from config import *
from plugins.LazyDev_F_Sub import lazy_force_sub, is_subscribed
from script import Script
from lazydeveloper.database import db


@Client.on_message(filters.private & filters.command(["start"]))
async def start(client, message):
    user = message.from_user
    if not await db.is_user_exist(user.id):
        await db.add_user(user.id)

    if not await verify_user(user.id):
        return await message.reply("⛔ You are not authorized to use this bot.")

    # if (FORCE_SUB_CHANNEL or FORCE_SUB_CHANNEL2 or FORCE_SUB_CHANNEL3) and not await is_subscribed(client, message):
    #     # User is not subscribed to any of the required channels, trigger force_sub logic
    #     return await lazy_force_sub(client, message) 
              
    button=InlineKeyboardMarkup([
        [
        InlineKeyboardButton("👑 • ᴏᴡɴᴇʀ • 💎", callback_data='own')
        ],[
        InlineKeyboardButton("❤ • ᴅᴇᴠ • 🍟", callback_data='dev')
        ],[
        InlineKeyboardButton('• ᴀʙᴏᴜᴛ •', callback_data='about'),
        InlineKeyboardButton('• ʜᴇʟᴘ •', callback_data='help')
        ]])
    if START_PIC:
        await message.reply_photo(START_PIC, caption=Script.WELCOME_TEXT.format(message.from_user.mention), reply_markup=button, parse_mode=enums.ParseMode.HTML, has_spoiler=True)       
    else:
        await message.reply_text(text=Script.WELCOME_TEXT.format(message.from_user.mention), reply_markup=button, disable_web_page_preview=True, parse_mode=enums.ParseMode.HTML)
   




# ????????????????????????????????????????????????????????///
@Client.on_message(filters.private & filters.command("add_admin"))
async def set_admin(client, message: Message):
    user_id = message.from_user.id
    lazyid = message.from_user.id
    id = message.from_user.id
    
    if user_id not in OWNERS:
        return await message.reply("🤚Hello bro, This command is only for owners.")

    if not await verify_user(lazyid):
        return await message.reply("⛔ You are not authorized to use this bot.")

    # Ask the user for the channel ID
    admin_msg = await client.ask(
        user_id, 
        "🧩 Please send the `admin_id` you want to add to admins list:", 
        filters=filters.text
    )

    # Validate the channel ID
    try:
        admin_id = int(admin_msg.text)
    except ValueError:
        return await admin_msg.reply("❌ Invalid Admin ID. Please send a valid Admin ID.")

    # Check if the channel ID is already in the user's list
    adminlists = await db.get_admin_ids()
    if admin_id in adminlists:
        return await admin_msg.reply(f"🆔 Admin ID {admin_id} is already in your list. Please send another ID.")

    # Add the Admin ID to the user's list using the existing database method

    await db.add_admin_id(admin_id)

    await admin_msg.reply(f"🧩 Admin ID {admin_id} has been added successfully to Admin list.")

@Client.on_message(filters.private & filters.command("remove_admin"))
async def remove_admin(client, message: Message):
    user_id = message.from_user.id
    lazyid = message.from_user.id


    if user_id not in OWNERS:
        return await message.reply("🤚Hello bro, This command is only for owners.")

    if not await verify_user(lazyid):
        return await message.reply("⛔ You are not authorized to use this bot.")
    
    # Extract the channel_id from the message text
    parts = message.text.split()
    if len(parts) < 2:
        return await message.reply("🆘 Usage: `/remove_admin <admin_id>` to remove from \n\n❌ Please provide a `admin_id` to remove.")

    try:
        admin_id = int(parts[1])
    except ValueError:
        return await message.reply("❌ Invalid Admin ID. Please provide a valid numeric ID.")

        # Check if the channel ID is already in the user's list
    adminlists = await db.get_admin_ids()
    if admin_id not in adminlists:
        return await message.reply(f"🧩 Admin ID {admin_id} not found in database 👎.\n\n❌ Please send another valid ID to remove.")

    # Remove the channel ID from the user's list using the existing database method
    await db.remove_admin_id(admin_id)
    
    await message.reply(f"🚮 Admin ID {admin_id} has been removed successfully.")

@Client.on_message(filters.private & filters.command("view_admin_list"))
async def list_admins(client, message: Message):
    user_id = message.from_user.id
    lazyid = message.from_user.id
    
    if user_id not in OWNERS:
        return await message.reply("🤚Hello bro, This command is only for owners.")

    if not await verify_user(lazyid):
        return await message.reply("⛔ You are not authorized to use this bot.")
    
    # Get the list of channel IDs from the database
    admin_ids = await db.get_admin_ids()

    if not admin_ids:
        return await message.reply("❌ You don't have any Admin IDs saved yet.")

    # Format the list of channel IDs and send it to the user
    admin_list = "\n├🆔 ".join([str(admin_id) for admin_id in admin_ids])
    await message.reply(f"🧩 Your saved Admin IDs:\n├🆔 {admin_list}", parse_mode=enums.ParseMode.HTML)

# ///////////////////////////////////////////////////////////////
# ///////////////////////////////////////////////////////////////
async def verify_user(user_id: int):
    LAZYLISTS = await db.get_admin_ids()
    return user_id in ADMIN or user_id in LAZYLISTS

