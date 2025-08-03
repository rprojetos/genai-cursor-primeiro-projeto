# Hello World API

Este é um projeto simples criado com FastAPI para demonstrar uma API básica com rota hello-world.

## Funcionalidades

- ✅ Endpoint hello-world simples
- ✅ Documentação automática da API
- ✅ Endpoint de saúde da aplicação

## Instalação

1. Crie um ambiente virtual (recomendado):
```bash
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

## Como executar

### Opção 1: Executar diretamente
```bash
python main.py
```

### Opção 2: Usar uvicorn
```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

## Endpoints disponíveis

- `GET /` - Endpoint hello-world
- `GET /health` - Verificar saúde da aplicação

## Documentação da API

Após executar o servidor, acesse:
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## Exemplo de uso

### Testar o endpoint hello-world
```bash
curl -X GET "http://localhost:8000/"
```

### Verificar saúde da aplicação
```bash
curl -X GET "http://localhost:8000/health"
```

## Estrutura do projeto

```
primeiro_projeto/
├── main.py              # Arquivo principal da aplicação
├── requirements.txt     # Dependências do projeto
└── README.md           # Este arquivo
```

## Tecnologias utilizadas

- **FastAPI**: Framework web moderno para APIs
- **Uvicorn**: Servidor ASGI 