import logging
import os

import interactions.api.events

from core.base import CustomClient
import asyncio
import logging
import interactions
ALLOWED_ROLE_NAMES_FOR_BOT_TO_ADD = ["new-role"]

from dotenv import load_dotenv

from interactions import (
    Button,
    ButtonStyle,
    ComponentContext,
    Embed,
    Extension,
    InteractionContext,
    component_callback,
    slash_command,
    slash_option,
    OptionType,
    Modal,
    ShortText,
    SlashContext,
    SlashCommandChoice,
    listen,
    Message,
    MessageInteraction,
    # MessagReaction,


)
# from interactions.api.events import MessagReaction
from interactions.api.events import Component, ModalCompletion
from interactions import ModalContext

# from interactions.something import ButtonStyles

load_dotenv()

guild_id = os.getenv("TEST_SERVER_ID")


class RolesExtension(Extension):
    bot: CustomClient

    @listen(interactions.api.events.MessageReactionAdd)
    async def on_message_reaction_add(self, reaction: interactions.api.events.MessageReactionAdd):
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
        name="emoji",
        description="Emoji",
        required=True,
        opt_type=OptionType.STRING
    )
    async def create_role_emoji_message(self, ctx: SlashContext, role_name: str, emoji: str):
        message_content = f'React with {emoji} to gain role {role_name}'
        bot_message = await ctx.send(message_content)
        await bot_message.add_reaction(emoji)

    # @Listen
    # async def listen_for_reaction(self, ):

    # @bot.event
    # async def on_message_reaction_add(reaction: MessageReaction):
    #
    # @listen(MessageReactionAdd)
    # async def message_reaction_event_handler(event: MessageReactionAdd):
    #     event.member.add_role('new-role')
    #     print('yeah yeah yeah')
    # # async def on_reaction_create(event: MessageReactionAdd):
    #     ctx = event.ctx
    #     print('got it')
    #     print('yeah')

    #
    # @listen
    # async def on_reaction_add(self, event):
    #     print(event.reaction)
    #


        # await asyncio.sleep(3)
        # await ctx.channel.fetch_messages()
        # received_message_content = None
        # while received_message_content != message_content:
        #     await ctx.defer()
        #     await asyncio.sleep(1)
        #     await ctx.channel.fetch_messages()
        #     last_message_id = ctx.channel.last_message_id
        #     received_message_content = ctx.channel.get_message(last_message_id).content
        # role_emoji_message = ctx.channel.get_message(last_message_id)
        #
        #
        # await role_emoji_message.add_reaction(emoji)
    #     # print('testing')
    #
    # @listen()
    # async def on_message_create(self, event):
    #     print(f"message received: {event.message.content}")
    #
    #
    #
    # @slash_command(name="add-role", scopes=[guild_id])
    # @slash_option(
    #     name="role_name",
    #     description="Role Name",
    #     required=True,
    #     opt_type=OptionType.STRING,
    #     min_length=1,
    #     max_length=50,
    # )
    # async def add_role(self, ctx: SlashContext, role_name: str):
    #     selected_role = None
    #     for role in ctx.guild.roles:
    #         logging.info(str(role))
    #         if role.name == role_name:
    #             selected_role = role
    #     if (
    #         selected_role is not None
    #         and selected_role in ALLOWED_ROLE_NAMES_FOR_BOT_TO_ADD
    #     ):
    #         await ctx.member.add_role(selected_role)
    #         await ctx.send("role added")
    #     else:
    #         logging.warning('role not found or not allowed"')
    #         await ctx.send("role not found or not allowed")
    #         return
    #
    # @slash_command(name="remove-role", scopes=[guild_id])
    # @slash_option(
    #     name="role_name",
    #     description="Role Name",
    #     required=True,
    #     opt_type=OptionType.STRING,
    #     min_length=1,
    #     max_length=50,
    # )
    # async def remove_Role(self, ctx: SlashContext, role_name: str):
    #     selected_role = None
    #     for role in ctx.guild.roles:
    #         logging.info(str(role))
    #         if role.name == role_name:
    #             selected_role = role
    #     if (
    #         selected_role is not None
    #         and selected_role in ALLOWED_ROLE_NAMES_FOR_BOT_TO_ADD
    #     ):
    #         await ctx.member.remove_role(selected_role)
    #         await ctx.send("role removed")
    #     else:
    #         await ctx.send("role not found or not allowed")
    #         return

    # @slash_command(
    #     name="create-role-reaction-message",
    #     description="Creates a message that users may respond to with emoji to get assigned roles",
    #     scopes=[guild_id],
    # )
    # async def create_role_reaction_message(self, ctx: SlashContext):
    #     """docsstring"""
    #     dict_of_role_name_to_emoji = {}
    #     role_modal = Modal(
    #         ShortText(label="Role name", custom_id="role_name"),
    #         ShortText(label="Reaction Emoji", custom_id="reaction_emoji"),
    #         title="Role Reaction Modal",
    #         custom_id="role_reaction_modal",
    #     )
    #     await ctx.send_modal(modal=role_modal)
    #     modal_ctx: ModalContext = await ctx.bot.wait_for_modal(role_modal)
    #
    #     role_name = modal_ctx.responses["role_name"]
    #     reaction_emoji = modal_ctx.responses["reaction_emoji"]
    #     dict_of_role_name_to_emoji[role_name] = reaction_emoji
    #
    #     await ctx.send("Hello World")
    #
    #     last_message_id = ctx.channel.last_message_id
    #
    #     @listen()
    #     async def on_component(event: ModalCompletion):
    #         ctx = event.ctx
    #         logging.info("ctx.custom_id", ctx.custom_id)
    #         match ctx.custom_id:
    #             case "role_reaction_modal":
    #                 logging.info("case role_reaction_modal")
    #                 await ctx.send("You clicked it!")
    #
    #     @slash_command(
    #         name="my_other_command",
    #         description="My first command :)",
    #         scopes=[guild_id],
    #     )
    #     async def my_other_command(ctx: SlashContext):
    #         components = Button(
    #             custom_id="my_button_id",
    #             style=ButtonStyle.GREEN,
    #             label="Click Me",
    #         )
    #
    #         await ctx.channel.send("Look a Button!", components=components)
    #
    #     @listen()
    #     async def on_component(event: Component):
    #         ctx = event.ctx
    #
    #         match ctx.custom_id:
    #             case "my_button_id":
    #                 await ctx.send("You clicked it!")
    #
    # #
    # @slash_command(name="hello_world", description="My first command :)")
    # async def my_command(self, ctx: InteractionContext):
    #     """Says hello to the world"""
    #
    #     # adds a component to the message
    #     components = Button(
    #         style=ButtonStyle.GREEN,
    #         label="Hiya",
    #         custom_id="hello_world_button"
    #     )
    #
    #     # adds an embed to the message
    #     embed = Embed(title="Hello World 2", description="Now extra fancy")
    #
    #     # respond to the interaction
    #     await ctx.send("Hello World", embeds=embed, components=components)
    #
    #
    # @component_callback("hello_world_button")
    # async def my_callback(self, ctx: ComponentContext):
    #     """Callback for the component from the hello_world command"""
    #
    #     await ctx.send("Hiya to you too")


def setup(bot: CustomClient):
    """Let interactions load the extension"""

    RolesExtension(bot)
