"""
PRÁTICA 4 - EXEMPLOS DE EXECUÇÃO ANOTADOS

Este arquivo mostra como cada função do código refatorado funciona
na prática, com exemplos de entrada e saída comentados.
"""

from typing import Tuple


# ============================================================================
# EXEMPLO 1: calcular_operacao()
# ============================================================================
print("=" * 70)
print("EXEMPLO 1: calcular_operacao()")
print("=" * 70)

def calcular_operacao(numero_a: int, numero_b: int) -> int:
    """Calcula a soma se a < b, caso contrário calcula a diferença."""
    # Esta função testa: numero_a < numero_b
    # Se verdadeiro: retorna soma
    # Se falso: retorna diferença
    
    if numero_a < numero_b:
        return numero_a + numero_b
    return numero_a - numero_b


# TESTE 1
print("\nTESTE 1: calcular_operacao(10, 20)")
print("├─ 10 < 20? SIM")
print("├─ Retorna: 10 + 20 = 30")
resultado1 = calcular_operacao(10, 20)
print(f"└─ Resultado: {resultado1}")

# TESTE 2
print("\nTESTE 2: calcular_operacao(30, 20)")
print("├─ 30 < 20? NÃO")
print("├─ Retorna: 30 - 20 = 10")
resultado2 = calcular_operacao(30, 20)
print(f"└─ Resultado: {resultado2}")

# TESTE 3
print("\nTESTE 3: calcular_operacao(20, 20)")
print("├─ 20 < 20? NÃO")
print("├─ Retorna: 20 - 20 = 0")
resultado3 = calcular_operacao(20, 20)
print(f"└─ Resultado: {resultado3}")


# ============================================================================
# EXEMPLO 2: calcular_valor_final()
# ============================================================================
print("\n" + "=" * 70)
print("EXEMPLO 2: calcular_valor_final()")
print("=" * 70)

def calcular_valor_final(valor_string: str) -> int:
    """Converte string para inteiro e adiciona 5."""
    try:
        # Tenta converter a string para inteiro
        valor_numerico = int(valor_string)
        # Se funcionar, adiciona 5 e retorna
        return valor_numerico + 5
    except ValueError:
        # Se der erro, lança exceção com mensagem clara
        raise ValueError(f"Erro: '{valor_string}' não é um número válido")


# TESTE 1: Conversão válida
print("\nTESTE 1: calcular_valor_final('123')")
print("├─ int('123') = 123")
print("├─ 123 + 5 = 128")
try:
    resultado1 = calcular_valor_final("123")
    print(f"└─ Resultado: {resultado1}")
except ValueError as e:
    print(f"└─ ERRO: {e}")

# TESTE 2: Conversão inválida
print("\nTESTE 2: calcular_valor_final('abc')")
print("├─ int('abc') = ValueError!")
print("├─ Exceção capturada")
try:
    resultado2 = calcular_valor_final("abc")
    print(f"└─ Resultado: {resultado2}")
except ValueError as e:
    print(f"└─ ERRO: {e}")

# TESTE 3: Conversão de número negativo
print("\nTESTE 3: calcular_valor_final('-10')")
print("├─ int('-10') = -10")
print("├─ -10 + 5 = -5")
try:
    resultado3 = calcular_valor_final("-10")
    print(f"└─ Resultado: {resultado3}")
except ValueError as e:
    print(f"└─ ERRO: {e}")


# ============================================================================
# EXEMPLO 3: eh_maior_de_idade()
# ============================================================================
print("\n" + "=" * 70)
print("EXEMPLO 3: eh_maior_de_idade()")
print("=" * 70)

def eh_maior_de_idade(idade: int) -> bool:
    """Verifica se a pessoa é maior de idade."""
    # Simples: retorna True se idade >= 18, senão False
    return idade >= 18


# TESTE 1
print("\nTESTE 1: eh_maior_de_idade(25)")
print("├─ 25 >= 18? SIM")
resultado1 = eh_maior_de_idade(25)
print(f"└─ Resultado: {resultado1}")

# TESTE 2
print("\nTESTE 2: eh_maior_de_idade(18)")
print("├─ 18 >= 18? SIM (Iguais contam!)")
resultado2 = eh_maior_de_idade(18)
print(f"└─ Resultado: {resultado2}")

# TESTE 3
print("\nTESTE 3: eh_maior_de_idade(17)")
print("├─ 17 >= 18? NÃO")
resultado3 = eh_maior_de_idade(17)
print(f"└─ Resultado: {resultado3}")


# ============================================================================
# EXEMPLO 4: processar_maioridade()
# ============================================================================
print("\n" + "=" * 70)
print("EXEMPLO 4: processar_maioridade()")
print("=" * 70)

def processar_maioridade(nome: str, idade: int) -> str:
    """Formata mensagem sobre maioridade."""
    # Chama eh_maior_de_idade() internamente
    # Formata mensagem diferente para cada caso
    if eh_maior_de_idade(idade):
        return f"✓ {nome} ({idade} anos) é maior de idade"
    else:
        return f"✗ {nome} ({idade} anos) é menor de idade"


# TESTE 1
print("\nTESTE 1: processar_maioridade('João', 25)")
print("├─ eh_maior_de_idade(25)? SIM")
print("├─ Formata mensagem com ✓")
resultado1 = processar_maioridade("João", 25)
print(f"└─ Resultado: {resultado1}")

# TESTE 2
print("\nTESTE 2: processar_maioridade('Ana', 16)")
print("├─ eh_maior_de_idade(16)? NÃO")
print("├─ Formata mensagem com ✗")
resultado2 = processar_maioridade("Ana", 16)
print(f"└─ Resultado: {resultado2}")

# TESTE 3
print("\nTESTE 3: processar_maioridade('Maria', 18)")
print("├─ eh_maior_de_idade(18)? SIM")
print("├─ Formata mensagem com ✓")
resultado3 = processar_maioridade("Maria", 18)
print(f"└─ Resultado: {resultado3}")


# ============================================================================
# EXEMPLO 5: exibir_contador()
# ============================================================================
print("\n" + "=" * 70)
print("EXEMPLO 5: exibir_contador()")
print("=" * 70)

def exibir_contador(iteracoes: int = 3) -> None:
    """Exibe um contador com lógica clara."""
    # Loop que itera de 0 a iteracoes-1
    # Exibe "Iteração 1", "Iteração 2", etc.
    # Na última iteração, exibe mensagem especial
    
    for numero in range(iteracoes):
        print(f"Iteração {numero + 1}")
        
        if numero == iteracoes - 1:
            print("✓ Fim das iterações")


# TESTE 1: Padrão (3 iterações)
print("\nTESTE 1: exibir_contador()")
print("├─ Sem parâmetro → usa padrão: 3")
exibir_contador()

# TESTE 2: Customizado (5 iterações)
print("\nTESTE 2: exibir_contador(5)")
print("├─ 5 iterações solicitadas")
exibir_contador(5)


# ============================================================================
# EXEMPLO 6: FLUXO COMPLETO
# ============================================================================
print("\n" + "=" * 70)
print("EXEMPLO 6: FLUXO COMPLETO")
print("=" * 70)

# Simulando desempacotamento de tupla
print("\nSimulando: obter_dados_usuario()")
print("├─ Coleta nome do usuário")
print("├─ Coleta idade do usuário")
print("├─ Retorna tupla (nome, idade)")

# Simulação: usuário digita "Pedro" e "30"
nome_simulado = "Pedro"
idade_simulada = 30

print(f"├─ Entrada: {nome_simulado}, {idade_simulada}")

# Desempacotamento
nome, idade = (nome_simulado, idade_simulada)
print(f"├─ Desempacotando: nome={nome}, idade={idade}")

# Processa maioridade
mensagem = processar_maioridade(nome, idade)
print(f"├─ Resultado: {mensagem}")


# ============================================================================
# EXEMPLO 7: TRATAMENTO DE ERROS
# ============================================================================
print("\n" + "=" * 70)
print("EXEMPLO 7: TRATAMENTO DE ERROS")
print("=" * 70)

print("\nTRY/EXCEPT em ação:")
print("├─ Tentando: calcular_valor_final('123abc')")

try:
    print("│  ├─ Entra no TRY")
    resultado = calcular_valor_final("123abc")
    print("│  ├─ Conversão bem-sucedida (nunca chega aqui)")
except ValueError as erro:
    print("│  ├─ ValueError lançado!")
    print(f"│  ├─ Entra no EXCEPT: {erro}")
    print("│  └─ Erro tratado com sucesso")


# ============================================================================
# EXEMPLO 8: DESEMPACOTAMENTO DE TUPLA
# ============================================================================
print("\n" + "=" * 70)
print("EXEMPLO 8: DESEMPACOTAMENTO DE TUPLA")
print("=" * 70)

print("\nO que é desempacotamento?")
print("├─ Tupla retornada: ('João', 25)")
print("├─ Atribuição simples:")
resultado_tupla = ("João", 25)
print(f"│  resultado_tupla = {resultado_tupla}")
print("├─ Desempacotamento:")
nome, idade = resultado_tupla
print(f"│  nome, idade = resultado_tupla")
print(f"│  nome = {nome}")
print(f"│  idade = {idade}")
print("└─ Agora pode usar as variáveis separadamente!")


# ============================================================================
# RESUMO VISUAL
# ============================================================================
print("\n" + "=" * 70)
print("RESUMO: COMO AS FUNÇÕES SE CONECTAM")
print("=" * 70)

print("""
main()
  │
  ├─→ calcular_operacao(10, 20)
  │   └─ Retorna: 30
  │
  ├─→ calcular_valor_final("123")
  │   └─ Retorna: 128
  │
  ├─→ exibir_contador(3)
  │   └─ Exibe: 3 linhas + mensagem de fim
  │
  └─→ Ciclo interativo:
      ├─ obter_dados_usuario()
      │  └─ Retorna: (nome, idade)
      │
      └─ processar_maioridade(nome, idade)
         ├─ Chama: eh_maior_de_idade(idade)
         └─ Retorna: mensagem formatada
""")

print("\n" + "=" * 70)
print("✅ EXEMPLOS CONCLUÍDOS!")
print("=" * 70)
