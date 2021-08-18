import discord
import datetime
from discord.ext import commands
from main1 import add_server, all_servers, get_amount, get_server, delete_server, get_warns,add_warn,add_amount, get_greet,add_greet,remove_greet,get_users,add_user,add_money,share_money, get_info,give_money,remove_money,add_inventory,update_greet, remove_code, add_code, get_codes, get_premiumservers, add_premium, add_funcmd, get_funcmd, remove_funcmd, add_chatbot, get_chatbot, remove_chatbot, add_joinchannel, get_join_channels, remove_joinchannel, all_afk, add_afk, remove_afk, get_welcome_channels, add_welcomechannel, remove_welcomechannel

class Greet(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Greet Command Loaded Succesfully')

    @commands.command()
    async def greet(self,ctx):
        if ctx.author.guild_permissions.manage_channels:
            servers = get_greet()
            valid = False
            try:
                for i in servers:
                    if i[2] == ctx.channel.id:
                        remove_greet(ctx.channel.id)
                        embed = discord.Embed(description=f"<a:deny:860216874163240961> Disabled greet announcement on: {ctx.channel.mention}", color=0xFF0000)
                        embed.set_author(name=f"{ctx.author}",icon_url=f"{ctx.author.avatar_url}")
                        embed.set_footer(text=f"Lunar • today {datetime.datetime.now().hour}:{datetime.datetime.now().minute}",icon_url="https://images-ext-2.discordapp.net/external/F08dR3mn0Eg3YLm2mTbyd4I52Z2XSffki_g-XlUqljg/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/859504107768250379/01ac1392401eecdee1380ba4d82062d0.webp?width=406&height=406")
                        await ctx.channel.send(embed=embed)
                        valid = True
                        break
            except:
                valid=False
            if valid == False:
                add_greet(ctx.guild.id,ctx.channel.id)
                embed = discord.Embed(description=f"<a:tick:859734309073715250> Enabled greet announcement on: {ctx.channel.mention}", color=0x00FF00)
                embed.set_author(name=f"{ctx.author}",icon_url=f"{ctx.author.avatar_url}")
                embed.set_footer(text=f"Lunar • today {datetime.datetime.now().hour}:{datetime.datetime.now().minute}",icon_url="https://images-ext-2.discordapp.net/external/F08dR3mn0Eg3YLm2mTbyd4I52Z2XSffki_g-XlUqljg/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/859504107768250379/01ac1392401eecdee1380ba4d82062d0.webp?width=406&height=406")
                await ctx.channel.send(embed=embed)
        else:
            embed1 = discord.Embed(description=f"<a:deny:860216874163240961>  you have insufficient permissions to execute this command.", color=0xFF0000)
            embed1.set_author(name=f"{ctx.author}",icon_url=f"{ctx.author.avatar_url}")
            embed1.add_field(name="**Missing permission(s)**",value="Manage Channels")
            embed1.set_footer(text=f"Lunar • today {datetime.datetime.now().hour}:{datetime.datetime.now().minute}",icon_url="https://images-ext-2.discordapp.net/external/F08dR3mn0Eg3YLm2mTbyd4I52Z2XSffki_g-XlUqljg/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/859504107768250379/01ac1392401eecdee1380ba4d82062d0.webp?width=406&height=406")
            await ctx.channel.send(embed=embed1)
    @commands.command()
    async def greetdel(self,ctx,amount):
        if ctx.author.guild_permissions.manage_channels:
            servers = get_greet()
            valid = False
            try:
                for i in servers:
                    if i[2] == ctx.channel.id:
                        if int(amount)>0:
                            update_greet(ctx.channel.id,int(amount))
                            embed = discord.Embed(description=f"<a:tick:859734309073715250> Seted greet announcement on: {amount}s", color=0x00FF00)
                            embed.set_author(name=f"{ctx.author}",icon_url=f"{ctx.author.avatar_url}")
                            embed.set_footer(text=f"Lunar • today {datetime.datetime.now().hour}:{datetime.datetime.now().minute}",icon_url="https://images-ext-2.discordapp.net/external/F08dR3mn0Eg3YLm2mTbyd4I52Z2XSffki_g-XlUqljg/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/859504107768250379/01ac1392401eecdee1380ba4d82062d0.webp?width=406&height=406")
                            await ctx.channel.send(embed=embed)
                            valid = True
                            break
                        else:
                            embed1 = discord.Embed(title="That's not a valid number",description="<a:deny:860216874163240961> Thats not a number you can use the help <command> for info on the command")
                            embed1.set_author(name=f"{ctx.author}",icon_url=f"{ctx.author.avatar_url}")
                            embed1.set_footer(text=f"Lunar • today {datetime.datetime.now().hour}:{datetime.datetime.now().minute}",icon_url="https://images-ext-2.discordapp.net/external/F08dR3mn0Eg3YLm2mTbyd4I52Z2XSffki_g-XlUqljg/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/859504107768250379/01ac1392401eecdee1380ba4d82062d0.webp?width=406&height=406")
                            await ctx.channel.send(embed=embed1)
                            valid = True
                            break
            except:
                valid=False
            if valid == False:
                embed = discord.Embed(description=f"<a:deny:860216874163240961> Greet command is not enabled on this channel", color=0xFF0000)
                embed.set_author(name=f"{ctx.author}",icon_url=f"{ctx.author.avatar_url}")
                embed.set_footer(text=f"Lunar • today {datetime.datetime.now().hour}:{datetime.datetime.now().minute}",icon_url="https://images-ext-2.discordapp.net/external/F08dR3mn0Eg3YLm2mTbyd4I52Z2XSffki_g-XlUqljg/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/859504107768250379/01ac1392401eecdee1380ba4d82062d0.webp?width=406&height=406")
                await ctx.channel.send(embed=embed)
def setup(client):
    client.add_cog(Greet(client))