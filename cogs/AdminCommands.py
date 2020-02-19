import discord
from discord.ext import commands

class AdminCommands(commands.Cog):

    def __init__(self, client):
        self.client = client

    #cogs event will go hear
    @commands.Cog.listener()
    async def on_ready(self):
        print('Cogs = AdminCommands is online.')

    #commands go hear 
    @commands.command()
    async def ban(self, ctx, member : discord.Member, *, reason=None):

        ban_alert = discord.Embed(
            colour = discord.Colour.red(),
            title = 'Member Banned',
            description = f'{member} has been banned for {reason}'
        )

        await ctx.send(embed=ban_alert)
        await member.ban(reason=reason)

    @ban.error
    async def ban_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):

            author = ctx.message.author
            ban_error = discord.Embed(
            colour = discord.Colour.green(),
            title = 'Ban Error',
            description = f'Hay uhh did u mention the user right ? {author}'
        )

        await ctx.send(embed=ban_error)

    @commands.command()
    async def unban(self, ctx, *, member):

        unban_alert = discord.Embed(
            colour = discord.Colour.green(),
            title = 'Member Unbanned',
            description = f'{member} has been unbanned'
        )

        await ctx.send(embed=unban_alert)
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')

        for ban_entry in banned_users:
            user = ban_entry.user


            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                return

    @unban.error
    async def unban_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):

            author = ctx.message.author
            unban_error = discord.Embed(
            colour = discord.Colour.green(),
            title = 'Unban Error',
            description = f'Hay uhh did u mention the user right ? {author}'
        )

        await ctx.send(embed=unban_error)

    @commands.command()
    async def kick(self, ctx, member : discord.Member, *, reason=None):

        kick_alert = discord.Embed(
            colour = discord.Colour.red(),
            title = 'Member Kicked',
            description = f'{member} has been kicked for {reason}'
        )

        await ctx.send(embed=kick_alert)
        await member.kick(reason=reason)

    @kick.error
    async def kick_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):

            author = ctx.message.author
            kick_error = discord.Embed(
            colour = discord.Colour.red(),
            title = 'Kick Error',
            description = f'Hay did mention a user ? {author}'
        )

        await ctx.send(embed=kick_error)

    @commands.command(pass_content=True)
    async def clear(self, ctx, amount : int):
        
        author = ctx.message.author
        clear_alert = discord.Embed(
            colour = discord.Colour.green(),
            title = 'Messages Cleared',
            description = f'{author} has cleared {amount} messages'
        )

        await ctx.channel.purge(limit=amount)
        await ctx.send(embed=clear_alert)

    @clear.error
    async def clear_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):

            author = ctx.message.author
            clear_error = discord.Embed(
            colour = discord.Colour.red(),
            title = 'Clear Error',
            description = f'Did u specify a number ? {author}'
        )

        await ctx.send(embed=clear_error)
        
       
def setup(client):
    client.add_cog(AdminCommands(client))