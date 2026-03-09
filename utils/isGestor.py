import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

load_dotenv()

CARGO_GESTOR = int(os.getenv("CARGO_GESTOR")) # ID do Cargo de Gestor no Server da LuaBot!

def verificar_gestor(membro: discord.Member):
    for cargo in membro.roles:
        if cargo.id == CARGO_GESTOR:
            return True