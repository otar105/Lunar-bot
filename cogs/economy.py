import discord
import datetime
from discord.ext import commands
import random
from main1 import add_server, all_servers, get_amount, get_server, delete_server, get_warns,add_warn,add_amount, get_greet,add_greet,remove_greet,get_users,add_user,add_money,share_money, get_info,give_money,remove_money,add_inventory,update_greet, remove_code, add_code, get_codes, get_premiumservers, add_premium, add_funcmd, get_funcmd, remove_funcmd, add_chatbot, get_chatbot, remove_chatbot, add_joinchannel, get_join_channels, remove_joinchannel, all_afk, add_afk, remove_afk, get_welcome_channels, add_welcomechannel, remove_welcomechannel

class Economy(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Economy Command Loaded Succesfully')

    @commands.command()
    @commands.cooldown(1, 30, commands.BucketType.user)
    async def beg(self,ctx):
        users = get_users()
        money = random.randint(100,1000)
        is_done = False
        for i in users:
            if i[1] == ctx.author.id:
                add_money(ctx.author.id,money)
                embed = discord.Embed(color=0xFF0000)
                embed.set_author(name=f"Lunar Bot Economy",url="")
                embed.add_field(name="Begging!",value=f"**Broken Tooth** Donated <:bitcoin:861527497178480651> {money} to {ctx.author.mention}")
                embed.set_footer(text=f"Lunar • today {datetime.datetime.now().hour}:{datetime.datetime.now().minute}",icon_url="https://images-ext-2.discordapp.net/external/F08dR3mn0Eg3YLm2mTbyd4I52Z2XSffki_g-XlUqljg/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/859504107768250379/01ac1392401eecdee1380ba4d82062d0.webp?width=406&height=406")
                await ctx.channel.send(embed=embed)
                is_done = True
                break
        if is_done == False:
            add_user(ctx.author.id)
            add_money(ctx.author.id,money)
            embed = discord.Embed(color=0xFF0000)
            embed.set_author(name=f"Lunar Bot Economy",url="")
            embed.add_field(name="Begging!",value=f"**Broken Tooth** Donated <:bitcoin:861527497178480651> {money} to {ctx.author.mention}")
            embed.set_footer(text=f"Lunar • today {datetime.datetime.now().hour}:{datetime.datetime.now().minute}",icon_url="https://images-ext-2.discordapp.net/external/F08dR3mn0Eg3YLm2mTbyd4I52Z2XSffki_g-XlUqljg/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/859504107768250379/01ac1392401eecdee1380ba4d82062d0.webp?width=406&height=406")
            await ctx.channel.send(embed=embed)

    @commands.command(pass_context = True , aliases=['give'])
    async def share(self,ctx,user : discord.Member, money):
        users = get_users()
        is_done = False
        for i in users:
            if i[1] == user.id:
                is_done = True
        if is_done == False:
            add_user(user.id)
            is_done = True
        #if is_done1 and i[2] >= money and is_done:
        userf = get_info(int(ctx.author.id))
        if userf[2] > int(money):
            share_money(int(ctx.author.id),int(user.id),int(money))
            embed = discord.Embed(color=0xFF0000)
            embed.set_author(name=f"Lunar Bot Economy",url="")
            embed.add_field(name="<a:waiting:861571631885451314> Sharing!",value=f"You shared <:bitcoin:861527497178480651> {money} coins to {user.mention}")
            embed.set_footer(text=f"Lunar • today {datetime.datetime.now().hour}:{datetime.datetime.now().minute}",icon_url="https://images-ext-2.discordapp.net/external/F08dR3mn0Eg3YLm2mTbyd4I52Z2XSffki_g-XlUqljg/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/859504107768250379/01ac1392401eecdee1380ba4d82062d0.webp?width=406&height=406")
            await ctx.channel.send(embed=embed)
        else:
            ctx.send(f"{ctx.author.mention}, You have insufficient balance!")

    @commands.command()
    async def devgive(self,ctx,user : discord.Member, money):
        if ctx.author.id == 792063761474394133:
            users = get_users()
            is_done = False
            for i in users:
                if i[1] == user.id:
                    is_done = True
            if is_done == False:
                add_user(user.id)
                is_done = True
            #if is_done1 and i[2] >= money and is_done:
            give_money(int(user.id),int(money))
            embed = discord.Embed(color=0xFF0000)
            embed.set_author(name=f"Lunar Bot Economy",url="")
            embed.add_field(name="Sharing!",value=f"You gave <:bitcoin:861527497178480651> {money} coins to {user.mention}")
            embed.set_footer(text=f"Lunar • today {datetime.datetime.now().hour}:{datetime.datetime.now().minute}",icon_url="https://images-ext-2.discordapp.net/external/F08dR3mn0Eg3YLm2mTbyd4I52Z2XSffki_g-XlUqljg/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/859504107768250379/01ac1392401eecdee1380ba4d82062d0.webp?width=406&height=406")
            await ctx.channel.send(embed=embed)

    @commands.command()
    @commands.cooldown(1, 86400, commands.BucketType.user)
    async def daily(self,ctx):
        users = get_users()
        is_done = False
        for i in users:
            if i[1] == ctx.author.id:
                add_money(ctx.author.id,5000)
                embed = discord.Embed(color=0xFF0000)
                embed.set_author(name=f"Lunar Bot Economy",url="")
                embed.add_field(name="Daily Reward",value=f"You got <:bitcoin:861527497178480651> **5000**")
                embed.set_footer(text=f"Lunar • today {datetime.datetime.now().hour}:{datetime.datetime.now().minute}",icon_url="https://images-ext-2.discordapp.net/external/F08dR3mn0Eg3YLm2mTbyd4I52Z2XSffki_g-XlUqljg/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/859504107768250379/01ac1392401eecdee1380ba4d82062d0.webp?width=406&height=406")
                await ctx.channel.send(embed=embed)
                is_done = True
                break
        if is_done == False:
            add_user(ctx.author.id)
            add_money(ctx.author.id,5000)
            embed = discord.Embed(color=0xFF0000)
            embed.set_author(name=f"Lunar Bot Economy",url="")
            embed.add_field(name="Daily Reward",value=f"You got <:bitcoin:861527497178480651> **5000**")
            embed.set_footer(text=f"Lunar • today {datetime.datetime.now().hour}:{datetime.datetime.now().minute}",icon_url="https://images-ext-2.discordapp.net/external/F08dR3mn0Eg3YLm2mTbyd4I52Z2XSffki_g-XlUqljg/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/859504107768250379/01ac1392401eecdee1380ba4d82062d0.webp?width=406&height=406")
            await ctx.channel.send(embed=embed)

    @commands.command(pass_context = True)
    @commands.cooldown(1, 30, commands.BucketType.user)
    async def bet(self,ctx, amount=None):
        if str(amount) == None:
            embed2 = discord.Embed(color=0xFF0000)
            embed2.set_author(name=f"Lunar Bot Economy",url="")
            embed2.add_field(name="Usage",value=f",bet <amount>")
            embed2.set_footer(text=f"Lunar • today {datetime.datetime.now().hour}:{datetime.datetime.now().minute}",icon_url="https://images-ext-2.discordapp.net/external/F08dR3mn0Eg3YLm2mTbyd4I52Z2XSffki_g-XlUqljg/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/859504107768250379/01ac1392401eecdee1380ba4d82062d0.webp?width=406&height=406")
            await ctx.channel.send(embed=embed2)
        else:
            users = get_users()
            is_done = False
            listx = ["lose","win"]
            result = random.choice(listx)
            for i in users:
                if i[1] == ctx.author.id and int(i[2]) > int(amount):
                    if result == "lose":
                        remove_money(ctx.author.id,int(amount))
                        embed = discord.Embed(color=0xFF0000)
                        embed.set_author(name=f"Lunar Bot Economy",url="")
                        embed.add_field(name="You Lost!",value=f":cry: Awww.. you lost the bet <:bitcoin:861527497178480651> **{amount}**")
                        embed.set_footer(text=f"Lunar • today {datetime.datetime.now().hour}:{datetime.datetime.now().minute}",icon_url="https://images-ext-2.discordapp.net/external/F08dR3mn0Eg3YLm2mTbyd4I52Z2XSffki_g-XlUqljg/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/859504107768250379/01ac1392401eecdee1380ba4d82062d0.webp?width=406&height=406")
                        await ctx.channel.send(embed=embed)
                        is_done = True
                        break
                    else:
                        give_money(ctx.author.id,int(amount)*2)
                        embed1 = discord.Embed(color=0x00FF00)
                        embed1.set_author(name=f"Lunar Bot Economy",url="")
                        embed1.add_field(name="You Won!",value=f"<a:yeey:861561586505875506> Congrats you have won the bet <:bitcoin:861527497178480651> **{int(amount)*2}**")
                        embed1.set_footer(text=f"Lunar • today {datetime.datetime.now().hour}:{datetime.datetime.now().minute}",icon_url="https://images-ext-2.discordapp.net/external/F08dR3mn0Eg3YLm2mTbyd4I52Z2XSffki_g-XlUqljg/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/859504107768250379/01ac1392401eecdee1380ba4d82062d0.webp?width=406&height=406")
                        await ctx.channel.send(embed=embed1)
                        is_done = True
                        break

        if is_done == False:
            add_user(ctx.author.id)

    @commands.command(pass_context = True , aliases=['bal'])
    async def balance(self,ctx, user : discord.Member =None):
        users = get_users()
        if user is None:
            member = ctx.author
        if user is not None:
            member = user
        is_done = False
        for i in users:
            if i[1] == member.id:
                embed = discord.Embed(color=0xFF0000)
                embed.set_author(name=f"Lunar Bot Economy",url="")
                embed.add_field(name="Balance",value=f"{member.name} has <:bitcoin:861527497178480651> **{i[2]}**")
                embed.set_footer(text=f"Lunar • today {datetime.datetime.now().hour}:{datetime.datetime.now().minute}",icon_url="https://images-ext-2.discordapp.net/external/F08dR3mn0Eg3YLm2mTbyd4I52Z2XSffki_g-XlUqljg/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/859504107768250379/01ac1392401eecdee1380ba4d82062d0.webp?width=406&height=406")
                await ctx.channel.send(embed=embed)
                is_done = True
                break
        if is_done == False:
            add_user(member.id)
            embed = discord.Embed(color=0xFF0000)
            embed.set_author(name=f"Lunar Bot Economy",url="")
            embed.add_field(name="Balance",value=f"{member.name} has <:bitcoin:861527497178480651> **0**")
            embed.set_footer(text=f"Lunar • today {datetime.datetime.now().hour}:{datetime.datetime.now().minute}",icon_url="https://images-ext-2.discordapp.net/external/F08dR3mn0Eg3YLm2mTbyd4I52Z2XSffki_g-XlUqljg/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/859504107768250379/01ac1392401eecdee1380ba4d82062d0.webp?width=406&height=406")
            await ctx.channel.send(embed=embed)

def setup(client):
    client.add_cog(Economy(client))