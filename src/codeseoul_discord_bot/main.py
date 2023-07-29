import discord
import logging
import os

from codeseoul_discord_bot.client import CodeSeoulBotClient


intents = discord.Intents.default()
intents.message_content = True
intents.reactions = True
logger = logging.getLogger("discord.codeseoul")
client = CodeSeoulBotClient(intents=intents)


def main():
    api_token = os.getenv("DISCORD_API_TOKEN")
    client.run(api_token)


if __name__ == "__main__":
    main()
