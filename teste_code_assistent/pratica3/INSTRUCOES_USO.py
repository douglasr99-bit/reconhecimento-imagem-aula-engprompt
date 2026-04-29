"""
PRÁTICA 3 - INSTRUÇÕES DE USO

Execute este arquivo para começar a prática de debug!
"""

import os
import sys

def exibir_menu():
    """Exibe menu de opções."""
    print("\n" + "=" * 70)
    print("PRÁTICA 3 - DEBUG COM IA")
    print("=" * 70)
    print("""
Escolha uma opção:

1. 📄 Ver GUIA de Erros e Soluções (RECOMENDADO PRIMEIRO)
2. ❌ Tentar executar código COM ERROS (vai quebrar)
3. ✅ Executar código CORRIGIDO (vai funcionar)
4. 📖 Ver Referência Rápida
5. 🧪 Executar Testes do Código Corrigido
6. 📊 Comparar Antes vs Depois
7. ❓ Instruções

0. Sair

Digite o número da opção: """)


def exibir_instrucoes():
    """Exibe instruções de uso."""
    print("""
INSTRUÇÕES DA PRÁTICA 3:

📌 O QUE VOCÊ VAI APRENDER:
   - Identificar diferentes tipos de erros em Python
   - Ler e interpretar mensagens de erro
   - Propor soluções para cada erro
   - Debugar código de forma eficiente

📌 PASSO A PASSO RECOMENDADO:
   
   1️⃣  LEIA o arquivo GUIA_ERROS_E_SOLUCOES.md
       - Entenda cada tipo de erro
       - Veja exemplos antes e depois
   
   2️⃣  VEJA a Referência Rápida
       - Consulta rápida durante debug
   
   3️⃣  EXAMINE pratica3_com_erros.py
       - Código com 15 erros intencionais
       - Tente identificar cada um
   
   4️⃣  ESTUDE pratica3_corrigido.py
       - Veja como todos os erros foram corrigidos
       - Compare com o original
   
   5️⃣  EXECUTE os testes
       - Rode pratica3_corrigido.py para ver funcionar

📌 DESAFIO PESSOAL:
   
   Pegue um código seu com erros e:
   ✓ Liste todos os erros encontrados
   ✓ Categorie os tipos (Syntax, Logic, Runtime)
   ✓ Explique a causa de cada um
   ✓ Proponha correções
   ✓ Teste as correções

📌 ARQUIVOS IMPORTANTES:

   GUIA_ERROS_E_SOLUCOES.md
   └─ Análise completa de cada erro
      • O erro original
      • Por que é um erro
      • Como corrigir
      • Dicas para evitar

   pratica3_com_erros.py
   └─ Código com 15 erros propositais
      • Nenhuma função funciona
      • Use como material de estudo

   pratica3_corrigido.py
   └─ Código completamente funcional
      • Todos os erros corrigidos
      • Inclui testes automatizados
      • Type hints e documentação

   REFERENCIA_RAPIDA.py
   └─ Consulta rápida durante debug
      • Resumo de erros comuns
      • Estratégia de debug
      • Tabela de erros

📌 COMO DEBUGAR EFICIENTEMENTE:

   ⚙️ ANTES (Improviso):
      - Chutar soluções
      - Tentar tudo aleatoricamente
      - Gastar muito tempo

   ⚙️ DEPOIS (Sistemático):
      1. Ler a mensagem de erro com atenção
      2. Identificar o tipo (NameError, TypeError, etc.)
      3. Ir para a linha indicada
      4. Verificar sintaxe
      5. Adicionar prints para debug
      6. Usar linter (pylint, flake8)
      7. Consultar documentação

📌 LISTA DE VERIFICAÇÃO:

   Quando encontrar um erro:
   □ Qual é o tipo? (SyntaxError, NameError, etc.)
   □ Em qual linha?
   □ Qual é a mensagem completa?
   □ Qual deveria ser o comportamento correto?
   □ Como corrigir?
   □ Como evitar no futuro?

📌 PRÓXIMOS PASSOS:

   Após completar esta prática:
   1. Faça debugging de um código antigo seu
   2. Implemente testes unitários
   3. Use type hints em todo novo código
   4. Configure linter no VS Code
   5. Aprenda a usar o debugger Python

Boa sorte! 🚀
""")


def tentar_codigo_com_erros():
    """Tenta executar código com erros."""
    print("\n" + "=" * 70)
    print("EXECUTANDO: pratica3_com_erros.py")
    print("=" * 70)
    print("\n⚠️  ESTE CÓDIGO TEM ERROS! Espere uma falha...\n")
    
    try:
        # Simular a execução
        print("Tentando executar...\n")
        
        # ERRO 1: Parênteses não fechado
        print("❌ ERRO 1: SyntaxError - Parênteses não fechado")
        print("   Arquivo: pratica3_com_erros.py, linha 13")
        print("   def calcular_media(notas")
        print("                                ^")
        print("   SyntaxError: '(' sem fechamento\n")
        
        # Não consegue nem compilar o arquivo
        print("Código não pode ser executado devido a erro de sintaxe!")
        print("\n💡 Próximo passo: Abra pratica3_com_erros.py e corrija o erro!")
        
    except Exception as e:
        print(f"❌ Erro: {type(e).__name__}: {e}\n")


def executar_codigo_corrigido():
    """Executa código corrigido."""
    print("\n" + "=" * 70)
    print("EXECUTANDO: pratica3_corrigido.py")
    print("=" * 70)
    print("\n✅ ESTE CÓDIGO FUNCIONA!\n")
    
    try:
        import subprocess
        resultado = subprocess.run(
            [sys.executable, 
             "pratica3_corrigido.py"],
            capture_output=True,
            text=True,
            timeout=10
        )
        print(resultado.stdout)
        if resultado.stderr:
            print("Erros:", resultado.stderr)
    except FileNotFoundError:
        print("⚠️ Arquivo pratica3_corrigido.py não encontrado")
        print("   Verifique se você está na pasta correta")
    except Exception as e:
        print(f"Erro ao executar: {e}")


def exibir_referencia():
    """Exibe referência rápida."""
    print("\n" + "=" * 70)
    print("REFERÊNCIA RÁPIDA - ERROS COMUNS")
    print("=" * 70)
    print("""
1️⃣  SyntaxError
    Problema: Erro de escrita (parênteses, pontuação)
    Solução: Verifique sintaxe cuidadosamente
    Exemplo: def funcao(  # Faltou fechar

2️⃣  IndentationError
    Problema: Indentação incorreta
    Solução: Use 4 espaços consistentemente
    Exemplo:
    if True:
    print("Sem indentação")  # Erro!

3️⃣  NameError
    Problema: Variável não existe
    Solução: Defina antes de usar
    Exemplo: print(resultado)  # Não foi definido

4️⃣  TypeError
    Problema: Tipos incompatíveis
    Solução: Converta tipos conforme necessário
    Exemplo: "texto" + 10  # Erro!

5️⃣  IndexError
    Problema: Índice fora de intervalo
    Solução: Verifique tamanho antes
    Exemplo: lista[10]  # Lista tem só 3 elementos

6️⃣  KeyError
    Problema: Chave não existe em dicionário
    Solução: Use .get() em vez de []
    Exemplo: dados["email"]  # Chave não existe

7️⃣  AttributeError
    Problema: Método não existe
    Solução: Verifique nome do método
    Exemplo: "texto".maiuscula()  # Deve ser upper()

8️⃣  ValueError
    Problema: Valor inválido para operação
    Solução: Valide entrada antes de processar
    Exemplo: int("abc")  # Não é número

Veja GUIA_ERROS_E_SOLUCOES.md para análise completa!
""")


def comparar_antes_depois():
    """Compara código antes e depois."""
    print("\n" + "=" * 70)
    print("COMPARAÇÃO: ANTES vs DEPOIS")
    print("=" * 70)
    print("""
ANTES (Com Erros):
─────────────────────────────────────────────────────

def calcular_media(notas          # ❌ Parêntese não fechado
    return sum(notas) / len(notas)

a = 10
b = 20
if a < b:                          # ❌ Indentação errada
print("resultado")

resultado = lista[10]             # ❌ Índice fora do intervalo


DEPOIS (Corrigido):
─────────────────────────────────────────────────────

def calcular_media(notas: List[float]) -> float:  # ✅ Correto
    \"\"\"Calcula a média das notas.\"\"\"
    return sum(notas) / len(notas)

numero_a = 10                     # ✅ Nome descritivo
numero_b = 20
if numero_a < numero_b:           # ✅ Indentação correta
    print("resultado")

if lista:                         # ✅ Validação antes
    resultado = lista[0]


DIFERENÇAS PRINCIPAIS:
✓ Nomes descritivos (a, b → numero_a, numero_b)
✓ Sintaxe corrigida (parênteses, indentação)
✓ Type hints adicionados
✓ Validações implementadas
✓ Docstrings adicionadas
✓ Tratamento de erros
""")


def menu_principal():
    """Loop principal do menu."""
    while True:
        exibir_menu()
        
        try:
            opcao = input().strip()
            
            if opcao == "1":
                print("\n📖 Abrindo GUIA_ERROS_E_SOLUCOES.md...")
                print("(Verifique em: teste_code_assistent/pratica3/)\n")
                print("Conteúdo principal disponível para leitura.")
                
            elif opcao == "2":
                tentar_codigo_com_erros()
                
            elif opcao == "3":
                executar_codigo_corrigido()
                
            elif opcao == "4":
                exibir_referencia()
                
            elif opcao == "5":
                print("\n✅ Executando testes...")
                executar_codigo_corrigido()
                
            elif opcao == "6":
                comparar_antes_depois()
                
            elif opcao == "7":
                exibir_instrucoes()
                
            elif opcao == "0":
                print("\nAté logo! 👋")
                break
                
            else:
                print("\n❌ Opção inválida. Tente novamente!")
                
        except KeyboardInterrupt:
            print("\n\nProgramado interrompido.")
            break
        except Exception as e:
            print(f"\n❌ Erro: {e}")


if __name__ == "__main__":
    print("""
╔════════════════════════════════════════════════════════════════════╗
║                   BEM-VINDO À PRÁTICA 3                           ║
║               DEBUG COM IA - APRENDENDO A DEBUGAR                 ║
╚════════════════════════════════════════════════════════════════════╝
""")
    
    menu_principal()
