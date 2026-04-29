"""
PRÁTICA 3 - CÓDIGO COM ERROS (PROPOSITAIS)

Este arquivo contém MÚLTIPLOS ERROS propositais para a prática de debug.

INSTRUÇÕES:
1. Leia este arquivo com cuidado
2. Identifique cada erro
3. Explique a causa de cada um
4. Proponha a correção
5. Verifique o arquivo pratica3_corrigido.py para ver as soluções

ERRO: Tente executar este arquivo - ele NÃO vai rodar sem erros!
"""

# ERRO 1: Parênteses não fechado (Sintaxe)
def calcular_media(notas
    """Calcula a média das notas."""
    return sum(notas) / len(notas)


# ERRO 2: Indentação incorreta
def validar_idade(idade):
    if idade >= 18:
    print("Maior de idade")
    else:
        print("Menor de idade")


# ERRO 3: Variável não definida (NameError)
def processar_dados(lista):
    total = 0
    for item in lista:
        total += item
    return media  # ❌ ERRO: 'media' não foi definida, só 'total'


# ERRO 4: Tipo incompatível (TypeError)
def concatenar_strings(texto1, texto2):
    resultado = texto1 + texto2 + 10  # ❌ ERRO: Não pode somar string + inteiro
    return resultado


# ERRO 5: Índice fora do intervalo (IndexError)
def acessar_primeiro_elemento(lista):
    return lista[10]  # ❌ ERRO: Lista não tem 10 elementos


# ERRO 6: Chave de dicionário não existe (KeyError)
def acessar_dicionario():
    dados = {"nome": "João", "idade": 25}
    return dados["email"]  # ❌ ERRO: Chave "email" não existe


# ERRO 7: Atributo que não existe (AttributeError)
def manipular_string(texto):
    return texto.maiuscula()  # ❌ ERRO: Método correto é 'upper()', não 'maiuscula()'


# ERRO 8: Valor inválido para conversão (ValueError)
def converter_para_inteiro():
    numero_texto = "123abc"
    return int(numero_texto)  # ❌ ERRO: Não pode converter "123abc" para inteiro


# ERRO 9: Variável local referenciada antes de ser atribuída
def calcular_resultado(x, y):
    resultado = x + y
    print(temporario)  # ❌ ERRO: 'temporario' não existe
    temporario = resultado * 2
    return temporario


# ERRO 10: Falta de argumentos na chamada de função
def saudar(nome, sobrenome):
    return f"Olá, {nome} {sobrenome}!"

mensagem = saudar("João")  # ❌ ERRO: Faltou 'sobrenome'


# ERRO 11: Indentação incorreta dentro de classe
class Pessoa:
    def __init__(self, nome):
    self.nome = nome  # ❌ ERRO: Indentação errada

    def apresentar(self):
        return f"Meu nome é {self.nome}"


# ERRO 12: Loop infinito sem break
def buscar_numero():
    numeros = [1, 2, 3, 4, 5]
    while True:
        print("Procurando...")
        # ❌ ERRO: Loop infinito, nunca sai


# ERRO 13: Uso de operador errado
def comparar_valores(a, b):
    if a = b:  # ❌ ERRO: Usar '=' (atribuição) em vez de '==' (comparação)
        return "Iguais"
    return "Diferentes"


# ERRO 14: Ordem de operações
def calcular_expressao():
    resultado = 2 + 3 * 4  # ✓ Isto está correto tecnicamente
    # Mas muitas vezes programadores iniciantes esperam 20 em vez de 14
    return resultado


# ERRO 15: Usar palavra-chave como nome de variável
def function():
    class = "Python"  # ❌ ERRO: 'class' é palavra-chave reservada
    return class


# ============================================================================
# TESTE - Tente rodar este arquivo
# ============================================================================

if __name__ == "__main__":
    print("Tentando executar o programa...")
    
    # Este bloco provavelmente quebrará em um dos erros acima
    try:
        print("Teste 1: Média")
        notas = [7, 8, 9]
        media = calcular_media(notas)
        print(f"Média: {media}")
    except Exception as e:
        print(f"❌ ERRO: {type(e).__name__}: {e}")
