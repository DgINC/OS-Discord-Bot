import os

from nextcord import Intents
from nextcord.ext import commands

TESTING_GUILD_ID = 440725941212413952

client = commands.Bot(command_prefix="!", intents=Intents.all())


@client.event
async def on_ready():
    print("OSDB start and ready to takeover of the world!")

if os.name != "nt":
    import uvloop
    uvloop.install()

client.load_extension("plugins.utilities")
client.load_extension("plugins.roles")

# for guild_id in TESTING_GUILD_ID:
#    guild = client.get_guild(guild_id)
#    await guild.rollout_application_commands()

client.run("NjI1NjkwNTExOTE4NzU5OTQ2.XYjNsg.cbFWuseJQCJS71wkVKwKG4fbLX0")

guild = client.get_guild(TESTING_GUILD_ID)
guild.rollout_application_commands()
