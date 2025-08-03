from fastapi import FastAPI
import uvicorn

# Criando a instância da aplicação FastAPI
app = FastAPI(
    title="Hello World API",
    description="Uma API simples com rota hello-world",
    version="1.0.0"
)

# Endpoint hello-world
@app.get("/")
async def hello_world():
    return {
        "mensagem": "Hello World!",
        "status": "success",
        "api": "FastAPI"
    }

# Endpoint de saúde da aplicação
@app.get("/health")
async def health_check():
    return {"status": "ok", "mensagem": "Aplicação funcionando normalmente"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000) 