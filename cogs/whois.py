import discord
import datetime
from discord.ext import commands
from main1 import add_server, all_servers, get_amount, get_server, delete_server, get_warns,add_warn,add_amount, get_greet,add_greet,remove_greet,get_users,add_user,add_money,share_money, get_info,give_money,remove_money,add_inventory,update_greet, remove_code, add_code, get_codes, get_premiumservers, add_premium, add_funcmd, get_funcmd, remove_funcmd, add_chatbot, get_chatbot, remove_chatbot, add_joinchannel, get_join_channels, remove_joinchannel, all_afk, add_afk, remove_afk, get_welcome_channels, add_welcomechannel, remove_welcomechannel

class Whois(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Whois Command Loaded Succesfully')

    @commands.command(pass_context = True , aliases=['userinfo'])
    async def whois(self,ctx, user:discord.Member = None):
        if user is None:
            user = ctx.author
        if len(user.public_flags.all()) < 1:
            bage = None
        else:
            bage = str(user.public_flags.all()).replace('[<UserFlags.', '').replace('>]', '').replace('_',' ').replace(':', '').title()
        date_format = "%a, %d %b %Y %I:%M %p"
        embed = discord.Embed(description=f"""**User**
        <a:Arrow_White:860428736637829121> **Username:** {user}
        <a:Arrow_White:860428736637829121> **ID:** {user.id}
        <a:Arrow_White:860428736637829121> **Flags:** {bage}
        <a:Arrow_White:860428736637829121> **Avatar:** [Link to avatar]({user.avatar_url})
        <a:Arrow_White:860428736637829121> **Time Created:** {user.created_at.strftime(date_format)}
        <a:Arrow_White:860428736637829121> **Status:** {user.status}
        <a:Arrow_White:860428736637829121> **Game:** {user.activity}

        **Member**
        <a:Arrow_White:860428736637829121> **Highest Role:** {user.top_role}
        <a:Arrow_White:860428736637829121> **Server Join Date:** {user.joined_at.strftime(date_format)}
        <a:Arrow_White:860428736637829121> **Roles [{len(user.roles)-1}]:** {' '.join([r.mention for r in user.roles][1:])}""")
        embed.set_thumbnail(url=user.avatar_url)
        await ctx.channel.send(embed=embed)

def setup(client):
    client.add_cog(Whois(client))