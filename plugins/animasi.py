"""Animasi AlphaZ Plugins"""
import asyncio
from collections import deque

from userge import Message, userge


@userge.on_cmd("nah$", about={"header": "Kasih Bunga Eh Layu"})
async def tiger_(message: Message):
    """tiger"""
    animation_interval = 0.1
    animation_ttl = range(117)
    await message.edit("`\n(\\_/)`"
                     "`\n(◕‿◕)`"
                     "`\n />🌹 *Ini Buat Kamu`")
    await asyncio.sleep(2)
    animation_chars = [
        "`\n(\\_/)`"
        "`\n(◡‿◡)`"
        "`\n🥀<\\  *Gajadi Layu`",


