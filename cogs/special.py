from discord.ext import commands


class Special(commands.Cog):
    """Description of what this file does"""
    def __init__(self, bot):
        self.bot = bot

    # TODO add a different command here


def setup(bot):
    bot.add_cog(Special(bot))
