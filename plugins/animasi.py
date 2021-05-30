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
        sleep(1)
        "`🏃       🐅`"
        "`🏃      🐅`"
        "`🏃     🐅`"
        "`🏃    🐅`"
        "`Dahlah Pasrah Aja`"
        sleep(1)
        "`🧎🐅`"
        sleep(2)
        "`-TAMAT-`"
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await message.edit(animation_chars[i % 32])
