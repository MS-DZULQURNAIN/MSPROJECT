from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors.exceptions.bad_request_400 import UserNotParticipant

@Bot.on_message(filters.incoming & filters.private, group=-1)
async def fsub(bot, message):
  if not FSUB:
    return True
  try:
    await bot.get_chat_member(FSUB, message.from_user.id)
  except UserNotParticipant:
    if FSUB.startswith("-100"):
      
