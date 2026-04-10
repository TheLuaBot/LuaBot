import discord
from discord.ext import commands



intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='+', intents=intents)



# Comandos de trancar o canal
@bot.tree.command(name="lock", description="[Caramelo Mod] Tranque um Canal do Servidor!")
async def lock(interaction: discord.Interaction):
    
    if not interaction.user.guild_permissions.manage_channels:
        await interaction.response.send_message("Você não tem permissão para Gerenciar Canais!")

    if interaction.user.guild_permissions.manage_channels:
        everyone = interaction.guild.default_role
        channel = interaction.channel

        overwrite = channel.overwrites_for(everyone)
        overwrite.send_messages = False

        await channel.set_permissions(everyone, overwrite=overwrite)
        
        await interaction.response.send_message(f"🔒 Este canal foi trancado por {interaction.user.mention}!")

@bot.tree.command(name="unlock", description="[Caramelo Mod] Desbloqueie um canal do servidor!")
async def unlock(interaction: discord.Interaction):

    if not interaction.user.guild.manage_channels:
        await interaction.response.send_message("Você não tem permissão de gerenciar canais!", ephemeral=True)

    if interaction.user.guild.manage_channels:
        everyone = interaction.guild.default_role
        channel = interaction.channel

        overwrite = channel.overwrites_for(everyone)
        overwrite.send_messages = True

        await channel.set_permissions(everyone, overwrite=overwrite)
        await interaction.response.send_message(f"🔓 Este canal foi desbloqueado por {interaction.user.mention}!")
