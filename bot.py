import discord
from discord.ext import commands 

token = "paste token here" #토큰 붙여넣으세요
#테스트 토큰: NzA1NTg1Nzk2NjY4NzE5MTY0.Xqt2EQ.DHOh7vGCU6nOLitoDrm-yPY91M8

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
