from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import random

app = FastAPI()

# modelo do usuário
class Usuario(BaseModel):
    id: int
    nome: str
    email: str

# simulando um "banco de dados"
usuarios = []

# criar usuário (CREATE)
@app.post("/usuarios")
def criar_usuario(usuario: Usuario):
    for u in usuarios:
        if u.id == usuario.id:
            raise HTTPException(status_code=400, detail="ID já existe")
    usuarios.append(usuario)
    return {"mensagem": "Usuário criado com sucesso"}

# listar todos os usuários (READ)
@app.get("/usuarios")
def listar_usuarios():
    return usuarios

# buscar usuário por ID (READ)
@app.get("/usuarios/{usuario_id}")
def buscar_usuario(usuario_id: int):
    for u in usuarios:
        if u.id == usuario_id:
            return u
    raise HTTPException(status_code=404, detail="Usuário não encontrado")

# atualizar usuário (UPDATE)
@app.put("/usuarios/{usuario_id}")
def atualizar_usuario(usuario_id: int, dados: Usuario):
    for i in range(len(usuarios)):
        if usuarios[i].id == usuario_id:
            usuarios[i] = dados
            return {"mensagem": "Usuário atualizado"}
    raise HTTPException(status_code=404, detail="Usuário não encontrado")

# deletar usuário (DELETE)
@app.delete("/usuarios/{usuario_id}")
def deletar_usuario(usuario_id: int):
    for u in usuarios:
        if u.id == usuario_id:
            usuarios.remove(u)
            return {"mensagem": "Usuário removido"}
    raise HTTPException(status_code=404, detail="Usuário não encontrado")

# deletar usuário aleatório (DELETE)
@app.delete("/usuarios/")
def deletar_usuario_aleatorio():
    id = random.randint(1, len(usuarios))

    usuarios.remove(usuarios[id - 1])
    return{"mensagem": f"Usuário {id} removido com sucesso!"}