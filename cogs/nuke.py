import discord
import datetime
from discord.ext import commands
from main1 import add_server, all_servers, get_amount, get_server, delete_server, get_warns,add_warn,add_amount, get_greet,add_greet,remove_greet,get_users,add_user,add_money,share_money, get_info,give_money,remove_money,add_inventory,update_greet, remove_code, add_code, get_codes, get_premiumservers, add_premium, add_funcmd, get_funcmd, remove_funcmd, add_chatbot, get_chatbot, remove_chatbot, add_joinchannel, get_join_channels, remove_joinchannel, all_afk, add_afk, remove_afk, get_welcome_channels, add_welcomechannel, remove_welcomechannel

class Nuke(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Nuke Command Loaded Succesfully')

    @commands.command()
    @commands.has_permissions(manage_channels=True)
    async def nuke(self,ctx):
        try:
            channel = ctx.channel
            channel_position = channel.position

            new_channel = await channel.clone()
            await channel.delete()
            await new_channel.edit(position=channel_position, sync_permissions=True)
            embed = discord.Embed(description=f"**{ctx.author}** nuked this channel.", color=0x0000FF)
            #embed.set_author(name=f"{ctx.author}",icon_url=f"{ctx.author.avatar_url}")
            embed.set_image(url="https://media1.tenor.com/images/06a954d40453aa8c364c5e3c4832f97b/tenor.gif?itemid=5552569")
            embed.set_footer(text=f"Lunar • today {datetime.datetime.now().hour}:{datetime.datetime.now().minute}",icon_url="https://images-ext-2.discordapp.net/external/F08dR3mn0Eg3YLm2mTbyd4I52Z2XSffki_g-XlUqljg/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/859504107768250379/01ac1392401eecdee1380ba4d82062d0.webp?width=406&height=406")
            await new_channel.send(embed=embed)
        except:
            embed1 = discord.Embed(description=f"<a:deny:860216874163240961>  I have insufficient permissions to execute this command.", color=0xFF0000)
            embed1.set_author(name=f"{ctx.author}",icon_url=f"{ctx.author.avatar_url}")
            embed1.add_field(name="**Missing permission(s)**",value="Manage Channels")
            embed1.set_footer(text=f"Lunar • today {datetime.datetime.now().hour}:{datetime.datetime.now().minute}",icon_url="https://images-ext-2.discordapp.net/external/F08dR3mn0Eg3YLm2mTbyd4I52Z2XSffki_g-XlUqljg/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/859504107768250379/01ac1392401eecdee1380ba4d82062d0.webp?width=406&height=406")
            await ctx.channel.send(embed=embed1)
def setup(client):
    client.add_cog(Nuke(client))