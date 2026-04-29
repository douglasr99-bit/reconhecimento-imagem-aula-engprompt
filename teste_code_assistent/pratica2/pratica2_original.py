"""
CÓDIGO ORIGINAL - COM PROBLEMAS

Este arquivo contém o código original com todos os problemas,
para que você possa comparar com a versão refatorada.

PROBLEMAS IDENTIFICADOS:
1. Nomes de variáveis genéricos (a, b, c, d, x, y, z)
2. Repetição de código (violação de DRY)
3. Código morto (condição que nunca é verdadeira)
4. Mistura de responsabilidades
5. Sem documentação (docstrings)
6. Sem tratamento de erros
7. Lógica de validação fraca (compara string "18" em vez de inteiro)
8. Sem type hints
"""

print("Inicio")

# ❌ PROBLEMA 1: Nomes genéricos (a, b, c)
# ❌ PROBLEMA 2: Repetição desnecessária de código (DRY violation)
a = 10
b = 20
c = 0

if a < b:
    c = a + b
    print("resultado:", c)
else:
    c = a - b
    print("resultado:", c)

# repetição desnecessária
if a < b:
    c = a + b
    print("de novo:", c)
else:
    c = a - b
    print("de novo:", c)

# ❌ PROBLEMA 1: Nomes genéricos (x, y, z)
# ❌ PROBLEMA 6: Sem tratamento de erros
variável sem sentido
x = "123"
y = int(x)  # Se x não for número, programa quebra!
z = y + 5

print("valor final:", z)

# ❌ PROBLEMA 7: Loop confuso
# ❌ PROBLEMA 1: Nomes genéricos (i)
for i in range(3):
    print("loop", i)
    if i == 2:
        print("fim do loop")

# ❌ PROBLEMA 3: Código morto (d é 100, nunca será < 50)
# ❌ PROBLEMA 1: Nome genérico (d)
d = 100
if d < 50:
    print("nunca vai acontecer")

# ❌ PROBLEMA 4: Mistura de responsabilidades
# ❌ PROBLEMA 6: Sem tratamento de erros
# ❌ PROBLEMA 7: Validação fraca (compara string "18", não inteiro)
# ❌ PROBLEMA 8: Sem type hints
# ❌ PROBLEMA 5: Sem documentação
nome = input("digite seu nome: ")
idade = input("idade: ")

if idade == "18":  # BUG! Comparando string "18", não inteiro 18
    print(nome + " é maior de idade")
else:
    print("não sei")  # Mensagem vaga
