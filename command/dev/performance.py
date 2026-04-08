import discord
from discord.ext import commands

import squarecloud as square
from dotenv import load_dotenv
import os

load_dotenv()

SQUARE_TOKEN = os.getenv("SQUARE_API_KEY")
SQUARE_APP_ID = os.getenv("SQUARE_APP_ID")
OWNER_ID = os.getenv("OWNER_ID")

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='+', intents=intents)

client = square.Client(api_key=SQUARE_TOKEN)

@bot.tree.command(name="performance", description="[Dev] Veja a performance da LuaBot!")
async def performance(interaction: discord.Interaction):
    if not OWNER_ID:
        await interaction.response.send_message("Tá querendo ver se eu tô funcionando?")
    else:
        status = await client.app_status(SQUARE_APP_ID)  # StatusData(...)

    await interaction.response.send_message(f"Performance: **RAM:**{status.ram}, **CPU:** {status.cpu}, **Network:** {status.network}")      
