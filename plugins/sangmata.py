""" Sangmata """

# By @kanjengungsun

from pyrogram.errors.exceptions.bad_request_400 import YouBlockedUser

from alpha import userge, Message
from alpha.utils.exceptions import StopConversation


@alpha.on_cmd("sg", about={
    'header': "Sangmata gives you user's last updated names and usernames.",
    'flags': {
        '-u': "To get Username history of a User"},
    'usage': "{tr}sg [Reply to user]\n"
             "{tr}sg -u [Reply to user]"}, allow_via_bot=False)
async def sangmata_(message: Message):
    """ Dapatkan Nama dan Nama Pengguna Sebelumnya yang Diperbarui Pengguna """
    replied = message.reply_to_message
    if not replied:
        await message.err("```Balas pesan untuk mendapatkan Nama dan Riwayat Nama Pengguna...```", del_in=5)
        return
    user = replied.from_user.id
    chat = "@Sangmatainfo_bot"
    await message.edit("```Mendapatkan Riwayat Pergantian Nama Pengguna ...```")
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
    name = "📄 Catatan Pergantian Nama 📄"
    username = "📄 Catatan Pergantian Usernam 📄"
    for msg in msgs:
        if '-u' in message.flags:
            if msg.text.startswith("Tidak ada catatan yang ditemukan"):
                await message.edit("```Pengguna tidak pernah mengubah Nama Penggunanya...```", del_in=5)
                return
            if msg.text.startswith(username):
                await message.edit(f"`{msg.text}`")
        else:
            if msg.text.startswith("Tidak ada catatan yang ditemukan"):
                await message.edit("```Pengguna tidak pernah mengubah Namanya...```", del_in=5)
                return
