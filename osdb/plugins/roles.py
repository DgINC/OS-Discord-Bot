import nextcord

from nextcord import Member, Forbidden
from nextcord.ext import commands


class Roles(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_update(self, before: Member, after: Member):
        try:
            role_id = 440731697504452610
            guild = nextcord.utils.find(lambda g: g.id == before.guild.id, self.bot.guilds)
            role = nextcord.utils.get(guild.roles, id=role_id)
            member = nextcord.utils.find(lambda m: m.id == before.id, guild.members)

            if before.bot or after.bot:
                return
            else:
                if before.pending and not after.pending:
                    await member.add_roles(role, atomic=True)
        except Forbidden:
            print("You do not have permissions to add these roles")

    @commands.Cog.listener()
    async def on_member_join(self, member: Member):
        log_actions_id = 926864971151835256
        guild = nextcord.utils.find(lambda g: g.id == member.guild.id, self.bot.guilds)
        channel = nextcord.utils.get(guild.text_channels, id=log_actions_id)
        await channel.send(f"User {member.display_name} join to the server \n Time: {member.joined_at}")

    @commands.Cog.listener()
    async def on_member_remove(self, member: Member):
        log_actions_id = 926864971151835256
        guild = nextcord.utils.find(lambda g: g.id == member.guild.id, self.bot.guilds)
        channel = nextcord.utils.get(guild.text_channels, id=log_actions_id)
        await channel.send(f"User {member.display_name} leave the server \n Time: {member.joined_at}")


def setup(bot):
    bot.add_cog(Roles(bot))
