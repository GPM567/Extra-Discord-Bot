import discord
from discord.ext import commands 

token = "paste token here" #토큰을 붙여넣으세요

class Bot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="!")

def load_cogs(bot):
    extensions = ['cogs.admin',
                'cogs.events']

    for extension in extensions:
        bot.load_extension(extension)
    

if __name__ == '__main__':
    bot = Bot()
    load_cogs(bot)
    bot.run(token)
