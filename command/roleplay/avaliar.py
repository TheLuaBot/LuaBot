import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='+', intents=intents)

@bot.tree.command(name="avaliar", description="[Social] Avalie um usuário!")
@discord.app_commands.describe(nota="A Nota em 10 que você vai dar pro usuário, se você for avaliado por motivos impróprios, chame a moderação do servidor.")
async def avaliar(interaction: discord.Interaction, user: discord.Member, nota: str):
    await interaction.response.send_message(f"💫 **|** O usuário `{user}` recebeu uma nota **{nota}**!")