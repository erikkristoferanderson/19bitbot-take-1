import os

from core.base import CustomClient

import logging

from interactions import (
    Button,
    ButtonStyle,
    ComponentContext,
    Embed,
    Extension,
    InteractionContext,
    component_callback,
    slash_command,
)
from dotenv import load_dotenv

load_dotenv()

guild_id = os.getenv("TEST_SERVER_ID")


class SoundboardExtension(Extension):
    bot: CustomClient

    @slash_command(name="soundboard-go", description="make it go", scopes=[guild_id])
    async def soundboard_go(selfself, ctx: InteractionContext):
        """Triggers the soundbaord to make a sound"""
        selected_channel = None
        for channel in ctx.guild.channels:
            if channel.name == "General":
                selected_channel = channel
        if selected_channel is None:
            logging.warning("Channel not found")
        # selected_channel.


def setup(bot: CustomClient):
    """Let interactions load the extension"""

    SoundboardExtension(bot)
