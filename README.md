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
Mac/Linux
```shell
set -a; source .env; set +a; bot
```
