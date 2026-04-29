"""
COMPARAÇÃO VISUAL: ANTES vs DEPOIS

Este arquivo mostra exemplos práticos de transformações
aplicadas durante a refatoração.
"""

print("=" * 70)
print("COMPARAÇÃO: CÓDIGO ORIGINAL vs REFATORADO")
print("=" * 70)

# ============================================================================
# PROBLEMA 1: NOMES GENÉRICOS
# ============================================================================

print("\n" + "=" * 70)
print("PROBLEMA 1: NOMES GENÉRICOS")
print("=" * 70)

# ❌ ANTES - Ruim
print("\n❌ ANTES (Ruim):")
print("""
a = 10
b = 20
c = a + b
print(c)
""")
print("Problema: Qual é o significado de a, b, c? É impossível saber!")

# ✅ DEPOIS - Bom
print("\n✅ DEPOIS (Bom):")
print("""
preco_produto = 10
quantidade = 20
total = preco_produto * quantidade
print(f"Total: R$ {total}")
""")
print("Benefício: Código auto-explicativo, claro!")

# ============================================================================
# PROBLEMA 2: REPETIÇÃO DE CÓDIGO (DRY)
# ============================================================================

print("\n" + "=" * 70)
print("PROBLEMA 2: REPETIÇÃO DE CÓDIGO (VIOLAÇÃO DE DRY)")
print("=" * 70)

# ❌ ANTES - Ruim
print("\n❌ ANTES (Ruim):")
print("""
if a < b:
    c = a + b
    print("resultado:", c)
else:
    c = a - b
    print("resultado:", c)

# Repetição desnecessária
if a < b:
    c = a + b
    print("de novo:", c)
else:
    c = a - b
    print("de novo:", c)
""")
print("Problemas:")
print("- Código duplicado em 2 lugares")
print("- Se precisar mudar a lógica, 2 alterações necessárias")
print("- Risco de bugs: um lugar é alterado, outro não")

# ✅ DEPOIS - Bom
print("\n✅ DEPOIS (Bom):")
print("""
def calcular_operacao(numero_a: int, numero_b: int) -> int:
    '''Calcula a soma se a < b, senão a diferença.'''
    if numero_a < numero_b:
        return numero_a + numero_b
    return numero_a - numero_b

resultado1 = calcular_operacao(10, 20)
print(f"Resultado 1: {resultado1}")

resultado2 = calcular_operacao(10, 20)
print(f"Resultado 2: {resultado2}")
""")
print("Benefícios:")
print("- Uma única implementação reutilizável")
print("- Alteração em um lugar afeta todas as chamadas")
print("- Código mais fácil de manter")
print("- Princípio DRY aplicado")

# ============================================================================
# PROBLEMA 3: CÓDIGO MORTO
# ============================================================================

print("\n" + "=" * 70)
print("PROBLEMA 3: CÓDIGO MORTO")
print("=" * 70)

# ❌ ANTES - Ruim
print("\n❌ ANTES (Ruim):")
print("""
d = 100
if d < 50:
    print("nunca vai acontecer")
""")
print("Problema: d é 100, então d < 50 NUNCA será verdadeiro")
print("Confunde desenvolvedores, aumenta complexidade")

# ✅ DEPOIS - Bom
print("\n✅ DEPOIS (Bom):")
print("""
# Código morto removido
# Mais limpo e focado
""")
print("Benefício: Código genuinamente útil")

# ============================================================================
# PROBLEMA 4: MISTURA DE RESPONSABILIDADES
# ============================================================================

print("\n" + "=" * 70)
print("PROBLEMA 4: MISTURA DE RESPONSABILIDADES")
print("=" * 70)

# ❌ ANTES - Ruim
print("\n❌ ANTES (Ruim):")
print("""
nome = input("digite seu nome: ")
idade = input("idade: ")

if idade == "18":  # Compara STRING "18", não inteiro!
    print(nome + " é maior de idade")
else:
    print("não sei")
""")
print("Problemas:")
print("- Compara string "18", não inteiro 18")
print("- Pessoa com 19, 25, 30 anos seria MENOR de idade (BUG!)")
print("- Input + Validação + Output misturados")
print("- Sem tratamento de erro se digitar "abc"")
print("- Mensagem vaga: "não sei"")

# ✅ DEPOIS - Bom
print("\n✅ DEPOIS (Bom):")
print("""
from typing import Tuple

def eh_maior_de_idade(idade: int) -> bool:
    \"\"\"Verifica se é maior de idade.\"\"\"
    return idade >= 18

def obter_dados_usuario() -> Tuple[str, int]:
    \"\"\"Coleta dados do usuário com validação.\"\"\"
    nome = input("Digite seu nome: ").strip()
    
    while True:
        try:
            idade = int(input("Digite sua idade: ").strip())
            if idade < 0:
                print("⚠️ Idade não pode ser negativa.")
                continue
            return nome, idade
        except ValueError:
            print("⚠️ Deve ser um número válido.")

def processar_maioridade(nome: str, idade: int) -> str:
    \"\"\"Formata mensagem sobre maioridade.\"\"\"
    if eh_maior_de_idade(idade):
        return f"✓ {nome} ({idade} anos) é maior de idade"
    return f"✗ {nome} ({idade} anos) é menor de idade"

nome, idade = obter_dados_usuario()
print(processar_maioridade(nome, idade))
""")
print("Benefícios:")
print("- Responsabilidades bem separadas")
print("- Compara INTEIRO, não string (correto!)")
print("- Funciona para 18, 19, 25, 30+ anos")
print("- Tratamento de erro robusto")
print("- Mensagens claras e informativas")
print("- Cada função é reutilizável")

# ============================================================================
# PROBLEMA 5: FALTA DE DOCUMENTAÇÃO
# ============================================================================

print("\n" + "=" * 70)
print("PROBLEMA 5: FALTA DE DOCUMENTAÇÃO (DOCSTRINGS)")
print("=" * 70)

# ❌ ANTES - Ruim
print("\n❌ ANTES (Ruim):")
print("""
def calcular(x, y):
    if x < y:
        return x + y
    return x - y
""")
print("Problema: Como saber o que a função faz?")

# ✅ DEPOIS - Bom
print("\n✅ DEPOIS (Bom):")
print("""
def calcular_operacao(numero_a: int, numero_b: int) -> int:
    \"\"\"
    Calcula a soma se a < b, caso contrário a diferença.
    
    Args:
        numero_a: Primeiro número inteiro
        numero_b: Segundo número inteiro
    
    Returns:
        int: Resultado da operação (soma ou diferença)
    \"\"\"
    if numero_a < numero_b:
        return numero_a + numero_b
    return numero_a - numero_b
""")
print("Benefícios:")
print("- Clareza instantânea do propósito")
print("- Parâmetros documentados")
print("- Retorno documentado")
print("- IDE mostra automaticamente ao chamar a função")

# ============================================================================
# RESUMO DAS TRANSFORMAÇÕES
# ============================================================================

print("\n" + "=" * 70)
print("📊 RESUMO DAS TRANSFORMAÇÕES")
print("=" * 70)

transformacoes = {
    "Variáveis sem sentido": "✓ Renomeadas com descrição clara",
    "Código repetido": "✓ Extraído em função reutilizável",
    "Código morto": "✓ Removido",
    "Sem documentação": "✓ Docstrings adicionadas",
    "Sem type hints": "✓ Type hints adicionados",
    "Sem tratamento de erro": "✓ Try/except implementado",
    "Responsabilidades misturadas": "✓ Separadas em funções",
    "Validação fraca": "✓ Validação robusta",
}

for problema, solucao in transformacoes.items():
    print(f"{problema:.<40} {solucao}")

print("\n" + "=" * 70)
print("✅ RESULTADO: Código mais limpo, legível e manutenível!")
print("=" * 70)
