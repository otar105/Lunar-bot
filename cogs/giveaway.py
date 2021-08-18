import discord
import datetime
from discord.ext import commands
from main1 import add_server, all_servers, get_amount, get_server, delete_server, get_warns,add_warn,add_amount, get_greet,add_greet,remove_greet,get_users,add_user,add_money,share_money, get_info,give_money,remove_money,add_inventory,update_greet, remove_code, add_code, get_codes, get_premiumservers, add_premium, add_funcmd, get_funcmd, remove_funcmd, add_chatbot, get_chatbot, remove_chatbot, add_joinchannel, get_join_channels, remove_joinchannel, all_afk, add_afk, remove_afk, get_welcome_channels, add_welcomechannel, remove_welcomechannel
import random
import asyncio

def ConvertSectoDay(n):

    day = n // (24 * 3600)

    n = n % (24 * 3600)
    hour = n // 3600

    n %= 3600
    minutes = n // 60

    n %= 60
    seconds = n

    return (day,"days", hour, "hours",
          minutes, "minutes",
          seconds, "seconds")

class Giveaway(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Giveaway Command Loaded Succesfully')

    @commands.command()
    async def gstart(self,ctx, time=None, winners = None, *, prize=None):
        has_role = False
        has_role1 = False
        role = discord.utils.find(lambda r: r.name == 'Giveaways', ctx.message.guild.roles)
        role = discord.utils.find(lambda r: r.name == 'giveaways', ctx.message.guild.roles)
        if role in ctx.author.roles:
            has_role = True
        if has_role1 in ctx.author.roles:
            has_role1 = True
        if ctx.author.guild_permissions.manage_channels or has_role == True or has_role1 == True:
            if time == None:
                return await ctx.channel.send("Please include a time!")
            elif prize == None:
                return await ctx.channel.send("Please unclude a prize!")
            time_converter = {"s":1, "m":60, "h":3600, "d":86400}
            t = time
            t = t.replace(f"{time[-1]}","")
            t = int(t)
            gawtime = int(t) * time_converter[time[-1]]
            await ctx.message.delete()
            w = gawtime
            ti = ConvertSectoDay(w)
            listx = list(ti)
            f = ""
            for i in listx:
                f += str(i) + " "
            embed = discord.Embed(
                    title="<a:giveaway_2:860953092274257921> New Giveaway! <a:giveaway_2:860953092274257921>",
                    description=f"**Prize:** {prize}\n"
                                f"**Hosted By:** {ctx.author.mention}\n"
                                f"**Ends In:** {f}\n\n"
                                f"**__Giveaway Winners__**\n"
                                "Not Decided.\n\n"
                                "[Upvote me for 35% Good luck](https://top.gg/bot/859504107768250379/vote) • [Invite me](https://discord.com/oauth2/authorize?client_id=841561994590289950&scope=bot%20applications.commands&permissions=8589934591)",
                    colour=discord.Color.green()
                )
            winners = winners.replace(f"{winners[-1]}","")
            winners = int(winners)
            embed.set_footer(text=f"{winners} winner(s)!",icon_url="https://images-ext-2.discordapp.net/external/F08dR3mn0Eg3YLm2mTbyd4I52Z2XSffki_g-XlUqljg/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/859504107768250379/01ac1392401eecdee1380ba4d82062d0.webp?width=406&height=406")
            gaw_msg = await ctx.channel.send(embed=embed)
            await gaw_msg.add_reaction("🎉")
            while w:
                await asyncio.sleep(10)
                w -= 10
                ti = ConvertSectoDay(w)
                f = ""
                listx = list(ti)
                for i in listx:
                    f += str(i) + " "
                embed.description= f"**Prize:** {prize}\n**Hosted By:** {ctx.author.mention}\n**Ends In:** {f}\n\n**__Giveaway Winners__**\nNot Decided.\n\n[Upvote me for 35% Good luck](https://top.gg/bot/859504107768250379/vote) • [Invite me](https://discord.com/oauth2/authorize?client_id=859504107768250379&scope=bot%20applications.commands&permissions=8589934591)"
                await gaw_msg.edit(embed=embed)
            new_gaw_msg = await ctx.channel.fetch_message(gaw_msg.id)
            users = await new_gaw_msg.reactions[0].users().flatten()
            if winners > 1:
                winner = random.choices(users, k=winners)
            else:
                winner = random.choice(users)
            embed.description= f"**Prize:** {prize}\n**Hosted By:** {ctx.author.mention}\n**Ends In:** {f}\n**__Giveaway Winners__**\n{winner.mention}."
            await gaw_msg.edit(embed=embed)
            await ctx.channel.send(f"<a:won:860433297992974346> **Giveaway Winner: {winner.mention} | Prize: {prize}**")
        else:
            embed1 = discord.Embed(description=f"<a:deny:860216874163240961>  you have insufficient permissions to execute this command.", color=0xFF0000)
            embed1.set_author(name=f"{ctx.author}",icon_url=f"{ctx.author.avatar_url}")
            embed1.add_field(name="**Missing permission(s)**",value="Manage Channels | Giveaways Roles")
            embed1.set_footer(text=f"Lunar • today {datetime.datetime.now().hour}:{datetime.datetime.now().minute}",icon_url="https://images-ext-2.discordapp.net/external/F08dR3mn0Eg3YLm2mTbyd4I52Z2XSffki_g-XlUqljg/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/859504107768250379/01ac1392401eecdee1380ba4d82062d0.webp?width=406&height=406")
            await ctx.channel.send(embed=embed1)

    @commands.command()
    @commands.has_permissions(manage_channels=True)
    async def greroll(self,ctx, id_ = None):
        has_role = False
        role = discord.utils.find(lambda r: r.name == 'Giveaways', ctx.message.guild.roles)
        if role in ctx.author.roles:
            has_role = True
        if ctx.author.guild_permissions.manage_channels or has_role == True:
            if id_ == None:
                await ctx.channel.send("please enter giveaway id.")
            else:
                id_ = int(id_)
            try:
                new_msg = await ctx.channel.fetch_message(id_)
            except:
                await ctx.channel.send("The id was enterd incorrectly.")
                return
            users = await new_msg.reactions[0].users().flatten()
            users.pop(users.index(self.client.user))

            winner = random.choice(users)
            await ctx.channel.send(f"<a:won:860433297992974346> **New giveaway Winner: {winner.mention}**")
        else:
            embed1 = discord.Embed(description=f"<a:deny:860216874163240961>  you have insufficient permissions to execute this command.", color=0xFF0000)
            embed1.set_author(name=f"{ctx.author}",icon_url=f"{ctx.author.avatar_url}")
            embed1.add_field(name="**Missing permission(s)**",value="Manage Channels | Giveaways Roles")
            embed1.set_footer(text=f"Lunar • today {datetime.datetime.now().hour}:{datetime.datetime.now().minute}",icon_url="https://images-ext-2.discordapp.net/external/F08dR3mn0Eg3YLm2mTbyd4I52Z2XSffki_g-XlUqljg/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/859504107768250379/01ac1392401eecdee1380ba4d82062d0.webp?width=406&height=406")
            await ctx.channel.send(embed=embed1)

    @commands.command()
    @commands.has_permissions(manage_channels=True)
    async def gend(self,ctx, id_ = None):
        has_role = False
        role = discord.utils.find(lambda r: r.name == 'Giveaways',ctx.message.guild.roles)
        if role in ctx.author.roles:
            has_role = True
        if ctx.author.guild_permissions.manage_channels or has_role == True:
            if id_ == None:
                await ctx.channel.send("please enter giveaway id.")
            else:
                id_ = int(id_)
            try:
                new_msg = await ctx.channel.fetch_message(id_)
            except:
                await ctx.channel.send("The id was enterd incorrectly.")
                return
            users = await new_msg.reactions[0].users().flatten()
            users.pop(users.index(self.client.user))
            winner = random.choice(users)
            await ctx.channel.send(f"<a:won:860433297992974346> **Giveaway Winner:** {winner.mention}")
        else:
            embed1 = discord.Embed(description=f"<a:deny:860216874163240961>  you have insufficient permissions to execute this command.", color=0xFF0000)
            embed1.set_author(name=f"{ctx.author}",icon_url=f"{ctx.author.avatar_url}")
            embed1.add_field(name="**Missing permission(s)**",value="Manage Channels | Giveaways Roles")
            embed1.set_footer(text=f"Lunar • today {datetime.datetime.now().hour}:{datetime.datetime.now().minute}",icon_url="https://images-ext-2.discordapp.net/external/F08dR3mn0Eg3YLm2mTbyd4I52Z2XSffki_g-XlUqljg/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/859504107768250379/01ac1392401eecdee1380ba4d82062d0.webp?width=406&height=406")
            await ctx.channel.send(embed=embed1)

def setup(client):
    client.add_cog(Giveaway(client))