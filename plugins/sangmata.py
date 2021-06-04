""" Sangmata """

# By @kanjengungsun

from pyrogram.errors.exceptions.bad_request_400 import YouBlockedUser
from alpha import Message, alpha
from alpha.utils.exceptions import StopConversation


@alpha.on_cmd(
    "sg",
    about={
        "header": "Sangmata gives you user's last updated names and usernames.",
        "flags": {"-u": "To get Username history of a User"},
        "usage": "{tr}sg [Reply to user]\n" "{tr}sg -u [Reply to user]",
    },
)
async def sangmata_(message: Message):
    """Get User's Updated previous Names and Usernames"""
    replied = message.reply_to_message
    if not replied:
        await message.err("```Balas untuk mendapatkan Nama dan Riwayat Nama Pengguna...```", del_in=5)
        return
    user = replied.from_user.id
    chat = "@Sangmatainfo_bot"
    await message.edit("```Mendapatkan Informasi Pergantian Nama ...```")
    msgs = []
    ERROR_MSG = "For your kind information, you blocked @Sangmatainfo_bot, Unblock it"
    try:
        async with alpha.conversation(chat) as conv:
            try:
                await conv.send_message("/search_id {}".format(user))
            except YouBlockedUser:
                await message.err(f"**{ERROR_MSG}**", del_in=5)
                return
            msgs.append(await conv.get_response(mark_read=True))
            msgs.append(await conv.get_response(mark_read=True))
            msgs.append(await conv.get_response(timeout=3, mark_read=True))
    except StopConversation:
        pass
    name = "📄 **Riwayat Pergantian Nama**"
    username = "📄 **Riwayat Pergantian Username**"
    for msg in msgs:
        if "-u" in message.flags:
            if msg.text.startswith("Tidak ada catatan yang ditemukan"):
                await message.edit("```Pengguna tidak pernah mengubah Nama Penggunanya...```", del_in=5)
                return
            if msg.text.startswith(username):
                await message.edit(f"`{msg.text}`")
        else:
            if msg.text.startswith("No records found"):
                await message.edit("```Pengguna tidak pernah mengubah Namanya...```", del_in=5)
                return
            if msg.text.startswith(name):
                await message.edit(f"`{msg.text}`")
