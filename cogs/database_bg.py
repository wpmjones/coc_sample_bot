from datetime import datetime
from discord.ext import tasks,commands
from coc import utils


class DatabaseBackground(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.update.start()

    @commands.command(name="add_user")
    async def add_user(self, ctx, player_tag):
        """Command is used to register a user to the database"""
        player_tag = utils.correct_tag(player_tag)
        player = await self.bot.coc.get_player(player_tag)
        self.bot.dbconn.register_user((player.tag, player.name, player.town_hall, ))
        await ctx.send(f"User added: {player.name}")
        
    @tasks.loop(minutes=3.0)
    async def update(self):
        """This method updates the database every 3 mintues"""
        tags = self.bot.dbconn.get_players()
        tag_list = [tag[0] for tag in tags]
        async for player in self.bot.coc.get_players(tag_list):
            self.bot.dbconn.update_donation((datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                                             player.tag,
                                             player.achievements_dict['Friend in Need'].value, ))

    @update.before_loop
    async def before_update(self):
        """This method prevents the task from running before the bot is connected"""
        await self.bot.wait_until_ready()


def setup(bot):
    bot.add_cog(DatabaseBackground(bot))
