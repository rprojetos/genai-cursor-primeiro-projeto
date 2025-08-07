"""
Módulo de Funções Matemáticas
Contém funções matemáticas úteis para cálculos básicos e avançados.
"""

import math
from typing import List

def soma(a: float, b: float) -> float:
    """Soma dois números."""
    return a + b

def subtracao(a: float, b: float) -> float:
    """Subtrai dois números."""
    return a - b

def multiplicacao(a: float, b: float) -> float:
    """Multiplica dois números."""
    return a * b

def divisao(a: float, b: float) -> float:
    """Divide dois números."""
    if b == 0:
        raise ZeroDivisionError("Não é possível dividir por zero!")
    return a / b

def potencia(base: float, expoente: float) -> float:
    """Calcula a potência de um número."""
    return math.pow(base, expoente)

def raiz_quadrada(numero: float) -> float:
    """Calcula a raiz quadrada de um número."""
    if numero < 0:
        raise ValueError("Não é possível calcular raiz quadrada de número negativo!")
    return math.sqrt(numero)

def fatorial(n: int) -> int:
    """Calcula o fatorial de um número."""
    if n < 0:
        raise ValueError("Não é possível calcular fatorial de número negativo!")
    if n == 0 or n == 1:
        return 1
    return n * fatorial(n - 1)

def media(lista_numeros: List[float]) -> float:
    """Calcula a média aritmética de uma lista de números."""
    if not lista_numeros:
        raise ValueError("A lista não pode estar vazia!")
    return sum(lista_numeros) / len(lista_numeros)

def maximo(lista_numeros: List[float]) -> float:
    """Encontra o valor máximo em uma lista de números."""
    if not lista_numeros:
        raise ValueError("A lista não pode estar vazia!")
    return max(lista_numeros)

def minimo(lista_numeros: List[float]) -> float:
    """Encontra o valor mínimo em uma lista de números."""
    if not lista_numeros:
        raise ValueError("A lista não pode estar vazia!")
    return min(lista_numeros)

def seno(angulo_radianos: float) -> float:
    """Calcula o seno de um ângulo em radianos."""
    return math.sin(angulo_radianos)

def cosseno(angulo_radianos: float) -> float:
    """Calcula o cosseno de um ângulo em radianos."""
    return math.cos(angulo_radianos)

def graus_para_radianos(graus: float) -> float:
    """Converte graus para radianos."""
    return math.radians(graus)

def radianos_para_graus(radianos: float) -> float:
    """Converte radianos para graus."""
    return math.degrees(radianos)

def valor_absoluto(numero: float) -> float:
    """Calcula o valor absoluto de um número."""
    return abs(numero)

def arredondar(numero: float, casas_decimais: int = 0) -> float:
    """Arredonda um número para um número específico de casas decimais."""
    return round(numero, casas_decimais)

def eh_par(numero: int) -> bool:
    """Verifica se um número é par."""
    return numero % 2 == 0

def eh_primo(numero: int) -> bool:
    """Verifica se um número é primo."""
    if numero < 2:
        return False
    if numero == 2:
        return True
    if numero % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(numero)) + 1, 2):
        if numero % i == 0:
            return False
    return True

def mdc(a: int, b: int) -> int:
    """Calcula o Máximo Divisor Comum (MDC) de dois números."""
    while b:
        a, b = b, a % b
    return abs(a)

def fibonacci(n: int) -> int:
    """Calcula o n-ésimo número da sequência de Fibonacci."""
    if n < 0:
        raise ValueError("O índice deve ser não negativo!")
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

# Constantes matemáticas
PI = math.pi
E = math.e
PHI = (1 + math.sqrt(5)) / 2  # Número áureo

if __name__ == "__main__":
    # Exemplos de uso
    print("=== Funções Matemáticas ===")
    print(f"Soma: 5 + 3 = {soma(5, 3)}")
    print(f"Potência: 2^8 = {potencia(2, 8)}")
    print(f"Fatorial de 5: {fatorial(5)}")
    print(f"7 é primo? {eh_primo(7)}")
    print(f"10º Fibonacci: {fibonacci(10)}")
    print(f"PI: {PI}") 