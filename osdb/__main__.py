import locale
import os
import gettext
from os.path import abspath, dirname, realpath, join

import nextcord
from nextcord import Intents
from nextcord.ext import commands

TESTING_GUILD_ID = 440725941212413952
APP = 'base'
WHERE_AM_I = abspath(dirname(realpath(__file__)))
LOCALE_DIR = join(WHERE_AM_I, 'language')

gettext.bindtextdomain(APP, LOCALE_DIR)
gettext.textdomain(APP)
ru = gettext.translation(APP, localedir=LOCALE_DIR, languages=["ru_RU"], fallback=True)
ru.install()

client = commands.Bot(command_prefix="!", intents=Intents.all())


@client.event
async def on_ready():
    print(_("OSDB start and ready to takeover of the world!"))
    await client.change_presence(activity=nextcord.CustomActivity(name="Online"))

if os.name != "nt":
    import uvloop
    uvloop.install()

client.load_extension("osdb.plugins.utilities")
client.load_extension("osdb.plugins.roles")

# for guild_id in TESTING_GUILD_ID:
#    guild = client.get_guild(guild_id)
#    await guild.rollout_application_commands()

client.run("NjI1NjkwNTExOTE4NzU5OTQ2.XYjNsg.MD_yMtlEoJUbtuLUIp-KYNqmw7Q")
