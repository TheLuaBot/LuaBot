import discord
from discord import app_commands
from discord import ui
from discord.ext import commands
from dotenv import load_dotenv
import random
import asyncio
import os

from database import checar_saldo, alterar_saldo

from utils.isGestor import verificar_gestor
from command.dev import shutdown, restart, performance
from command.roleplay import abraco, invocar, beijar
from command.infos import userinfo, botinfo, perfil
from shih.shih_manager import DiscordTokenManager, MongoDBTokenManager
from caramelo.blacklist.blacklist import blacklist_add, save_blacklist, blacklist_data, blacklist_remove
from caramelo.caramelo import lock, unlock


TOSCO_MODE = False

dtm = DiscordTokenManager()
mdbtm = MongoDBTokenManager()

load_dotenv()

TOKEN = os.getenv("TOKEN")
CARGO_GESTOR = os.getenv("CARGO_GESTOR") 

intents = discord.Intents.default()
intents.members = True


bot = commands.Bot(command_prefix='+', intents=intents)

textos = (
    "🌙| Olá Eu Sou a LuaBot!"
)

@bot.event
async def on_ready():
    print("--- LUA BOT :P ---")
    print(f"LuaBot Online! - {bot.user.name} ({bot.user.id})")
                                                             
    print("-------------------")
    await bot.change_presence(
        activity=discord.CustomActivity(
            textos
        )
    )

    
    blacklist_cache = save_blacklist()

    # Registra o comando manualmente na árvore

    # Comandos de Development :D
    bot.tree.add_command(shutdown.shutdown)
    bot.tree.add_command(restart.restart)
    bot.tree.add_command(performance.performance)

    # Comandos de Roleplay
    bot.tree.add_command(abraco.abracar)
    bot.tree.add_command(invocar.invocar)
    bot.tree.add_command(beijar.beijar)

    # Comandos de Infos
    bot.tree.add_command(userinfo.userinfo)
    bot.tree.add_command(botinfo.botinfo)
    bot.tree.add_command(perfil.perfil)

    # Comandos do Caramelo Automod/Mod
    bot.tree.add_command(lock) # Comando de Trancar o Canal
    bot.tree.add_command(unlock)
    bot.tree.add_command(blacklist_add) # comando de adicionar um usuário na blacklist
    bot.tree.add_command(blacklist_remove) # Comando de Remover um usuário da blacklist!


    try:
        synced = await bot.tree.sync()
        print(f"Sincronizados {len(synced)} comandos..")
    except Exception as e:
        print(f"Erro ao sincronizar comandos: {e}")
    print(f'Bot conectado como {bot.user}')



@bot.tree.command(name="ping", description="Veja o ping do bot")
async def ping(interaction: discord.Interaction):
    latency = round(bot.latency * 1000)  
    await interaction.response.send_message(f"AU AU!! \nLatência: {latency}ms")


@bot.tree.command(name="morder", description="Dá uma mordida carinhosa em alguém")
async def morder(interaction: discord.Interaction, user: discord.Member):
    await interaction.response.send_message(
        f"🐾 A Lua correu e deu uma mordidinha carinhosa em {user.mention}!!"
    )


@bot.tree.command(name="chinelos", description="Lua mostra um chinelo destruído")
async def chinelos(interaction: discord.Interaction):
    embed = discord.Embed(title="O Chinelo virou pó!")
    embed.set_image(url="https://i.postimg.cc/fL8khMgX/Opera-Instant-neo-2025-09-16-194923-www-canva-com.png")
    await interaction.response.send_message(embed=embed)

@bot.tree.command(name="carinho", description="Faça carinho na Lua!!")
async def carinho(interaction: discord.Interaction):
    await interaction.response.send_message(
        "💖 A Lua aceitou seu carinho!! (mas cuidado, ela ainda pode te morder hehe:P)"
    )


@bot.tree.command(name="latir", description="Lua manda latidos para você")
async def latir(interaction: discord.Interaction):
    await interaction.response.send_message("AU AU AUUUUUUUUUUUUUUUUUUUUUUUUUUU!")


@bot.tree.command(name="brinquedo", description="Lua mostra um brinquedo para você :3")
async def brinquedo(interaction: discord.Interaction):
    embed = discord.Embed(title="Aqui ó, um brinquedo pra você!")
    embed.set_image(url="https://imgur.com/a/cNUnoSo")
    await interaction.response.send_message(embed=embed)

@bot.tree.command(name="ajuda", description="As vezes precisamos de Ajuda :3")
async def ajuda(interaction: discord.Interaction):
  await interaction.response.send_message("Olá! meu prefixo nesse servidor é "/", :3")

@bot.tree.command(name="saldo", description="Verifique quanto você tem de MoonCoins!")
async def saldo(interaction: discord.Interaction):
    moedas = await checar_saldo(interaction.user)

    await interaction.response.send_message(
        f"Você possui 🪙 **{moedas}** MoonCoins!"
    )

@bot.tree.command(name="daily", description="Pegue sua recompensa")
@app_commands.checks.cooldown(1, 86400, key=lambda i: (i.guild_id, i.user.id))
async def daily(interaction: discord.Interaction):
    valor = random.randint(40,150)

    await alterar_saldo(interaction.user,valor)

    await interaction.response.send_message(f"<:gatodojoia:1419360636084682812> | Au Au {interaction.user.mention}! Você ganhou {valor} MoonCoins!")

@daily.error
async def daily_error(interaction: discord.Interaction, error: app_commands.AppCommandError):

    if isinstance(error,app_commands.CommandOnCooldown):
        await interaction.response.send_message(f"❌ | **Você já recebeu sua recompensa diária de MoonCoins hoje!** Você poderá pegar novamente em {round(error.cooldown.get_retry_after()/3600,2)} horas!", ephemeral=True)

    else:
        raise(error)     


@bot.tree.command(name="minerar", description="[Minecraft] Minere Minérios no Discord!")
async def minerar(interaction: discord.Interaction):
    minerios = ["Pedra", "Carvão", "Cobre", "Ferro", "Ouro", "Diamante"]

    resultado = random.choices(minerios)


    embed = discord.Embed(
        title="⛏️ Mineração",
        description=f"{interaction.user.mention} foi pras profundezas e encontrou:",
        color=discord.Color.blue()
    )

    embed.add_field(name="Minério Coletado", value=f"Minério: ⛏️ {resultado}")

    await interaction.response.send_message(embed=embed)

@bot.tree.command(name="coinflip", description="Faça um Cara ou Coroa no Discord!")
async def coinflip(interaction: discord.Interaction):
    caraoucoroa = ["Cara", "Coroa"]

    resultado = random.choices(caraoucoroa)

    await interaction.response.send_message(f"🪙 {resultado}!")

@bot.tree.command(name="minecraft_skin", description="Veja a skin de um jogador de Minecraft")
@app_commands.describe(player="O nome (nickname) do jogador")
async def skin(interaction: discord.Interaction, player: str):
    # Render "body" mostra o corpo inteiro do personagem
    skin_url = f"https://crafatar.com/renders/body/{player}?overlay"
    
    
    embed = discord.Embed(
        title=f"Skin de {player}",
        color=discord.Color.blue()
    )
    embed.set_image(url=skin_url)
    embed.set_footer(text="API fornecida por Crafatar")

    await interaction.response.send_message(embed=embed)

@bot.tree.command(name="modo_tosco", description="Veja para que serve o Modo Tosco da LuaBot!")
async def modo_tosco(interaction: discord.Interaction):
    embed = discord.Embed(
        title="💩 Modo Tosco",
        color=discord.Color.blue(),
        description="O Modo Tosco serve para deixar seu servidor muito divertido, por exemplo, eu vou reagir a mensagens aleatórias do seu servidor!"
    )

    await interaction.response.send_message(embed=embed)

@bot.tree.command(name="ativar_modo_tosco", description="Ativa o Modo Tosco da LuaBot!")
async def ativar_tosco_mode(interaction: discord.Interaction):
    global TOSCO_MODE
    TOSCO_MODE = True
    await interaction.response.send_message("**Modo Tosco Ativado!**")

@bot.tree.command(name="desativar_modo_tosco", description="Desativa o Modo Tosco!")
async def desativar_tosco_mode(interaction: discord.Interaction):
    TOSCO_MODE = False
    await interaction.response.send_message(f"**Modo Tosco Desativado!**")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    
    if TOSCO_MODE == True:
        
        
        
        if random.randint(1, 100) <= 50:
            emoji_tosco = "🙌"
            
            
            await message.add_reaction(emoji_tosco)

    await bot.process_commands(message)

@bot.tree.command(name="gerenciar_produtos", description="[Administração] Gerencie os Produtos da Lojinha da LuaBot!")
async def gerenciar(interaction: discord.Interaction):

    if not verificar_gestor(interaction.user):
        return await interaction.response.send_message("💻 Você não tem permissão pra gerenciar minha loja!", ephemeral=True)
    await interaction.response.send_message("Funcionando!")


@bot.tree.command(name="ban", description="Joga o martelo em alguém que quebrou as regras :D")
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
            f"<:lua_ban_hammer:1429136081768419480> {user.mention} foi banido! Alguém quebrou as regras do servidor >:C",
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

@bot.tree.command(name="monica_coringa_ata", description="Veja um coringa no pc kkk")
async def coringa_ata(interaction: discord.Interaction):
    with open('commands_assets/monica_ata.png', 'rb') as coringa:
        image = discord.File(coringa)
        await interaction.response.send_message(file=image)

@bot.tree.command(name="eventos", description="Veja se tem algum evento disponível na LuaBot!")
async def eventos(interaction: discord.Interaction):
    avaible_events = "Aniversário da Lua - Feliz 1 Ano Luinha!"

    await interaction.response.send_message(f"O Evento disponível é o(a) **{avaible_events}**!")

bot.run(TOKEN)