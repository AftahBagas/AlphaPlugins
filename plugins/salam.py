"""Command Salam Dan Jawab Salam"""
import asyncio
from collections import deque

from alpha import Message, alpha


@alpha.on_cmd("p$", about={"header": "Salam Dulu"})
async def tiger_(message: Message):
    """salam"""
    animation_interval = 0.1
    animation_ttl = range(117)
    await message.edit("`Assalamu'alaikum`")


@alpha.on_cmd("l$", about={"header": "Jawab Salam"})
async def tiger_(message: Message):
    """jawab salam"""
    animation_interval = 0.1
    animation_ttl = range(117)
    await message.edit("`Waalaikumsallam`")
    
