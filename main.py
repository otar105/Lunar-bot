import os
os.system('pip3 install -r requirements.txt')

import discord
import datetime
import keep_alive
from discord.utils import get
#from discord_slash import SlashCommand
import json
from main1 import add_server, all_servers, get_amount, get_server, delete_server, get_warns,add_warn,add_amount, get_greet,add_greet,remove_greet,get_users,add_user,add_money,share_money, get_info,give_money,remove_money,add_inventory,update_greet, remove_code, add_code, get_codes, get_premiumservers, add_premium, add_funcmd, get_funcmd, remove_funcmd, add_chatbot, get_chatbot, remove_chatbot, add_joinchannel, get_join_channels, remove_joinchannel, all_afk, add_afk, remove_afk, get_welcome_channels, add_welcomechannel, remove_welcomechannel
from giphy_client.rest import ApiException
import giphy_client
from discord.ext import commands, tasks
import asyncio
import random
from prsaw import RandomStuffV2
import DiscordUtils
import aiosqlite
from discord_components import *
import youtube_dl
from async_timeout import timeout
import functools
import itertools
import math

intents = discord.Intents.default()
intents.members = True
intents.presences = True
client = commands.Bot(command_prefix=",", intents=intents, case_insensitve=True)
client.remove_command('help')
#slash = SlashCommand(client, sync_commands=True)
rs = RandomStuffV2(async_mode=True)

@client.event
async def on_ready():
    members = 0
    for guild in client.guilds:
      members += guild.member_count
    await client.change_presence(status=discord.Status.online, activity=discord.Game(f"watching {str(len(client.guilds))} servers and {members} users, dm for prefix"))
    DiscordComponents(client)
    print("Bot Is Ready.")
    await status_task()

async def status_task():
    while True:
        members = 0
        for guild in client.guilds:
          members += guild.member_count
        await client.change_presence(status=discord.Status.online, activity=discord.Game(f"watching {str(len(client.guilds))} servers and {members} users, dm for prefix"))
        await asyncio.sleep(5)
        await client.change_presence(status=discord.Status.online, activity=discord.Game(f"watching {str(len(client.guilds))} servers and {members} users, dm for prefix"))
        await asyncio.sleep(5)
        
@client.event
async def on_message(message):
    """
    if client.user.mentioned_in(message):
        await message.channel.send("My prefix is `,`")
    """
    if isinstance(message.channel, discord.channel.DMChannel) and message.author != client.user and message.content != ",help":
        await message.channel.send('Type `,help` for help.')
    users = get_funcmd()
    for i in users:
      if i[1] == message.author.id:
        await message.channel.send(f"{message.author.mention} shitt yourself")
    channels = get_chatbot();
    if client.user == message.author:
      return
    for i in channels:
      if message.channel.id == i[1]:
        try:
          if "@" not in message.content and "who made you" not in message.content and "who made you?" not in message.content and "who created you" not in message.content and "who created you?" not in message.content:
            response = await rs.get_ai_response(message.content)
            await message.reply(response["message"])
          elif "who made you" in message.content or "who made you?" in message.content or "who created you" in message.content or "who created you?" in message.content:
              await message.reply("My dear great botmasters, and Destiny.")
        except:
          await message.reply("No answer....")
    if message.content.startswith(f"<@!{client.user.id}>"):
        await message.channel.send("My prefix is `,`")
    userss = all_afk()
    for i in userss:
        if i[1] == message.guild.id and f"<@!{i[2]}>" in message.content and message.author.id != i[2]:
            await message.channel.send(f"<@!{i[2]}> is AFK: {i[3]}")
        elif i[1] == message.guild.id and message.author.id == i[2]:
            remove_afk(message.guild.id,message.author.id)
            await message.channel.send(f"Welcome back {message.author}, I removed your AFK")
            result = message.author.replace("[AFK] ","")

    await client.process_commands(message)

@client.event
async def on_raw_reaction_add(payload):

    if payload.member.bot:
        pass

    else:
        with open('reactrole.json') as react_file:
            data = json.load(react_file)
            for x in data:
                if x['emoji'] == payload.emoji.name:
                    role = discord.utils.get(client.get_guild(
                        payload.guild_id).roles, id=x['role_id'])

                    await payload.member.add_roles(role)


@client.event
async def on_raw_reaction_remove(payload):

    with open('reactrole.json') as react_file:
        data = json.load(react_file)
        for x in data:
            if x['emoji'] == payload.emoji.name:
                role = discord.utils.get(client.get_guild(
                    payload.guild_id).roles, id=x['role_id'])


                await client.get_guild(payload.guild_id).get_member(payload.user_id).remove_roles(role)

@client.command(help=",reactrole <emoji> <role> <description>")
@commands.has_permissions(administrator=True, manage_roles=True)
async def reactrole(ctx, emoji, role: discord.Role, *, message):
    emb = discord.Embed(description=message)
    msg = await ctx.channel.send(embed=emb)
    await msg.add_reaction(emoji)

    with open('reactrole.json') as json_file:
        data = json.load(json_file)

        new_react_role = {'role_name': role.name,
        'role_id': role.id,
        'emoji': emoji,
        'message_id': msg.id}

        data.append(new_react_role)

    with open('reactrole.json', 'w') as f:
        json.dump(data, f, indent=4)

@client.event
async def on_member_join(member):
    servers = get_greet()
    for i in servers:
        if i[1] == member.guild.id:
          try:
            channel = client.get_channel(i[2])
            msg = await channel.send(f"**Welcome {member.mention} in {member.guild.name}**")
            await asyncio.sleep(i[3])
            await msg.delete()
          except:
            pass
    serverss = get_welcome_channels()
    for i in serverss:
        if i[1] == member.guild.id:
          try:
            channel = client.get_channel(i[2])
            msg = await channel.send(f"**Welcome {member.mention} in {member.guild.name}**")
          except:
            pass

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CommandOnCooldown):
        return await ctx.send('The command **{}** is still on cooldown for {:.2f}'.format(ctx.command.name, error.retry_after))

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

keep_alive.keep_alive()
client.run("ODQxNTYxOTk0NTkwMjg5OTUw.YJojrg.OwwjNgM5UIz5M9i6Ny7a_ulj8gU")