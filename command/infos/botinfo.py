import discord
from discord import ui
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='+', intents=intents)

class ButtonView(discord.ui.View):
    def __init__(self):
        super().__init__()

        self.add_item(discord.ui.Button(
            label="Website",
            url="https://theluabot.squareweb.app/"
        ))

class ButtonView(discord.ui.View):
    def __init__(self):
        super().__init__()

        self.add_item(discord.ui.Button(
            label="Website",
            url="https://theluabot.squareweb.app/"
        ))

@bot.tree.command(name="botinfo", description="[Info] Um pouquinho da História da LuaBot!")
async def botinfo(interaction: discord.Interaction):

    embed = discord.Embed(
        title="Au, Au! Eu sou a LuaBot!",
        description="Olá, eu me chamo LuaBot (mas meu nome é Lua!)!\n"
                    "**Fui desenvolvida para entreter os membros do seu servidor!** <:lua_emoji_reading:ID>"
    )

    embed.add_field(
        name="📅 História",
        value="Fui criada em **16 de Setembro de 2025**,\n"
              "mas meu aniversário é em **12 de Agosto!**\n"
              "E desde então transformei o mundo em um lugar melhor!",
        inline=False
    )

    embed.set_footer(text="PerfectTea © 2026")

    
    embed.set_image(url="https://imgur.com/oiTh7tz")

    view = ButtonView()

    await interaction.response.send_message(embed=embed, view=view)
