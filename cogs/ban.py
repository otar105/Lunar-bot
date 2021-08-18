import discord
import datetime
from discord.ext import commands

class Ban(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Ban Command Loaded Succesfully')

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self,ctx,user:discord.Member,*,reason="No reason provided"):
        try:
            await user.ban(reason=reason)
            embed = discord.Embed(description=f"<a:tick:859734309073715250> Successfully Banned **{user}**", color=0x00FF00)
            embed.set_author(name=f"{ctx.author}",icon_url=f"{ctx.author.avatar_url}")
            embed.set_footer(text=f"Lunar • today {datetime.datetime.now().hour}:{datetime.datetime.now().minute}",icon_url="https://images-ext-2.discordapp.net/external/F08dR3mn0Eg3YLm2mTbyd4I52Z2XSffki_g-XlUqljg/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/859504107768250379/01ac1392401eecdee1380ba4d82062d0.webp?width=406&height=406")
            await ctx.channel.send(embed=embed)
            """
            embed1 = discord.Embed(description=f"**Server:** {ctx.guild.name}
            **Actioned by:** {ctx.author.mention}
            **Action:**` Ban
            **Reason** {reason}")
            embed1.set_footer(text=f"Lunar • today {datetime.datetime.now().hour}:{datetime.datetime.now().minute}", icon_url="https://images-ext-2.discordapp.net/external/F08dR3mn0Eg3YLm2mTbyd4I52Z2XSffki_g-XlUqljg/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/859504107768250379/01ac1392401eecdee1380ba4d82062d0.webp?width=406&height=406")
            await user.send(embed=embed1)
            """
        except:
            embed = discord.Embed(description=f"<a:deny:860216874163240961> Unable to ban member.", color=0xFF0000)
            embed.set_author(name=f"{ctx.author}",icon_url=f"{ctx.author.avatar_url}")
            embed.set_footer(text=f"Lunar • today {datetime.datetime.now().hour}:{datetime.datetime.now().minute}",icon_url="https://images-ext-2.discordapp.net/external/F08dR3mn0Eg3YLm2mTbyd4I52Z2XSffki_g-XlUqljg/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/859504107768250379/01ac1392401eecdee1380ba4d82062d0.webp?width=406&height=406")
            await ctx.channel.send(embed=embed)

def setup(client):
    client.add_cog(Ban(client))