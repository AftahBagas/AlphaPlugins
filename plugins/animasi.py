"""Animasi AlphaZ Plugins"""
import asyncio
from collections import deque

from userge import Message, userge


@userge.on_cmd("tiger$", about={"header": "animasi dikejar harimau"})
async def tiger_(message: Message):
    """tiger"""
    animation_interval = 0.1
    animation_ttl = range(117)
    await message.edit("`HARIMAU 😱`")
    animation_chars = [
        "`HA HAAA.....`",
        "`HARIIIMAAAUUUUU!!`",
        "`🏃                        🐅`",
        "`🏃                       🐅`",
        "`🏃                      🐅`",
        "`🏃                     🐅`",
        "`🏃   `LARII`          🐅`",
        "`🏃                   🐅`"
        "`🏃                  🐅`"
        "`🏃                 🐅`"
        "`🏃                🐅`"
        "`🏃               🐅`"
        "`🏃              🐅`"
        "`🏃             🐅`"
        "`🏃            🐅`"
        "`🏃           🐅`"
        "`🏃WOARGH!   🐅`"
        "`🏃           🐅`"
        "`🏃            🐅`"
        "`🏃             🐅`"
        "`🏃              🐅`"
        "`🏃               🐅`"
        "`🏃                🐅`"
        "`🏃                 🐅`"
        "`🏃                  🐅`"
        "`🏃                   🐅`"
        "`🏃                    🐅`"
        "`🏃                     🐅`"
        "`🏃  Huh-Huh           🐅`"
        "`🏃                   🐅`"
        "`🏃                  🐅`"
        "`🏃                 🐅`"
        "`🏃                🐅`"
        "`🏃               🐅`"
        "`🏃              🐅`"
        "`🏃             🐅`"
        "`🏃            🐅`"
        "`🏃           🐅`"
        "`🏃          🐅`"
        "`🏃         🐅`"
        "`DIA SEMAKIN MENDEKAT!!!`"
        "`🏃       🐅`"
        "`🏃      🐅`"
        "`🏃     🐅`"
        "`🏃    🐅`"
        "`Dahlah Pasrah Aja`"
        "`🧎🐅`"
        "`-TAMAT-`"
    ]
    max_ani = len(animation_chars)
    for i in range(max_ani):
        await asyncio.sleep(1)
        await message.edit(animation_chars[i % max_ani])
    await message.edit(😱)
