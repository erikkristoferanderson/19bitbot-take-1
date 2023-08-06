from core.base import CustomClient

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


class SoundboardExtension(Extension):
    bot: CustomClient


def setup(bot: CustomClient):
    """Let interactions load the extension"""

    SoundboardExtension(bot)
