import discord
import datetime
from discord.ext import commands
from main1 import add_server, all_servers, get_amount, get_server, delete_server, get_warns,add_warn,add_amount, get_greet,add_greet,remove_greet,get_users,add_user,add_money,share_money, get_info,give_money,remove_money,add_inventory,update_greet, remove_code, add_code, get_codes, get_premiumservers, add_premium, add_funcmd, get_funcmd, remove_funcmd, add_chatbot, get_chatbot, remove_chatbot, add_joinchannel, get_join_channels, remove_joinchannel, all_afk, add_afk, remove_afk, get_welcome_channels, add_welcomechannel, remove_welcomechannel

class Tracker(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Tracker Command Loaded Succesfully')

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def joinchannel(self,ctx, channel = None):
        if channel is None:
            embed2 = discord.Embed(description=f"Mention channel. | ,joinchannel #channel", color=0xFF0000)
            embed2.set_author(name=f"{ctx.author}",icon_url=f"{ctx.author.avatar_url}")
            embed2.set_footer(text=f"Lunar • today {datetime.datetime.now().hour}:{datetime.datetime.now().minute}",icon_url="https://images-ext-2.discordapp.net/external/F08dR3mn0Eg3YLm2mTbyd4I52Z2XSffki_g-XlUqljg/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/859504107768250379/01ac1392401eecdee1380ba4d82062d0.webp?width=406&height=406")
            await ctx.channel.send(embed=embed2)
        servers = get_join_channels()
        valid = False
        a = channel.replace("<#","").replace(">","")
        for i in servers:
            if i[1] == ctx.guild.id:
              valid = True
              remove_joinchannel(int(i[2]))
              add_joinchannel(ctx.guild.id,int(a))
              embed = discord.Embed(description=f"<a:tick:859734309073715250> Enabled joinchannel announcement on: {channel}", color=0x00FF00)
              embed.set_author(name=f"{ctx.author}",icon_url=f"{ctx.author.avatar_url}")
              embed.set_footer(text=f"Lunar • today {datetime.datetime.now().hour}:{datetime.datetime.now().minute}",icon_url="https://images-ext-2.discordapp.net/external/F08dR3mn0Eg3YLm2mTbyd4I52Z2XSffki_g-XlUqljg/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/859504107768250379/01ac1392401eecdee1380ba4d82062d0.webp?width=406&height=406")
              await ctx.channel.send(embed=embed)
              break
        if valid == False:
            add_joinchannel(ctx.guild.id,int(a))
            embed = discord.Embed(description=f"<a:tick:859734309073715250> Enabled joinchannel announcement on: {channel}", color=0x00FF00)
            embed.set_author(name=f"{ctx.author}",icon_url=f"{ctx.author.avatar_url}")
            embed.set_footer(text=f"Lunar • today {datetime.datetime.now().hour}:{datetime.datetime.now().minute}",icon_url="https://images-ext-2.discordapp.net/external/F08dR3mn0Eg3YLm2mTbyd4I52Z2XSffki_g-XlUqljg/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/859504107768250379/01ac1392401eecdee1380ba4d82062d0.webp?width=406&height=406")
            await ctx.channel.send(embed=embed)
            
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def removejoinchannel(self,ctx):
        servers = get_join_channels()
        valid = False
        for i in servers:
            if i[1] == ctx.guild.id:
              valid = True
              remove_joinchannel(int(i[2]))
              embed = discord.Embed(description=f"<a:tick:859734309073715250> Removed joinchannel on this server.", color=0x00FF00)
              embed.set_author(name=f"{ctx.author}",icon_url=f"{ctx.author.avatar_url}")
              embed.set_footer(text=f"Lunar • today {datetime.datetime.now().hour}:{datetime.datetime.now().minute}",icon_url="https://images-ext-2.discordapp.net/external/F08dR3mn0Eg3YLm2mTbyd4I52Z2XSffki_g-XlUqljg/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/859504107768250379/01ac1392401eecdee1380ba4d82062d0.webp?width=406&height=406")
              await ctx.channel.send(embed=embed)
              break
        if valid == False:
            embed = discord.Embed(description=f"<a:tick:859734309073715250> joinchannel is not enabled on this server.", color=0x00FF00)
            embed.set_author(name=f"{ctx.author}",icon_url=f"{ctx.author.avatar_url}")
            embed.set_footer(text=f"Lunar • today {datetime.datetime.now().hour}:{datetime.datetime.now().minute}",icon_url="https://images-ext-2.discordapp.net/external/F08dR3mn0Eg3YLm2mTbyd4I52Z2XSffki_g-XlUqljg/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/859504107768250379/01ac1392401eecdee1380ba4d82062d0.webp?width=406&height=406")
            await ctx.channel.send(embed=embed)

def setup(client):
    client.add_cog(Tracker(client))