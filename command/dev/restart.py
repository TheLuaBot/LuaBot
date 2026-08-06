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

@bot.tree.command(name="restart", description="Reinicia a LuaBot em casos de emergência :D")
async def restart(interaction: discord.Interaction):
    if str(interaction.user.id) != OWNER_ID:
        await interaction.response.send_message("Você não pode me reiniciar! >:C")

    if str(interaction.user.id) == OWNER_ID:
      await interaction.response.send_message("Reiniciando...")
      print(f"{interaction.user.id} me reiniciou!")
      await client.stop_app(SQUARE_APP_ID)
