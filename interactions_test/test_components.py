from interactions import Button, ActionRow, ButtonStyle, Extension
from interactions.ext.prefixed_commands import prefixed_command


class ButtonExampleSkin(Extension):
    @prefixed_command()
    async def blurple_button(self, ctx):
        await ctx.send("hello there", components=Button(ButtonStyle.BLURPLE, "A blurple button"))

    @prefixed_command()
    async def multiple_buttons(self, ctx):
        await ctx.send(
            "2 buttons in a row",
            components=[Button(ButtonStyle.BLURPLE, "A blurple button"), Button(ButtonStyle.RED, "A red button")],
        )

    @prefixed_command()
    async def action_rows(self, ctx):
        await ctx.send(
            "2 buttons in 2 rows, using nested lists",
            components=[[Button(ButtonStyle.BLURPLE, "A blurple button")], [Button(ButtonStyle.RED, "A red button")]],
        )

    @prefixed_command()
    async def action_rows_more(self, ctx):
        await ctx.send(
            "2 buttons in 2 rows, using explicit action_rows lists",
            components=[
                ActionRow(Button(ButtonStyle.BLURPLE, "A blurple button")),
                ActionRow(Button(ButtonStyle.RED, "A red button")),
            ],
        )


def setup(bot):
    ButtonExampleSkin(bot)