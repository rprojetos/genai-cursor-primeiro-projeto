from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel

# Criando a instância da aplicação FastAPI
app = FastAPI(
    title="Hello World API",
    description="Uma API simples com rota hello-world",
    version="1.0.0"
)

# Modelos de resposta (Boas práticas com Pydantic)
class HelloWorldResponse(BaseModel):
    mensagem: str
    status: str
    api: str

class HealthCheckResponse(BaseModel):
    status: str
    mensagem: str

# Endpoint hello-world
@app.get("/", response_model=HelloWorldResponse)
async def hello_world():
    return HelloWorldResponse(mensagem="Hello World!", status="success", api="FastAPI")

# Endpoint de saúde da aplicação
@app.get("/health", response_model=HealthCheckResponse)
async def health_check():
    return HealthCheckResponse(status="ok", mensagem="status app ok")


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000) 