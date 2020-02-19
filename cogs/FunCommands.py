import discord
import random
from discord.ext import commands

class FunCommands(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Cogs = FunCommands.py is online.')

def setup(client):
    client.add_cog(FunCommands(client))