from dotenv import load_dotenv
import os
import discord
from discord.ext import commands

# Enable necessary Discord intents
intents = discord.Intents.default()
intents.message_content = True

load_dotenv()

# Set command prefix and intents
bot = commands.Bot(command_prefix='!', intents=intents)

# Dictionary to store user points
points = {}

@bot.event
async def on_ready():
    print(f'Bot connected as {bot.user}')

# Helper function to modify points
def modify_points(user_id, amount):
    if user_id not in points:
        points[user_id] = 0
    points[user_id] += amount

# Command to check a user's points
@bot.command()
async def points_of(ctx, member: discord.Member):
    user_id = str(member.id)
    score = points.get(user_id, 0)
    await ctx.send(f'{member.display_name} has {score} points.')

# Command to give points to someone with a reason
@bot.command()
async def give_points(ctx, member: discord.Member, amount: int, *, reason: str):
    if member == ctx.author:
        await ctx.send("You can't modify your own points!")
        return

    user_id = str(member.id)
    modify_points(user_id, amount)
    await ctx.send(f"{ctx.author.display_name} gave {amount} point(s) to {member.display_name}.\nReason: {reason}")

# Command to remove points from someone with a reason
@bot.command()
async def remove_points(ctx, member: discord.Member, amount: int, *, reason: str):
    if member == ctx.author:
        await ctx.send("You can't modify your own points!")
        return

    user_id = str(member.id)
    modify_points(user_id, -amount)
    await ctx.send(f"{ctx.author.display_name} removed {amount} point(s) from {member.display_name}.\nReason: {reason}")

# Run the bot using token from environment variable
bot.run(os.getenv("DISCORD_TOKEN"))
