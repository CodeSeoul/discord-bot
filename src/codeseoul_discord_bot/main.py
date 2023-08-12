import discord
import os

from codeseoul_discord_bot.client import CodeSeoulBotClient


def main():
    intents = discord.Intents.default()
    intents.message_content = True
    intents.reactions = True
    client = CodeSeoulBotClient(intents=intents)
    api_token = os.getenv("DISCORD_API_TOKEN")
    client.run(api_token)


if __name__ == "__main__":
    main()
