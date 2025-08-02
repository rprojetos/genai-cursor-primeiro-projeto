#!/usr/bin/env python3
"""
Script de teste para demonstrar o uso da API FastAPI
"""

import requests
import json
import time

# URL base da API
BASE_URL = "http://localhost:8000"

def test_api():
    """Função para testar todos os endpoints da API"""
    
    print("🚀 Iniciando testes da API FastAPI...")
    print("=" * 50)
    
    # Teste 1: Verificar se a API está rodando
    try:
        response = requests.get(f"{BASE_URL}/health")
        if response.status_code == 200:
            print("✅ API está funcionando!")
        else:
            print("❌ API não está respondendo corretamente")
            return
    except requests.exceptions.ConnectionError:
        print("❌ Não foi possível conectar à API. Certifique-se de que ela está rodando.")
        print("Execute: python main.py ou uvicorn main:app --reload")
        return
    
    # Teste 2: Endpoint raiz
    print("\n📋 Testando endpoint raiz...")
    response = requests.get(f"{BASE_URL}/")
    if response.status_code == 200:
        data = response.json()
        print(f"✅ Endpoint raiz: {data['mensagem']}")
    
    # Teste 3: Listar itens (deve estar vazio inicialmente)
    print("\n📦 Testando listagem de itens...")
    response = requests.get(f"{BASE_URL}/items")
    if response.status_code == 200:
        items = response.json()
        print(f"✅ Itens encontrados: {len(items)}")
    
    # Teste 4: Criar um item
    print("\n➕ Testando criação de item...")
    novo_item = {
        "nome": "Produto Teste",
        "descricao": "Um produto criado durante o teste",
        "preco": 29.99,
        "disponivel": True
    }
    
    response = requests.post(
        f"{BASE_URL}/items",
        headers={"Content-Type": "application/json"},
        data=json.dumps(novo_item)
    )
    
    if response.status_code == 200:
        item_criado = response.json()
        print(f"✅ Item criado com ID: {item_criado['id']}")
        item_id = item_criado['id']
    else:
        print(f"❌ Erro ao criar item: {response.status_code}")
        return
    
    # Teste 5: Buscar item por ID
    print(f"\n🔍 Testando busca do item {item_id}...")
    response = requests.get(f"{BASE_URL}/items/{item_id}")
    if response.status_code == 200:
        item = response.json()
        print(f"✅ Item encontrado: {item['nome']} - R$ {item['preco']}")
    
    # Teste 6: Atualizar item
    print(f"\n✏️ Testando atualização do item {item_id}...")
    item_atualizado = {
        "nome": "Produto Atualizado",
        "descricao": "Produto modificado durante o teste",
        "preco": 39.99,
        "disponivel": False
    }
    
    response = requests.put(
        f"{BASE_URL}/items/{item_id}",
        headers={"Content-Type": "application/json"},
        data=json.dumps(item_atualizado)
    )
    
    if response.status_code == 200:
        item_modificado = response.json()
        print(f"✅ Item atualizado: {item_modificado['nome']} - R$ {item_modificado['preco']}")
    
    # Teste 7: Listar itens novamente
    print("\n📦 Listando itens após modificação...")
    response = requests.get(f"{BASE_URL}/items")
    if response.status_code == 200:
        items = response.json()
        print(f"✅ Total de itens: {len(items)}")
        for item in items:
            print(f"   - {item['nome']} (ID: {item['id']})")
    
    # Teste 8: Deletar item
    print(f"\n🗑️ Testando remoção do item {item_id}...")
    response = requests.delete(f"{BASE_URL}/items/{item_id}")
    if response.status_code == 200:
        resultado = response.json()
        print(f"✅ {resultado['mensagem']}")
    
    # Teste 9: Verificar se o item foi removido
    print(f"\n🔍 Verificando se o item {item_id} foi removido...")
    response = requests.get(f"{BASE_URL}/items/{item_id}")
    if response.status_code == 404:
        print("✅ Item foi removido com sucesso!")
    else:
        print("❌ Item ainda existe")
    
    print("\n" + "=" * 50)
    print("🎉 Todos os testes foram concluídos!")

if __name__ == "__main__":
    test_api() 