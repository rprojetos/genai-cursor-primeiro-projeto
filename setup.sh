#!/bin/bash

# Script de setup para o projeto FastAPI

echo "🔧 Configurando o projeto FastAPI..."

# Verificar se o Python está disponível
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 não encontrado"
    echo "Por favor, instale o Python 3 primeiro"
    exit 1
fi

echo "✅ Python 3 encontrado: $(python3 --version)"

# Tentar diferentes métodos de instalação
echo "📦 Tentando instalar dependências..."

# Método 1: Tentar instalar com --break-system-packages
echo "🔄 Tentando instalar com --break-system-packages..."
if python3 -m pip install --break-system-packages fastapi uvicorn[standard]; then
    echo "✅ Dependências instaladas com sucesso!"
    exit 0
fi

# Método 2: Tentar instalar com --user
echo "🔄 Tentando instalar com --user..."
if python3 -m pip install --user fastapi uvicorn[standard]; then
    echo "✅ Dependências instaladas com sucesso!"
    exit 0
fi

# Método 3: Tentar criar ambiente virtual em /tmp
echo "🔄 Tentando criar ambiente virtual em /tmp..."
if cd /tmp && python3 -m venv fastapi_temp_env; then
    echo "✅ Ambiente virtual criado em /tmp/fastapi_temp_env"
    echo "📝 Para ativar: source /tmp/fastapi_temp_env/bin/activate"
    echo "📝 Para instalar: pip install -r /media/rprojetos/rprojetos/0_0_gitspace/rprojetos/generative-ia/genai-cursor/genai-cursor-primeiro-projeto/requirements.txt"
    exit 0
fi

# Método 4: Verificar se já está instalado
echo "🔄 Verificando se as dependências já estão instaladas..."
if python3 -c "import fastapi, uvicorn; print('✅ Dependências já estão instaladas!')" 2>/dev/null; then
    echo "✅ Dependências já estão disponíveis!"
    exit 0
fi

echo "❌ Não foi possível instalar as dependências automaticamente"
echo ""
echo "💡 Soluções alternativas:"
echo "1. Execute: sudo apt install python3-fastapi python3-uvicorn"
echo "2. Ou use: python3 -m pip install --break-system-packages fastapi uvicorn[standard]"
echo "3. Ou crie um ambiente virtual manualmente em outro diretório"
echo ""
echo "🚀 O projeto pode funcionar sem instalar as dependências se elas já estiverem no sistema" 