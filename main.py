import discord
from discord.ext import commands, tasks
from itertools import cycle
import os
import random
#import keep_alive

bot = commands.Bot(command_prefix = '$')

@bot.event
async def on_ready():
    print("Bot wystartował.")
    channels = bot.get_all_channels()
    for channel in channels:
        print(channel.name)
        print(channel.id)

@bot.command()
async def loadCog(ctx, extensionName):
    bot.load_extension(f'cogs.{extensionName}')

@bot.command()
async def unloadCog(ctx, extensionName):
    bot.unload_extension(f'cogs.{extensionName}')

@bot.command()
async def reloadCog(ctx, extensionName):
    bot.reload_extension(f'cogs.{extensionName}')

@bot.command()
async def deleteMessages(ctx, numberOfMessages = 5):
    await ctx.channel.purge(limit=numberOfMessages + 1)

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

#keep_alive.keep_alive()
bot.run('ODAyNjIwNDU1MDEzMzE4NjY2.YAx4jA.P2YeeEbMvUqPQPsH6Kr-DR7yHNY')