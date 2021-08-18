import discord
import datetime
from discord.ext import commands
from main1 import add_server, all_servers, get_amount, get_server, delete_server, get_warns,add_warn,add_amount, get_greet,add_greet,remove_greet,get_users,add_user,add_money,share_money, get_info,give_money,remove_money,add_inventory,update_greet, remove_code, add_code, get_codes, get_premiumservers, add_premium, add_funcmd, get_funcmd, remove_funcmd, add_chatbot, get_chatbot, remove_chatbot, add_joinchannel, get_join_channels, remove_joinchannel, all_afk, add_afk, remove_afk, get_welcome_channels, add_welcomechannel, remove_welcomechannel

class Afk(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Afk Command Loaded Succesfully')

    @commands.command()
    async def afk(self, ctx,*,msg = None):
        if msg == None:
            message = "AFK"
        else:
            message = msg
        valid = False
        print("here #1")
        users = all_afk()
        print("here #2",users)
        for i in users:
          print("here #3",i[1],ctx.guild.id,i[2],ctx.author.id)
          if int(i[1]) == int(ctx.guild.id) and int(i[2]) == int(ctx.author.id):
              valid = True
              print("here #3.5")
              break
        if valid == False:
            print("here #4",ctx.guild.id)
            if "@" not in message:
                add_afk(ctx.guild.id,ctx.author.id,message)
                await ctx.channel.send(f"{ctx.author.mention} I set your AFK: {message}")
                await ctx.author.edit(nick=f"[AFK] {ctx.author.name}")
            else:
              await ctx.channel.send("you should not mention anyone")

def setup(client):
    client.add_cog(Afk(client))