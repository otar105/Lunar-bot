import discord
import datetime
from discord.ext import commands
from main1 import add_server, all_servers, get_amount, get_server, delete_server, get_warns,add_warn,add_amount, get_greet,add_greet,remove_greet,get_users,add_user,add_money,share_money, get_info,give_money,remove_money,add_inventory,update_greet, remove_code, add_code, get_codes, get_premiumservers, add_premium, add_funcmd, get_funcmd, remove_funcmd, add_chatbot, get_chatbot, remove_chatbot, add_joinchannel, get_join_channels, remove_joinchannel, all_afk, add_afk, remove_afk, get_welcome_channels, add_welcomechannel, remove_welcomechannel

class Redeem(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Redeem Command Loaded Succesfully')

    @commands.command(pass_context = True , aliases=['claim'])
    async def redeem(self,ctx, code):
        servers = get_premiumservers()
        is_server = False
        for i in servers:
          if i[1] == int(ctx.guild.id):
            is_server = True
            break
        codes = get_codes()
        valid = False
        if is_server == False:
            for i in codes:
              if str(i[1]) == str(code):
                remove_code(str(code))
                add_premium(int(ctx.guild.id))
                embed = discord.Embed(description=f"<a:tick:859734309073715250> Enabled premium on: {ctx.guild.name}", color=0x00FF00)
                embed.set_author(name=f"{ctx.author}",icon_url=f"{ctx.author.avatar_url}")
                embed.set_footer(text=f"Lunar • today {datetime.datetime.now().hour}:{datetime.datetime.now().minute}",icon_url="https://images-ext-2.discordapp.net/external/F08dR3mn0Eg3YLm2mTbyd4I52Z2XSffki_g-XlUqljg/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/859504107768250379/01ac1392401eecdee1380ba4d82062d0.webp?width=406&height=406")
                await ctx.channel.send(embed=embed)
                valid = True
            if valid == False:
              embed = discord.Embed(description=f"<a:deny:860216874163240961> Unknown code.", color=0xFF0000)
              embed.set_author(name=f"{ctx.author}",icon_url=f"{ctx.author.avatar_url}")
              embed.set_footer(text=f"Lunar • today {datetime.datetime.now().hour}:{datetime.datetime.now().minute}",icon_url="https://images-ext-2.discordapp.net/external/F08dR3mn0Eg3YLm2mTbyd4I52Z2XSffki_g-XlUqljg/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/859504107768250379/01ac1392401eecdee1380ba4d82062d0.webp?width=406&height=406")
              await ctx.channel.send(embed=embed)
        else:
            embed = discord.Embed(description=f"<a:deny:860216874163240961> This server already has premium.", color=0xFF0000)
            embed.set_author(name=f"{ctx.author}",icon_url=f"{ctx.author.avatar_url}")
            embed.set_footer(text=f"Lunar • today {datetime.datetime.now().hour}:{datetime.datetime.now().minute}",icon_url="https://images-ext-2.discordapp.net/external/F08dR3mn0Eg3YLm2mTbyd4I52Z2XSffki_g-XlUqljg/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/859504107768250379/01ac1392401eecdee1380ba4d82062d0.webp?width=406&height=406")
            await ctx.channel.send(embed=embed)
def setup(client):
    client.add_cog(Redeem(client))