import discord
from discord.ext import commands
from discord import Member
from discord.ext.commands import has_permissions
from tinydb import database

permissions = []
channelsWithSetRules = []
textChannelList = []

def containsAny(arrayIn, arrayOut):
    for arrayInIndex in arrayIn:
        if arrayInIndex in arrayOut:
            return True
    return False

def getChannelByName(bot, name):
    # first we have to know ID of that channel
    for guild in bot.guilds:
        for channel in guild.channels:
            if channel.name == name:
                channelID = channel.id
    if not channelID:
        print('ERROR: getChannelByName/ChannelID empty')
        return
    # then we are returning channel by ID
    return bot.get_channel(channelID)




class AdminCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # adding new role that have permission to send commands
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def addRolePermission(self, ctx, rolePermission):
        permissions.append(rolePermission)
        await ctx.channel.send(permissions)

    @addRolePermission.error
    async def addRolePermission_error(self, error, ctx):
        await ctx.channel.send('Nie masz uprawnień.')

    # removing role permission
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def removeRolePermission(self, ctx, rolePermission):
        permissions.remove(rolePermission)

    @removeRolePermission.error
    async def removeRolePermission_error(self, error, ctx):
        await ctx.channel.send('Nie masz uprawnień.')

    @commands.command()
    async def addTimePingRule(self, ctx, channel, hourFrom, hourTo, sanction):
        if not containsAny(ctx.message.author.roles, permissions):
            await ctx.channel.send('Nie masz uprawnień.')
        else:
            channelsWithSetRules.append(channel)

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.mentions:
            #teleportChannel = getChannelByName(self.bot, 'teleport')
            await getChannelByName(self.bot, 'teleport').send('Nie Pingujemy!')
            await message.channel.purge(limit=1)




def setup(bot):
    bot.add_cog(AdminCommands(bot))