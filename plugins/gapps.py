# BY code-rgb
"""Gapps via inline bot"""
from userge import userge, Message
@userge.on_cmd("gapps", about={
    'header': "Get Gapps"}, allow_channels=False)
async def gapps_inline(message: Message):
    await message.edit("`🔍 Finding Latest Gapps...`")
    bot = await userge.bot.get_me()
    x = await userge.get_inline_bot_results(bot.username, "gapps")
    await userge.send_inline_bot_result(chat_id=message.chat.id,
                                        query_id=x.query_id,
                                        result_id=x.results[1].id)
    await message.delete()