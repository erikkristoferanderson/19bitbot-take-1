import os


import logging
import interactions

from dotenv import load_dotenv

from interactions import (
    Extension,
    slash_command,
    slash_option,
    OptionType,
    SlashContext,
    listen,
)
from interactions.api.events import MessageReactionAdd, MessageReactionRemove

from core.base import CustomClient

load_dotenv()

guild_id = os.getenv("TEST_SERVER_ID")


class RolesExtension(Extension):
    bot: CustomClient

    @slash_command(name="create-role-emoji-message", scopes=[guild_id])
    @slash_option(
        name="role_name",
        description="Role Name",
        required=True,
        opt_type=OptionType.STRING,
        min_length=1,
        max_length=50,
    )
    @slash_option(
        name="emoji", description="Emoji", required=True, opt_type=OptionType.STRING
    )
    async def create_role_emoji_message(
        self, ctx: SlashContext, role_name: str, emoji: str
    ):
        message_content = f"React with {emoji} to gain role {role_name}"
        bot_message = await ctx.send(message_content)
        await bot_message.add_reaction(emoji)

    @listen(MessageReactionAdd)
    async def on_message_reaction_add(
        self, reaction: interactions.api.events.MessageReactionAdd
    ):
        if reaction.author.id == self.bot.user.id:
            return
        if reaction.message.author.id != reaction.bot.user.id:
            return
        role_name = reaction.message.content.split()[-1]
        selected_role = None
        for role in reaction.message.guild.roles:
            if role.name == role_name:
                selected_role = role
        if selected_role is not None:
            await reaction.author.add_role(selected_role.id)
        else:
            logging.warning("on_message_reaction_add(): role_name not recognized")

    @listen(MessageReactionRemove)
    async def on_message_reaction_remove(
        self, reaction: interactions.api.events.MessageReactionRemove
    ):
        if reaction.author.id == self.bot.user.id:
            return
        if reaction.message.author.id != reaction.bot.user.id:
            return
        role_name = reaction.message.content.split()[-1]
        selected_role = None
        for role in reaction.message.guild.roles:
            if role.name == role_name:
                selected_role = role
        if selected_role is not None:
            await reaction.author.add_role(selected_role.id)
        else:
            logging.warning("on_message_reaction_remove(): role_name not recognized")


def setup(bot: CustomClient):
    """Let interactions load the extension"""

    RolesExtension(bot)
