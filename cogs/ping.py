import discord
import datetime
from discord.ext import commands
from main1 import add_server, all_servers, get_amount, get_server, delete_server, get_warns,add_warn,add_amount, get_greet,add_greet,remove_greet,get_users,add_user,add_money,share_money, get_info,give_money,remove_money,add_inventory,update_greet, remove_code, add_code, get_codes, get_premiumservers, add_premium, add_funcmd, get_funcmd, remove_funcmd, add_chatbot, get_chatbot, remove_chatbot, add_joinchannel, get_join_channels, remove_joinchannel, all_afk, add_afk, remove_afk, get_welcome_channels, add_welcomechannel, remove_welcomechannel

class Ping(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Ping Command Loaded Succesfully')

    @commands.command()
    async def ping(self,ctx):
        embed = discord.Embed(description=f"<a:tick:859734309073715250> Pong! {round(self.client.latency * 1000)}ms", color=0x00FF00)
        embed.set_author(name=f"{ctx.author}",icon_url=f"{ctx.author.avatar_url}")
        embed.set_footer(text=f"Lunar • today {datetime.datetime.now().hour}:{datetime.datetime.now().minute}",icon_url="https://media.discordapp.net/859872371842088981/860186039784439864/fd9a5fe710d981cd296503ccc4df0af5.gif?width=549&height=412")
        await ctx.channel.send(embed=embed)

def setup(client):
    client.add_cog(Ping(client))