import discord
import datetime
from discord.ext import commands
from main1 import add_server, all_servers, get_amount, get_server, delete_server, get_warns,add_warn,add_amount, get_greet,add_greet,remove_greet,get_users,add_user,add_money,share_money, get_info,give_money,remove_money,add_inventory,update_greet, remove_code, add_code, get_codes, get_premiumservers, add_premium, add_funcmd, get_funcmd, remove_funcmd, add_chatbot, get_chatbot, remove_chatbot, add_joinchannel, get_join_channels, remove_joinchannel, all_afk, add_afk, remove_afk, get_welcome_channels, add_welcomechannel, remove_welcomechannel

class Botinfo(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Botinfo Command Loaded Succesfully')

    @commands.command()
    async def botinfo(self,ctx):
        members = 0
        for guild in self.client.guilds:
          members += guild.member_count
        embed = discord.Embed(color=discord.Color.blue())
        embed.add_field(name="**Version**",value="1.0.0")
        embed.add_field(name="**Users**",value=members)
        embed.add_field(name="**Servers**",value=str(len(self.client.guilds)))
        embed.add_field(name="**Discord.py Version**",value="1.7. 3")
        embed.add_field(name="**Developers**",value="""spyde 🌙#0001\naunny#0001""",inline=False)
        embed.add_field(name="\u200b",value="[Join my support server](https://discord.gg/ZGjrDPzN) • [Invite me](https://discord.com/oauth2/authorize?client_id=841561994590289950&scope=bot%20applications.commands&permissions=8589934591)")
        embed.set_thumbnail(url=str(ctx.guild.icon_url))
        embed.set_author(name=f"{ctx.author}",icon_url=f"{ctx.author.avatar_url}")
        embed.set_footer(text=f"Lunar • today {datetime.datetime.now().hour}:{datetime.datetime.now().minute}",icon_url="https://images-ext-2.discordapp.net/external/F08dR3mn0Eg3YLm2mTbyd4I52Z2XSffki_g-XlUqljg/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/859504107768250379/01ac1392401eecdee1380ba4d82062d0.webp?width=406&height=406")
        await ctx.channel.send(embed=embed)

def setup(client):
    client.add_cog(Botinfo(client))