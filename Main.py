import discord
from discord.ext import commands

intents = discord.Intents.default()

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Bot is ready. Logged in as {bot.user.name}')

@bot.event
async def on_message(message):
    if message.author.id == 1111444119680733195:
        thunder_emoji = '\N{THUNDER CLOUD AND RAIN}'
        await message.add_reaction(thunder_emoji)

    await bot.process_commands(message)

bot.run('token')
