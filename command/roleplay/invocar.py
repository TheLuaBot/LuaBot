import discord
from discord.ext import commands
from discord import app_commands

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='+', intents=intents)


@bot.tree.command(name="invocar", description="Invoque algum personagem!")
@app_commands.describe(personagem="O Personagem que você vai invocar")
async def invocar(interaction: discord.Interaction, personagem: str):

    await interaction.response.defer()

    embed = discord.Embed(
        title="Invocação Suprema!",
        description=f"💥 {interaction.user.mention} invocou {personagem}!"
    )

    embed.set_footer(text="Invocação")


    await interaction.followup.send(embed=embed)
