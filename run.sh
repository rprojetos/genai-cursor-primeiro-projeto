#!/bin/bash

# Script para executar o projeto FastAPI

VENV_DIR="venv"

# Tenta ativar o ambiente virtual se ele existir e não estiver ativo
if [ -d "$VENV_DIR" ] && [ -z "$VIRTUAL_ENV" ]; then
    echo "🐍 Ativando ambiente virtual..."
    source "$VENV_DIR/bin/activate"
fi

echo "🚀 Iniciando o projeto FastAPI..."

# Verificar se o ambiente virtual está ativado
if [ -z "$VIRTUAL_ENV" ]; then
    echo "⚠️  Ambiente virtual não ativado!"
    echo "Por favor, execute o script de setup primeiro: ./setup.sh"
    exit 1
fi

# Verificar se o uvicorn está disponível no ambiente virtual
if ! command -v uvicorn &> /dev/null; then
    echo "❌ O comando 'uvicorn' não foi encontrado."
    echo "Certifique-se de que as dependências foram instaladas com './setup.sh'."
    exit 1
fi

echo "📡 Iniciando servidor na porta 8000..."
echo "🌐 Acesse: http://localhost:8000"
echo "📚 Documentação: http://localhost:8000/docs"
echo ""
echo "Pressione Ctrl+C para parar o servidor"
echo ""

# Usar uvicorn diretamente para aproveitar o --reload durante o desenvolvimento
uvicorn main:app --reload --host 0.0.0.0 --port 8000