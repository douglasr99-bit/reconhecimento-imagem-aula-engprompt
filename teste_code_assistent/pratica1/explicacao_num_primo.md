# Verificação de Números Primos em Python

## O que é um Número Primo?

Um número primo é um número natural maior que 1 que possui exatamente dois divisores: 1 e ele mesmo. Exemplos: 2, 3, 5, 7, 11, 13, 17...

## Função Básica

```python
def eh_primo(numero):
    if numero < 2:
        return False
    
    for i in range(2, numero):
        if numero % i == 0:
            return False
    
    return True
```

## Explicação Linha a Linha

### Definição da Função
```python
def eh_primo(numero):
```
- Define uma função chamada `eh_primo`
- Recebe um parâmetro `numero` (o número a ser verificado)

### Validação Inicial
```python
if numero < 2:
    return False
```
- Verifica se o número é menor que 2
- Números menores que 2 (incluindo 0, 1 e negativos) não são primos
- Retorna `False` (não é primo)

### Loop de Verificação
```python
for i in range(2, numero):
```
- Cria um loop que itera de 2 até `numero-1`
- Cada iteração testa se `numero` é divisível por `i`

### Teste de Divisibilidade
```python
if numero % i == 0:
    return False
```
- O operador `%` calcula o resto da divisão
- Se o resto é 0, significa que `numero` é divisível por `i`
- Se encontrar um divisor, retorna `False` (não é primo)

### Resultado Final
```python
return True
```
- Se passar por todo o loop sem encontrar divisores
- Significa que o número é primo
- Retorna `True`

## Exemplos de Uso

```python
print(eh_primo(5))   # True (5 é primo)
print(eh_primo(10))  # False (10 = 2 × 5)
print(eh_primo(2))   # True (2 é o menor primo)
print(eh_primo(1))   # False (1 não é primo)
print(eh_primo(17))  # True (17 é primo)
```

## Complexidade

- **Tempo**: O(n) - no pior caso, verifica até n-1 divisores
- **Espaço**: O(1) - usa apenas uma variável adicional

## Limitações

- Função lenta para números muito grandes
- Verifica todos os números de 2 a n-1 (desnecessário)

---

# Versão Otimizada - Clean Code

## Função Otimizada

```python
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
```

## Melhorias Implementadas

| Melhoria | Descrição |
|----------|-----------|
| **Type Hints** | `(numero: int) -> bool` deixa claro os tipos de entrada e saída |
| **Docstring** | Documenta o propósito, argumentos, retorno e exceções |
| **Validação** | Verifica entrada inválida (números negativos) |
| **Otimização Matemática** | Verifica até √n em vez de n (muito mais rápido) |
| **Verificação de Pares** | Elimina números pares imediatamente |
| **Incremento de 2** | No loop, verifica apenas números ímpares |
| **Comentários Claros** | Explica decisões importantes do código |

## Análise de Performance

### Função Básica
```
Número 1000003:
Iterações necessárias: ~1 milhão
Tempo: lento
```

### Função Otimizada
```
Número 1000003:
Iterações necessárias: ~1000 (até √1000003)
Tempo: até 1000x mais rápido!
```

## Complexidade

- **Tempo**: O(√n) - verifica apenas até a raiz quadrada
- **Espaço**: O(1) - usa apenas variáveis auxiliares

## Por que √n funciona?

Se um número n tem um divisor maior que √n, ele também deve ter um divisor menor que √n.

**Exemplo com 36:**
- √36 = 6
- Divisores de 36: 1, 2, 3, **4, 6**, 9, 12, 18, 36
- Basta verificar até 6, pois se houvesse divisor > 6, haveria outro < 6

## Exemplos de Uso

```python
print(eh_primo(5))    # True
print(eh_primo(10))   # False
print(eh_primo(2))    # True
print(eh_primo(1))    # False
print(eh_primo(17))   # True
print(eh_primo(100))  # False

# Tratamento de erro
try:
    eh_primo(-5)
except ValueError as e:
    print(f"Erro: {e}")  # Erro: O número deve ser não-negativo
```

## Quando Usar?

- **Para números pequenos (< 10.000)**: Ambas funcionam bem
- **Para números médios (10.000 - 1 milhão)**: Use a versão otimizada
- **Para números muito grandes**: Considere algoritmos ainda mais avançados (Miller-Rabin, etc)
