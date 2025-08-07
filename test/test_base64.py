"""
Testes para o módulo de funções Base64.
"""

import sys
import os
import unittest

# Adiciona o diretório raiz ao path para importar os módulos
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from utils.base64 import (
    encode64, decode64, encode64_url_safe, decode64_url_safe,
    encode64_bytes, decode64_bytes, verificar_base64
)

class TestBase64(unittest.TestCase):
    """Testes para as funções Base64."""
    
    def test_encode64_decode64_basico(self):
        """Testa encode64 e decode64 com texto básico."""
        texto_original = "Olá, mundo!"
        texto_codificado = encode64(texto_original)
        texto_decodificado = decode64(texto_codificado)
        
        self.assertEqual(texto_original, texto_decodificado)
        self.assertIsInstance(texto_codificado, str)
        self.assertIsInstance(texto_decodificado, str)
    
    def test_encode64_decode64_texto_complexo(self):
        """Testa encode64 e decode64 com texto complexo."""
        texto_original = "Texto com acentos: áéíóú çãõ ñ"
        texto_codificado = encode64(texto_original)
        texto_decodificado = decode64(texto_codificado)
        
        self.assertEqual(texto_original, texto_decodificado)
    
    def test_encode64_decode64_texto_vazio(self):
        """Testa encode64 e decode64 com texto vazio."""
        texto_original = ""
        texto_codificado = encode64(texto_original)
        texto_decodificado = decode64(texto_codificado)
        
        self.assertEqual(texto_original, texto_decodificado)
    
    def test_encode64_decode64_texto_longo(self):
        """Testa encode64 e decode64 com texto longo."""
        texto_original = "Este é um texto muito longo que contém muitas palavras e caracteres especiais como: @#$%^&*()_+-=[]{}|;':\",./<>?`~"
        texto_codificado = encode64(texto_original)
        texto_decodificado = decode64(texto_codificado)
        
        self.assertEqual(texto_original, texto_decodificado)
    
    def test_encode64_tipo_invalido(self):
        """Testa encode64 com tipo inválido."""
        with self.assertRaises(TypeError):
            encode64(123)
        
        with self.assertRaises(TypeError):
            encode64(None)
        
        with self.assertRaises(TypeError):
            encode64([])
    
    def test_decode64_tipo_invalido(self):
        """Testa decode64 com tipo inválido."""
        with self.assertRaises(TypeError):
            decode64(123)
        
        with self.assertRaises(TypeError):
            decode64(None)
    
    def test_decode64_texto_invalido(self):
        """Testa decode64 com texto Base64 inválido."""
        with self.assertRaises(ValueError):
            decode64("texto inválido!")
        
        with self.assertRaises(ValueError):
            decode64("T2zDoSwgbXVuZG8h!")  # Base64 com caracteres inválidos
    
    def test_encode64_url_safe_decode64_url_safe(self):
        """Testa encode64_url_safe e decode64_url_safe."""
        texto_original = "https://exemplo.com/path?param=value&outro=123"
        texto_codificado = encode64_url_safe(texto_original)
        texto_decodificado = decode64_url_safe(texto_codificado)
        
        self.assertEqual(texto_original, texto_decodificado)
        self.assertIsInstance(texto_codificado, str)
        self.assertIsInstance(texto_decodificado, str)
        
        # Verifica se não contém caracteres problemáticos para URL
        self.assertNotIn('+', texto_codificado)
        self.assertNotIn('/', texto_codificado)
    
    def test_encode64_url_safe_tipo_invalido(self):
        """Testa encode64_url_safe com tipo inválido."""
        with self.assertRaises(TypeError):
            encode64_url_safe(123)
    
    def test_decode64_url_safe_tipo_invalido(self):
        """Testa decode64_url_safe com tipo inválido."""
        with self.assertRaises(TypeError):
            decode64_url_safe(123)
    
    def test_decode64_url_safe_texto_invalido(self):
        """Testa decode64_url_safe com texto inválido."""
        with self.assertRaises(ValueError):
            decode64_url_safe("texto inválido!")
    
    def test_encode64_bytes_decode64_bytes(self):
        """Testa encode64_bytes e decode64_bytes."""
        dados_originais = b"Bytes de teste com caracteres especiais: \x00\x01\x02"
        dados_codificados = encode64_bytes(dados_originais)
        dados_decodificados = decode64_bytes(dados_codificados)
        
        self.assertEqual(dados_originais, dados_decodificados)
        self.assertIsInstance(dados_codificados, str)
        self.assertIsInstance(dados_decodificados, bytes)
    
    def test_encode64_bytes_tipo_invalido(self):
        """Testa encode64_bytes com tipo inválido."""
        with self.assertRaises(TypeError):
            encode64_bytes("não são bytes")
        
        with self.assertRaises(TypeError):
            encode64_bytes(123)
    
    def test_decode64_bytes_tipo_invalido(self):
        """Testa decode64_bytes com tipo inválido."""
        with self.assertRaises(TypeError):
            decode64_bytes(123)
    
    def test_decode64_bytes_texto_invalido(self):
        """Testa decode64_bytes com texto inválido."""
        with self.assertRaises(ValueError):
            decode64_bytes("texto inválido!")
    
    def test_verificar_base64_valido(self):
        """Testa verificar_base64 com Base64 válido."""
        texto_valido = "T2zDoSwgbXVuZG8h"  # "Olá, mundo!" em Base64
        self.assertTrue(verificar_base64(texto_valido))
        
        texto_valido_vazio = ""  # String vazia é Base64 válido
        self.assertTrue(verificar_base64(texto_valido_vazio))
    
    def test_verificar_base64_invalido(self):
        """Testa verificar_base64 com Base64 inválido."""
        texto_invalido = "texto inválido!"
        self.assertFalse(verificar_base64(texto_invalido))
        
        texto_invalido_caracteres = "T2zDoSwgbXVuZG8h!"  # Base64 com caracteres extras
        self.assertFalse(verificar_base64(texto_invalido_caracteres))
    
    def test_verificar_base64_tipo_invalido(self):
        """Testa verificar_base64 com tipo inválido."""
        self.assertFalse(verificar_base64(123))
        self.assertFalse(verificar_base64(None))
        self.assertFalse(verificar_base64([]))
    
    def test_comparacao_base64_padrao_vs_url_safe(self):
        """Testa a diferença entre Base64 padrão e URL-safe."""
        texto_original = "Texto com caracteres especiais: +/="
        
        # Base64 padrão pode conter + e /
        texto_padrao = encode64(texto_original)
        
        # Base64 URL-safe substitui + por - e / por _
        texto_url_safe = encode64_url_safe(texto_original)
        
        # Decodifica ambos para verificar que são equivalentes
        texto_decodificado_padrao = decode64(texto_padrao)
        texto_decodificado_url = decode64_url_safe(texto_url_safe)
        
        self.assertEqual(texto_original, texto_decodificado_padrao)
        self.assertEqual(texto_original, texto_decodificado_url)
        
        # Verifica que são diferentes na codificação
        self.assertNotEqual(texto_padrao, texto_url_safe)
    
    def test_caracteres_especiais_unicode(self):
        """Testa encode64 e decode64 com caracteres Unicode."""
        texto_original = "Texto com emojis: 🚀🌟🎉 e caracteres especiais: 中文 Español Français"
        texto_codificado = encode64(texto_original)
        texto_decodificado = decode64(texto_codificado)
        
        self.assertEqual(texto_original, texto_decodificado)

if __name__ == '__main__':
    unittest.main() 