# CodeSeoul Discord Bot

## Current Features
* Translation
    * Add the `english` or `korean` emoji to a message, and the bot will reply to the message with a translation.

## Setup
Mac/Linux:

```shell
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e '.[dev]'
pre-commit install
```

## Running it
Make sure to create a `.env` file based on `.env.template` and to get a valid `application_default_credentials.json` file. Need help? [Ask us on Discord](https://discord.gg/HFknCs8).

Mac/Linux
```shell
set -a; source .env; set +a; bot
```
