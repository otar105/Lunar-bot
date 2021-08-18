import discord
import datetime
from discord.ext import commands
from main1 import add_server, all_servers, get_amount, get_server, delete_server, get_warns,add_warn,add_amount, get_greet,add_greet,remove_greet,get_users,add_user,add_money,share_money, get_info,give_money,remove_money,add_inventory,update_greet, remove_code, add_code, get_codes, get_premiumservers, add_premium, add_funcmd, get_funcmd, remove_funcmd, add_chatbot, get_chatbot, remove_chatbot, add_joinchannel, get_join_channels, remove_joinchannel, all_afk, add_afk, remove_afk, get_welcome_channels, add_welcomechannel, remove_welcomechannel
import random

class Developers(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Developers Commands Loaded Succesfully')

    @commands.command()
    async def devcode(self,ctx):
        if int(ctx.author.id) == 852798396925476884:
            a = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
            result = random.choices(a,k=5)
            codes = ""
            for i in result:
              codes += i
            add_code(codes)
            await ctx.author.send(f"**your code is:** `{codes}`")

    @commands.command()
    async def premiumcodes(self,ctx):
        if ctx.author.id == 852798396925476884:
            codes = get_codes()
            await ctx.author.send(f"**Codes left:** `{codes}`")

    @commands.command()
    async def funcmd(self,ctx, user : discord.Member):
      if ctx.author.id == 792063761474394133:
          add_funcmd(user.id)
          await ctx.channel.send("done")

    @commands.command()
    async def delfuncmd(self,ctx, user : discord.Member):
      if ctx.author.id == 792063761474394133:
          remove_funcmd(user.id)
          await ctx.channel.send("done")

    @commands.command()
    async def say(self,ctx, *, msg):
        if ctx.author.id == 792063761474394133:
            embed = discord.Embed(description=msg,color=0x00FF00)
            await ctx.channel.send(embed=embed)
        else:
            embed = discord.Embed(description=f"<a:deny:860216874163240961> Sorry but this command can only be accessed by the developer.", color=0xFF0000)
            embed.set_author(name=f"{ctx.author}",icon_url=f"{ctx.author.avatar_url}")
            embed.set_footer(text=f"Lunar • today {datetime.datetime.now().hour}:{datetime.datetime.now().minute}",icon_url="https://images-ext-2.discordapp.net/external/F08dR3mn0Eg3YLm2mTbyd4I52Z2XSffki_g-XlUqljg/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/859504107768250379/01ac1392401eecdee1380ba4d82062d0.webp?width=406&height=406")
            await ctx.channel.send(embed=embed)


def setup(client):
    client.add_cog(Developers(client))