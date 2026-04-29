"""
Prática 2: Refatoração de código com boas práticas

Este módulo demonstra como transformar código desorganizado
em código limpo, legível e bem estruturado (Clean Code).
"""

from typing import Tuple


def calcular_operacao(numero_a: int, numero_b: int) -> int:
    """
    Calcula a soma se a < b, caso contrário calcula a diferença.
    
    Args:
        numero_a: Primeiro número inteiro
        numero_b: Segundo número inteiro
        
    Returns:
        int: Resultado da operação (soma ou diferença)
    """
    if numero_a < numero_b:
        return numero_a + numero_b
    return numero_a - numero_b


def calcular_valor_final(valor_string: str) -> int:
    """
    Converte string para inteiro e adiciona 5.
    
    Args:
        valor_string: String contendo um número
        
    Returns:
        int: Número convertido mais 5
        
    Raises:
        ValueError: Se a string não puder ser convertida para inteiro
    """
    try:
        valor_numerico = int(valor_string)
        return valor_numerico + 5
    except ValueError:
        raise ValueError(f"Erro: '{valor_string}' não é um número válido")


def eh_maior_de_idade(idade: int) -> bool:
    """
    Verifica se a pessoa é maior de idade.
    
    Args:
        idade: Idade em anos (inteiro)
        
    Returns:
        bool: True se idade >= 18, False caso contrário
    """
    return idade >= 18


def obter_dados_usuario() -> Tuple[str, int]:
    """
    Coleta nome e idade do usuário com validação.
    
    Returns:
        Tuple[str, int]: Tupla contendo (nome, idade)
        
    Raises:
        ValueError: Se a idade não for um número válido
    """
    nome = input("Digite seu nome: ").strip()
    
    while True:
        try:
            idade_input = input("Digite sua idade: ").strip()
            idade = int(idade_input)
            
            if idade < 0:
                print("⚠️ Idade não pode ser negativa. Tente novamente.")
                continue
            
            return nome, idade
        
        except ValueError:
            print(f"⚠️ Erro: '{idade_input}' não é um número válido. Tente novamente.")


def processar_maioridade(nome: str, idade: int) -> str:
    """
    Determina e retorna mensagem sobre maioridade.
    
    Args:
        nome: Nome da pessoa
        idade: Idade em anos
        
    Returns:
        str: Mensagem formatada sobre o status de maioridade
    """
    if eh_maior_de_idade(idade):
        return f"✓ {nome} ({idade} anos) é maior de idade"
    else:
        return f"✗ {nome} ({idade} anos) é menor de idade"


def exibir_contador(iteracoes: int = 3) -> None:
    """
    Exibe um contador com lógica clara.
    
    Args:
        iteracoes: Número de iterações (padrão: 3)
    """
    for numero in range(iteracoes):
        print(f"Iteração {numero + 1}")
        
        if numero == iteracoes - 1:
            print("✓ Fim das iterações")


def main() -> None:
    """
    Função principal que orquestra todo o programa.
    Mantém separação clara de responsabilidades.
    """
    print("=" * 50)
    print("PROGRAMA REFATORADO - VERSÃO LIMPA")
    print("=" * 50)
    
    # Seção 1: Operações matemáticas
    print("\n📊 OPERAÇÕES MATEMÁTICAS:")
    numero_a = 10
    numero_b = 20
    resultado = calcular_operacao(numero_a, numero_b)
    print(f"calcular_operacao({numero_a}, {numero_b}) = {resultado}")
    
    # Seção 2: Conversão e cálculo
    print("\n🔢 CONVERSÃO E CÁLCULO:")
    try:
        valor_final = calcular_valor_final("123")
        print(f"Valor final: {valor_final}")
    except ValueError as erro:
        print(f"Erro: {erro}")
    
    # Seção 3: Contador
    print("\n🔄 CONTADOR:")
    exibir_contador(3)
    
    # Seção 4: Dados do usuário com validação
    print("\n👤 INFORMAÇÕES DO USUÁRIO:")
    try:
        nome_usuario, idade_usuario = obter_dados_usuario()
        mensagem = processar_maioridade(nome_usuario, idade_usuario)
        print(f"Resultado: {mensagem}")
    except ValueError as erro:
        print(f"Erro: {erro}")
    
    print("\n" + "=" * 50)
    print("Programa finalizado com sucesso!")
    print("=" * 50)


if __name__ == "__main__":
    main()
