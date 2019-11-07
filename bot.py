# Import other libraries to be used in your code
import coc
import traceback
import creds

from discord.ext import commands

description = "This is where you provide a concise description of your bot. Not sure if this is ever visible anywhere."

# This is where you can select the prefix you'd like used for your bot commands
prefix = "!"

# Here you make the connection to the COC API using the coc.py library
coc_client = coc.login(creds.coc_dev_email, creds.coc_dev_password)

# These are the cogs that you are using in your bot
initial_extensions = (
    "cogs.general",
    "cogs.special"
)


class MyBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix=prefix,
                         description=description,
                         case_insensitive=True)
        self.coc = coc_client

        for extension in initial_extensions:
            try:
                self.load_extension(extension)
            except Exception as extension:
                traceback.print_exc()

    async def on_ready(self):
        print(f"Bot is logged in as {self.user} ID: {self.user.id}")


if __name__ == "__main__":
    try:
        bot = MyBot()
        bot.run(creds.discord_bot_token)
    except:
        traceback.print_exc()