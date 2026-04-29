"""
PRÁTICA 3 - RESUMO RÁPIDO DE ERROS E CORREÇÕES

Consulte este arquivo como referência rápida enquanto debug!
"""

print("=" * 70)
print("RESUMO RÁPIDO - ERROS COMUNS EM PYTHON")
print("=" * 70)

# ============================================================================
# 1. SyntaxError - Parênteses/Colchetes/Chaves não balanceados
# ============================================================================
print("\n1️⃣  SyntaxError - Parênteses não balanceados")
print("-" * 70)
print("""
❌ ERRO:
def funcao(parametros
    return "sem fechar"

✅ CORREÇÃO:
def funcao(parametros):
    return "fechado corretamente"

💡 DICA: Verifique se (), [], {} estão em pares
""")

# ============================================================================
# 2. IndentationError - Indentação incorreta
# ============================================================================
print("\n2️⃣  IndentationError - Indentação")
print("-" * 70)
print("""
❌ ERRO:
if condicao:
print("sem indentação")

✅ CORREÇÃO:
if condicao:
    print("com indentação")

💡 DICA: Use 4 espaços por nível de indentação
""")

# ============================================================================
# 3. NameError - Variável não definida
# ============================================================================
print("\n3️⃣  NameError - Variável não definida")
print("-" * 70)
print("""
❌ ERRO:
return resultado  # 'resultado' não existe

✅ CORREÇÃO:
resultado = 10 + 20
return resultado

💡 DICA: Defina variáveis antes de usar
""")

# ============================================================================
# 4. TypeError - Tipos incompatíveis
# ============================================================================
print("\n4️⃣  TypeError - Tipos incompatíveis")
print("-" * 70)
print("""
❌ ERRO:
texto = "Python" + 10  # str + int

✅ CORREÇÃO:
texto = "Python" + str(10)  # Converter para string

💡 DICA: Use type() para verificar: type(variavel)
""")

# ============================================================================
# 5. IndexError - Índice fora do intervalo
# ============================================================================
print("\n5️⃣  IndexError - Índice inválido")
print("-" * 70)
print("""
❌ ERRO:
lista = [1, 2, 3]
print(lista[10])  # Lista só tem 3 elementos (índices 0, 1, 2)

✅ CORREÇÃO:
lista = [1, 2, 3]
if len(lista) > 10:
    print(lista[10])

💡 DICA: Verifique len(lista) antes de acessar índice
""")

# ============================================================================
# 6. KeyError - Chave de dicionário não existe
# ============================================================================
print("\n6️⃣  KeyError - Chave não existe")
print("-" * 70)
print("""
❌ ERRO:
dados = {"nome": "João"}
print(dados["email"])  # Chave não existe

✅ CORREÇÃO:
dados = {"nome": "João"}
print(dados.get("email", "Não fornecido"))

💡 DICA: Use .get() em vez de [chave]
""")

# ============================================================================
# 7. AttributeError - Método/atributo não existe
# ============================================================================
print("\n7️⃣  AttributeError - Método/atributo inexistente")
print("-" * 70)
print("""
❌ ERRO:
texto = "python"
print(texto.maiuscula())  # Método não existe

✅ CORREÇÃO:
texto = "python"
print(texto.upper())  # Método correto

💡 DICA: Use IDE com autocompletar (Ctrl+Space)
""")

# ============================================================================
# 8. ValueError - Conversão inválida
# ============================================================================
print("\n8️⃣  ValueError - Valor inválido para conversão")
print("-" * 70)
print("""
❌ ERRO:
numero = int("123abc")  # Não pode converter

✅ CORREÇÃO:
try:
    numero = int("123abc")
except ValueError:
    print("Não é um número válido")

💡 DICA: Use try/except para conversões
""")

# ============================================================================
# 9. UnboundLocalError - Variável referenciada antes de atribuição
# ============================================================================
print("\n9️⃣  UnboundLocalError - Variável antes de atribuição")
print("-" * 70)
print("""
❌ ERRO:
print(resultado)
resultado = 10 + 20

✅ CORREÇÃO:
resultado = 10 + 20
print(resultado)

💡 DICA: Declare variáveis antes de usar
""")

# ============================================================================
# 10. TypeError - Argumentos faltando
# ============================================================================
print("\n🔟 TypeError - Argumentos insuficientes")
print("-" * 70)
print("""
❌ ERRO:
def saudar(nome, sobrenome):
    return f"Olá {nome} {sobrenome}"

saudar("João")  # Faltou 'sobrenome'

✅ CORREÇÃO:
saudar("João", "Silva")

💡 DICA: Verifique quantos argumentos a função espera
""")

# ============================================================================
# 11. SyntaxError - Operador errado em condicional
# ============================================================================
print("\n1️⃣1️⃣  SyntaxError - Operador errado (= vs ==)")
print("-" * 70)
print("""
❌ ERRO:
if x = 5:  # '=' é atribuição
    print("Igual")

✅ CORREÇÃO:
if x == 5:  # '==' é comparação
    print("Igual")

Outros operadores:
- ==  (igual)
- !=  (diferente)
- >   (maior)
- <   (menor)
- >=  (maior ou igual)
- <=  (menor ou igual)
""")

# ============================================================================
# 12. Loop Infinito
# ============================================================================
print("\n1️⃣2️⃣  Loop Infinito - while sem break")
print("-" * 70)
print("""
❌ ERRO:
while True:
    print("Infinito!")
    # Sem break, nunca sai

✅ CORREÇÃO (Opção 1):
for i in range(10):
    print(i)

✅ CORREÇÃO (Opção 2):
contador = 0
while contador < 10:
    print(contador)
    contador += 1

💡 DICA: for é melhor para loops contáveis
""")

# ============================================================================
# 13. SyntaxError - Palavra-chave reservada como variável
# ============================================================================
print("\n1️⃣3️⃣  SyntaxError - Palavra-chave como nome de variável")
print("-" * 70)
print("""
❌ ERRO:
class = "Python"  # 'class' é palavra-chave

✅ CORREÇÃO:
classe = "Python"

Palavras-chave reservadas (não use como nomes):
if, else, for, while, def, class, return, import, 
try, except, raise, pass, break, continue, yield, etc.
""")

# ============================================================================
# ESTRATÉGIA DE DEBUG
# ============================================================================
print("\n" + "=" * 70)
print("ESTRATÉGIA DE DEBUG")
print("=" * 70)
print("""
1. 📖 LEA A MENSAGEM DE ERRO
   - Tipo do erro (SyntaxError, TypeError, etc.)
   - Linha do erro
   - Mensagem explicativa

2. 🔍 IDENTIFIQUE O TIPO
   - SyntaxError → Erro de escrita
   - NameError → Variável não existe
   - TypeError → Tipos incompatíveis
   - IndexError → Índice fora de intervalo
   - KeyError → Chave não existe
   - AttributeError → Método não existe

3. ✋ VERIFIQUE A LINHA INDICADA
   - Nem sempre é onde parece
   - Pode ser alguns linhas antes

4. 🖨️  USE PRINT PARA DEBUG
   print(f"Variável = {variavel}, tipo = {type(variavel)}")

5. 🧪 TESTE EM PARTES
   - Teste cada linha separadamente
   - Isole o problema

6. 📚 PROCURE DOCUMENTAÇÃO
   - Google o erro
   - Stack Overflow
   - Documentação oficial Python

7. 🐛 USE DEBUGGER
   import pdb
   pdb.set_trace()
""")

# ============================================================================
# ERROS POR CATEGORIA
# ============================================================================
print("\n" + "=" * 70)
print("ERROS POR CATEGORIA")
print("=" * 70)

erros_categoria = {
    "SINTAXE": [
        "SyntaxError - Parênteses/colchetes não balanceados",
        "SyntaxError - Palavra-chave como variável",
        "IndentationError - Indentação incorreta"
    ],
    "NOMES": [
        "NameError - Variável não definida",
        "AttributeError - Método/atributo não existe"
    ],
    "TIPOS": [
        "TypeError - Tipos incompatíveis",
        "TypeError - Argumentos insuficientes",
        "ValueError - Conversão inválida"
    ],
    "ACESSO": [
        "IndexError - Índice fora de intervalo",
        "KeyError - Chave não existe",
        "UnboundLocalError - Variável antes de atribuição"
    ],
    "LÓGICA": [
        "Loop infinito",
        "Ordem de operações incorreta"
    ]
}

for categoria, erros in erros_categoria.items():
    print(f"\n{categoria}:")
    for erro in erros:
        print(f"  • {erro}")

print("\n" + "=" * 70)
print("💡 LEMBRE-SE: PRATICAR IDENTIFICAR ERROS É ESSENCIAL!")
print("=" * 70)
