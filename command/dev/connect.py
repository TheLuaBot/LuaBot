import discord
from discord.ext import commands
import aiohttp

import squarecloud as square
from dotenv import load_dotenv
import os

load_dotenv()

OWNER_ID = os.getenv("OWNER_ID")

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='+', intents=intents)

@bot.tree.command(name="conectar_api", description="[Dev] Fazer uma requisição para a url da API")
async def conectar_api(interaction: discord.Interaction):
    if str(interaction.user.id) != OWNER_ID:
        await interaction.response.send_message("Você não tem permissão para fazer isso!", ephemeral=True)

    if str(interaction.user.id) == OWNER_ID:
        url = "https://tealand.squareweb.app/endpoint/connect"
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status == 200:
                    dados = await response.json()
                    await interaction.response.send_message("Conectado com sucesso com a TeaLand!")
                else:
                    await interaction.response.send_message("Não foi possível se conectar a API!", ephemeral=True)
