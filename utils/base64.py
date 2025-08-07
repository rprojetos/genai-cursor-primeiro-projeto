"""
Módulo de Funções Base64
Contém funções para codificar e decodificar strings usando Base64.
"""

import base64
from typing import Union

def encode64(texto: str) -> str:
    """
    Codifica uma string para Base64.
    
    Args:
        texto: String a ser codificada
        
    Returns:
        String codificada em Base64
        
    Raises:
        TypeError: Se o texto não for uma string
    """
    if not isinstance(texto, str):
        raise TypeError("O texto deve ser uma string!")
    
    # Converte a string para bytes usando UTF-8
    bytes_texto = texto.encode('utf-8')
    
    # Codifica para Base64
    bytes_codificados = base64.b64encode(bytes_texto)
    
    # Converte de volta para string
    return bytes_codificados.decode('utf-8')

def decode64(texto_codificado: str) -> str:
    """
    Decodifica uma string Base64 para texto original.
    
    Args:
        texto_codificado: String codificada em Base64
        
    Returns:
        String decodificada
        
    Raises:
        TypeError: Se o texto não for uma string
        ValueError: Se o texto não for um Base64 válido
    """
    if not isinstance(texto_codificado, str):
        raise TypeError("O texto deve ser uma string!")
    
    try:
        # Converte a string para bytes
        bytes_codificados = texto_codificado.encode('utf-8')
        
        # Decodifica de Base64
        bytes_decodificados = base64.b64decode(bytes_codificados)
        
        # Converte de volta para string
        return bytes_decodificados.decode('utf-8')
    
    except Exception as e:
        raise ValueError(f"Erro ao decodificar Base64: {str(e)}")

def encode64_url_safe(texto: str) -> str:
    """
    Codifica uma string para Base64 URL-safe (usando - e _ em vez de + e /).
    
    Args:
        texto: String a ser codificada
        
    Returns:
        String codificada em Base64 URL-safe
    """
    if not isinstance(texto, str):
        raise TypeError("O texto deve ser uma string!")
    
    bytes_texto = texto.encode('utf-8')
    bytes_codificados = base64.urlsafe_b64encode(bytes_texto)
    return bytes_codificados.decode('utf-8')

def decode64_url_safe(texto_codificado: str) -> str:
    """
    Decodifica uma string Base64 URL-safe para texto original.
    
    Args:
        texto_codificado: String codificada em Base64 URL-safe
        
    Returns:
        String decodificada
    """
    if not isinstance(texto_codificado, str):
        raise TypeError("O texto deve ser uma string!")
    
    try:
        bytes_codificados = texto_codificado.encode('utf-8')
        bytes_decodificados = base64.urlsafe_b64decode(bytes_codificados)
        return bytes_decodificados.decode('utf-8')
    
    except Exception as e:
        raise ValueError(f"Erro ao decodificar Base64 URL-safe: {str(e)}")

def encode64_bytes(dados: bytes) -> str:
    """
    Codifica bytes para Base64.
    
    Args:
        dados: Bytes a serem codificados
        
    Returns:
        String codificada em Base64
    """
    if not isinstance(dados, bytes):
        raise TypeError("Os dados devem ser bytes!")
    
    bytes_codificados = base64.b64encode(dados)
    return bytes_codificados.decode('utf-8')

def decode64_bytes(texto_codificado: str) -> bytes:
    """
    Decodifica uma string Base64 para bytes.
    
    Args:
        texto_codificado: String codificada em Base64
        
    Returns:
        Bytes decodificados
    """
    if not isinstance(texto_codificado, str):
        raise TypeError("O texto deve ser uma string!")
    
    try:
        bytes_codificados = texto_codificado.encode('utf-8')
        return base64.b64decode(bytes_codificados)
    
    except Exception as e:
        raise ValueError(f"Erro ao decodificar Base64: {str(e)}")

def verificar_base64(texto: str) -> bool:
    """
    Verifica se uma string é um Base64 válido.
    
    Args:
        texto: String a ser verificada
        
    Returns:
        True se for Base64 válido, False caso contrário
    """
    if not isinstance(texto, str):
        return False
    
    try:
        bytes_codificados = texto.encode('utf-8')
        base64.b64decode(bytes_codificados)
        return True
    except Exception:
        return False

if __name__ == "__main__":
    # Exemplos de uso
    print("=== Funções Base64 ===")
    
    # Exemplo básico
    texto_original = "Olá, mundo! Este é um teste de Base64."
    print(f"Texto original: {texto_original}")
    
    # Encode
    texto_codificado = encode64(texto_original)
    print(f"Texto codificado: {texto_codificado}")
    
    # Decode
    texto_decodificado = decode64(texto_codificado)
    print(f"Texto decodificado: {texto_decodificado}")
    
    print(f"Codificação/Decodificação funcionou: {texto_original == texto_decodificado}")
    
    # Exemplo URL-safe
    print("\n=== Base64 URL-Safe ===")
    texto_url = "https://exemplo.com/path?param=value"
    print(f"URL original: {texto_url}")
    
    url_codificada = encode64_url_safe(texto_url)
    print(f"URL codificada: {url_codificada}")
    
    url_decodificada = decode64_url_safe(url_codificada)
    print(f"URL decodificada: {url_decodificada}")
    
    # Verificação
    print(f"\nVerificação Base64 válido: {verificar_base64(texto_codificado)}")
    print(f"Verificação texto inválido: {verificar_base64('texto inválido!')}") 