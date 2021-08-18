import discord
import datetime
from discord.ext import commands
from main1 import add_server, all_servers, get_amount, get_server, delete_server, get_warns,add_warn,add_amount, get_greet,add_greet,remove_greet,get_users,add_user,add_money,share_money, get_info,give_money,remove_money,add_inventory,update_greet, remove_code, add_code, get_codes, get_premiumservers, add_premium, add_funcmd, get_funcmd, remove_funcmd, add_chatbot, get_chatbot, remove_chatbot, add_joinchannel, get_join_channels, remove_joinchannel, all_afk, add_afk, remove_afk, get_welcome_channels, add_welcomechannel, remove_welcomechannel

class Mute(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Mute Command Loaded Succesfully')

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def mute(self,ctx, member: discord.Member, *, reason="No reason provided"):
        guild = ctx.guild
        mutedRole = discord.utils.get(guild.roles, name="Luner mute")

        if not mutedRole:
            mutedRole = await guild.create_role(name="Lunar mute")

            for channel in guild.channels:
                await channel.set_permissions(mutedRole, speak=False, send_messages=False, read_message_history=True, read_messages=False)
        valid = False
        warns = get_warns()
        for i in warns:
            if i[1] == ctx.guild.id:
                valid = True
                break
            else:
                valid = False
        if valid == False:
            add_warn(ctx.guild.id)
            embed = discord.Embed(description=f"""**Server:** {ctx.guild.name}
            **Actioned by:** {ctx.author.mention}
            **Action:** Warn
            **Reason** {reason}""")
            embed.set_footer(text=f"Case #1•today {datetime.datetime.now().hour}:{datetime.datetime.now().minute}", icon_url="https://images-ext-2.discordapp.net/external/F08dR3mn0Eg3YLm2mTbyd4I52Z2XSffki_g-XlUqljg/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/859504107768250379/01ac1392401eecdee1380ba4d82062d0.webp?width=406&height=406")
            await member.send(embed=embed)
            await ctx.channel.send(f"<a:wtf_pepe:859732800378634270> `Case #1` {member.mention} has been muted.")
        else:
            add_amount(ctx.guild.id)
            amount = get_amount(ctx.guild.id)
            embed = discord.Embed(description=f"""**Server:** {ctx.guild.name}
            **Actioned by:** {ctx.author.mention}
            **Action:** Warn
            **Reason** {reason}""")
            embed.set_footer(text=f"Case #{amount}•today {datetime.datetime.now().hour}:{datetime.datetime.now().minute}",icon_url="https://images-ext-2.discordapp.net/external/F08dR3mn0Eg3YLm2mTbyd4I52Z2XSffki_g-XlUqljg/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/859504107768250379/01ac1392401eecdee1380ba4d82062d0.webp?width=406&height=406")
            await member.send(embed=embed)
            await ctx.channel.send(f"<a:wtf_pepe:859732800378634270> `Case #{amount}` {member.mention} has been muted.")
        await member.add_roles(mutedRole, reason=reason)
    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def unmute(self,ctx, member: discord.Member):
        try:
            mutedRole = discord.utils.get(ctx.guild.roles, name="Lunar mute")
            await member.remove_roles(mutedRole)
            await member.send(f" you have unmutedd from: - {ctx.guild.name}")
            embed = discord.Embed(description=f"<a:deny:860216874163240961> Unmuted {member.mention}", color=0xFF0000)
            embed.set_author(name=f"{ctx.author}",icon_url=f"{ctx.author.avatar_url}")
            embed.set_footer(text=f"Lunar • today {datetime.datetime.now().hour}:{datetime.datetime.now().minute}",icon_url="https://images-ext-2.discordapp.net/external/F08dR3mn0Eg3YLm2mTbyd4I52Z2XSffki_g-XlUqljg/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/859504107768250379/01ac1392401eecdee1380ba4d82062d0.webp?width=406&height=406")
            await ctx.channel.send(embed=embed)
        except:
            embed1 = discord.Embed(description=f"<a:deny:860216874163240961>  I have insufficient permissions to execute this command.", color=0xFF0000)
            embed1.set_author(name=f"{ctx.author}",icon_url=f"{ctx.author.avatar_url}")
            embed1.add_field(name="**Missing permission(s)**",value="Manage Roles")
            embed1.set_footer(text=f"Lunar • today {datetime.datetime.now().hour}:{datetime.datetime.now().minute}",icon_url="https://images-ext-2.discordapp.net/external/F08dR3mn0Eg3YLm2mTbyd4I52Z2XSffki_g-XlUqljg/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/859504107768250379/01ac1392401eecdee1380ba4d82062d0.webp?width=406&height=406")
            await ctx.channel.send(embed=embed1)
def setup(client):
    client.add_cog(Mute(client))