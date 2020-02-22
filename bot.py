import discord
import os
from discord.ext import commands, tasks
from itertools import cycle

#all client side stuff gose here
client = commands.Bot(command_prefix = '.')
client.remove_command('help')
client.remove_command('load')
client.remove_command('unload')
status = cycle(['Subscribe to BugleTV.', 'Do .help for help list.', 'Thanks to BulbaLord#3934'])

#all events will go here

@client.event
async def on_ready():
    change_status.start()
    print('Bot is going on line.')

@tasks.loop(seconds=5)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send('Command not found')

@client.event
async def on_member_join(member):
    print(f'{member} has joined a server')

@client.event
async def on_member_remove(member):
    print(f'{member} has been removed a server')


#commands will go hear
@client.command(pass_context=True)
async def help(ctx):
    author = ctx.message.author

    help_embed = discord.Embed(
        colour = discord.Colour.green()
    )

    help_embed.set_author(name='Help Geneal Commands')
    help_embed.add_field(name='help', value='Shows this message.', inline=False)
    help_embed.add_field(name='load {etc}', value='Owner only.', inline=False)
    help_embed.add_field(name='unload {etc}', value='Owner only.', inline=False)
    help_embed.set_footer(text='Bot made by: BugleTV')

    help_Admin = discord.Embed(
        colour = discord.Colour.orange()
    )

    help_Admin.set_author(name='Help Admin Commands')
    help_Admin.add_field(name='ban @example {reason not needed}', value='Bans a user.', inline=False)
    help_Admin.add_field(name='unban @example', value='unban user mentioned [very sensitive command].', inline=False)
    help_Admin.add_field(name='kick @example {reason not needed}', value='kickes a user mentioned', inline=False)
    help_Admin.add_field(name='clear {amount}', value='clears given amount', inline=False)
    help_Admin.set_footer(text='Bot made by: BugleBoy#1503 ')
    help_Admin.url='https://www.youtube.com/channel/UCJjGApYSgQKWgtKAJj7Pa1g?view_as=subscriber'
    
    await ctx.send(f'Check you dms {author} :thumbsup:')
    await ctx.author.send(author, embed=help_embed)
    await ctx.author.send(author, embed=help_Admin)


@client.command()
async def load(ctx, extension):
    client.load_extension(f'cpgs.{extension}')

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cpgs.{extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run('Njc5NDQxMjgwNTUxMzU0Mzc5.XlFXHg._f3RzBBGJ3wjbS03gCUYd6DYu_g')
