import discord
import datetime
from discord.ext import commands
import asyncio
import random
from main1 import add_server, all_servers, get_amount, get_server, delete_server, get_warns,add_warn,add_amount, get_greet,add_greet,remove_greet,get_users,add_user,add_money,share_money, get_info,give_money,remove_money,add_inventory,update_greet, remove_code, add_code, get_codes, get_premiumservers, add_premium, add_funcmd, get_funcmd, remove_funcmd, add_chatbot, get_chatbot, remove_chatbot, add_joinchannel, get_join_channels, remove_joinchannel, all_afk, add_afk, remove_afk, get_welcome_channels, add_welcomechannel, remove_welcomechannel

class Fun(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Fun Command Loaded Succesfully')

    @commands.command()
    async def hack(self, ctx, user : discord.Member):
        message = await ctx.send(f"Hacking {user} now...")
        words = ["dank memer is a terrible bot",]
        await asyncio.sleep(3)
        await message.edit(content="[**11.32%**] Finding discord login... (2fa bypassed)")
        await asyncio.sleep(3)
        await message.edit(content=f"[**18.19%**] Found:\n**Email:** `{user}*****@gmail.com`\n**Password:** `123456789`")
        await asyncio.sleep(3)
        await message.edit(content="[**24.05%**] Fetching dms with closet friends (if there are any friends at all)")
        await asyncio.sleep(3)
        await message.edit(content="[**28.65%**] **Last DM:** 'I hope no one sees my nudes folder'")
        await asyncio.sleep(3)
        await message.edit(content="[**37.65%**] Finding most common word...")
        await asyncio.sleep(3)
        await message.edit(content="[**44.62%**] `const mostCommonWord: string = 'meme';`")
        await asyncio.sleep(3)
        await message.edit(content=f"[**50.57%**] Injecting trojan virus into discriminator {user.discriminator}")
        await asyncio.sleep(3)
        await message.edit(content=f"[**48.62%**] Virus injected, emotes stolen <a:wtf_pepe:859732800378634270>")
        await asyncio.sleep(3)
        await message.edit(content=f"[**60.25%**] Hacking Epic Store account... <:pepe_yeaaa:861552350924767252>")
        await asyncio.sleep(3)
        await message.edit(content=f"[**69.69**] Breached Epic Store Account: No More 19 Dollar Fortnite Cards 🚫")
        await asyncio.sleep(3)
        await message.edit(content=f"[**69.11%**] Finding IP address")
        await asyncio.sleep(3)
        await message.edit(content=f"[**76.65%**] **IP address:** 127.0.0.1.4292")
        await asyncio.sleep(3)
        await message.edit(content=f"[**90.27%**] Selling data to the Goverment...")
        await asyncio.sleep(3)
        await message.edit(content=f"[**93.12%**] Reporting account to Discord for breaking TOS...")
        await asyncio.sleep(3)
        await message.edit(content=f"[**95.70%**] Finished hacking {user}")
        await asyncio.sleep(3)
        await message.edit(content=f"[**100%**] The **totally** real and dangerous hack is complete")

    @commands.command(name="8ball")
    async def _8ball(self,ctx, *, question):
      responses = [
                "It is certain.",
                "It is decidedly so.",
                "Without a doubt.",
                "Yes - definitely.",
                "You may rely on it.",
                "As I see it, yes.",
                "Most likely.",
                "Outlook good.",
                "Yes.",
                "Signs point to yes.",
                "Reply hazy, try again.",
                "Ask again later.",
                "Better not tell you now.",
                "Cannot predict now.",
                "Concentrate and ask again.",
                "Don't count on it.",
                "My reply is no.",
                "My sources say no.",
                "Outlook not so good.",
                "Very doubtful."]
      result = random.choice(responses)
      await ctx.reply(f"🎱 {result}", mention_author=True)
def setup(client):
    client.add_cog(Fun(client))