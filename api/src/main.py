from fastapi import FastAPI, HTTPException
from db.perfilDB import ver_perfil


app = FastAPI()

# Rotas

@app.get("/perfil/{user_id}")
async def catch_perfil(user_id: str):
    ver_perfil()