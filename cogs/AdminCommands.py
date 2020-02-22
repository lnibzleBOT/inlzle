import discord
from discord.ext import commands

class AdminCommands(commands.Cog):

    def __init__(self, client):
        self.client = client

    mutelist = []

    #cogs event will go hear
    @commands.Cog.listener()
    async def on_ready(self):
        print('Cogs = AdminCommands is online.')


    #commands go hear 
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def ban(self, ctx, member : discord.Member, *, reason=None):

        ban_alert = discord.Embed(
            colour = discord.Colour.green(),
            title = 'Member Banned',
            description = f'{member} has been banned for {reason}'
        )

        ban_alert.set_footer(text='Bot made by: BugleBoy#1503 ')
        await ctx.send(embed=ban_alert)
        await member.ban(reason=reason)

    @ban.error
    async def ban_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
             
            author = ctx.message.author
            permisson_error1 = discord.Embed(
            colour = discord.Colour.red(),
            title = 'Permmisson Error',
            description = f'Do you have permissons ? {author}'
        )

        permisson_error1.set_footer(text='Bot made by: BugleBoy#1503 ')
        await ctx.send(embed=permisson_error1)

        if isinstance(error, commands.MissingRequiredArgument):

            author = ctx.message.author
            ban_error = discord.Embed(
            colour = discord.Colour.green(),
            title = 'Ban Error',
            description = f'Hay uhh did u mention the user right ? {author}'
        )

        ban_error.set_footer(text='Bot made by: BugleBoy#1503 ')
        await ctx.send(embed=ban_error)

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def unban(self, ctx, *, member):

        unban_alert = discord.Embed(
            colour = discord.Colour.green(),
            title = 'Member Unbanned',
            description = f'{member} has been unbanned'
        )

        unban_alert.set_footer(text='Bot made by: BugleBoy#1503 ')
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
        if isinstance(error, commands.MissingPermissions):
             
            author = ctx.message.author
            permisson_error2 = discord.Embed(
            colour = discord.Colour.red(),
            title = 'Permmisson Error',
            description = f'Do you have permissons ? {author}'
        )

        permisson_error2.set_footer(text='Bot made by: BugleBoy#1503 ')
        await ctx.send(embed=permisson_error2)

        if isinstance(error, commands.MissingRequiredArgument):

            author = ctx.message.author
            unban_error = discord.Embed(
            colour = discord.Colour.green(),
            title = 'Unban Error',
            description = f'Hay uhh did u mention the user right ? {author}'
        )

        unban_error.set_footer(text='Bot made by: BugleBoy#1503 ')
        await ctx.send(embed=unban_error)


    @commands.command()
    @commands.has_permissions(administrator=True)
    async def kick(self, ctx, member : discord.Member, *, reason=None):

        kick_alert = discord.Embed(
            colour = discord.Colour.green(),
            title = 'Member Kicked',
            description = f'{member} has been kicked for {reason}'
        )

        kick_alert.set_footer(text='Bot made by: BugleBoy#1503 ')
        await ctx.send(embed=kick_alert)
        await member.kick(reason=reason)

    @kick.error
    async def kick_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
             
            author = ctx.message.author
            permisson_error3 = discord.Embed(
            colour = discord.Colour.red(),
            title = 'Permmisson Error',
            description = f'Do you have permissons ? {author}'
        )

        permisson_error3.set_footer(text='Bot made by: BugleBoy#1503 ')
        await ctx.send(embed=permisson_error3)

        if isinstance(error, commands.MissingRequiredArgument):

            author = ctx.message.author
            kick_error = discord.Embed(
            colour = discord.Colour.red(),
            title = 'Kick Error',
            description = f'Hay did mention a user ? {author}'
        )

        kick_error.set_footer(text='Bot made by: BugleBoy#1503 ')
        await ctx.send(embed=kick_error)

    @commands.command(pass_content=True)
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount : int):
        
            author = ctx.message.author
            clear_alert = discord.Embed(
            colour = discord.Colour.green(),
            title = 'Messages Cleared',
            description = f'{author} has cleared {amount} messages'
        )
            
            clear_alert.set_footer(text='Bot made by: BugleBoy#1503 ')
            await ctx.channel.purge(limit=amount)
            await ctx.send(embed=clear_alert)

    @clear.error
    async def clear_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):

            author = ctx.message.author
            permisson_error4 = discord.Embed(
            colour = discord.Colour.red(),
            title = 'Permmisson Error',
            description = f'Do you have permissons ? {author}'
        )

        await ctx.send(embed=permisson_error4)



def setup(client):
    client.add_cog(AdminCommands(client))