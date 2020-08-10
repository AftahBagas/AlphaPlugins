"""Anime Girl Game Cut-Scene"""

# BY code-rgb [https://github.com/code-rgb]

import random
import re
from userge import userge, Message
import requests
from validators.url import url


EMOJI_PATTERN = re.compile(
    "["
    "\U0001F1E0-\U0001F1FF"  # flags (iOS)
    "\U0001F300-\U0001F5FF"  # symbols & pictographs
    "\U0001F600-\U0001F64F"  # emoticons
    "\U0001F680-\U0001F6FF"  # transport & map symbols
    "\U0001F700-\U0001F77F"  # alchemical symbols
    "\U0001F780-\U0001F7FF"  # Geometric Shapes Extended
    "\U0001F800-\U0001F8FF"  # Supplemental Arrows-C
    "\U0001F900-\U0001F9FF"  # Supplemental Symbols and Pictographs
    "\U0001FA00-\U0001FA6F"  # Chess Symbols
    "\U0001FA70-\U0001FAFF"  # Symbols and Pictographs Extended-A
    "\U00002702-\U000027B0"  # Dingbats
    "]+")


def deEmojify(inputString: str) -> str:
    """Remove emojis and other non-safe characters from string"""
    return re.sub(EMOJI_PATTERN, '', inputString)


@userge.on_cmd("sc", about={
    'header': "Creates Random Anime Cut Scene",
    'flags': {
    "y": "yuri",
    "n": "natsuki",
    "m": "monika",
    "s": "sayori"
   },
    'usage': "{tr}sc [text | reply to message]\n"
             "{tr}sc [flags] [text | reply to message]",
    'examples': [
        "{tr}sc Hello Anon",
        "{tr}sc [flags] Hello Anon"]})
async def anime_Scene(message: Message):
    """ Creates random anime Cut Scene! """

    monika_faces = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r"]

    natsuki_faces = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "1t", "2bt", "2bta", "2btb", "2btc", "2btd", "2bte", "2btf", "2btg", "2bth", "2bti", "2t", "2ta", "2tb", "2tc", "2td", "2te", "2tf", "2tg", "2th", "2ti"]

    sayori_faces = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y"]

    yuri_faces = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y1", "y2", "y3", "y4", "y5", "y6", "y7"]

    background = ["bedroom", "class", "closet", "club", "corridor", "house", "kitchen", "residential", "sayori_bedroom"]


    ddlc_items = {
        "body": {
            "monika": [ "1", "2" ],
            "natsuki": [ "1b", "1", "2b", "2"],
            "yuri": ["1b", "1", "2b", "2"],
            "sayori": ["1b", "1", "2b", "2"]
        },
        "face": {
            "monika": monika_faces,
            "natsuki": natsuki_faces,
            "yuri": yuri_faces,
            "sayori": sayori_faces
        }
    }

    ddlc_char = ["yuri", "natsuki", "monika", "sayori"]
    
    replied = message.reply_to_message
    args = message.filtered_input_str
    if args:
        text = args
    elif replied:
        text = args if args else replied.text
    else:
        await message.err("```Input not found!...```", del_in=3)
        return
    await message.delete()
    if '-y' in message.flags:
        character = "yuri"
    if '-n' in message.flags:
        character = "natsuki"
    if '-m' in message.flags:
        character = "monika"
    elif '-s' in message.flags:
        character = "sayori"
    else:
        character = rand(ddlc_char)

    body = ddlc_items["body"][character]
    rando_body = rand(body)
    face = ddlc_items["face"][character]
    rando_face = rand(face)
    rand_background = rand(background)
    text = str(deEmojify(text))

    path = await ddlc(character, rando_face, rando_body, rand_background, text)
    if path == "ERROR":
        return await message.edit("😔 Something Wrong see Help!", del_in=2)
    chat_id = message.chat.id
    message_id = replied.message_id if replied else None
    await message.delete()
    await message.client.send_photo(
        chat_id=chat_id,
        photo=path,
        reply_to_message_id=message_id
    )


async def ddlc(text1, text2, text3, text4, text5):
    site = "https://nekobot.xyz/api/imagegen?type=ddlc&character="
    r = requests.get(f"{site}{text1}&face={text2}&body={text3}&background={text4}&text={text5}").json()
    urlx = r.get("message")
    anim_url = url(urlx)
    if not anim_url:
        return "ERROR"
    return urlx


def rand(array):
    random_num = random.choice(array) 
    return (str(random_num)) 




