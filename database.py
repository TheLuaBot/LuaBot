# Talvez tenha alguns erros ou sei lá aqui pois não sei mexer tanto com mongo db e fiz essa db vendo um tutorial no yt :C

import pymongo
from dotenv import load_dotenv
import os


load_dotenv()
client = pymongo.MongoClient(os.getenv("MONGODB_TOKEN"))

db = client["lua_db_economy"]
usuarios = db["usuarios"]

async def new_user(usuario):
    filtro = {"discord_id":usuario.id}

    if usuarios.count_documents(filtro) == 0:
        objeto = {
            "discord_id":usuario.id,
            "moedas":50
        }

        usuarios.insert_one(objeto)
        return objeto
    else:
        return False

async def checar_saldo(usuario):

    await new_user(usuario)

    filtro = {"discord_id":usuario.id}
    resultado = usuarios.find(filtro)

    return resultado.__getitem__(0)["moedas"]

async def transferir(usuario,quantidade):
    await new_user(usuario)

    mooncoins_atuais = await checar_saldo(usuario)

    filtro = {"discord_id":usuario.id}
    relacao = {"$set": {
        "moedas": mooncoins_atuais+quantidade
    }}

    usuarios.update_one(filtro,relacao)
