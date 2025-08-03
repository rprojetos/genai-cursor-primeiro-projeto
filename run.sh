#!/bin/bash

# Script para executar o projeto FastAPI

echo "🚀 Iniciando o projeto FastAPI..."

# Verificar se o Python está disponível
if command -v python3 &> /dev/null; then
    echo "✅ Python 3 encontrado"
    
    # Tentar executar o projeto
    echo "📡 Iniciando servidor na porta 8000..."
    echo "🌐 Acesse: http://localhost:8000"
    echo "📚 Documentação: http://localhost:8000/docs"
    echo ""
    echo "Pressione Ctrl+C para parar o servidor"
    echo ""
    
    python3 main.py
else
    echo "❌ Python 3 não encontrado"
    echo "Por favor, instale o Python 3 primeiro"
    exit 1
fi 