from database import checar_saldo
import discord
from discord import app_commands
from discord.ext import commands
from dreamconta.conta import update_user_profile, get_user_profile, load_contas

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='+', intents=intents)

@bot.tree.command(name="perfil", description="Configura ou visualiza suas informações de perfil")
@app_commands.describe(bio="Sua biografia curta")
async def perfil(interaction: discord.Interaction, user: discord.Member, bio: str = None):
    user_id = str(interaction.user.id)
    profiles = load_contas()
    
    
    if user_id not in profiles:
        await interaction.response.send_message(
            "❌ Você ainda não tem uma **DreamConta**!\n"
            "Use o comando `/registrar` para criar sua conta antes de usar este recurso.",
            ephemeral=True
        )
        return
    
    if bio:
       
        update_user_profile(user_id, "bio", bio)
        await interaction.response.send_message(f"Perfil atualizado com sucesso! Bio: `{bio}`", ephemeral=True)
    else:
        
        profile = get_user_profile(user_id)
        user_bio = profile.get("bio", "Nenhuma bio definida.")
        
        embed = discord.Embed(
            title=f"Perfil de {interaction.user.name}",
            description=user_bio,
            color=discord.Color.blurple()
        )

        saldo = await checar_saldo(user)

        joined = user.joined_at.strftime("%d/%m/%Y %H:%M:%S") if user.joined_at else "Indisponível"

        embed.set_footer(text=f"MoonCoins: {saldo} | Entrou em: {joined}")

        await interaction.response.send_message(embed=embed, ephemeral=True)
