# tg-serverless

[![CI Status](https://github.com/illvart/tg-serverless/workflows/CI/badge.svg)](https://github.com/illvart/tg-serverless/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)][1]

> A Telegram bot Python 3.7+ app use [Vercel][2] as Serverless Function!

## Install dependencies

```sh
pip install -r requirements.txt
pip install -r requirements-dev.txt
```

## Develop locally

```sh
vercel dev
```

Or running without vercel.

```sh
# without webhook
python -m app
# with webhook
python -m api.bot
# index webpage
python -m api.index
```

Linting and format code.

```sh
./lint.sh
```

## Environment variables

At `.env` file or configure at [vercel][2].

```sh
BOT_API_TOKEN=123456789:AbCdfGhIJKlmNoQQRsTUVwxyZ
WEBHOOK_HOST=https://{project_name}.vercel.app
SERVERLESS=True
```

## Bugs

This bot was built using [aiogram]. Currently this bot doesn't run perfectly because vercel runtime `@vercel/python` does not use Python 3.7+. When access `/api/bot` you got errors:

```sh
[GET] /api/bot

Unable to import module 'now__handler__python': Your Python version 3.6.12 is not supported by aiogram, please install Python 3.7+
```

Why? It's because `aiogram` required Python 3.7+ and currently vercel use Python 3.6.12.

Stay tune, hopefully [this request](https://github.com/vercel/vercel/discussions/5486) accepted.

## License

This project is licensed under the **MIT License**. See the [LICENSE][1] file for details.


[1]: https://github.com/illvart/tg-serverless/blob/main/LICENSE
[2]: https://vercel.com
[aiogram]: https://github.com/aiogram/aiogram
