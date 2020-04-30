import discord
import datetime
from discord.ext import commands

class Hello(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="안녕")
    async def _hello(self, ctx):
        await ctx.send("안녕하세요!")

def setup(bot):
    bot.add_cog(Hello(bot)) 