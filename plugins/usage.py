import math
import asyncio

import requests

from userge import Config, userge, Message


@userge.on_cmd("usage", about={'header': "Dapatkan penggunaan jam Dyno"})  # pylint:disable=E0602
async def usage(message: Message):
    """Dapatkan akun Anda Dyno Usage"""
    if not Config.HEROKU_APP:
        await message.err("Aplikasi Heroku Tidak Ditemukan !")
        return
    await message.edit("`Processing...`")
    useragent = ('Mozilla/5.0 (Linux; Android 10; SM-G975F) '
                 'AppleWebKit/537.36 (KHTML, like Gecko) '
                 'Chrome/80.0.3987.149 Mobile Safari/537.36')
    u_id = Config.HEROKU_APP.owner.id
    headers = {
        'User-Agent': useragent,
        'Authorization': f'Bearer {Config.HEROKU_API_KEY}',
        'Accept': 'application/vnd.heroku+json; version=3.account-quotas',
    }
    path = "/accounts/" + u_id + "/actions/get-quota"
    r = requests.get("https://api.heroku.com" + path, headers=headers)
    if r.status_code != 200:
        return await message.edit("`Error: sesuatu yang buruk telah terjadi`\n\n"
                                  f">.`{r.reason}`\n")
    result = r.json()
    quota = result['account_quota']
    quota_used = result['quota_used']

    # Used
    remaining_quota = quota - quota_used
    percentage = math.floor(remaining_quota / quota * 100)
    minutes_remaining = remaining_quota / 60
    hours = math.floor(minutes_remaining / 60)
    minutes = math.floor(minutes_remaining % 60)

    # Current
    App = result['apps']
    try:
        App[0]['quota_used']
    except IndexError:
        AppQuotaUsed = 0
        AppPercentage = 0
    else:
        AppQuotaUsed = App[0]['quota_used'] / 60
        AppPercentage = math.floor(App[0]['quota_used'] * 100 / quota)
    AppHours = math.floor(AppQuotaUsed / 60)
    AppMinutes = math.floor(AppQuotaUsed % 60)

    await asyncio.sleep(1.5)

    await message.edit("⚙️ **Informasi Dyno** ⚙️\n\n"
                       f"┏━━━━━━━━━━━━━━━━━━━━━┓\n"
                       f" ⛽ `Penggunaan Dyno`  **{Config.HEROKU_APP_NAME}**:\n"
                       f"     ➤  `{AppHours}`**h**  `{AppMinutes}`**m**  "
                       f"**|**  [`{AppPercentage}`**%**]"
                       "\n"
                       " 🛢️ `Sisa kuota jam Dyno bulan ini`:\n"
                       f"     ➤  `{hours}`**h**  `{minutes}`**m**  "
                       f"**|**  [`{percentage}`**%**]\n"
                       f"┗━━━━━━━━━━━━━━━━━━━━━┛")
