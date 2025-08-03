# Hello World API

Este é um projeto simples criado com FastAPI para demonstrar uma API básica com rota hello-world.

## Funcionalidades

- ✅ Endpoint hello-world simples
- ✅ Documentação automática da API
- ✅ Endpoint de saúde da aplicação

## Instalação

O projeto funciona diretamente com Python 3 sem necessidade de ambiente virtual.

**Nota:** Se você quiser usar um ambiente virtual, pode criar um:
```bash
python3 -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Como executar

### Opção 1: Usar o script de execução (Recomendado)
```bash
./run.sh
```

### Opção 2: Executar diretamente
```bash
python3 main.py
```

### Opção 3: Usar uvicorn
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

### Acessar a documentação interativa
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## Estrutura do projeto

```
genai-cursor-primeiro-projeto/
├── main.py              # Arquivo principal da aplicação
├── requirements.txt     # Dependências do projeto (opcional)
├── run.sh              # Script de execução
├── README.md           # Este arquivo
├── GITHUB_SETUP.md     # Instruções para GitHub
└── .gitignore          # Arquivos ignorados pelo Git
```

## Tecnologias utilizadas

- **FastAPI**: Framework web moderno para APIs
- **Uvicorn**: Servidor ASGI 