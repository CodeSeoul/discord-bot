from os import getenv
import discord
import logging

from discord import app_commands


MY_GUILD = discord.Object(id=0)  # replace with your guild id


logger = logging.getLogger("discord.codeseoul")
logger.setLevel(getenv("LOG_LEVEL", logging.DEBUG))


# Based on https://github.com/Rapptz/discord.py/blob/master/examples/app_commands/basic.py
class CodeSeoulBotClient(discord.Client):
    def __init__(self, *, intents: discord.Intents):
        super().__init__(intents=intents)
        self.target_languages = {
            "english",
            "korean",
        }
        self.done_emoji: discord.PartialEmoji = discord.PartialEmoji(name="✅")

    async def retrieve_message(
        self, channel_id: int, message_id: int
    ) -> discord.Message:
        channel = self.get_channel(channel_id)
        message = channel.get_partial_message(message_id)
        return await message.fetch()

    async def translate(self, message: str, target_language: str):
        return f"[{target_language}] {message}"

    async def on_ready(self):
        logger.info(f"We have logged in as {self.user}")

    async def on_message(self, message):
        logger.debug("caught message: %s", message)
        if message.author == self.user:
            return

        if message.content.startswith("$hello"):
            await message.channel.send("Hello!")

    async def on_raw_reaction_add(self, payload: discord.RawReactionActionEvent):
        logger.debug("caught raw reaction: %s", payload)
        logger.debug("emoji name: %s", payload.emoji.name)
        logger.debug("emoji id: %s", payload.emoji.id)
        logger.debug(
            "emoji in targets: %s", payload.emoji.name in self.target_languages
        )
        # Only handle emojis that are our targets
        if payload.emoji.name in self.target_languages:
            # Get the message
            logger.debug("matched for message id: %d", payload.message_id)
            message = await self.retrieve_message(
                payload.channel_id, payload.message_id
            )

            # Skip if we've already done this one
            for reaction in message.reactions:
                logger.debug("reaction on message: %s", reaction)
                if reaction.emoji == self.done_emoji.name:
                    async for reaction_user in reaction.users():
                        if reaction_user == self.user:
                            logger.debug("skipping because I marked as done")
                            return

            # Translate the message text
            translated_message = await self.translate(
                message.content, payload.emoji.name
            )

            # Send the translated message and mark the original message as done
            await message.reply(translated_message)
            await message.add_reaction(self.done_emoji)
