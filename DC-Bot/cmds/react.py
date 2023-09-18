import discord
from discord.ext import commands
from core.classes import Cog_Extension
import random
import json

with open('setting.json',mode='r',encoding='utF8') as jfile:
    jdata =json.load(jfile)

class React(Cog_Extension):

    @commands.command()
    async def 頭像(self,ctx):
        pic=discord.File('D:\Discord Bot\GitHub\DC-Bot\頭像\F5todOZbQAAWUkE.jpg')
        await ctx.send(file=pic)
    @commands.command()
    async def 圖片(self,ctx):
        random_pic = random.choice(jdata['url_pic'])
        await ctx.send(random_pic)

def setup(bot):
    bot.add_cog(React(bot))