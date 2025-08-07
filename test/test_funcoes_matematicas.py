"""
Testes para o módulo de funções matemáticas.
"""

import sys
import os
import unittest

# Adiciona o diretório raiz ao path para importar os módulos
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from utils.funcoes_matematicas import (
    soma, subtracao, multiplicacao, divisao, potencia, raiz_quadrada,
    fatorial, media, maximo, minimo, seno, cosseno, graus_para_radianos,
    radianos_para_graus, valor_absoluto, arredondar, eh_par, eh_primo,
    mdc, fibonacci, PI, E, PHI
)

class TestFuncoesMatematicas(unittest.TestCase):
    """Testes para as funções matemáticas básicas."""
    
    def test_soma(self):
        """Testa a função soma."""
        self.assertEqual(soma(5, 3), 8)
        self.assertEqual(soma(-5, 3), -2)
        self.assertEqual(soma(0, 0), 0)
        self.assertEqual(soma(1.5, 2.5), 4.0)
    
    def test_subtracao(self):
        """Testa a função subtração."""
        self.assertEqual(subtracao(10, 4), 6)
        self.assertEqual(subtracao(5, 10), -5)
        self.assertEqual(subtracao(0, 0), 0)
        self.assertEqual(subtracao(3.5, 1.5), 2.0)
    
    def test_multiplicacao(self):
        """Testa a função multiplicação."""
        self.assertEqual(multiplicacao(6, 7), 42)
        self.assertEqual(multiplicacao(-3, 4), -12)
        self.assertEqual(multiplicacao(0, 5), 0)
        self.assertEqual(multiplicacao(2.5, 3), 7.5)
    
    def test_divisao(self):
        """Testa a função divisão."""
        self.assertEqual(divisao(15, 3), 5.0)
        self.assertEqual(divisao(10, 2), 5.0)
        self.assertEqual(divisao(7, 2), 3.5)
        
        # Testa divisão por zero
        with self.assertRaises(ZeroDivisionError):
            divisao(10, 0)
    
    def test_potencia(self):
        """Testa a função potência."""
        self.assertEqual(potencia(2, 8), 256)
        self.assertEqual(potencia(5, 0), 1)
        self.assertEqual(potencia(2, -1), 0.5)
        self.assertEqual(potencia(3, 3), 27)
    
    def test_raiz_quadrada(self):
        """Testa a função raiz quadrada."""
        self.assertEqual(raiz_quadrada(16), 4.0)
        self.assertEqual(raiz_quadrada(0), 0.0)
        self.assertEqual(raiz_quadrada(2), 2**0.5)
        
        # Testa raiz de número negativo
        with self.assertRaises(ValueError):
            raiz_quadrada(-4)
    
    def test_fatorial(self):
        """Testa a função fatorial."""
        self.assertEqual(fatorial(0), 1)
        self.assertEqual(fatorial(1), 1)
        self.assertEqual(fatorial(5), 120)
        self.assertEqual(fatorial(10), 3628800)
        
        # Testa fatorial de número negativo
        with self.assertRaises(ValueError):
            fatorial(-5)
    
    def test_media(self):
        """Testa a função média."""
        self.assertEqual(media([1, 2, 3, 4, 5]), 3.0)
        self.assertEqual(media([10]), 10.0)
        self.assertEqual(media([1.5, 2.5, 3.5]), 2.5)
        
        # Testa lista vazia
        with self.assertRaises(ValueError):
            media([])
    
    def test_maximo(self):
        """Testa a função máximo."""
        self.assertEqual(maximo([1, 5, 3, 9, 2, 8]), 9)
        self.assertEqual(maximo([-5, -10, -1]), -1)
        self.assertEqual(maximo([1.5, 2.5, 1.0]), 2.5)
        
        # Testa lista vazia
        with self.assertRaises(ValueError):
            maximo([])
    
    def test_minimo(self):
        """Testa a função mínimo."""
        self.assertEqual(minimo([1, 5, 3, 9, 2, 8]), 1)
        self.assertEqual(minimo([-5, -10, -1]), -10)
        self.assertEqual(minimo([1.5, 2.5, 1.0]), 1.0)
        
        # Testa lista vazia
        with self.assertRaises(ValueError):
            minimo([])
    
    def test_seno(self):
        """Testa a função seno."""
        self.assertAlmostEqual(seno(0), 0.0, places=7)
        self.assertAlmostEqual(seno(3.14159/2), 1.0, places=5)
        self.assertAlmostEqual(seno(3.14159), 0.0, places=5)
    
    def test_cosseno(self):
        """Testa a função cosseno."""
        self.assertAlmostEqual(cosseno(0), 1.0, places=7)
        self.assertAlmostEqual(cosseno(3.14159/2), 0.0, places=5)
        self.assertAlmostEqual(cosseno(3.14159), -1.0, places=5)
    
    def test_graus_para_radianos(self):
        """Testa a conversão de graus para radianos."""
        self.assertAlmostEqual(graus_para_radianos(0), 0.0, places=7)
        self.assertAlmostEqual(graus_para_radianos(180), 3.14159, places=5)
        self.assertAlmostEqual(graus_para_radianos(360), 2 * 3.14159, places=5)
    
    def test_radianos_para_graus(self):
        """Testa a conversão de radianos para graus."""
        self.assertAlmostEqual(radianos_para_graus(0), 0.0, places=7)
        self.assertAlmostEqual(radianos_para_graus(3.14159), 180.0, places=2)
        self.assertAlmostEqual(radianos_para_graus(2 * 3.14159), 360.0, places=2)
    
    def test_valor_absoluto(self):
        """Testa a função valor absoluto."""
        self.assertEqual(valor_absoluto(5), 5)
        self.assertEqual(valor_absoluto(-5), 5)
        self.assertEqual(valor_absoluto(0), 0)
        self.assertEqual(valor_absoluto(-3.5), 3.5)
    
    def test_arredondar(self):
        """Testa a função arredondar."""
        self.assertEqual(arredondar(3.14159), 3)
        self.assertEqual(arredondar(3.14159, 2), 3.14)
        self.assertEqual(arredondar(3.14159, 4), 3.1416)
        self.assertEqual(arredondar(-3.7), -4)
    
    def test_eh_par(self):
        """Testa a função eh_par."""
        self.assertTrue(eh_par(2))
        self.assertTrue(eh_par(0))
        self.assertTrue(eh_par(-4))
        self.assertFalse(eh_par(1))
        self.assertFalse(eh_par(-3))
    
    def test_eh_primo(self):
        """Testa a função eh_primo."""
        self.assertTrue(eh_primo(2))
        self.assertTrue(eh_primo(3))
        self.assertTrue(eh_primo(7))
        self.assertTrue(eh_primo(11))
        self.assertFalse(eh_primo(1))
        self.assertFalse(eh_primo(4))
        self.assertFalse(eh_primo(9))
        self.assertFalse(eh_primo(0))
        self.assertFalse(eh_primo(-5))
    
    def test_mdc(self):
        """Testa a função MDC."""
        self.assertEqual(mdc(48, 18), 6)
        self.assertEqual(mdc(12, 18), 6)
        self.assertEqual(mdc(7, 13), 1)
        self.assertEqual(mdc(0, 5), 5)
        self.assertEqual(mdc(5, 0), 5)
    
    def test_fibonacci(self):
        """Testa a função Fibonacci."""
        self.assertEqual(fibonacci(0), 0)
        self.assertEqual(fibonacci(1), 1)
        self.assertEqual(fibonacci(2), 1)
        self.assertEqual(fibonacci(3), 2)
        self.assertEqual(fibonacci(4), 3)
        self.assertEqual(fibonacci(5), 5)
        self.assertEqual(fibonacci(10), 55)
        
        # Testa índice negativo
        with self.assertRaises(ValueError):
            fibonacci(-1)
    
    def test_constantes(self):
        """Testa as constantes matemáticas."""
        self.assertIsInstance(PI, float)
        self.assertIsInstance(E, float)
        self.assertIsInstance(PHI, float)
        self.assertGreater(PI, 3.0)
        self.assertGreater(E, 2.0)
        self.assertGreater(PHI, 1.0)

if __name__ == '__main__':
    unittest.main() 