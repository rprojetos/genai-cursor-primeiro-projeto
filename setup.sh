#!/bin/bash

# Script de setup para o projeto FastAPI

echo "🔧 Configurando o ambiente para o projeto FastAPI..."

# 1. Verificar se o Python 3 está disponível
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 não encontrado. Por favor, instale o Python 3."
    exit 1
fi
echo "✅ Python 3 encontrado: $(python3 --version)"

# 2. Verificar se o pip está disponível
if ! python3 -m pip --version &> /dev/null; then
    echo "❌ pip para Python 3 não encontrado. Tente instalar com 'sudo apt install python3-pip'."
    exit 1
fi
echo "✅ pip encontrado."

# 3. Criar e ativar um ambiente virtual
if [ ! -d "venv" ]; then
    echo "🐍 Criando ambiente virtual na pasta 'venv'..."
    python3 -m venv venv
    if [ $? -ne 0 ]; then
        echo "❌ Falha ao criar o ambiente virtual."
        exit 1
    fi
else
    echo "🐍 Ambiente virtual 'venv' já existe."
fi

echo "⚡ Ativando o ambiente virtual..."
source venv/bin/activate

# 4. Instalar dependências do requirements.txt
if [ -f "requirements.txt" ]; then
    echo "📦 Instalando dependências de requirements.txt..."
    pip install -r requirements.txt
    if [ $? -ne 0 ]; then
        echo "❌ Falha ao instalar as dependências."
        echo "💡 Tente executar 'pip install -r requirements.txt' manualmente após ativar o ambiente com 'source venv/bin/activate'."
        exit 1
    fi
    echo "✅ Dependências instaladas com sucesso!"
else
    echo "⚠️ Arquivo requirements.txt não encontrado. Pulando instalação de dependências."
fi

echo ""
echo "🎉 Setup concluído!"
echo "Agora você pode iniciar a API com o comando:"
echo "./run.sh"