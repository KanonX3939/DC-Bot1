import discord
from discord.ext import commands
from core.classes import Cog_Extension
import datetime



class Main(Cog_Extension):

    @commands.command()
    async def ping(self,ctx):
        await ctx.send(f'{round(self.bot.latency*1000)}ms')
    
    @commands.command()
    async def 資訊(self,ctx):
        embed=discord.Embed(title="關於我", color=0x99ccff,timestamp=datetime.datetime.now())
        embed.set_author(name="KanonX")
        embed.set_thumbnail(url="https://www.pixiv.net/artworks/111769682")
        embed.add_field(name="測試機器人", value="開發中", inline=False)
        embed.set_footer(text="by KanonX")
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Main(bot))