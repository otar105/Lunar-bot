import discord
import datetime
from discord.ext import commands
from main1 import add_server, all_servers, get_amount, get_server, delete_server, get_warns,add_warn,add_amount, get_greet,add_greet,remove_greet,get_users,add_user,add_money,share_money, get_info,give_money,remove_money,add_inventory,update_greet, remove_code, add_code, get_codes, get_premiumservers, add_premium, add_funcmd, get_funcmd, remove_funcmd, add_chatbot, get_chatbot, remove_chatbot, add_joinchannel, get_join_channels, remove_joinchannel, all_afk, add_afk, remove_afk, get_welcome_channels, add_welcomechannel, remove_welcomechannel

class Bug(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Bug Command Loaded Succesfully')

    @commands.command()
    async def bug(self,ctx,*,message):
        await ctx.channel.send(f"""{ctx.author.mention}, Thanks for submitting a bug!, we will check your report
    we will DM you when this bug is resolved
    please also activate DM permissions all""")
        channel = self.client.get_channel(869484135482286110)
        embed = discord.Embed(title="New Report Bug")
        embed.add_field(name = 'User Name', value= f"{ctx.author}", inline = True)
        embed.add_field(name = 'ID User', value= f"{ctx.author.id}", inline = True)
        embed.add_field(name = 'Reported', value= f"{message}", inline = True)
        embed.add_field(name = 'Server Name', value= f"{ctx.guild.name}", inline = True)
        embed.add_field(name = 'ID Server', value= f"{ctx.guild.id}", inline = True)
        link = await ctx.channel.create_invite(max_age = 0)
        embed.add_field(name = 'Link Server', value= f"{link}", inline = True)
        embed.set_footer(text=f"Lunar • today {datetime.datetime.now().hour}:{datetime.datetime.now().minute}",icon_url="https://images-ext-2.discordapp.net/external/F08dR3mn0Eg3YLm2mTbyd4I52Z2XSffki_g-XlUqljg/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/859504107768250379/01ac1392401eecdee1380ba4d82062d0.webp?width=406&height=406")
        await channel.send(embed=embed)

def setup(client):
    client.add_cog(Bug(client))