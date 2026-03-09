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


@bot.tree.command(name="shutdown", description="[Dev] Para o processo de execução da LuaBot")
async def shutdown(interaction: discord.Interaction):
    if not OWNER_ID:
        await interaction.response.send_message("Tá querendo me desligar é? **Você não tem permissão para me desativar!**")
    else:
        await client.stop_app(SQUARE_APP_ID)
        print("Adeus Mundo Cruel")