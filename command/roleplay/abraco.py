import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='+', intents=intents)

@bot.tree.command(name="abracar", description="Abraçe aquele teu amigo ote coisinha fofa cuti cuti")
async def abracar(interaction: discord.Interaction, user: discord.Member):
    embed = discord.Embed(
        title="Abraço!",
        description=f"{interaction.user.mention} abraçou {user.mention}! Ote coisinha fofa cuti cuti"
        
    )
    embed.set_image(url="https://media.tenor.com/NGFif4dxa-EAAAAi/hug-hugs.gif")

    await interaction.response.send_message(embed=embed)
