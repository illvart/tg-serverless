from sanic import Sanic, response

from app.bot import bot_register

# https://api.telegram.org/bot{your_bot_token}/setWebhook?url={your_vercel_domain_url}/api/bot

app = Sanic(__name__)


@app.route("/api/bot", strict_slashes=False)
async def _bot(request):
    response.text("This endpoint is meant for bot and telegram communication.")
    return bot_register(True)

if __name__ == "__main__":
    app.run(debug=True, auto_reload=True, host="0.0.0.0", port=3000)
