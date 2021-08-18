import discord
import datetime
from discord.ext import commands
from main1 import add_server, all_servers, get_amount, get_server, delete_server, get_warns,add_warn,add_amount, get_greet,add_greet,remove_greet,get_users,add_user,add_money,share_money, get_info,give_money,remove_money,add_inventory,update_greet, remove_code, add_code, get_codes, get_premiumservers, add_premium, add_funcmd, get_funcmd, remove_funcmd, add_chatbot, get_chatbot, remove_chatbot, add_joinchannel, get_join_channels, remove_joinchannel, all_afk, add_afk, remove_afk, get_welcome_channels, add_welcomechannel, remove_welcomechannel

class Chatbot(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Chatbot Command Loaded Succesfully')

    @commands.command()
    async def chatbot(self,ctx):
        if ctx.author.guild_permissions.manage_channels:
            channels = get_chatbot()
            valid = False
            try:
                for i in channels:
                    if i[1] == ctx.channel.id:
                        remove_chatbot(ctx.channel.id)
                        embed = discord.Embed(description=f"<a:deny:860216874163240961> Disabled chatbot announcement on: {ctx.channel.mention}", color=0xFF0000)
                        embed.set_author(name=f"{ctx.author}",icon_url=f"{ctx.author.avatar_url}")
                        embed.set_footer(text=f"Lunar • today {datetime.datetime.now().hour}:{datetime.datetime.now().minute}",icon_url="https://images-ext-2.discordapp.net/external/F08dR3mn0Eg3YLm2mTbyd4I52Z2XSffki_g-XlUqljg/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/859504107768250379/01ac1392401eecdee1380ba4d82062d0.webp?width=406&height=406")
                        await ctx.channel.send(embed=embed)
                        valid = True
                        break
            except:
                valid=False
            if valid == False:
                add_chatbot(ctx.channel.id)
                embed = discord.Embed(description=f"<a:tick:859734309073715250> Enabled chatbot announcement on: {ctx.channel.mention}", color=0x00FF00)
                embed.set_author(name=f"{ctx.author}",icon_url=f"{ctx.author.avatar_url}")
                embed.set_footer(text=f"Lunar • today {datetime.datetime.now().hour}:{datetime.datetime.now().minute}",icon_url="https://images-ext-2.discordapp.net/external/F08dR3mn0Eg3YLm2mTbyd4I52Z2XSffki_g-XlUqljg/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/859504107768250379/01ac1392401eecdee1380ba4d82062d0.webp?width=406&height=406")
                await ctx.channel.send(embed=embed)
        else:
            embed1 = discord.Embed(description=f"<a:deny:860216874163240961>  you have insufficient permissions to execute this command.", color=0xFF0000)
            embed1.set_author(name=f"{ctx.author}",icon_url=f"{ctx.author.avatar_url}")
            embed1.add_field(name="**Missing permission(s)**",value="Manage Channels")
            embed1.set_footer(text=f"Lunar • today {datetime.datetime.now().hour}:{datetime.datetime.now().minute}",icon_url="https://images-ext-2.discordapp.net/external/F08dR3mn0Eg3YLm2mTbyd4I52Z2XSffki_g-XlUqljg/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/859504107768250379/01ac1392401eecdee1380ba4d82062d0.webp?width=406&height=406")
            await ctx.channel.send(embed=embed1)

def setup(client):
    client.add_cog(Chatbot(client))