import logging
import os

from dotenv import load_dotenv
from interactions import Client, Intents, listen
from interactions.api.events import Component
from interactions.ext import prefixed_commands


load_dotenv()


# define your own logger with custom logging settings
logging.basicConfig()
cls_log = logging.getLogger("MyLogger")
cls_log.setLevel(logging.DEBUG)

bot = Client(intents=Intents.ALL, sync_interactions=True, asyncio_debug=True, logger=cls_log)
prefixed_commands.setup(bot)


@listen()
async def on_ready():
    print("Ready")
    print(f"This bot is owned by {bot.owner}")


@listen()
async def on_guild_create(event):
    print(f"guild created : {event.guild.name}")


@listen()
async def on_message_create(event):
    print(f"message received: {event.message.content}")


@listen()
async def on_component(event: Component):
    ctx = event.ctx
    await ctx.edit_origin("test")


bot.load_extension("test_components")
bot.load_extension("test_application_commands")
bot.start(os.getenv('DISCORD_TOKEN'))
