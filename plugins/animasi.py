"""Animasi AlphaZ Plugins"""
import asyncio
from collections import deque

from userge import Message, userge


@userge.on_cmd("tiger$", about={"header": "animasi dikejar harimau"})
async def tiger_(message: Message):
    """tiger"""
    animation_interval = 0.1
    animation_ttl = range(117)
    await message.edit("`DIKEJAR HARIMAU`")
    animation_chars = [
        "`HA HAAA.....`",
        "`HARIIIMAAAUUUUU!!`",
        "`🏃                        🐅`",
        "`🏃                       🐅`",
        "`🏃                      🐅`",
        "`🏃                     🐅`",
        "`🏃   `LARII`          🐅`",
        "🌖",
        "🌗",
        "🌘",
        "🌑",
        "🌒",
        "🌓",
        "🌔",
        "🌕",
        "🌖",
        "🌗",
        "🌘",
        "🌑",
        "🌒",
        "🌓",
        "🌔",
        "🌕",
        "🌖",
        "🌗",
        "🌘",
        "🌑",
        "🌒",
        "🌓",
        "🌔",
        "🌕",
        "🌖",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await message.edit(animation_chars[i % 32])
