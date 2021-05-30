"""Animasi AlphaZ Plugins"""
import asyncio
from collections import deque

from userge import Message, userge


@userge.on_cmd("nah$", about={"header": "animasi cek aja sendiri"})
async def tiger_(message: Message):
    """nah"""
    animation_interval = 0.1
    animation_ttl = range(117)
    animation_chars = [
        await typew.edit("`\n(\\_/)`"
                     "`\n(◕‿◕)`"
                     "`\n />🌹 *Ini Buat Kamu`")
    sleep(2)
    await typew.edit("`\n(\\_/)`"
                     "`\n(◡‿◡)`"
                     "`\n🥀<\\  *Gajadi Layu`")
    
