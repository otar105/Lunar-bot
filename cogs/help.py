import discord
import datetime
from discord.ext import commands
from main1 import add_server, all_servers, get_amount, get_server, delete_server, get_warns,add_warn,add_amount, get_greet,add_greet,remove_greet,get_users,add_user,add_money,share_money, get_info,give_money,remove_money,add_inventory,update_greet, remove_code, add_code, get_codes, get_premiumservers, add_premium, add_funcmd, get_funcmd, remove_funcmd, add_chatbot, get_chatbot, remove_chatbot, add_joinchannel, get_join_channels, remove_joinchannel, all_afk, add_afk, remove_afk, get_welcome_channels, add_welcomechannel, remove_welcomechannel

class Help(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Help Command Loaded Succesfully')

    @commands.command()
    async def help(self,ctx):
        embed = discord.Embed(title="Lunar + Help",description="""**My prefix:** `,`

        <a:hey:870384221703778355> **Help Menu**
        `,help`

        <:developer:861623651053207612> **Bot Info**
        `,botinfo`

        <a:868768970323402802:870381602679717918> **Administration Commands**
        `,warn` `,hide` `,nuke` `,autostatus` `,greet` `,greetdel` `,lock` `,mute` `,kick` `,ban` `,clear` `,serverinfo` `,whois` `,role` `,8ball` `,hack` `,gif` `,ping` `,reactrole` `,afk`

        <a:868769499845910538:870381606119047168> **Economy Menu**
        `,balance` `,beg` `,bet` `,daily` `,share`

        <a:868771181682106418:870381598577664080> **Invite Tracker Commands**
        `,top` `,invites` `,restinvites all` `,joinchannel` `,removejoinchannel`

        <a:868411787618426941:870381602864246805> **Giveaway Commands**
        `,gstart` `,gend` `,greroll`

        <a:logo:862056920445222932> **Music Commands**
        `,play` `,queue` `,now` `,remove` `,loop` `,skip` `,volume` `,disconnect` `,shuffle`

        <:856078293726789632:861620851962413096> [Get Support](https://discord.gg/ZGjrDPzN)
        <:856077920637614796:861620850477498379> [Invite the bot here](https://discord.com/oauth2/authorize?client_id=841561994590289950&scope=bot%20applications.commands&permissions=8589934591)
        <:developer:861623651053207612> Our Developers <:859023921948393512:861620850498338817> `,botinfo`""", color=0xe6b5bd)
        embed.set_footer(text=f"Requested by {ctx.author} • today {datetime.datetime.now().hour}:{datetime.datetime.now().minute}", icon_url=f"{ctx.author.avatar_url}")
        await ctx.channel.send(embed=embed)

def setup(client):
    client.add_cog(Help(client))