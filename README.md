# Hello World API

Este é um projeto simples criado com FastAPI para demonstrar uma API básica com rota hello-world.

## Funcionalidades

- ✅ Endpoint hello-world simples
- ✅ Documentação automática da API
- ✅ Endpoint de saúde da aplicação

## Instalação

O projeto funciona diretamente com Python 3 sem necessidade de ambiente virtual.

### 🔧 Setup Automático
Execute o script de setup para verificar e instalar dependências:
```bash
./setup.sh
```

### 📦 Instalação Manual
Se precisar instalar as dependências manualmente:

**Opção 1 - Instalar no sistema (recomendado):**
```bash
python3 -m pip install --break-system-packages fastapi uvicorn[standard]
```

**Opção 2 - Instalar para o usuário:**
```bash
python3 -m pip install --user fastapi uvicorn[standard]
```

**Opção 3 - Usar pacotes do sistema:**
```bash
sudo apt install python3-fastapi python3-uvicorn
```

### 🌍 Ambiente Virtual (Opcional)
Se quiser usar um ambiente virtual, crie em outro diretório:
```bash
cd /tmp
python3 -m venv fastapi_env
source fastapi_env/bin/activate
pip install -r /caminho/para/seu/projeto/requirements.txt
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
├── setup.sh            # Script de configuração
├── README.md           # Este arquivo
├── GITHUB_SETUP.md     # Instruções para GitHub
└── .gitignore          # Arquivos ignorados pelo Git
```

## Tecnologias utilizadas

- **FastAPI**: Framework web moderno para APIs
- **Uvicorn**: Servidor ASGI 