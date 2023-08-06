from interactions import slash_command, slash_option, SlashContext, context_menu, CommandType, Button, ActionRow, ButtonStyle, Extension


class CommandsExampleSkin(Extension):
    @slash_command("command", description="This is a test", scopes=[1137787643690766401])
    @slash_option("another", "str option", 3, required=True)
    @slash_option("option", "int option", 4, required=True)
    async def command(self, ctx: SlashContext, **kwargs):
        await ctx.send(str(ctx.resolved))
        await ctx.send(f"Test: {kwargs}", components=[ActionRow(Button(1, "Test"))])
        print(ctx.resolved)

    @command.error
    async def command_error(self, e, *args, **kwargs):
        print(f"Command hit error with {args=}, {kwargs=}")

    @command.pre_run
    async def command_pre_run(self, context, *args, **kwargs):
        print("I ran before the command did!")

    @context_menu(name="user menu", context_type=CommandType.USER, scopes=[1137787643690766401])
    async def user_context(self, ctx):
        await ctx.send("Context menu:: user")


def setup(bot):
    CommandsExampleSkin(bot)