import discord
import random
from discord.ext import commands
import os

client = commands.Bot(command_prefix='*')
client.remove_command('help')

token = "ODM4NzUwMTU0NDE2MDYyNTI0.YI_o9A.6MUzyxPG0Berr1aElh2JIWNi9_k"

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game('*help'))
    print("Bot is ready!")
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            try:
                client.load_extension(f"cogs.{filename[:-3]}")
                print(f"loaded {filename}")
            except Exception as e:
                print(f"Failed to load {filename}")
                print(f"[ERROR] {e}")


@client.group(invoke_without_command=True)
async def help(ctx):
    em = discord.Embed(title = "Help", description = "Use *help <command> for extended information on a command.",color = ctx.author.color)

    em.add_field(name = "Info", value = "*userinfo <id> - to see user info\n*serverinfo - to see server info")
    em.add_field(name = "Fun", value = "*hi\n*hit <user>\n*fact")


    await ctx.send(embed = em)

client.run(token)
