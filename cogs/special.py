import discord

from discord.ext import commands


class Special(commands.Cog):
    """Description of what this file does"""
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="avatar", hidden=True)
    async def avatar(self, ctx, user: discord.Member = None):
        """Command to see a larger version of the given member's avatar
        Examples:
        ++avatar @mention
        ++avatar 123456789
        ++avatar member#1234
        """
        if not user:
            user = ctx.author
        embed = discord.Embed(color=discord.Color.blue())
        embed.add_field(name=f"{user.name}#{user.discriminator}", value=user.display_name, inline=True)
        embed.add_field(name="Avatar URL", value=user.avatar_url, inline=True)
        embed.set_image(url=user.avatar_url_as(size=128))
        embed.set_footer(text=f"Discord ID: {user.id}",
                         icon_url="https://discordapp.com/assets/2c21aeda16de354ba5334551a883b481.png")
        response = await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Special(bot))
