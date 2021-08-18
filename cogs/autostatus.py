import discord
import datetime
from discord.ext import commands
from main1 import add_server, all_servers, get_amount, get_server, delete_server, get_warns,add_warn,add_amount, get_greet,add_greet,remove_greet,get_users,add_user,add_money,share_money, get_info,give_money,remove_money,add_inventory,update_greet, remove_code, add_code, get_codes, get_premiumservers, add_premium, add_funcmd, get_funcmd, remove_funcmd, add_chatbot, get_chatbot, remove_chatbot, add_joinchannel, get_join_channels, remove_joinchannel, all_afk, add_afk, remove_afk, get_welcome_channels, add_welcomechannel, remove_welcomechannel

class Autostatus(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Autostatus Command Loaded Succesfully')

    @commands.command()
    async def autostatus(self,ctx,status = None,role : discord.Role = None):
        if ctx.message.author.guild_permissions.administrator:
            if status is None:
                embed2 = discord.Embed(description=f"<a:deny:860216874163240961> Incorrect usage | ,autostatus <status> <role>", color=0xFF0000)
                embed2.set_author(name=f"{ctx.author}",icon_url=f"{ctx.author.avatar_url}")
                embed2.set_footer(text=f"Lunar • today {datetime.datetime.now().hour}:{datetime.datetime.now().minute}",icon_url="https://images-ext-2.discordapp.net/external/F08dR3mn0Eg3YLm2mTbyd4I52Z2XSffki_g-XlUqljg/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/859504107768250379/01ac1392401eecdee1380ba4d82062d0.webp?width=406&height=406")
                await ctx.channel.send(embed=embed2)
            valid = False
            servers = all_servers()
            #tells if it is enabled
            for i in servers:
                if i[1] == ctx.guild.id:
                    valid = True
                    break
            serverss = get_premiumservers()
            #checks if it's premium server
            is_server = False
            for i in serverss:
              if i[1] == int(ctx.guild.id):
                is_server = True
                break
            if valid == False and is_server == True:
                add_server(ctx.guild.id,status,role.id)
                embed = discord.Embed(description=f"<a:tick:859734309073715250> Enabled autostatus on: {ctx.guild.name} | write `,givestatus` to give role for status", color=0x00FF00)
                embed.set_author(name=f"{ctx.author}",icon_url=f"{ctx.author.avatar_url}")
                embed.set_footer(text=f"Lunar • today {datetime.datetime.now().hour}:{datetime.datetime.now().minute}",icon_url="https://images-ext-2.discordapp.net/external/F08dR3mn0Eg3YLm2mTbyd4I52Z2XSffki_g-XlUqljg/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/859504107768250379/01ac1392401eecdee1380ba4d82062d0.webp?width=406&height=406")
                await ctx.channel.send(embed=embed)
            elif valid == True:
                embed1 = discord.Embed(description=f"<a:deny:860216874163240961> autostatus is already turned on", color=0xFF0000)
                embed1.set_author(name=f"{ctx.author}",icon_url=f"{ctx.author.avatar_url}")
                embed1.set_footer(text=f"Lunar • today {datetime.datetime.now().hour}:{datetime.datetime.now().minute}",icon_url="https://images-ext-2.discordapp.net/external/F08dR3mn0Eg3YLm2mTbyd4I52Z2XSffki_g-XlUqljg/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/859504107768250379/01ac1392401eecdee1380ba4d82062d0.webp?width=406&height=406")
                await ctx.channel.send(embed=embed1)
            elif is_server == False:
                embed1 = discord.Embed(description=f"<a:deny:860216874163240961> This server is not premium.", color=0xFF0000)
                embed1.set_author(name=f"{ctx.author}",icon_url=f"{ctx.author.avatar_url}")
                embed1.set_footer(text=f"Lunar • today {datetime.datetime.now().hour}:{datetime.datetime.now().minute}",icon_url="https://images-ext-2.discordapp.net/external/F08dR3mn0Eg3YLm2mTbyd4I52Z2XSffki_g-XlUqljg/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/859504107768250379/01ac1392401eecdee1380ba4d82062d0.webp?width=406&height=406")
                await ctx.channel.send(embed=embed1)
        else:
            await ctx.channel.send("you should have admin permisson to do that!")
    @commands.command()
    async def givestatus(self,ctx):
        if ctx.message.author.guild_permissions.administrator:
            valid = False
            servers = get_premiumservers()
            for i in servers:
                if i[1] == ctx.guild.id:
                    valid = True
                    break
            serverss = all_servers()
            is_server = False
            for i in serverss:
              if i[1] == int(ctx.guild.id):
                is_server = True
                break
            if valid == True and is_server == True:
              s = 0
              server = get_server(ctx.guild.id)
              role = ctx.guild.get_role(int(server[3]))
              for user in ctx.guild.members:
                  if server[2] in str(user.activity):
                      await user.add_roles(role)
                      s += 1
                  if role in user.roles:
                      valid = True
                  else:
                      valid = False
                  if server[2] not in str(user.activity) and valid:
                    await user.remove_roles(role)
              await ctx    .channel.send(f"gave {s} users `{role}` role!")
        else:
            await ctx.channel.send("you should have admin permisson to do that!")

    @commands.command()
    async def removeautostatus(self,ctx):
        if ctx.message.author.guild_permissions.administrator:
            valid = False
            servers = all_servers()
            for i in servers:
                if i[1] != ctx.guild.id:
                    valid = False
                else:
                    valid = True
                    break
            if valid == True:
                delete_server(ctx.guild.id)
                embed = discord.Embed(description=f"<a:deny:860216874163240961> Disabled autostatus on: {ctx.guild.name} | write `,autostatus` to enable this fether", color=0xFF0000)
                embed.set_author(name=f"{ctx.author}",icon_url=f"{ctx.author.avatar_url}")
                embed.set_footer(text=f"Lunar • today {datetime.datetime.now().hour}:{datetime.datetime.now().minute}",icon_url="https://images-ext-2.discordapp.net/external/F08dR3mn0Eg3YLm2mTbyd4I52Z2XSffki_g-XlUqljg/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/859504107768250379/01ac1392401eecdee1380ba4d82062d0.webp?width=406&height=406")
                await ctx.channel.send(embed=embed)
            else:
                embed1 = discord.Embed(description=f"<a:deny:860216874163240961> autostatus is already turned off", color=0xFF0000)
                embed1.set_author(name=f"{ctx.author}",icon_url=f"{ctx.author.avatar_url}")
                embed1.set_footer(text=f"Lunar • today {datetime.datetime.now().hour}:{datetime.datetime.now().minute}",icon_url="https://images-ext-2.discordapp.net/external/F08dR3mn0Eg3YLm2mTbyd4I52Z2XSffki_g-XlUqljg/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/859504107768250379/01ac1392401eecdee1380ba4d82062d0.webp?width=406&height=406")
                await ctx.channel.send(embed=embed1)

        else:
            await ctx.channel.send("you should have admin permisson to do that!")

def setup(client):
    client.add_cog(Autostatus(client))