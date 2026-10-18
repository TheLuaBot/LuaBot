import discord
from discord import app_commands

from database import comprar_produto


PRODUTOS = (
    {"id": "biscoito_lunar", "nome": "Biscoito Lunar", "emoji": "🍪", "preco": 30},
    {"id": "pingente_de_lua", "nome": "Pingente de Lua", "emoji": "🌙", "preco": 90},
    {"id": "bolinha_estelar", "nome": "Bolinha Estelar", "emoji": "🎾", "preco": 150},
    {"id": "nuvem_de_descanso", "nome": "Nuvem de Descanso", "emoji": "☁️", "preco": 300},
)


class BotaoCompra(discord.ui.Button):
    def __init__(self, produto: dict[str, str | int]):
        super().__init__(
            label=f"{produto['preco']} MoonCoins",
            emoji=produto["emoji"],
            style=discord.ButtonStyle.primary,
            custom_id=f"lojinha:{produto['id']}",
        )
        self.produto = produto

    async def callback(self, interaction: discord.Interaction):
        comprado = await comprar_produto(
            interaction.user,
            self.produto["id"],
            self.produto["preco"],
        )

        if comprado:
            await interaction.response.send_message(
                f"{self.produto['emoji']} Você comprou **{self.produto['nome']}**!",
                ephemeral=True,
            )
            return

        await interaction.response.send_message(
            "❌ Você não tem MoonCoins suficientes para esse item.",
            ephemeral=True,
        )


class LojaView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=180)
        for produto in PRODUTOS:
            self.add_item(BotaoCompra(produto))


@app_commands.command(name="lojinha", description="Veja e compre itens com MoonCoins")
async def lojinha_command(interaction: discord.Interaction):
    embed = discord.Embed(
        title="🌙 Lojinha da LuaBot",
        description="Escolha um mimo para levar para casa:",
        color=discord.Color.gold(),
    )

    for produto in PRODUTOS:
        embed.add_field(
            name=f"{produto['emoji']} {produto['nome']}",
            value=f"🪙 {produto['preco']} MoonCoins",
            inline=True,
        )

    await interaction.response.send_message(embed=embed, view=LojaView())