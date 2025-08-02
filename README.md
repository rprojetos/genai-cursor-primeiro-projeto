# Meu Primeiro Projeto FastAPI

Este é um projeto simples criado com FastAPI para demonstrar as funcionalidades básicas de uma API REST.

## Funcionalidades

- ✅ CRUD completo de itens
- ✅ Validação de dados com Pydantic
- ✅ Documentação automática da API
- ✅ Endpoints de saúde da aplicação

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

- `GET /` - Página inicial com informações da API
- `GET /items` - Listar todos os itens
- `GET /items/{id}` - Buscar item por ID
- `POST /items` - Criar novo item
- `PUT /items/{id}` - Atualizar item existente
- `DELETE /items/{id}` - Deletar item
- `GET /health` - Verificar saúde da aplicação

## Documentação da API

Após executar o servidor, acesse:
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## Exemplo de uso

### Criar um item
```bash
curl -X POST "http://localhost:8000/items" \
     -H "Content-Type: application/json" \
     -d '{
       "nome": "Produto Teste",
       "descricao": "Um produto de exemplo",
       "preco": 29.99,
       "disponivel": true
     }'
```

### Listar todos os itens
```bash
curl -X GET "http://localhost:8000/items"
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
- **Pydantic**: Validação de dados
- **Uvicorn**: Servidor ASGI 