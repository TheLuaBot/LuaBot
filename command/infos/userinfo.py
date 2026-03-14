import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='+', intents=intents)

@bot.tree.command(name="userinfo", description="Mostra informações de um usuário")
async def userinfo(interaction: discord.Interaction, membro: discord.Member = None):
    if membro is None:
        membro = interaction.user 

    joined = membro.joined_at.strftime("%d/%m/%Y %H:%M:%S") if membro.joined_at else "Indisponível"
    created = membro.created_at.strftime("%d/%m/%Y %H:%M:%S")
    top_role = membro.top_role.mention if membro.top_role != interaction.guild.default_role else "Nenhum"
    roles = [r.mention for r in membro.roles if r != interaction.guild.default_role]
    roles_str = ", ".join(roles[:10]) + (" ..." if len(roles) > 10 else "")

    embed = discord.Embed(
        title=f"👤 {membro.display_name}",
        description=f"Tag: **{membro}**",
        color=discord.Color.blurple()
    )
    embed.set_thumbnail(url=membro.display_avatar.url)
    embed.add_field(name="🤖 Bot?", value="Sim" if membro.bot else "Não", inline=True)
    embed.add_field(name="📅 Conta criada", value=created, inline=False)
    embed.add_field(name="📥 Entrou no servidor", value=joined, inline=False)
    embed.add_field(name="🏷️ Top cargo", value=top_role, inline=True)
    embed.add_field(name=f"🎭 Cargos ({len(roles)})", value=roles_str or "Nenhum", inline=False)

    await interaction.response.send_message(embed=embed)
