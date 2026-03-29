import json
import discord
from discord.ext import commands
from discord import app_commands
import os
from dotenv import load_dotenv

BLACKLIST_ARCHIVE = "blacklisted_users.json" # arquivo da Caramelo BlackList

load_dotenv()

owner_id = os.getenv("OWNER_ID")

# --- BOT --- #
bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())
# ----------- #

def load_blacklist():
    try:
        with open('blacklisted_users.json', 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {"usuarios": [], "servidores": []} # Retorna nada quando tiver erro

def save_blacklist():
    with open('blacklisted_users.json', 'w') as f:
        json.dump(blacklist_data, f, indent=4)

blacklist_data = load_blacklist() # carrega os dados na memória ao iniciar

@bot.check
async def check_blacklist(interaction: discord.Interaction):
    user_id = interaction.user.id
    guild_id = interaction.guild.id if interaction.guild else None

    if user_id in blacklist_data["usuarios"]:
        await interaction.response.send_message("🚫 Você está na minha blacklist e não pode usar meus comandos!", ephemeral=True)
        return False
    return True
        

@bot.tree.command(name="blacklist_add", description="[Caramelo Blacklist] Adiciona um usuário à blacklist")
async def blacklist_add(interaction: discord.Interaction, usuario: discord.User):

    if owner_id:
        if usuario.id not in blacklist_data["usuarios"]:
            blacklist_data["usuarios"].append(usuario.id)
            save_blacklist()
            await interaction.response.send_message(f"✅ {usuario.name} foi silenciado globalmente.")
        else:
            await interaction.response.send_message("Este usuário já está na lista.", ephemeral=True)
    
    if owner_id == interaction.user.id:
        await interaction.response.send_message("Você não pode usar esse comando!")

@bot.tree.command(name="blacklist_remove", description="[Caramelo Blacklist] Remove um usuário da Blacklist")
async def blacklist_remove(interaction: discord.Interaction, usuario: discord.User):
        try:
            blacklist_data["usuarios"].remove(usuario.id)

            save_blacklist

            await interaction.response.send_message("Usuário removido!")
        except ValueError: 
    
            await interaction.response.send_message("Erro: O usuário não estava na lista.")
        
        if usuario.id not in blacklist_data["usuarios"]:
            await interaction.response.send_message(f"💥 O Usuário {usuario} não está na lista! Por isso não tem como ele ser removido!")
            return
