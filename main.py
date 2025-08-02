from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import uvicorn

# Criando a instância da aplicação FastAPI
app = FastAPI(
    title="Meu Primeiro Projeto FastAPI",
    description="Uma API simples criada com FastAPI",
    version="1.0.0"
)

# Modelo Pydantic para os dados
class Item(BaseModel):
    id: Optional[int] = None
    nome: str
    descricao: Optional[str] = None
    preco: float
    disponivel: bool = True

# Lista para armazenar os itens (simulando um banco de dados)
items_db = []
item_id_counter = 1

# Endpoint raiz
@app.get("/")
async def root():
    return {
        "mensagem": "Bem-vindo ao meu primeiro projeto FastAPI!",
        "endpoints_disponiveis": [
            "GET /items - Listar todos os itens",
            "GET /items/{id} - Buscar item por ID",
            "POST /items - Criar novo item",
            "PUT /items/{id} - Atualizar item",
            "DELETE /items/{id} - Deletar item"
        ]
    }

# Endpoint para listar todos os itens
@app.get("/items", response_model=List[Item])
async def listar_items():
    return items_db

# Endpoint para buscar item por ID
@app.get("/items/{item_id}", response_model=Item)
async def buscar_item(item_id: int):
    for item in items_db:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item não encontrado")

# Endpoint para criar novo item
@app.post("/items", response_model=Item)
async def criar_item(item: Item):
    global item_id_counter
    item.id = item_id_counter
    item_id_counter += 1
    items_db.append(item)
    return item

# Endpoint para atualizar item
@app.put("/items/{item_id}", response_model=Item)
async def atualizar_item(item_id: int, item_atualizado: Item):
    for i, item in enumerate(items_db):
        if item.id == item_id:
            item_atualizado.id = item_id
            items_db[i] = item_atualizado
            return item_atualizado
    raise HTTPException(status_code=404, detail="Item não encontrado")

# Endpoint para deletar item
@app.delete("/items/{item_id}")
async def deletar_item(item_id: int):
    for i, item in enumerate(items_db):
        if item.id == item_id:
            item_removido = items_db.pop(i)
            return {"mensagem": f"Item '{item_removido.nome}' removido com sucesso"}
    raise HTTPException(status_code=404, detail="Item não encontrado")

# Endpoint de saúde da aplicação
@app.get("/health")
async def health_check():
    return {"status": "ok", "mensagem": "Aplicação funcionando normalmente"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000) 