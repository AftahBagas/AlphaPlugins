"""Dibuat Karena Gabut:v"""
import asyncio
from collections import deque

from alpha import Message, alpha


@alpha.on_cmd("alfareza$", about={"header": "perkenalkan dulu gais"})
async def alfareza_(message: Message):
    """perkenalan"""
    animation_interval = 0.0
    animation_ttl = range(117)
    await message.edit("`Hallo 🤗`")
    await asyncio.sleep(2)
    await message.edit("`Namaku Alfareza`")
    await asyncio.sleep(2)
    await message.edit("`Umurku 16 Tahun, Asal Jateng Pati`")
    await asyncio.sleep(2)
    await message.edit("`Salam Kenal Ya:)`")


@alpha.on_cmd("punten$", about={"header": "punten slur"})
async def punten_(message: Message):
    """Punten Slur"""
    animation_interval = 0.0
    animation_ttl = range(117)
    await message.edit("`\n┻┳|―-∩`"
                       "`\n┳┻|     ヽ`"
                       "`\n┻┳|    ● |`"
                       "`\n┳┻|▼) _ノ`"
                       "`\n┻┳|￣  )`"
                       "`\n┳ﾐ(￣ ／`"
                       "`\n┻┳T￣|`"
                       "\n**Punten**")
    
