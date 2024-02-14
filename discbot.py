import discord
import os
from discord.ext import commands
from dotenv import load_dotenv

# Create bot instance
load_dotenv()
token = os.getenv('TOKEN')
intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)

# Event listener for when the bot is ready
@bot.event
async def on_ready():
    print('Bot is ready!')

# Command to send "hello world" message
@bot.command(name='send')
async def send_message(ctx, *, message: str):
    channel = discord.utils.get(ctx.guild.text_channels, name="604-alpha-testing")
    await channel.send(message)

# Run the bot
bot.run(token)
