import re
from asyncio import sleep

from newspaper import Article, ArticleException
from alpha import Message, alpha

regex: str = (
    r"(https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\."
    r"[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&\/\/=]*))"
)
max_chars = 3900


@alpha.on_cmd(
    "con",
    about={"header": "Memo konten artikel", "usage": "{tr}con [link | reply to msg]"},
)
async def con_(message: Message):
    """Artikel Scraper"""
    text = message.input_str
    if message.reply_to_message:
        text = message.reply_to_message.text
    if not text:
        await message.err("Input not found")
        return
    try:
        url: str = re.search(regex, text).group(1)
        article: Article = Article(url)
        article.download()
        article.parse()
        # split article content into chunks
        # credits to https://github.com/eternnoir/pyTelegramBotAPI/blob/
        # 2dec4f1ffc3f7842844e747b388edf0d6560a5b6/telebot/util.py#L224
        chunks = [
            article.text[i : i + max_chars]
            for i in range(0, len(article.text), max_chars)
        ]
        header = f"**{article.title}**\n{article.publish_date}\n\n"
        if len(chunks) == 1:
            await message.edit(header + article.text)
        else:
            await message.edit(header + chunks[0])
            for chunk in chunks[1:]:
                await message.reply(chunk)
                await sleep(2)
    except AttributeError:
        await message.edit("`Tidak dapat menemukan URL yang valid!`")
    except ArticleException:
        await message.edit("`Gagal mengikis artikel!`")
