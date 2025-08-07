"""
Testes para a API FastAPI (main.py).
"""

import sys
import os
import unittest
from fastapi.testclient import TestClient

# Adiciona o diretório raiz ao path para importar os módulos
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from main import app

class TestFastAPI(unittest.TestCase):
    """Testes para a API FastAPI."""
    
    def setUp(self):
        """Configura o cliente de teste."""
        self.client = TestClient(app)
    
    def test_hello_world_endpoint(self):
        """Testa o endpoint hello-world (/)"""
        response = self.client.get("/")
        
        # Verifica status code
        self.assertEqual(response.status_code, 200)
        
        # Verifica estrutura da resposta
        data = response.json()
        self.assertIn("mensagem", data)
        self.assertIn("status", data)
        self.assertIn("api", data)
        
        # Verifica valores específicos
        self.assertEqual(data["mensagem"], "Hello World!")
        self.assertEqual(data["status"], "success")
        self.assertEqual(data["api"], "FastAPI")
    
    def test_health_check_endpoint(self):
        """Testa o endpoint de health check (/health)"""
        response = self.client.get("/health")
        
        # Verifica status code
        self.assertEqual(response.status_code, 200)
        
        # Verifica estrutura da resposta
        data = response.json()
        self.assertIn("status", data)
        self.assertIn("mensagem", data)
        
        # Verifica valores específicos
        self.assertEqual(data["status"], "ok")
        self.assertEqual(data["mensagem"], "Aplicação funcionando normalmente")
    
    def test_endpoint_not_found(self):
        """Testa endpoint inexistente"""
        response = self.client.get("/endpoint-inexistente")
        
        # Verifica status code 404
        self.assertEqual(response.status_code, 404)
    
    def test_hello_world_response_model(self):
        """Testa se a resposta do hello-world segue o modelo Pydantic"""
        response = self.client.get("/")
        data = response.json()
        
        # Verifica tipos dos campos
        self.assertIsInstance(data["mensagem"], str)
        self.assertIsInstance(data["status"], str)
        self.assertIsInstance(data["api"], str)
    
    def test_health_check_response_model(self):
        """Testa se a resposta do health check segue o modelo Pydantic"""
        response = self.client.get("/health")
        data = response.json()
        
        # Verifica tipos dos campos
        self.assertIsInstance(data["status"], str)
        self.assertIsInstance(data["mensagem"], str)
    
    def test_api_documentation_available(self):
        """Testa se a documentação da API está disponível"""
        response = self.client.get("/docs")
        
        # Verifica se a documentação está disponível (status 200)
        self.assertEqual(response.status_code, 200)
        
        # Verifica se contém elementos da documentação
        content = response.text
        self.assertIn("FastAPI", content)
        self.assertIn("Hello World API", content)
    
    def test_openapi_schema_available(self):
        """Testa se o schema OpenAPI está disponível"""
        response = self.client.get("/openapi.json")
        
        # Verifica status code
        self.assertEqual(response.status_code, 200)
        
        # Verifica estrutura do schema
        schema = response.json()
        self.assertIn("openapi", schema)
        self.assertIn("info", schema)
        self.assertIn("paths", schema)
        
        # Verifica informações da API
        info = schema["info"]
        self.assertEqual(info["title"], "Hello World API")
        self.assertEqual(info["version"], "1.0.0")
        self.assertIn("Uma API simples com rota hello-world", info["description"])
    
    def test_hello_world_method_not_allowed(self):
        """Testa método não permitido no endpoint hello-world"""
        response = self.client.post("/")
        
        # Verifica status code 405 (Method Not Allowed)
        self.assertEqual(response.status_code, 405)
    
    def test_health_check_method_not_allowed(self):
        """Testa método não permitido no endpoint health check"""
        response = self.client.post("/health")
        
        # Verifica status code 405 (Method Not Allowed)
        self.assertEqual(response.status_code, 405)

if __name__ == '__main__':
    unittest.main() 