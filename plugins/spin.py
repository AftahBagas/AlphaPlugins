import os
import shutil

from PIL import Image
from userge import Message, userge
from userge.plugins.utils.circle import crop_vid
from userge.utils import media_to_image, runcmd

path = "userge/xcache/rotate-disc/"


@userge.on_cmd(
    "spin",
    about={
        "header": "Brr... 🌀",
        "flags": {
            "-s": "Speed -> 1-6",
            "-c": "Spin Clockwise",
            "-r": "for round video",
        },
        "description": "Reply to any media to spin",
        "usage": "{tr}spin [flags] [reply to media]",
        "examples": [
            "{tr}spin",
            "{tr}spin -s4 -c -r",
        ],
    },
)
async def spinn(message: Message):
    pic_loc = await media_to_image(message)
    if not pic_loc:
        return await message.err("Reply to a valid media first", del_in=5)
    await message.edit("🌀 `Tighten your seatbelts, sh*t is about to get wild ...`")
    step_dict = {"1": 1, "2": 3, "3": 6, "4": 12, "5": 24, "6": 60}
    if "-s" in message.flags:
        step = step_dict.get(message.flags["-s"], None)
        if not step:
            return await message.err("Not valid value for flag '-s'", del_in=5)
    else:
        step = 1

    spin_dir = -1 if "-c" in message.flags else 1

    if not os.path.exists(path):
        os.mkdir(path)

    reply = message.reply_to_message
    reply_id = reply.message_id if reply else None

    im = Image.open(pic_loc)
    if im.mode != "RGB":
        im = im.convert("RGB")

    for k, nums in enumerate(range(1, 360, step), start=0):
        y = im.rotate(nums * spin_dir)
        y.save(os.path.join(path, "spinx%s.jpg" % k))

    output_vid = os.path.join(path, "out.mp4")
    frate = int(((90 / 59) * step) + (1680 / 59))
    await runcmd(
        f"ffmpeg -framerate {frate} -i {path}spinx%d.jpg -c:v libx264 -pix_fmt yuv420p {output_vid}"
    )
    if os.path.exists(output_vid):
        await message.delete()
        if "-r" in message.flags:
            round_vid = os.path.join(path, "out_round.mp4")
            await crop_vid(output_vid, round_vid)
            await message.client.send_video_note(
                message.chat.id, round_vid, reply_to_message_id=reply_id
            )
        else:
            await message.client.send_animation(
                message.chat.id,
                output_vid,
                unsave=(not message.client.is_bot),
                reply_to_message_id=reply_id,
            )
    os.remove(pic_loc)
    shutil.rmtree(path)
