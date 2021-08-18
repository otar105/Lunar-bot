import discord
import datetime
from discord.ext import commands
from main1 import add_server, all_servers, get_amount, get_server, delete_server, get_warns,add_warn,add_amount, get_greet,add_greet,remove_greet,get_users,add_user,add_money,share_money, get_info,give_money,remove_money,add_inventory,update_greet, remove_code, add_code, get_codes, get_premiumservers, add_premium, add_funcmd, get_funcmd, remove_funcmd, add_chatbot, get_chatbot, remove_chatbot, add_joinchannel, get_join_channels, remove_joinchannel, all_afk, add_afk, remove_afk, get_welcome_channels, add_welcomechannel, remove_welcomechannel

class Poll(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Poll Command Loaded Succesfully')

    @commands.command()
    async def poll(self,ctx, *,message):
      embed = discord.Embed(title=" POLL ", description=f"{message}")
      msg = await ctx.channel.send(embed=embed)
      await msg.add_reaction("👍")
      await msg.add_reaction("👎")

def setup(client):
    client.add_cog(Poll(client))