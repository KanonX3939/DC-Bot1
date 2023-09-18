import discord
from discord.ext import commands
intents = discord.Intents.all()
import requests
import json
import random
import os
import datetime

with open('setting.json','r',encoding='utF8') as jFile:
    jdata =json.load(jFile)

bot = commands.Bot(command_prefix='h/',intents = intents)

@bot.event

async def on_ready():
    print(">>連線成功<<")

@bot.event

async def on_member_join(member):
    channel=bot.get_channel(int(jdata['歡迎']))
    await channel.send(f'**歡迎@{member}!**')

@bot.event

async def on_member_remove(member):
    channel=bot.get_channel(int(jdata['離開']))
    await channel.send(f'**{member}已離開**')


@bot.command()
async def 頭像(ctx):
        pic=discord.File('D:\Discord Bot\GitHub\DC-Bot\頭像\F5todOZbQAAWUkE.jpg')
        await ctx.send(file=pic)
@bot.command()
async def 圖片(ctx):
        random_pic = random.choice(jdata['url_pic'])
        await ctx.send(random_pic)

@bot.command()
async def ping(ctx):
        await ctx.send(f'{round(bot.latency*1000)}ms')
    
@bot.command()
async def 資訊(ctx):
        embed=discord.Embed(title="haruka", description="None")
        embed.set_author(name="KanonX", url="https://x.com/KanonX2006", icon_url="https://twitter.com/KanonX2006/photo")
        embed.add_field(name="測試機器人", value="None", inline=False)
        embed.set_footer(text="by KanonX")
        await ctx.send(embed=embed)

@bot.command()

async def load(ctx,extension):
    bot.load_extension(f'cmds.{extension}')
    await ctx.send(f'Loaded {extension} done.')

@bot.command()

async def unload(ctx,extension):
    bot.unload_extension(f'cmds.{extension}')
    await ctx.send(f'UnLoaded {extension} done.')

@bot.command()

async def reload(ctx,extension):
    bot.reload_extension(f'cmds.{extension}')
    await ctx.send(f'ReLoaded {extension} done.')

for filename in os.listdir('./cmds'):
    if filename.endswith('.py'):
        bot.load_extension(f'cmds.{filename[:-3]}')

    
if __name__ == "__main__":

    bot.run(jdata['TOKEN'])