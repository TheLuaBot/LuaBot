
import pymongo
from dotenv import load_dotenv
import os

load_dotenv()

client = pymongo.MongoClient(os.getenv("MONGODB_TOKEN"))

db = client["users-luabot"]
usuarios = db["usuarios"]

async def new_user(usuario):
     

     if usuarios.count_documents == 0:
        objeto = {
            "discord_id":usuario.id,
            "username":usuario.name
            }
        usuarios.insert_one(objeto)
        return objeto
     else:
        return False
     
async def ver_perfil(usuario):

    await new_user(usuario)

    filtro = {"discord_id":usuario.id}
    resultado = usuarios.find(filtro)

    return resultado
