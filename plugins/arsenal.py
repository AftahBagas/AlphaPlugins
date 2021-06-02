import asyncio
import time

from pyrogram.errors import FloodWait
from alpha import Config, Message, logging, alpha

_LOG = logging.getLogger(__name__)


async def banager(message: Message, chat_id: int, user_id: int, until_date: int) -> str:
    log_msg = ""
    try:
        await message.client.kick_chat_member(
            chat_id=chat_id, user_id=user_id, until_date=until_date
        )
        log_msg = "Success"
    except FloodWait as fw:
        _LOG.info("Sleeping for some time due to flood wait")
        await asyncio.sleep(fw.x + 10)
        return await banager(message, chat_id, user_id, until_date)
    except Exception as u_e:
        if hasattr(u_e, "NAME"):
            log_msg = f"ERROR:- {u_e.NAME} >>" f" {type(u_e).__name__} > {u_e.MESSAGE}"
        else:
            log_msg = f"ERROR:- {type(u_e).__name__} > {str(u_e)}"
    return log_msg


@alpha.on_cmd(
    "snap",
    about={
        "header": "Ban All",
        "description": "Haha, jepretan Mighty Thanos ke Ban"
        " Semua Anggota SuperGroup",
        "flags": {"-k": "Tendang Anggota alih-alih melarang"},
        "usage": "{tr}snap [(optional flag)]",
    },
    allow_private=False,
    only_admins=True,
)
async def snapper(message: Message):
    chat_id = message.chat.id
    act = "Banning"
    if "-k" in message.flags:
        act = "Kicking"
    await message.edit(
        f"⚠️ {act} all Anggota obrolan. [`Periksa log aplikasi"
        f" untuk status`]\nUse `{Config.CMD_TRIGGER}membatalkan` sebagai balasan untuk "
        "pesan ini untuk menghentikan proses ini."
    )
    _LOG.info(f"Menghapus Anggota dalam {message.chat.title}")
    s_c = 0
    e_c = 0
    async for member in message.client.iter_chat_members(chat_id):
        if message.process_is_canceled:
            await message.edit("`Keluar dari snap...`")
            break
        if (
            member.status in ("administrator", "creator")
            or member.user.is_self
            or member.user.id in Config.OWNER_ID
        ):
            continue
        until = int(time.time()) + 45 if "-k" in message.flags else 0
        log_msg = await banager(message, chat_id, member.user.id, until)
        user_tag = f"[{member.user.first_name}]: Ban Status --> "
        if log_msg.lower() == "success":
            s_c += 1
        else:
            e_c += 1
        _LOG.info(user_tag + log_msg)
    await message.edit(f"[<b>{act} Completed</b>]:\nSuccess: `{s_c}`\nFailed: `{e_c}`")
