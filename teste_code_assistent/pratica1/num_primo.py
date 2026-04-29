"""
Comparação entre função básica e otimizada para verificar números primos
"""

# ============= VERSÃO BÁSICA =============
def eh_primo_basico(numero):
    """Versão básica - O(n)"""
    if numero < 2:
        return False
    
    for i in range(2, numero):
        if numero % i == 0:
            return False
    
    return True


# ============= VERSÃO OTIMIZADA =============
def eh_primo(numero: int) -> bool:
    """
    Verifica se um número é primo.
    
    Args:
        numero: Um inteiro a ser verificado
        
    Returns:
        True se o número é primo, False caso contrário
        
    Raises:
        ValueError: Se o número for negativo
    """
    if numero < 0:
        raise ValueError("O número deve ser não-negativo")
    
    if numero < 2:
        return False
    
    if numero == 2:
        return True
    
    if numero % 2 == 0:
        return False
    
    # Verifica apenas até a raiz quadrada do número
    # e apenas números ímpares
    for i in range(3, int(numero**0.5) + 1, 2):
        if numero % i == 0:
            return False
    
    return True


# ============= TESTES =============
if __name__ == "__main__":
    # Números de teste
    numeros_teste = [1, 2, 5, 10, 17, 20, 97, 100, 289, 1009]
    
    print("=" * 60)
    print("COMPARAÇÃO: Versão Básica vs Versão Otimizada")
    print("=" * 60)
    
    for num in numeros_teste:
        resultado_basico = eh_primo_basico(num)
        resultado_otimizado = eh_primo(num)
        
        # Verifica se os resultados são iguais
        match = "✓" if resultado_basico == resultado_otimizado else "✗"
        
        print(f"{match} {num:4d} → Básico: {resultado_basico:5} | Otimizado: {resultado_otimizado:5}")
    
    print("\n" + "=" * 60)
    print("TESTE DE PERFORMANCE")
    print("=" * 60)
    
    import time
    
    numero_grande = 104729  # Um número primo grande
    
    # Teste versão básica
    inicio = time.time()
    resultado_basico = eh_primo_basico(numero_grande)
    tempo_basico = time.time() - inicio
    
    # Teste versão otimizada
    inicio = time.time()
    resultado_otimizado = eh_primo(numero_grande)
    tempo_otimizado = time.time() - inicio
    
    print(f"\nNúmero testado: {numero_grande}")
    print(f"Resultado: {resultado_otimizado} (é primo)")
    print(f"\nVersão Básica:    {tempo_basico:.6f} segundos")
    print(f"Versão Otimizada: {tempo_otimizado:.6f} segundos")
    print(f"Melhoria: {tempo_basico/tempo_otimizado:.1f}x mais rápido!")
    
    print("\n" + "=" * 60)
    print("TRATAMENTO DE ERROS")
    print("=" * 60)
    
    try:
        eh_primo(-5)
    except ValueError as e:
        print(f"✓ Erro capturado corretamente: {e}")
