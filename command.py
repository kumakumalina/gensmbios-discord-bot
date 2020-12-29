import discord
from discord.ext import commands
import string
import random
import random
import json
import traceback
import sys
import config

class Cmd(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
        self.bot.remove_command("help")

    async def reload_extension(self, ctx, extension):
        try:
            self.bot.unload_extension(extension)
            self.bot.load_extension(extension)
            print("Reloading " + extension + "...Done'")
            await ctx.confirm()
        except:
            print(f"Failed reloading {extension}:\n{traceback.format_exc()}")
            await ctx.deny()

    async def reload_all_extensions(self, ctx):
        for extension in config.extension:
            self.bot.unload_extension(extension)
        check = True
        for extension in config.extension:
            try:
                self.bot.load_extension(extension)
                print("Reloading " + extension + "...Done")
            except Exception as e:
                print(f"Failed reloading {extension}:\n{traceback.format_exc()}")
                check = False
        if check:
            await ctx.send("Processing...")
        else:
            await ctx.send("Error!")

    @commands.command(aliases=["rl"])
    async def reload(self, ctx, extension=""):
        print("Reloading module(s)...Please wait")
        await ctx.send("Reloading `all` extensions...Please wait")
        await self.reload_all_extensions(ctx)
        print("All Done.")
        print("----------------------------")
        await ctx.send("Done")

#Help function
    @commands.command()
    async def help(self, ctx):
        embed = discord.Embed()
        await ctx.trigger_typing()
        embed = discord.Embed(colour=discord.Colour.blue())
        embed=discord.Embed(title="Kokoroちゃん#7506", color=0x14a5ff)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/780671387878031360/793145627696955412/Untitled.png")
        embed.add_field(name="Categories", value="-Currently generating SMBIOS only!", inline=False)
        embed.add_field(name="Note", value="-Command needs few seconds to cooldown. Please do not spam! \n-If you get an error, capture screenshot and send to me. Thank you!", inline=False)                
        embed.set_footer(text= f"Default prefix: {config.prefix} or bot mention")
        await ctx.send(embed=embed)

#About function  
    @commands.command()
    async def about(self, ctx):
        await ctx.trigger_typing()
        owner = self.bot.get_user(config.owner_id)
        embed = discord.Embed(colour=discord.Colour.blue(),
            description="Kokoro is a maid bot will help for generating SMBIOS data information for Hackintosh. Currently supports some models, from Haswell to Comet Lake, Ice Lake (laptop) and AMD system.")
        embed.set_author(name=self.bot.user.name, icon_url="https://cdn.discordapp.com/attachments/780671387878031360/793145627696955412/Untitled.png")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/780671387878031360/793145627696955412/Untitled.png")
        embed.add_field(name="Avatar source:", value="【ごまし】: https://www.pixiv.net/en/artworks/86267893", inline=False)
        embed.add_field(name="Owner", value=owner.mention if owner in getattr(ctx.guild, "members", ()) else str(owner))
        v = sys.version_info
        embed.add_field(name="Language - \nLibrary", value=f"Python {v.major}.{v.minor}.{v.micro} - \n[discord.py\\[rewrite\\]](https://github.com/Rapptz/discord.py/tree/rewrite)")
        embed.add_field(name="Created at", value=str(self.bot.user.created_at)[:10])

        embed.add_field(name="Servers", value=f"{len(self.bot.guilds)} servers")
        ch_count = 0
        txt_count = 0
        ctgr_count = 0
        voice_count = 0
        member_count = 0
        off_members = set()
        for g in self.bot.guilds:
            ch_count += len(g.channels)
            txt_count += len(g.text_channels)
            ctgr_count += len(g.categories)
            voice_count += len(g.voice_channels)
            member_count += g.member_count
            for m in g.members:
                if m.status is discord.Status.offline:
                    off_members.add(m.id)
        off_count = len(off_members)
        user_count = len(self.bot.users)
        embed.add_field(name="Members",
                        value=f"{member_count} members\n{user_count} unique\n{user_count - off_count} online\n{off_count} offline")
        embed.add_field(name="Channels",
                        value=f"{ch_count} total\n{ctgr_count} categories\n{txt_count} text channels\n{voice_count} voice channels")
        await ctx.send(embed=embed)

#Create invite link
    @commands.command(aliases=["inv"])
    async def invite(self, ctx):
        perms = discord.Permissions(permissions=271707222)
        await ctx.send(
            f"Invite URL: <{discord.utils.oauth_url(ctx.me.id, perms)}>"
        )

def setup(bot):
    bot.add_cog(Cmd(bot))