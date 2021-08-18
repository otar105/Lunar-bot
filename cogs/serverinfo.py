import discord
import datetime
from discord.ext import commands
from main1 import add_server, all_servers, get_amount, get_server, delete_server, get_warns,add_warn,add_amount, get_greet,add_greet,remove_greet,get_users,add_user,add_money,share_money, get_info,give_money,remove_money,add_inventory,update_greet, remove_code, add_code, get_codes, get_premiumservers, add_premium, add_funcmd, get_funcmd, remove_funcmd, add_chatbot, get_chatbot, remove_chatbot, add_joinchannel, get_join_channels, remove_joinchannel, all_afk, add_afk, remove_afk, get_welcome_channels, add_welcomechannel, remove_welcomechannel

class Serverinfo(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Serverinfo Command Loaded Succesfully')

    @commands.command()
    async def serverinfo(self,ctx):
        name = str(ctx.guild.name)
        text_channels = len(ctx.guild.text_channels)
        voice_channels = len(ctx.guild.voice_channels)
        categories = len(ctx.guild.categories)

        owner = str(ctx.guild.owner)
        id = str(ctx.guild.id)
        region = str(ctx.guild.region)
        memberCount = str(ctx.guild.member_count)
        icon = str(ctx.guild.icon_url)
        embed = discord.Embed(
            description=f"**Guild information for __{name}__**",
            color=discord.Color.blue()
            )
        embed.set_thumbnail(url=icon)
        embed.add_field(name="<a:Arrow_White:860428736637829121> **Owner**", value=f"**{owner}**", inline=True)
        embed.add_field(name="<a:Arrow_White:860428736637829121> **Channel Categories**", value=categories, inline=True)
        embed.add_field(name="<a:Arrow_White:860428736637829121> **Text Channels**", value=text_channels, inline=True)
        embed.add_field(name="<a:Arrow_White:860428736637829121> **Voice Channels**", value=voice_channels, inline=True)
        embed.add_field(name="<a:Arrow_White:860428736637829121> **Members**", value=memberCount, inline=True)
        embed.add_field(name="<a:Arrow_White:860428736637829121> **Region**", value=region, inline=True)
        embed.add_field(name="<a:Arrow_White:860428736637829121> **Boost Count**", value=ctx.guild.premium_subscription_count, inline=True)
        embed.set_footer(text=f"ID: {id} | Server Created • {ctx.guild.created_at.month}/{ctx.guild.created_at.day}/{ctx.guild.created_at.year}")
        embed.set_thumbnail(url=f"{icon}")
        """
        async with ctx.typing():
            await asyncio.sleep(3)
        """
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Serverinfo(client))