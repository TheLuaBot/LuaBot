from database import checar_saldo
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='+', intents=intents)

@bot.tree.command(name="perfil", description="Veja o Perfil de Alguém!")
async def perfil(interaction: discord.Interaction, user: discord.Member):

    embed = discord.Embed(
        title=f"Perfil de {user}",
        colour=discord.Colour.dark_blue(),
    )

    saldo = await checar_saldo(user)

    joined = user.joined_at.strftime("%d/%m/%Y %H:%M:%S") if user.joined_at else "Indisponível"

    embed.set_footer(text=f"MoonCoins: {saldo} | Entrou em: {joined}")

    await interaction.response.send_message(embed=embed)
