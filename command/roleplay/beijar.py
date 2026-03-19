import discord
from discord.ext import commands
from discord import app_commands

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='+', intents=intents)

@bot.tree.command(name="beijar", description="Beije alguém")
async def beijar(interaction: discord.Interaction, usuario: discord.Member):
    embed = discord.Embed(
        title="💥 Alerta de Beijo!",
        description=f"{interaction.user.mention} beijou {usuario}!"
    )


    await interaction.response.send_message(embed=embed)
