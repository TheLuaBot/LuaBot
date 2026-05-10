import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='+', intents=intents)

@bot.tree.command(name="galleryofmoon_about", description="[Info] Mostra as informações sobre a GalleryOfMoon")
async def gofmoon(interaction: discord.Interaction):
    embed = discord.Embed(
        title="GalleryOfMoon - Informações",
        colour=discord.Colour.blurple()
    )

    embed.set_footer(text="A GalleryOfMoon(GofMoon) é a Galeria de fanarts da LuaBot, inspirada na GalleryOfDreams da Loritta.")

    await interaction.response.send_message(embed=embed)