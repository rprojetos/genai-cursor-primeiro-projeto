#!/usr/bin/env python3
"""
Script para executar todos os testes do projeto.
"""

import sys
import os
import unittest
import subprocess

def run_all_tests():
    """Executa todos os testes do projeto."""
    print("🚀 Executando todos os testes do projeto...")
    print("=" * 50)
    
    # Adiciona o diretório raiz ao path
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    sys.path.insert(0, project_root)
    
    # Lista de módulos de teste
    test_modules = [
        "test_funcoes_matematicas",
        "test_base64", 
        "test_main"
    ]
    
    # Contadores
    total_tests = 0
    passed_tests = 0
    failed_tests = 0
    
    # Executa cada módulo de teste
    for module_name in test_modules:
        print(f"\n📋 Executando testes: {module_name}")
        print("-" * 30)
        
        try:
            # Importa e executa o módulo de teste
            module = __import__(f"test.{module_name}", fromlist=["*"])
            
            # Cria um test suite
            loader = unittest.TestLoader()
            suite = loader.loadTestsFromModule(module)
            
            # Executa os testes
            runner = unittest.TextTestRunner(verbosity=2)
            result = runner.run(suite)
            
            # Atualiza contadores
            total_tests += result.testsRun
            passed_tests += result.testsRun - len(result.failures) - len(result.errors)
            failed_tests += len(result.failures) + len(result.errors)
            
        except Exception as e:
            print(f"❌ Erro ao executar {module_name}: {e}")
            failed_tests += 1
    
    # Resumo final
    print("\n" + "=" * 50)
    print("📊 RESUMO DOS TESTES")
    print("=" * 50)
    print(f"Total de testes: {total_tests}")
    print(f"Testes aprovados: {passed_tests}")
    print(f"Testes falharam: {failed_tests}")
    
    if failed_tests == 0:
        print("✅ Todos os testes passaram!")
        return True
    else:
        print("❌ Alguns testes falharam!")
        return False

def run_specific_test(module_name):
    """Executa um módulo de teste específico."""
    print(f"🚀 Executando testes: {module_name}")
    print("=" * 50)
    
    try:
        # Importa e executa o módulo de teste
        module = __import__(f"test.{module_name}", fromlist=["*"])
        
        # Cria um test suite
        loader = unittest.TestLoader()
        suite = loader.loadTestsFromModule(module)
        
        # Executa os testes
        runner = unittest.TextTestRunner(verbosity=2)
        result = runner.run(suite)
        
        return len(result.failures) + len(result.errors) == 0
        
    except Exception as e:
        print(f"❌ Erro ao executar {module_name}: {e}")
        return False

def run_with_coverage():
    """Executa os testes com cobertura de código."""
    print("🚀 Executando testes com cobertura...")
    
    try:
        # Verifica se o coverage está instalado
        import coverage
    except ImportError:
        print("❌ Coverage não está instalado. Instalando...")
        subprocess.run([sys.executable, "-m", "pip", "install", "coverage"])
    
    # Executa com coverage
    cmd = [
        sys.executable, "-m", "coverage", "run", 
        "--source=utils,main", 
        "-m", "unittest", "discover", "test", "-v"
    ]
    
    result = subprocess.run(cmd, capture_output=True, text=True)
    
    if result.returncode == 0:
        print("✅ Testes executados com sucesso!")
        
        # Gera relatório de cobertura
        subprocess.run([sys.executable, "-m", "coverage", "report"])
        subprocess.run([sys.executable, "-m", "coverage", "html"])
        print("📊 Relatório de cobertura gerado em htmlcov/index.html")
    else:
        print("❌ Erro ao executar testes com cobertura:")
        print(result.stderr)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        command = sys.argv[1]
        
        if command == "coverage":
            run_with_coverage()
        elif command in ["math", "funcoes_matematicas"]:
            run_specific_test("test_funcoes_matematicas")
        elif command in ["base64", "base"]:
            run_specific_test("test_base64")
        elif command in ["api", "main", "fastapi"]:
            run_specific_test("test_main")
        else:
            print(f"❌ Comando desconhecido: {command}")
            print("Comandos disponíveis:")
            print("  - coverage: Executa testes com cobertura")
            print("  - math: Executa testes das funções matemáticas")
            print("  - base64: Executa testes das funções Base64")
            print("  - api: Executa testes da API FastAPI")
            print("  - (sem argumentos): Executa todos os testes")
    else:
        run_all_tests() 