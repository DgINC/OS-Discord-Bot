from datetime import time

import nextcord
import gettext
from nextcord.ext import tasks, commands


class Utilities(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.data = []
        # self.batch_update.add_exception_type(asyncpg.PostgresConnectionError)

        self.trash_id = 936682591262769205
        self.news_id = 763296193719435265

    @commands.Cog.listener()
    async def on_ready(self):
        self.clear_trash.start()

    def cog_unload(self):
        self.clear_trash.cancel()

    @tasks.loop(time=time.fromisoformat('04:00:00+03:00'))
    async def clear_trash(self):
        guild = nextcord.utils.find(lambda g: g.id == 440725941212413952, self.bot.guilds)
        channel = nextcord.utils.get(guild.text_channels, id=self.trash_id)
        await channel.purge()
        print(_(f'Channel "{channel}" purged!'))

    @commands.Cog.listener()
    async def on_guild_scheduled_event_create(self, event: nextcord.ScheduledEvent):
        guild = nextcord.utils.find(lambda g: g.id == 440725941212413952, self.bot.guilds)
        channel = nextcord.utils.get(guild.text_channels, id=self.news_id)
        role = guild.get_role(928713881562529842)
        await channel.send(f"{role.mention} Create guild event {event.name}. \n With context {event.description}")

    @nextcord.slash_command(name="ping", description="Test bot ping/pong command.")
    async def ping(self, interaction: nextcord.Interaction, ):
        await interaction.response.send_message(
            "Pong!"
        )


def setup(bot):
    bot.add_cog(Utilities(bot))
