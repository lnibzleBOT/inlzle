import discord
import random
from discord.ext import commands

class FunCommands(commands.Cog):

    def __init__(self, client):
        self.client = client

    #event gose up here
    @commands.Cog.listener()
    async def on_ready(self):
        print('Cogs = FunCommands.py is online.')

    #commands go belows here
    @commands.command()
    async def coinflip(self, ctx):
        choices = ["Heads", "Talis"]
        rancoin = random.choice(choices)
        
        author = ctx.message.author
        coinflip_alert = discord.Embed(
            colour = discord.Colour.green(),
            title = 'LOOK BELOW',
            description =f'You fliped {rancoin} {author}'
        )

        coinflip_alert.set_footer(text='Bot made by: BugleBoy#1503 ')
        await ctx.send(embed=coinflip_alert)

    @coinflip.error
    async def coinflip_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):

            coinflip_error = discord.Embed(
            colour = discord.Colour.red(),
            title = 'CoinFlip Error',
            description = f'Check Thats u siad Heads or Tails at the end of coinflip'
        )

        coinflip_error.set_footer(text='Bot made by: BugleBoy#1503 ')
        await ctx.send(embed=coinflip_error)

def setup(client):
    client.add_cog(FunCommands(client))