"""
PRÁTICA 3 - CÓDIGO CORRIGIDO

Este arquivo contém todas as soluções para os erros encontrados
em pratica3_com_erros.py

Cada erro foi identificado, explicado e corrigido.
"""

from typing import List, Dict, Optional, Tuple


# ✅ ERRO 1 CORRIGIDO: Parênteses fechado
def calcular_media(notas: List[float]) -> float:
    """
    Calcula a média das notas.
    
    Args:
        notas: Lista de notas
        
    Returns:
        float: A média das notas
    """
    return sum(notas) / len(notas)


# ✅ ERRO 2 CORRIGIDO: Indentação correta
def validar_idade(idade: int) -> None:
    """Valida se a pessoa é maior de idade."""
    if idade >= 18:
        print("Maior de idade")
    else:
        print("Menor de idade")


# ✅ ERRO 3 CORRIGIDO: Variável definida corretamente
def processar_dados(lista: List[float]) -> float:
    """
    Calcula a média dos dados.
    
    Args:
        lista: Lista de números
        
    Returns:
        float: A média dos números
    """
    total = 0
    for item in lista:
        total += item
    
    media = total / len(lista)  # Definir 'media' antes de retornar
    return media


# ✅ ERRO 4 CORRIGIDO: Tipos compatíveis
def concatenar_strings(texto1: str, texto2: str, numero: int) -> str:
    """
    Concatena duas strings com um número.
    
    Args:
        texto1: Primeira string
        texto2: Segunda string
        numero: Número a concatenar
        
    Returns:
        str: Strings concatenadas
    """
    resultado = texto1 + texto2 + str(numero)  # Converter número para string
    return resultado


# ✅ ERRO 5 CORRIGIDO: Validação de índice
def acessar_primeiro_elemento(lista: List) -> Optional[any]:
    """
    Acessa o primeiro elemento da lista com validação.
    
    Args:
        lista: Lista de elementos
        
    Returns:
        Primeiro elemento ou None se lista vazia
    """
    if lista:  # Verificar se lista não está vazia
        return lista[0]  # Primeiro elemento (índice 0)
    return None


# ✅ ERRO 6 CORRIGIDO: Usar .get() para dicionário
def acessar_dicionario() -> str:
    """Acessa dados do dicionário com segurança."""
    dados = {"nome": "João", "idade": 25}
    return dados.get("email", "Email não fornecido")  # get() evita KeyError


# ✅ ERRO 7 CORRIGIDO: Usar método correto de string
def manipular_string(texto: str) -> str:
    """
    Converte string para maiúsculas.
    
    Args:
        texto: String a converter
        
    Returns:
        String em maiúsculas
    """
    return texto.upper()  # Método correto é 'upper()', não 'maiuscula()'


# ✅ ERRO 8 CORRIGIDO: Tratamento de erro para conversão
def converter_para_inteiro(valor: str) -> Optional[int]:
    """
    Converte string para inteiro com tratamento de erro.
    
    Args:
        valor: String contendo número
        
    Returns:
        int: Número convertido ou None se inválido
    """
    try:
        return int(valor)
    except ValueError:
        print(f"Erro: '{valor}' não é um número válido")
        return None


# ✅ ERRO 9 CORRIGIDO: Variável atribuída antes de usar
def calcular_resultado(x: float, y: float) -> float:
    """
    Calcula resultado de operação.
    
    Args:
        x: Primeiro número
        y: Segundo número
        
    Returns:
        float: Resultado calculado
    """
    resultado = x + y
    temporario = resultado * 2  # Definir ANTES de usar
    print(f"Resultado temporário: {temporario}")
    return temporario


# ✅ ERRO 10 CORRIGIDO: Argumentos suficientes
def saudar(nome: str, sobrenome: str) -> str:
    """
    Cria uma saudação personalizada.
    
    Args:
        nome: Nome da pessoa
        sobrenome: Sobrenome da pessoa
        
    Returns:
        str: Mensagem de saudação
    """
    return f"Olá, {nome} {sobrenome}!"


# Chamada correta com ambos os argumentos
mensagem_corrigida = saudar("João", "Silva")  # ✓ Ambos argumentos fornecidos


# ✅ ERRO 11 CORRIGIDO: Indentação em classe
class Pessoa:
    """Classe que representa uma pessoa."""
    
    def __init__(self, nome: str):
        """
        Inicializa a pessoa com um nome.
        
        Args:
            nome: Nome da pessoa
        """
        self.nome = nome  # ✓ Indentação correta
    
    def apresentar(self) -> str:
        """Retorna apresentação da pessoa."""
        return f"Meu nome é {self.nome}"


# ✅ ERRO 12 CORRIGIDO: Loop com condição de parada
def buscar_numero() -> None:
    """Busca e exibe números de forma segura."""
    numeros = [1, 2, 3, 4, 5]
    
    # Opção 1: Usar for (recomendado)
    for numero in numeros:
        print(f"Procurando {numero}...")
    
    # Opção 2: Usar while com contador
    # indice = 0
    # while indice < len(numeros):
    #     print(f"Procurando {numeros[indice]}...")
    #     indice += 1


# ✅ ERRO 13 CORRIGIDO: Operador correto para comparação
def comparar_valores(a: any, b: any) -> str:
    """
    Compara dois valores.
    
    Args:
        a: Primeiro valor
        b: Segundo valor
        
    Returns:
        str: Resultado da comparação
    """
    if a == b:  # ✓ '==' para comparação, não '='
        return "Iguais"
    return "Diferentes"


# ✅ ERRO 14 CORRIGIDO: Ordem de operações com parênteses
def calcular_expressao() -> int:
    """Calcula expressão matemática."""
    # Sem parênteses: 2 + 3 * 4 = 2 + 12 = 14
    resultado_padrao = 2 + 3 * 4
    
    # Com parênteses: (2 + 3) * 4 = 5 * 4 = 20
    resultado_forcado = (2 + 3) * 4
    
    print(f"Sem parênteses: {resultado_padrao}")
    print(f"Com parênteses: {resultado_forcado}")
    
    return resultado_padrao


# ✅ ERRO 15 CORRIGIDO: Não usar palavra-chave reservada
def obter_classe() -> str:
    """Retorna nome da classe."""
    classe = "Python"  # ✓ 'classe' em vez de 'class'
    return classe


# ============================================================================
# TESTES - Demonstração das funções corrigidas
# ============================================================================

def main() -> None:
    """Função principal que testa todas as correções."""
    
    print("=" * 70)
    print("PRÁTICA 3 - CÓDIGO CORRIGIDO - TESTES")
    print("=" * 70)
    
    # Teste 1: Calcular média
    print("\n1️⃣  TESTE: Calcular Média")
    try:
        notas = [7, 8, 9, 10]
        media = calcular_media(notas)
        print(f"✓ Média das notas {notas}: {media}")
    except Exception as e:
        print(f"✗ Erro: {type(e).__name__}: {e}")
    
    # Teste 2: Validar idade
    print("\n2️⃣  TESTE: Validar Idade")
    try:
        print("Validando idade 20:")
        validar_idade(20)
    except Exception as e:
        print(f"✗ Erro: {type(e).__name__}: {e}")
    
    # Teste 3: Processar dados
    print("\n3️⃣  TESTE: Processar Dados")
    try:
        dados = [10, 20, 30, 40]
        resultado = processar_dados(dados)
        print(f"✓ Média dos dados: {resultado}")
    except Exception as e:
        print(f"✗ Erro: {type(e).__name__}: {e}")
    
    # Teste 4: Concatenar strings
    print("\n4️⃣  TESTE: Concatenar Strings")
    try:
        resultado = concatenar_strings("Hello ", "World ", 123)
        print(f"✓ Concatenação: {resultado}")
    except Exception as e:
        print(f"✗ Erro: {type(e).__name__}: {e}")
    
    # Teste 5: Acessar elemento
    print("\n5️⃣  TESTE: Acessar Primeiro Elemento")
    try:
        lista = [1, 2, 3, 4, 5]
        elemento = acessar_primeiro_elemento(lista)
        print(f"✓ Primeiro elemento: {elemento}")
    except Exception as e:
        print(f"✗ Erro: {type(e).__name__}: {e}")
    
    # Teste 6: Acessar dicionário
    print("\n6️⃣  TESTE: Acessar Dicionário")
    try:
        resultado = acessar_dicionario()
        print(f"✓ Email: {resultado}")
    except Exception as e:
        print(f"✗ Erro: {type(e).__name__}: {e}")
    
    # Teste 7: Manipular string
    print("\n7️⃣  TESTE: Manipular String")
    try:
        resultado = manipular_string("python")
        print(f"✓ String em maiúsculas: {resultado}")
    except Exception as e:
        print(f"✗ Erro: {type(e).__name__}: {e}")
    
    # Teste 8: Converter inteiro
    print("\n8️⃣  TESTE: Converter para Inteiro")
    try:
        resultado = converter_para_inteiro("123")
        print(f"✓ Conversão válida: {resultado}")
        resultado_invalido = converter_para_inteiro("123abc")
        print(f"✓ Conversão inválida: {resultado_invalido}")
    except Exception as e:
        print(f"✗ Erro: {type(e).__name__}: {e}")
    
    # Teste 9: Calcular resultado
    print("\n9️⃣  TESTE: Calcular Resultado")
    try:
        resultado = calcular_resultado(10, 20)
        print(f"✓ Resultado: {resultado}")
    except Exception as e:
        print(f"✗ Erro: {type(e).__name__}: {e}")
    
    # Teste 10: Saudar
    print("\n🔟 TESTE: Saudar")
    try:
        mensagem = saudar("João", "Silva")
        print(f"✓ {mensagem}")
    except Exception as e:
        print(f"✗ Erro: {type(e).__name__}: {e}")
    
    # Teste 11: Classe Pessoa
    print("\n1️⃣1️⃣  TESTE: Classe Pessoa")
    try:
        pessoa = Pessoa("Maria")
        print(f"✓ {pessoa.apresentar()}")
    except Exception as e:
        print(f"✗ Erro: {type(e).__name__}: {e}")
    
    # Teste 12: Buscar número
    print("\n1️⃣2️⃣  TESTE: Buscar Número")
    try:
        print("✓ Números encontrados:")
        buscar_numero()
    except Exception as e:
        print(f"✗ Erro: {type(e).__name__}: {e}")
    
    # Teste 13: Comparar valores
    print("\n1️⃣3️⃣  TESTE: Comparar Valores")
    try:
        print(f"✓ 5 == 5: {comparar_valores(5, 5)}")
        print(f"✓ 5 == 3: {comparar_valores(5, 3)}")
    except Exception as e:
        print(f"✗ Erro: {type(e).__name__}: {e}")
    
    # Teste 14: Expressão matemática
    print("\n1️⃣4️⃣  TESTE: Expressão Matemática")
    try:
        resultado = calcular_expressao()
        print(f"✓ Resultado: {resultado}")
    except Exception as e:
        print(f"✗ Erro: {type(e).__name__}: {e}")
    
    # Teste 15: Classe
    print("\n1️⃣5️⃣  TESTE: Obter Classe")
    try:
        resultado = obter_classe()
        print(f"✓ Classe: {resultado}")
    except Exception as e:
        print(f"✗ Erro: {type(e).__name__}: {e}")
    
    print("\n" + "=" * 70)
    print("✅ TODOS OS TESTES CONCLUÍDOS!")
    print("=" * 70)


if __name__ == "__main__":
    main()
