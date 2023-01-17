import discord, datetime, time
from discord.ext import commands
from discord import app_commands


global startTime
startTime = time.time()
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"We have logged in!")
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command")
    except Exception as e:
        print(e)
@bot.tree.command(name="help", description="Get help on bugs/suggestions")
async def help_command(interaction: discord.Interaction):
    await interaction.response.send_message(f"/helpbug | Gives help on how to successfully submit a bug | /helpsuggest | Gives help on how to submit a suggestion")
    
@bot.tree.command(name="helpsuggest", description="Get help on how to submit a suggestion")
async def helpsuggest(interaction: discord.Interaction):
    await interaction.response.send_message(f"1. Go to the Suggestions forum | 2. Click New Post. | 3. Enter a title and give it some context such as what the aim is| 4.  Give it the nessisary tags like games/discord| NOTES: Don't make duplicates. instead upvote the suggesting or add a comment. It will be agnowledged")
        

@bot.tree.command(name="helpbug", description="Help on how to report a bug async def bug(interaction: discord.Interaction")
async def helpbug(interaction: discord.Interaction):
       await interaction.response.send_message(f"1. Go to the bugs forum | 2. Click New Post. | 3. Enter a title and give it some context such as how to reproduce the bug. | 4. Give it a tag of what it affects | NOTES: Don't make duplicates. instead upvote the issue or add a comment. It will be agnowledged")
        

bot.run('x')


