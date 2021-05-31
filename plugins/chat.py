""" Info obrolan, Bergabung dan tinggalkan obrolan, tagall dan tag admin """


import asyncio
import html
import os

from pyrogram.errors import (
    BadRequest,
    PeerIdInvalid,
    UsernameInvalid,
    UsernameNotOccupied,
    UsernameOccupied,
)
from alphaz import Config, Message, alphaz

LOG = alphaz.getLogger(__name__)

PATH = Config.DOWN_PATH + "chat_pic.jpg"


def mention_html(user_id, name):
    return '<a href="tg://user?id={}">{}</a>'.format(user_id, html.escape(name))


@alphaz.on_cmd(
    "join",
    about={
        "header": "Bergabunglah dengan obrolan",
        "usage": "{tr}join [chat username | balas nama pengguna Obrolan Text]",
        "examples": "{tr}join @kanjengingsun",
    },
)
async def join_chat(message: Message):
    """Bergabunglah dengan obrolan"""
    replied = message.reply_to_message
    text = replied.text if replied else message.input_str
    if not text:
        await message.edit(
            "```Bruh, Tanpa nama obrolan, saya tidak bisa Bergabung...^_^```", del_in=3
        )
        return
    try:
        chat = await alphaz.get_chat(text)
        await alphaz.join_chat(text)
        await alphaz.send_message(text, f"```Bergabung {chat.title} Berhasil...```")
    except UsernameNotOccupied:
        await message.edit("```Nama pengguna, Anda masuk, tidak ada... ```", del_in=3)
        return
    except PeerIdInvalid:
        await message.edit("```Id obrolan, yang Anda masukkan, tidak ada... ```", del_in=3)
        return
    else:
        await message.delete()
        await asyncio.sleep(2)


@alphaz.on_cmd(
    "leave",
    about={
        "header": "Tinggalkan Obrolan",
        "usage": "{tr}leave\n{tr}leave [chat username | membalas teks nama pengguna Obrolan]",
        "examples": ["{tr}leave", "{tr}leave User AlphaZ Out"],
    },
    allow_private=False,
)
async def leave_chat(message: Message):
    """Tinggalkan obrolan"""
    input_str = message.input_str
    text = input_str or message.chat.id
    try:
        await alphaz.send_message(text, "```Selamat tinggal, Dunia Kejam ... :-) ```")
        await alphaz.leave_chat(text)
    except UsernameNotOccupied:
        await message.edit(
            "```Nama pengguna yang Anda masukkan, tidak ada... ```", del_in=3
        )
        return
    except PeerIdInvalid:
        await message.edit(
            "```Id obrolan yang Anda masukkan sepertinya tidak ada...```", del_in=3
        )
        return
    else:
        await message.delete()
        await asyncio.sleep(2)


@alphaz.on_cmd(
    "invite",
    about={
        "header": "Buat tautan Undangan obrolan",
        "usage": "{tr}invite\n{tr}invite [Chat Id | Chat Username]",
    },
    allow_channels=False,
    allow_private=False,
)
async def invite_link(message: Message):
    """Generate invite link"""
    chat_id = message.chat.id
    user_id = message.input_str
    if not user_id and message.reply_to_message:
        user_id = message.reply_to_message.from_user.id
    if not user_id:
        try:
            chat = await userge.get_chat(chat_id)
            chat_name = chat.title
            if chat.type in ["group", "supergroup"]:
                link = await alphaz.export_chat_invite_link(chat_id)
                await message.edit(
                    "**Invite link Genrated Successfully for\n"
                    f"{chat_name}**\n[Click here to join]({link})",
                    disable_web_page_preview=True,
                )
            else:
                await message.err("Requirements not met...")
        except Exception as e_f:
            await message.err(e_f)
    else:
        try:
            await alphaz.add_chat_members(chat_id, user_id)
            await message.edit("`Invited Successfully...`")
        except Exception as e_f:
            await message.err(e_f)


@alphaz.on_cmd(
    "tagall",
    about={
        "header": "Tagall recent 100 members with caption",
        "usage": "{tr}tagall [Text | reply to text Msg]",
    },
    allow_via_bot=False,
    allow_private=False,
)
async def tagall_(message: Message):
    """Tag recent members"""
    replied = message.reply_to_message
    text = message.input_str
    if not (text or replied):
        await message.err("Without reason, I will not tag Members...(=_=)")
        return
    c_title = message.chat.title
    c_id = message.chat.id
    await message.edit(f"`Tagging recent members in {c_title}...`")
    text = f"**{text}**\n" if text else ""
    message_id = replied.message_id if replied else None
    try:
        async for members in message.client.iter_chat_members(c_id, filter="recent"):
            if not members.user.is_bot:
                u_id = members.user.id
                u_name = members.user.username or None
                f_name = (await message.client.get_user_dict(u_id))["fname"]
                text += f"@{u_name} " if u_name else f"[{f_name}](tg://user?id={u_id}) "
    except Exception as e:
        text += " " + str(e)
    await message.client.send_message(c_id, text, reply_to_message_id=message_id)
    await message.edit("```Tagged recent Members Successfully...```", del_in=3)


@alphaz.on_cmd(
    "stagall",
    about={
        "header": "Silent tag recent 100 members with caption",
        "usage": "{tr}stagall [Text | reply to text Msg]",
    },
    allow_private=False,
    allow_via_bot=False,
)
async def stagall_(message: Message):
    """tag recent members without spam"""
    chat_id = message.chat.id
    chat = await alphaz.get_chat(chat_id)
    await message.edit(f"```tagging everyone in {chat.title}```")
    replied = message.reply_to_message
    text = message.input_str
    if not (text or replied):
        await message.err("Without reason, I will not tag Members...(=_=)")
        return
    text = f"`{text}`" if text else ""
    message_id = replied.message_id if replied else None
    member = alphaz.iter_chat_members(chat_id)
    async for members in member:
        if not members.user.is_bot:
            text += mention_html(members.user.id, "\u200b")
    await message.delete()
    await alphaz.send_message(chat_id, text, reply_to_message_id=message_id)


@alphaz.on_cmd(
    "tadmins",
    about={
        "header": "Tag admins in group",
        "usage": "{tr}tadmins [Text | reply to text Msg]",
    },
    allow_private=False,
)
async def tadmins_(message: Message):
    """Tag admins in a group"""
    replied = message.reply_to_message
    text = message.input_str
    if not (text or replied):
        await message.err("Without reason, I will not tag Admins...(=_=)")
        return
    c_title = message.chat.title
    c_id = message.chat.id
    await message.edit(f"```Tagging admins in {c_title}...```")
    text = f"**{text}**\n" if text else ""
    message_id = replied.message_id if replied else None
    try:
        async for members in message.client.iter_chat_members(
            c_id, filter="administrators"
        ):
            status = members.status
            u_id = members.user.id
            u_name = members.user.username or None
            f_name = (await message.client.get_user_dict(u_id))["fname"]
            if status == "administrator" and u_name or status == "creator" and u_name:
                text += f"@{u_name} "
            elif status in ["administrator", "creator"]:
                text += f"[{f_name}](tg://user?id={u_id}) "
    except Exception as e:
        text += " " + str(e)
    await message.client.send_message(c_id, text, reply_to_message_id=message_id)
    await message.edit("```Admins tagged Successfully...```", del_in=3)


@alphaz.on_cmd(
    "schat",
    about={
        "header": "Update and delete chat info",
        "flags": {
            "-title": "update chat title",
            "-uname": "update chat username",
            "-des": "update chat description",
            "-ddes": "delete chat description",
        },
        "usage": "{tr}schat [flag]\n" "{tr}schat [flags] [input]",
    },
    allow_via_bot=False,
    allow_private=False,
    only_admins=True,
)
async def set_chat(message: Message):
    """Set or delete chat info"""
    if not message.flags:
        await message.err("```Flags required!...```", del_in=3)
        return
    chat = await alphaz.get_chat(message.chat.id)
    if "-ddes" in message.flags:
        if not chat.description:
            await message.edit("```Chat already not have description...```", del_in=5)
        else:
            await userge.set_chat_description(message.chat.id, "")
            await message.edit(
                "```Chat Description is Successfully removed...```", del_in=3
            )
    args = message.filtered_input_str
    if not args:
        await message.edit("```Need Text to Update chat info...```", del_in=5)
        return
    if "-title" in message.flags:
        await alphaz.set_chat_title(message.chat.id, args.strip())
        await message.edit("```Chat Title is Successfully Updated...```", del_in=3)
    elif "-uname" in message.flags:
        try:
            await userge.update_chat_username(message.chat.id, args.strip())
        except ValueError:
            await message.edit("```I think its a private chat...(^_-)```", del_in=3)
            return
        except UsernameInvalid:
            await message.edit("```Username, you entered, is invalid... ```", del_in=3)
            return
        except UsernameOccupied:
            await message.edit(
                "```Username, you entered, is already Occupied... ```", del_in=3
            )
            return
        else:
            await message.edit(
                "```Chat Username is Successfully Updated...```", del_in=3
            )
    elif "-des" in message.flags:
        try:
            await userge.set_chat_description(message.chat.id, args.strip())
        except BadRequest:
            await message.edit("```Chat description is Too Long...  ```", del_in=3)
        else:
            await message.edit(
                "```Chat description is Successfully Updated...```", del_in=3
            )
    else:
        await message.edit("```Invalid args, Exiting...  ```", del_in=5)


@alphaz.on_cmd(
    "vchat",
    about={
        "header": "View Chat",
        "flags": {
            "-title": "Print chat title",
            "-uname": "Print chat user name",
            "-des": "Print chat description",
        },
        "usage": ["{tr}vchat [flags]", "{tr}vchat : upload chat photo"],
    },
    allow_private=False,
)
async def view_chat(message: Message):
    """View chat info"""
    chat_id = message.chat.id
    chat = await alphaz.get_chat(chat_id)
    if "-title" in message.flags:
        await message.edit("```checking, wait plox !...```", del_in=3)
        title = chat.title
        await message.edit("<code>{}</code>".format(title), parse_mode="html")
    elif "-uname" in message.flags:
        if not chat.username:
            await message.err("```I think its private chat !...( ･ิω･ิ)```", del_in=3)
        else:
            await message.edit("```checking, wait plox !...```", del_in=3)
            uname = chat.username
            await message.edit("<code>{}</code>".format(uname), parse_mode="html")
    elif "-des" in message.flags:
        if not chat.description:
            await message.err("```I think, chat not have description...```", del_in=3)
        else:
            await message.edit("```checking, Wait plox !...```", del_in=3)
            await message.edit(
                "<code>{}</code>".format(chat.description), parse_mode="html"
            )
    else:
        if not chat.photo:
            await message.err("```Chat not have photo... ```", del_in=3)
        else:
            await message.edit("```Checking chat photo, wait plox !...```", del_in=3)
            await message.client.download_media(chat.photo.big_file_id, file_name=PATH)
            await message.client.send_photo(message.chat.id, PATH)
            if os.path.exists(PATH):
                os.remove(PATH)


@alphaz.on_cmd(
    "bots",
    about={
        "header": "View Chat bots",
        "flags": {"-id": "name with id"},
        "usage": ["{tr}bots -id", "{tr}bots"],
    },
    allow_private=False,
)
async def bots_in_chat(message: Message):
    admin, member = [], []
    async for bots in userge.iter_chat_members(message.chat.id, filter="bots"):
        status = bots.status
        u_id = bots.user.id
        username = bots.user.username
        bot_info = f"  • @{username}"
        if "-id" in message.flags:
            bot_info += f"  [<code>{u_id}</code>]"
        if status == "administrator":
            admin.append(bot_info)
        else:
            member.append(bot_info)
    await message.reply(
        f"🤖  <b>BOTS</b> in {message.chat.title}\n\n"
        + "<b>Admin:</b>\n"
        + "\n".join(admin)
        + "\n\n"
        + "<b>Member:</b>\n"
        + "\n".join(member)
    )
