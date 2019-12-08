import coc

from discord.ext import commands


class General(commands.Cog):
    """Description of what this file does"""
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="get_clan", aliases=["getclan", "clan"])
    async def get_clan(self, ctx, clan_tag):
        """Gets clan information from API and displays it for user"""
        # This line uses a utility in the coc.py library to correct clan tags (case, missing #, etc.)
        clan_tag = coc.utils.correct_tag(clan_tag)

        clan = await self.bot.coc.get_clan(clan_tag)
        content = f"The clan name for {clan_tag} is {clan.name}.\n"
        content += f"{clan.name} currently has {clan.member_count} members.\n\n"

        war = await self.bot.coc.get_current_war(clan_tag)
        if war:
            content += f"Current war state is {war.state}\n"
            if war.state != "notInWar":
                content += f"Opponent: {war.opponent}"

        await ctx.send(content)


def setup(bot):
    bot.add_cog(General(bot))
