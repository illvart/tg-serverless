import asyncio

from aiogram import __main__ as aiogram_core
from aiogram import filters, md, types
from aiogram.dispatcher.webhook import SendMessage

from app.bot import bot, dp
from app.config import SERVERLESS

throttled = "Too many requests, relax!"


# start, help command handler
@dp.message_handler(filters.Command(commands=["start", "help"], prefixes="!/", ignore_case=False))
@dp.throttled(
    lambda msg, loop, *args, **kwargs: loop.create_task(
        bot.send_message(
            msg.from_user.id,
            throttled,
            parse_mode=types.ParseMode.MARKDOWN,
            reply_to_message_id=msg.message_id,
        )
    ),
    rate=2,
)
async def cmd_start(message: types.Message) -> None:
    await bot.send_message(
        message.from_user.id,
        "Welcome!",
        parse_mode=types.ParseMode.MARKDOWN,
    )


# version command handler
@dp.message_handler(
    filters.Command(commands=["v", "version"], prefixes="!/", ignore_case=False),
    content_types=types.ContentType.TEXT,
)
@dp.throttled(
    lambda msg, loop, *args, **kwargs: loop.create_task(
        bot.send_message(
            msg.from_user.id,
            throttled,
            parse_mode=types.ParseMode.MARKDOWN,
            reply_to_message_id=msg.message_id,
        )
    ),
    rate=2,
)
async def cmd_version(message: types.Message) -> None:
    await message.reply("My Engine\n{api_info}".format(api_info=md.quote_html(str(aiogram_core.SysInfo()))))


# messages equals handler
@dp.message_handler(
    filters.Text(
        equals=[
            "hi",
            "hello",
            "hey",
            "hallo",
            "hei",
            "helo",
            "hola",
            "privet",
            "hai",
        ],
        ignore_case=True,
    ),
    content_types=types.ContentType.TEXT,
)
async def text_equals(message: types.Message) -> None:
    await asyncio.sleep(1)
    await types.ChatActions.typing()
    await message.reply(message.text)


# any type messages handler
@dp.message_handler(content_types=types.ContentType.ANY)
async def any_messages(message: types.Message) -> None:
    if SERVERLESS is True:
        return SendMessage(message.chat.id, "🤔")
    else:
        await bot.send_message(message.chat.id, "🤔")
