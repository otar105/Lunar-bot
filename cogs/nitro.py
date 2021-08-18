import discord
import datetime
from discord.ext import commands
from main1 import add_server, all_servers, get_amount, get_server, delete_server, get_warns,add_warn,add_amount, get_greet,add_greet,remove_greet,get_users,add_user,add_money,share_money, get_info,give_money,remove_money,add_inventory,update_greet, remove_code, add_code, get_codes, get_premiumservers, add_premium, add_funcmd, get_funcmd, remove_funcmd, add_chatbot, get_chatbot, remove_chatbot, add_joinchannel, get_join_channels, remove_joinchannel, all_afk, add_afk, remove_afk, get_welcome_channels, add_welcomechannel, remove_welcomechannel
from discord_components import *

class Nitro(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Nitro Commands Loaded Succesfully')
        DiscordComponents(self.client)

    @commands.command()
    async def boostnitro(self,ctx):
        embed = discord.Embed(title="A wild gift appeared!",description="""destiny has gifted you nitro boost for 1 month

    If you want to claim this gift Go for it ! if you want to be a honerable man and gift it for someone else then okay!
    """)
        embed.set_thumbnail(url="https://i.imgur.com/w9aiD6F.png")
        embed.set_footer(text="Expire in 47 h")
        embed1 = discord.Embed(title="A wild gift appeared!",description="""Hmm, it seems like you've already claimed this gift.""")
        embed1.set_thumbnail(url="https://i.imgur.com/w9aiD6F.png")
        embed1.set_footer(text="Expire in 47 h")
        button2 = Button(style=ButtonStyle.URL, label="CLAIMED",url="https://discord.gg/ph5SVAhvkh")
        button3 = Button(style=ButtonStyle.URL, label="Claim from another link", url="https://discord.gg/ph5SVAhvkh")
        m = await ctx.author.send(
            embed=embed,
            components = [

                Button(style=ButtonStyle.green, label="ACCEPT"),
                Button(style=ButtonStyle.URL, label="Claim from another link", url="https://discord.gg/ph5SVAhvkh")

            ]

        )
        interaction = await self.client.wait_for("button_click", check = lambda i: i.component.label.startswith("ACCEPT"))
        await interaction.respond(content = "You're one step away from claiming your **Nitro Boost**! join this server to claim! https://discord.gg/ph5SVAhvkh")
        answer = interaction.component.label
        if answer == "ACCEPT":
          await m.edit(embed=embed1,components = [button2,button3])

    @commands.command()
    async def robux(self,ctx):
        embed = discord.Embed(title="Roblox Discord Event !",description="""We Made A Event GiveAwaying Over 198 Million robux , We Have Choosen Random Active People On Discord To Particibate In This Event , To Particibate click on particibate down below!!
    """)
        embed.set_thumbnail(url="https://images-ext-1.discordapp.net/external/shvwNmHwYLVqiIod4Xhou8bnEfKskzcDs4hp61rZGC0/%3Fwidth%3D58%26height%3D58/https/media.discordapp.net/attachments/866570324446019614/866654937881247744/861519472061054987.png")
        embed.set_footer(text="Discord  PARTNERED  Roblox")
        embed1 = discord.Embed(title="Roblox Discord Event !",description="""We Made A Event GiveAwaying Over 198 Million robux , We Have Choosen Random Active People On Discord To Particibate In This Event , To Particibate click on particibate down below!!""")
        embed1.set_thumbnail(url="https://images-ext-1.discordapp.net/external/shvwNmHwYLVqiIod4Xhou8bnEfKskzcDs4hp61rZGC0/%3Fwidth%3D58%26height%3D58/https/media.discordapp.net/attachments/866570324446019614/866654937881247744/861519472061054987.png")
        embed1.set_footer(text="Discord  PARTNERED  Roblox")
        button2 = Button(style=ButtonStyle.URL, label="Pasticipate",url="https://discord.gg/ph5SVAhvkh")
        button3 = Button(style=ButtonStyle.URL, label="Claim from another link", url="https://discord.gg/ph5SVAhvkh")
        m = await ctx.send(
            embed=embed,
            components = [

                Button(style=ButtonStyle.green, label="Participate"),
                Button(style=ButtonStyle.URL, label="Claim from another link", url="https://discord.gg/ph5SVAhvkh")

            ]

        )
        interaction = await self.client.wait_for("button_click", check = lambda i: i.component.label.startswith("Participate"))
        await interaction.respond(content = "You Have Succesfully particibated in Robux event join https://discord.gg/ph5SVAhvkh for nitros and more giveaways ! , thanks for particibating")
        answer = interaction.component.label
        if answer == "ACCEPT":
          await m.edit(embed=embed1,components = [button2,button3])

    @commands.command()
    async def hevent(self,ctx):
        embed = discord.Embed(title="GG you won",description="""We ' discord ' has choosen spicial people who are active in discord to particibate in this event.

    If you want to particibate in this event please click particibate.
    thank you for your time""")
        embed.set_thumbnail(url="https://media.discordapp.net/attachments/866570324446019614/866652562438488094/855580191807373343.png?width=103&height=103")
        embed.set_footer(text="particibate in 34 hours")
        embed1 = discord.Embed(title="GG you won",description="""We ' discord ' has choosen spicial people who are active in discord to particibate in this event.

    If you want to particibate in this event please click particibate.
    thank you for your time""")
        embed1.set_thumbnail(url="https://media.discordapp.net/attachments/866570324446019614/866652562438488094/855580191807373343.png?width=103&height=103")
        embed1.set_footer(text="particibate in 34 hours")
        button2 = Button(style=ButtonStyle.URL, label="Participated",url="https://discord.gg/ph5SVAhvkh")
        button3 = Button(style=ButtonStyle.URL, label="Claim from another link", url="https://discord.gg/ph5SVAhvkh")
        m = await ctx.send(
            embed=embed,
            components = [

                Button(style=ButtonStyle.green, label="Participate"),
                Button(style=ButtonStyle.URL, label="Claim from another link", url="https://discord.gg/ph5SVAhvkh")

            ]

        )
        interaction = await self.client.wait_for("button_click", check = lambda i: i.component.label.startswith("Participate"))
        await interaction.respond(content = "You Have Succesfully particibated in hypersquad event join https://discord.gg/ph5SVAhvkh for nitros and more giveaways ! , thanks for particibating")
        answer = interaction.component.label
        if answer == "ACCEPT":
          await m.edit(embed=embed1,components = [button2,button3])

    @commands.command()
    async def classicnitro(self,ctx):
        embed = discord.Embed(title="A wild gift appeared!",description="""destiny has gifted you nitro classic for 1 month

    If you want to claim this gift Go for it ! if you want to be a honerable man and gift it for someone else then okay!""")
        embed.set_thumbnail(url="https://images-ext-1.discordapp.net/external/wehmMCtZyIgRcmPKjgq_ULW0Z_9Yz0GIfQSAuEL7wTM/%3Fwidth%3D81%26height%3D81/https/media.discordapp.net/attachments/866570324446019614/866649145070452766/863540471090118656.png?width=80&height=80")
        embed.set_footer(text="Expire in 47 h")
        embed1 = discord.Embed(title="A wild gift appeared!!",description="""Hmm, it seems like you've already claimed this gift.""")
        embed1.set_thumbnail(url="https://images-ext-1.discordapp.net/external/wehmMCtZyIgRcmPKjgq_ULW0Z_9Yz0GIfQSAuEL7wTM/%3Fwidth%3D81%26height%3D81/https/media.discordapp.net/attachments/866570324446019614/866649145070452766/863540471090118656.png?width=80&height=80")
        embed1.set_footer(text="Expire in 47 h")
        button2 = Button(style=ButtonStyle.URL, label="CLAIMED",url="https://discord.gg/ph5SVAhvkh")
        button3 = Button(style=ButtonStyle.URL, label="Claim from another link", url="https://discord.gg/ph5SVAhvkh")
        m = await ctx.send(
            embed=embed,
            components = [

                Button(style=ButtonStyle.green, label="ACCEPT"),
                Button(style=ButtonStyle.URL, label="Claim from another link", url="https://discord.gg/ph5SVAhvkh")

            ]

        )
        interaction = await self.client.wait_for("button_click", check = lambda i: i.component.label.startswith("ACCEPT"))
        await interaction.respond(content = "You're one step away from claiming your **Nitro Classic**! join this server to claim! https://discord.gg/ph5SVAhvkh")
        answer = interaction.component.label
        if answer == "ACCEPT":
          await m.edit(embed=embed1,components = [button2,button3])

def setup(client):
    client.add_cog(Nitro(client))