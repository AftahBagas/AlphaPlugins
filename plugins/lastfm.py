"""Last FM"""


from userge import Config, Message, userge
from userge.utils.helper import AioHttp

##The following command has been taken from lastfm plugin of a group management bot that can be found on telegram as @TheRealPhoenixBot (https://t.me/TheRealPhoenixBot)##
##The above stated bot's repo link - https://github.com/rsktg/TheRealPhoenixBot##
##The owner of this command and the above stated bot can be found on telegram as @TheRealPhoenix and on github as Real Phoenix (https://github.com/rsktg)##


@userge.on_cmd(
    "lastfm",
    about={
        "header": "Shows currently scrobbling track or most recent scrobbles if nothing is playing."
    },
)
async def last_fm_pic_(message: Message):
    user = await userge.get_me()
    base_url = "http://ws.audioscrobbler.com/2.0"
    res = await AioHttp.get_json(
        f"{base_url}?method=user.getrecenttracks&limit=3&extended=1&user={Config.LASTFM_USERNAME}&api_key={Config.LASTFM_API_KEY}&format=json"
    )
    if not res[0] == 200:
        return await message.edit(
            "Hmm... something went wrong.\nPlease ensure that you've set the correct username!"
        )
    res = res[1]
    try:
        first_track = res.get("recenttracks").get("track")[0]
    except IndexError:
        return await message.edit("You don't seem to have scrobbled any songs...")
    if first_track.get("@attr"):
        # Ensures the track is now playing
        image = first_track.get("image")[3].get("#text")  # Grab URL of 300x300 image
        artist = first_track.get("artist").get("name")
        song = first_track.get("name")
        loved = int(first_track.get("loved"))
        rep = f"<b>{user.first_name}</b> is currently listening to:\n"
        if not loved:
            rep += f"🎧  <code>{artist} - {song}</code>"
        else:
            rep += f"🎧  <code>{artist} - {song}</code> (♥️, loved)"
        if image:
            rep += f"<a href='{image}'>\u200c</a>"
    else:
        tracks = res.get("recenttracks").get("track")
        track_dict = {
            tracks[i].get("artist").get("name"): tracks[i].get("name") for i in range(3)
        }
        rep = f"<b>{user.first_name}</b> was listening to:\n"
        for artist, song in track_dict.items():
            rep += f"🎧  <code>{artist} - {song}</code>\n"

        last_user = (
            await AioHttp.get_json(
                f"{base_url}?method=user.getinfo&user={Config.LASTFM_USERNAME}&api_key={Config.LASTFM_API_KEY}&format=json"
            )
        )[1].get("user")
        scrobbles = last_user.get("playcount")
        rep += f"\n(<code>{scrobbles}</code> scrobbles so far)"

    return await message.edit(rep, parse_mode="html")
