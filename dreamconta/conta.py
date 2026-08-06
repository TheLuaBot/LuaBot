import discord
from discord.ext import commands
from discord import app_commands
import os
import json

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix="+", intents=intents)

CONTA_PATH = "dreamconta.json"

def load_contas():
    if not os.path.exists(CONTA_PATH):
        return {}

    with open(CONTA_PATH, 'r', encoding='utf-8') as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return {}
            
def save(data):
    with open(CONTA_PATH, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def get_user_profile(user_id: int):
    profiles = load_contas()
    return profiles.get(str(user_id), {})

def update_user_profile(user_id: int, key: str, value):
    profiles = load_contas()
    uid = str(user_id)
    
    if uid not in profiles:
        profiles[uid] = {}
        
    profiles[uid][key] = value
    save(profiles)

@bot.tree.command(name="registrar", description="[DreamConta] Registre sua DreamConta!")
@app_commands.describe(
    nome="Seu nome/apelido principal",
    bio="Uma breve biografia sobre você",
    jogo="Seu jogo favorito"
)
async def registrar_conta(interaction: discord.Interaction, bio: str, jogo: str, nome: str):
    user_id = str(interaction.user.id)
    profiles = load_contas()

    if user_id in profiles:
        await interaction.response.send_message("❌ **|** Você já possui uma DreamConta! Use `/perfil` para ver seu perfil na DreamConta!", ephemeral=True)
        return

    profiles[user_id] = {
        "nome": nome,
        "bio": bio,
        "jogo_favorito": jogo,
        "criado_em": discord.utils.utcnow().isoformat()
    }

    save(profiles)

    embed = discord.Embed(
        title="✨ Conta Registrada com Sucesso!",
        description="Seus dados foram salvos e já podem ser usados em outros comandos da LuaBot.",
        color=discord.Color.green()
    )
    embed.add_field(name="Nome", value=nome, inline=True)
    embed.add_field(name="Jogo Favorito", value=jogo, inline=True)
    embed.add_field(name="Bio", value=bio, inline=False)
    
    await interaction.response.send_message(embed=embed, ephemeral=True)