import logging
from urllib.parse import urljoin

from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.middlewares.logging import LoggingMiddleware

from app.config import BOT_API_TOKEN, SERVERLESS, WEBAPP_HOST, WEBAPP_PORT, WEBHOOK_HOST

WEBHOOK_PATH = "/api/bot"
WEBHOOK_URL = urljoin(WEBHOOK_HOST, WEBHOOK_PATH)

logging.basicConfig(level=logging.INFO)

bot = Bot(token=BOT_API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
dp.middleware.setup(LoggingMiddleware())


async def on_startup(dispatcher: Dispatcher) -> None:
    if SERVERLESS is True:
        logging.info("🚀 Bot launched as Serverless!")
        logging.info(f"webhook: {WEBHOOK_URL}")

        webhook = await dispatcher.bot.get_webhook_info()

        if webhook.url:
            await bot.delete_webhook()
        await bot.set_webhook(WEBHOOK_URL)
    else:
        logging.info("🚀 Bot launched!")

    await dispatcher.bot.set_my_commands([types.BotCommand(command="/start", description="Start the bot")])


async def on_shutdown(dispatcher: Dispatcher) -> None:
    logging.warning("😴 Bot shutdown...")
    if SERVERLESS is True:
        await bot.delete_webhook()
    await dispatcher.storage.close()
    await dispatcher.storage.wait_closed()


def bot_register(webhook: bool = False) -> None:
    import app.handlers  # noqa: F401

    try:
        if webhook is True and SERVERLESS is True:
            executor.start_webhook(
                dispatcher=dp,
                webhook_path=WEBHOOK_PATH,
                on_startup=on_startup,
                on_shutdown=on_shutdown,
                skip_updates=True,
                host=WEBAPP_HOST,
                port=WEBAPP_PORT,
            )
        else:
            executor.start_polling(
                dp,
                skip_updates=True,
                on_startup=on_startup,
                on_shutdown=on_shutdown,
            )
    except Exception:
        raise
    except KeyboardInterrupt:
        pass
