import discord
from discord.ext import commands
intents = discord.Intents.all()
import requests
import json
import random
import os

with open('setting.json','r',encoding='utF8') as jFile:
    jdata =json.load(jFile)

bot = commands.Bot(command_prefix='[',intents = intents)

@bot.event

async def on_ready():
    print(">>連線成功<<")



    bot.run('MTE1MjQ5Njk1OTM1ODI0NjkzMw.G4VFjH.03_VO3fzM546UrfuYIphCko9abqaWQvDXYGfCg')