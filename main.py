import discord
from discord import app_commands
from discord.ext import commands
from dotenv import load_dotenv
import random
import os

from database import *

load_dotenv()

TOKEN = os.getenv("TOKEN")


intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='+', intents=intents)

textos = (
    "🌙| Use meus novos comandos! /saldo e /daily!"
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



bot.run(TOKEN)  
