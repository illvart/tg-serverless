from jinja2 import Environment, FileSystemLoader
from sanic import Sanic, response

env = Environment(loader=FileSystemLoader("api/templates"))

app = Sanic(__name__)


@app.route("/")
async def _index(request):
    title = "tg-serverless"
    description = "A Telegram bot Python app use Vercel as Serverless Function!"
    color = "#2962ff"
    repo = "https://github.com/illvart/tg-serverless"

    template = env.get_template("app.html")
    content = template.render(title=title, description=description, color=color, repo=repo)
    return response.html(content, status=200)


if __name__ == "__main__":
    app.run(debug=True, auto_reload=True, host="0.0.0.0", port=3000)
