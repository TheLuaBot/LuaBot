import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

load_dotenv()

LUA_HELPER_TOKEN = os.getenv("LUA_HELPER_TOKEN")

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='+', intents=intents)

@bot.event
async def on_ready():
    print("Pronto! {bot.user}")
    await bot.tree.sync()

@bot.tree.command(name="ban", description="Bane um usuário do servidor.")
async def ban(interaction: discord.Interaction, user: discord.Member, reason: str = "Sem motivo especificado"):
    # Verifica se quem usou o comando pode banir
    if not interaction.user.guild_permissions.ban_members:
        await interaction.response.send_message("❌ Você não tem permissão para banir membros.", ephemeral=True)
        return

    # Impede quem usou o comando de se banir
    if user == interaction.user:
        await interaction.response.send_message("❌ Você não pode se banir.", ephemeral=True)
        return

  # Tenta Banir alguém
    try:
        await user.ban(reason=reason)
        await interaction.response.send_message(
            f"<:lua_ban_hammer:1429136081768419480> {user.mention} foi banido!\n**Motivo:** {reason}",
            ephemeral=False
        )
    except discord.Forbidden:
        await interaction.response.send_message("❌ Não consegui banir esse membro. Verifique a hierarquia.", ephemeral=True)
    except Exception as e:
        await interaction.response.send_message(f"❌ Erro inesperado: {e}", ephemeral=True)

@bot.tree.command(name="unban", description="Desbane um usuário do servidor pelo ID.")
async def unban(interaction: discord.Interaction, user_id: str, reason: str = "Sem motivo especificado"):
    if not interaction.guild:
        await interaction.response.send_message("❌ Este comando só pode ser usado em servidores.", ephemeral=True)
        return

    if not interaction.user.guild_permissions.ban_members:
        await interaction.response.send_message("❌ Você não tem permissão pra desbanir membros.", ephemeral=True)
        return

    try:
        user = await bot.fetch_user(int(user_id))
        await interaction.guild.unban(user, reason=reason)
        await interaction.response.send_message(f"✅ {user.mention} foi desbanido!\n**Motivo:** {reason}")
    except discord.NotFound:
        await interaction.response.send_message("❌ Usuário não encontrado ou não está banido.", ephemeral=True)
    except discord.Forbidden:
        await interaction.response.send_message("❌ Eu não tenho permissão pra desbanir esse usuário.", ephemeral=True)
    except Exception as e:
        await interaction.response.send_message(f"❌ Erro ao desbanir: `{e}`", ephemeral=True)

bot.run(LUA_HELPER_TOKEN)