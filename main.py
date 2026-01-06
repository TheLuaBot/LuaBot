import discord
from discord.ext import commands
from dotenv import load_dotenv
import os 

load_dotenv()

TOKEN = os.getenv("TOKEN")

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='+', intents=intents)

textos = (
    "🌙| Atualizando!"
)

@bot.event
async def on_ready():
    print(f"LuaBot Online! - {bot.user.name} ({bot.user.id})")
    await bot.tree.sync()
    await bot.change_presence(
        activity=discord.CustomActivity(
            textos
        )
    )

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
async def ajuda(interaction: discord.Interaction, user: discord.Member):
  await interaction.response.send_message("Olá! meu prefixo nesse servidor é "/", :3")

bot.run(TOKEN)
