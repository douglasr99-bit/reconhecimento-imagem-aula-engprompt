# PRÁTICA 4 - IA EXPLICANDO CÓDIGO

## Explicação Linha a Linha do Código Refatorado (pratica2_refatorado.py)

---

## 📋 Índice

1. [Imports](#imports)
2. [Função 1: calcular_operacao()](#função-1-calcular_operacao)
3. [Função 2: calcular_valor_final()](#função-2-calcular_valor_final)
4. [Função 3: eh_maior_de_idade()](#função-3-eh_maior_de_idade)
5. [Função 4: obter_dados_usuario()](#função-4-obter_dados_usuario)
6. [Função 5: processar_maioridade()](#função-5-processar_maioridade)
7. [Função 6: exibir_contador()](#função-6-exibir_contador)
8. [Função 7: main()](#função-7-main)
9. [Bloco de Execução](#bloco-de-execução)
10. [Fluxo Completo](#fluxo-completo)

---

## IMPORTS

```python
from typing import Tuple
```

### 📍 Linha 1
**O que faz:** Importa o tipo `Tuple` do módulo `typing`

**Explicação detalhada:**
- `from typing import` → Importação seletiva (traz apenas `Tuple`)
- `Tuple` → Tipo de dado que permite retornar múltiplos valores
- **Por quê?** Para indicar que uma função retorna uma dupla de valores (nome, idade)

**Exemplo de uso:**
```python
def funcao() -> Tuple[str, int]:  # Retorna (string, inteiro)
    return "João", 25
```

---

## FUNÇÃO 1: calcular_operacao()

```python
def calcular_operacao(numero_a: int, numero_b: int) -> int:
```

### 📍 Linha 4-5
**O que faz:** Define uma função que realiza uma operação matemática

**Análise linha por linha:**

| Parte | Explicação |
|-------|-----------|
| `def` | Palavra-chave para definir função |
| `calcular_operacao` | Nome descritivo da função |
| `numero_a: int` | Primeiro parâmetro, tipo inteiro |
| `numero_b: int` | Segundo parâmetro, tipo inteiro |
| `-> int:` | Retorna um inteiro |

**Type hints em detalhes:**
```
def funcao(parametro: tipo_entrada) -> tipo_saida:
           ↑                            ↑
        Input                        Output
```

---

```python
    """
    Calcula a soma se a < b, caso contrário calcula a diferença.
    
    Args:
        numero_a: Primeiro número inteiro
        numero_b: Segundo número inteiro
        
    Returns:
        int: Resultado da operação (soma ou diferença)
    """
```

### 📍 Linhas 6-14
**O que faz:** Docstring (documentação da função)

**Estrutura:**
```
"""
Descrição breve (primeira linha)

Descrição detalhada (opcional)

Args:
    parametro1: Descrição
    parametro2: Descrição
    
Returns:
    tipo: Descrição do retorno
"""
```

**Benefícios:**
- IDE mostra automaticamente ao chamar a função
- Documenta propósito e comportamento
- Explicita argumentos e retorno

---

```python
    if numero_a < numero_b:
        return numero_a + numero_b
    return numero_a - numero_b
```

### 📍 Linhas 15-17
**Fluxo de execução:**

**Linha 15: `if numero_a < numero_b:`**
- Testa se `numero_a` é menor que `numero_b`
- Se VERDADEIRO → executa linha 16
- Se FALSO → pula para linha 17

**Linha 16: `return numero_a + numero_b`**
- Se a condição for verdadeira:
  - Soma os dois números
  - Retorna o resultado
  - Função termina aqui

**Linha 17: `return numero_a - numero_b`**
- Se a condição for falsa (numero_a >= numero_b):
  - Subtrai numero_b de numero_a
  - Retorna o resultado

**Exemplos práticos:**
```python
calcular_operacao(10, 20)  # 10 < 20? SIM → 10+20 = 30
calcular_operacao(30, 20)  # 30 < 20? NÃO → 30-20 = 10
calcular_operacao(20, 20)  # 20 < 20? NÃO → 20-20 = 0
```

---

## FUNÇÃO 2: calcular_valor_final()

```python
def calcular_valor_final(valor_string: str) -> int:
```

### 📍 Linha 20
**O que faz:** Define função que converte string para inteiro e adiciona 5

**Análise:**
- `valor_string: str` → Recebe um texto
- `-> int` → Retorna um inteiro

---

```python
    """
    Converte string para inteiro e adiciona 5.
    
    Args:
        valor_string: String contendo um número
        
    Returns:
        int: Número convertido mais 5
        
    Raises:
        ValueError: Se a string não puder ser convertida para inteiro
    """
```

### 📍 Linhas 21-32
**Novo elemento: `Raises:`**
- Documenta exceções que a função pode lançar
- `ValueError` → Exceção se conversão falhar
- Ajuda o programador a tratar erros

---

```python
    try:
        valor_numerico = int(valor_string)
        return valor_numerico + 5
    except ValueError:
        raise ValueError(f"Erro: '{valor_string}' não é um número válido")
```

### 📍 Linhas 33-37
**Estrutura try/except (tratamento de erros):**

**Linha 33: `try:`**
- Tenta executar o código abaixo
- Se der erro, pula para `except`

**Linha 34: `valor_numerico = int(valor_string)`**
- Converte string para inteiro
- Se `valor_string = "123"` → `valor_numerico = 123` ✓
- Se `valor_string = "abc"` → Lança `ValueError` ✗

**Linha 35: `return valor_numerico + 5`**
- Se conversão funcionou:
  - Soma 5 ao número
  - Retorna resultado
  - Try/except termina

**Linha 36: `except ValueError:`**
- Se erro `ValueError` foi lançado, executa este bloco

**Linha 37: `raise ValueError(...)`**
- Lança um novo erro (ValueError customizado)
- Mensagem clara: "Erro: 'abc' não é um número válido"
- `f"..."` → f-string (interpola variáveis)

**Exemplos:**
```python
calcular_valor_final("100")    # 100 + 5 = 105 ✓
calcular_valor_final("abc")    # Lança ValueError ✗
calcular_valor_final("50.5")   # 50 + 5 = 55 ✓ (converte ponto flutuante)
```

---

## FUNÇÃO 3: eh_maior_de_idade()

```python
def eh_maior_de_idade(idade: int) -> bool:
```

### 📍 Linha 40
**O que faz:** Verifica se pessoa é maior de idade

**Análise:**
- `idade: int` → Recebe idade em anos
- `-> bool` → Retorna verdadeiro ou falso

---

```python
    """
    Verifica se a pessoa é maior de idade.
    
    Args:
        idade: Idade em anos (inteiro)
        
    Returns:
        bool: True se idade >= 18, False caso contrário
    """
    return idade >= 18
```

### 📍 Linhas 41-50
**Docstring e implementação:**

**Linha 50: `return idade >= 18`**
- Expressão booleana:
  - `idade >= 18` → Verdadeiro se idade é 18 ou mais
  - Retorna `True` ou `False` direto

**Exemplos:**
```python
eh_maior_de_idade(18)   # 18 >= 18? SIM → True
eh_maior_de_idade(25)   # 25 >= 18? SIM → True
eh_maior_de_idade(17)   # 17 >= 18? NÃO → False
eh_maior_de_idade(16)   # 16 >= 18? NÃO → False
```

---

## FUNÇÃO 4: obter_dados_usuario()

```python
def obter_dados_usuario() -> Tuple[str, int]:
```

### 📍 Linha 53
**O que faz:** Coleta nome e idade com validação

**Análise:**
- Sem parâmetros (não precisa de input)
- `-> Tuple[str, int]` → Retorna dupla (nome_string, idade_inteiro)

---

```python
    """
    Coleta nome e idade do usuário com validação.
    
    Returns:
        Tuple[str, int]: Tupla contendo (nome, idade)
        
    Raises:
        ValueError: Se a idade não for um número válido
    """
```

### 📍 Linhas 54-62
**Docstring especificando retorno e exceções**

---

```python
    nome = input("Digite seu nome: ").strip()
```

### 📍 Linha 63
**O que faz:** Coleta nome do usuário

**Análise linha a linha:**
- `input("Digite seu nome: ")` → Exibe mensagem e aguarda entrada
- `.strip()` → Remove espaços em branco do início e fim
  - `"  João  ".strip()` → `"João"`
  - Remove \n do final da entrada

---

```python
    while True:
```

### 📍 Linha 65
**O que faz:** Loop infinito

**Por quê?**
- Continua pedindo idade até obter valor válido
- Quando `return` é executado, loop termina

---

```python
        try:
            idade_input = input("Digite sua idade: ").strip()
            idade = int(idade_input)
```

### 📍 Linhas 66-68
**Bloco try - tenta conversão**

**Linha 66: `try:`**
- Tenta executar linhas 67-68

**Linha 67: `idade_input = input("Digite sua idade: ").strip()`**
- Coleta entrada do usuário
- Remove espaços
- Armazena como string

**Linha 68: `idade = int(idade_input)`**
- Converte para inteiro
- Se "25" → 25 ✓
- Se "abc" → Lança ValueError ✗

---

```python
            if idade < 0:
                print("⚠️ Idade não pode ser negativa. Tente novamente.")
                continue
```

### 📍 Linhas 70-72
**Validação adicional**

**Linha 70: `if idade < 0:`**
- Verifica se idade é negativa

**Linhas 71-72:**
- Se negativa: exibe mensagem
- `continue` → Volta ao `while True` (pede novamente)

---

```python
            return nome, idade
```

### 📍 Linha 74
**O que faz:** Retorna dados válidos

**Quando executa?**
- Só chega aqui se:
  1. Conversão funcionou (linha 68)
  2. Idade >= 0 (linha 70)

**Retorno:**
- `(nome, idade)` → Tupla com dois valores

---

```python
        except ValueError:
            print(f"⚠️ Erro: '{idade_input}' não é um número válido. Tente novamente.")
```

### 📍 Linhas 76-77
**Tratamento de erro**

**Linha 76: `except ValueError:`**
- Se conversão falhar (linha 68 lança ValueError)

**Linha 77: print com f-string**
- Exibe mensagem de erro
- `{idade_input}` → Interpola o valor que o usuário digitou
- Loop continua (volta ao `while True`)

**Fluxo completo da função:**
```
Entrada: "João" e "25"
  ↓
nome = "João"
  ↓
Pedir idade: "25"
  ↓
Converter: 25 (inteiro)
  ↓
Validar: 25 >= 0? SIM
  ↓
return ("João", 25) ✓

---

Entrada: "Maria" e "abc"
  ↓
nome = "Maria"
  ↓
Pedir idade: "abc"
  ↓
Converter: ERRO ValueError
  ↓
except: exibir mensagem
  ↓
Volta ao while: pedir novamente
  ↓
(loop continua até entrada válida)
```

---

## FUNÇÃO 5: processar_maioridade()

```python
def processar_maioridade(nome: str, idade: int) -> str:
```

### 📍 Linha 80
**O que faz:** Formata mensagem sobre maioridade

**Análise:**
- `nome: str` → Nome da pessoa
- `idade: int` → Idade da pessoa
- `-> str` → Retorna mensagem formatada

---

```python
    """
    Determina e retorna mensagem sobre maioridade.
    
    Args:
        nome: Nome da pessoa
        idade: Idade em anos
        
    Returns:
        str: Mensagem formatada sobre o status de maioridade
    """
```

### 📍 Linhas 81-91
**Documentação clara**

---

```python
    if eh_maior_de_idade(idade):
        return f"✓ {nome} ({idade} anos) é maior de idade"
    else:
        return f"✗ {nome} ({idade} anos) é menor de idade"
```

### 📍 Linhas 92-95
**Lógica com formatação**

**Linha 92: `if eh_maior_de_idade(idade):`**
- Chama função auxiliar `eh_maior_de_idade()`
- Se retornar `True` → executa linha 93

**Linha 93:**
- f-string com emojis e variáveis interpoladas
- Exemplo: `f"✓ João (25 anos) é maior de idade"`

**Linhas 94-95:**
- `else` → Se `eh_maior_de_idade()` retornar `False`
- Retorna mensagem diferente

**Exemplos:**
```python
processar_maioridade("João", 25)
# Retorna: "✓ João (25 anos) é maior de idade"

processar_maioridade("Ana", 16)
# Retorna: "✗ Ana (16 anos) é menor de idade"
```

---

## FUNÇÃO 6: exibir_contador()

```python
def exibir_contador(iteracoes: int = 3) -> None:
```

### 📍 Linha 98
**O que faz:** Exibe um contador

**Análise:**
- `iteracoes: int = 3` → Parâmetro com **valor padrão 3**
- `-> None` → Não retorna nada (só exibe)

**Parâmetro com padrão:**
```python
exibir_contador()      # Usa padrão: iteracoes = 3
exibir_contador(5)     # Customizado: iteracoes = 5
```

---

```python
    """
    Exibe um contador com lógica clara.
    
    Args:
        iteracoes: Número de iterações (padrão: 3)
    """
```

### 📍 Linhas 99-104
**Docstring mencionando padrão**

---

```python
    for numero in range(iteracoes):
        print(f"Iteração {numero + 1}")
        
        if numero == iteracoes - 1:
            print("✓ Fim das iterações")
```

### 📍 Linhas 105-109
**Loop com lógica**

**Linha 105: `for numero in range(iteracoes):`**
- `range(3)` → Cria sequência: 0, 1, 2
- `numero` → Variável do loop
- Itera 3 vezes

**Exemplo com iteracoes=3:**
```
Iteração 1: numero=0
Iteração 2: numero=1
Iteração 3: numero=2
```

**Linha 106: `print(f"Iteração {numero + 1}")`**
- `numero + 1` → Incrementa para exibir 1, 2, 3 (em vez de 0, 1, 2)
- Saída:
  ```
  Iteração 1
  Iteração 2
  Iteração 3
  ```

**Linhas 108-109: Condicional dentro do loop**
- `if numero == iteracoes - 1:` → Verdadeiro na **última iteração**
- Com `iteracoes=3`:
  - `iteracoes - 1 = 2` (último índice)
  - Quando `numero == 2` → exibe mensagem final

**Exemplo de execução:**
```python
exibir_contador(3)

Saída:
Iteração 1
Iteração 2
Iteração 3
✓ Fim das iterações
```

---

## FUNÇÃO 7: main()

```python
def main() -> None:
```

### 📍 Linha 112
**O que faz:** Função principal que coordena tudo

**Análise:**
- `-> None` → Não retorna valor (só executa)
- Convenção: chamar função principal de `main()`

---

```python
    """
    Função principal que orquestra todo o programa.
    Mantém separação clara de responsabilidades.
    """
```

### 📍 Linhas 113-116
**Docstring explicando o propósito**

---

```python
    print("=" * 50)
    print("PROGRAMA REFATORADO - VERSÃO LIMPA")
    print("=" * 50)
```

### 📍 Linhas 117-119
**Cabeçalho visual**

**`"=" * 50`**
- Multiplica string por número
- Cria linha com 50 iguais: `==================================================`

---

```python
    # Seção 1: Operações matemáticas
    print("\n📊 OPERAÇÕES MATEMÁTICAS:")
    numero_a = 10
    numero_b = 20
    resultado = calcular_operacao(numero_a, numero_b)
    print(f"calcular_operacao({numero_a}, {numero_b}) = {resultado}")
```

### 📍 Linhas 122-127
**Seção 1: Testar função calcular_operacao()**

**Linha 122:** Comentário explicativo

**Linha 123:** Emojis + título (visual)

**Linhas 124-125:** Define variáveis

**Linha 126:** Chama função
- `calcular_operacao(10, 20)` → Retorna 30 (10+20)

**Linha 127:** Exibe resultado com f-string

**Saída esperada:**
```
📊 OPERAÇÕES MATEMÁTICAS:
calcular_operacao(10, 20) = 30
```

---

```python
    # Seção 2: Conversão e cálculo
    print("\n🔢 CONVERSÃO E CÁLCULO:")
    try:
        valor_final = calcular_valor_final("123")
        print(f"Valor final: {valor_final}")
    except ValueError as erro:
        print(f"Erro: {erro}")
```

### 📍 Linhas 129-135
**Seção 2: Testar função calcular_valor_final()**

**Linha 130:** Título com emoji

**Linhas 131-135:** Try/except local
- Tenta converter "123" → 123 + 5 = 128
- Se erro, exibe mensagem

**Saída esperada:**
```
🔢 CONVERSÃO E CÁLCULO:
Valor final: 128
```

---

```python
    # Seção 3: Contador
    print("\n🔄 CONTADOR:")
    exibir_contador(3)
```

### 📍 Linhas 137-139
**Seção 3: Testar função exibir_contador()**

**Linha 139:** Chama função com parâmetro padrão

**Saída esperada:**
```
🔄 CONTADOR:
Iteração 1
Iteração 2
Iteração 3
✓ Fim das iterações
```

---

```python
    # Seção 4: Dados do usuário com validação
    print("\n👤 INFORMAÇÕES DO USUÁRIO:")
    try:
        nome_usuario, idade_usuario = obter_dados_usuario()
        mensagem = processar_maioridade(nome_usuario, idade_usuario)
        print(f"Resultado: {mensagem}")
    except ValueError as erro:
        print(f"Erro: {erro}")
```

### 📍 Linhas 141-149
**Seção 4: Interação com usuário**

**Linha 145: Desempacotamento de tupla**
```python
nome_usuario, idade_usuario = obter_dados_usuario()
                              ↑
                        Retorna (nome, idade)
                              ↓
nome_usuario = nome
idade_usuario = idade
```

**Linhas 146-147:**
- Chama `processar_maioridade()` com dados
- Exibe resultado

**Linhas 148-149:**
- Try/except para tratar erros de validação

---

```python
    print("\n" + "=" * 50)
    print("Programa finalizado com sucesso!")
    print("=" * 50)
```

### 📍 Linhas 151-153
**Rodapé visual**

---

## BLOCO DE EXECUÇÃO

```python
if __name__ == "__main__":
    main()
```

### 📍 Linhas 156-157
**Por que isto existe?**

**Explicação:**
- `if __name__ == "__main__":` → Condicional especial
- Verdadeira apenas quando arquivo é executado direto
- Falsa se arquivo é importado em outro programa

**Exemplo:**
```python
# Se você rodar: python pratica2_refatorado.py
__name__ == "__main__"  # True → executa main()

# Se você faz: from pratica2_refatorado import calcular_operacao
__name__ == "pratica2_refatorado"  # False → não executa main()
```

**Benefício:**
- Permite usar funções importadas em outros arquivos
- Sem executar `main()` automaticamente

---

## FLUXO COMPLETO

### Diagrama de Execução:

```
┌─────────────────────────────────────────┐
│         INICIA O PROGRAMA               │
└──────────────────┬──────────────────────┘
                   │
            ┌──────▼──────┐
            │    main()   │
            └──────┬──────┘
                   │
    ┌──────────────┼──────────────┐
    │              │              │
    ▼              ▼              ▼
 SEÇÃO 1      SEÇÃO 2        SEÇÃO 3
 Matemática   Conversão      Contador
    │              │              │
    └──────────────┼──────────────┘
                   │
            ┌──────▼──────┐
            │  SEÇÃO 4    │
            │  Usuário    │
            └──────┬──────┘
                   │
    ┌──────────────┴──────────────┐
    │                             │
    ▼                             ▼
 Sucesso                     Erro Capturado
    │                             │
    └──────────────┬──────────────┘
                   │
            ┌──────▼─────────────┐
            │    FIM DO PROG     │
            └────────────────────┘
```

---

## RESUMO EXECUTIVO

### O que cada função faz:

| Função | Entrada | Saída | Propósito |
|--------|---------|-------|----------|
| `calcular_operacao()` | 2 inteiros | 1 inteiro | Soma ou subtrai |
| `calcular_valor_final()` | 1 string | 1 inteiro | Converte + 5 |
| `eh_maior_de_idade()` | 1 inteiro | bool | Verifica age |
| `obter_dados_usuario()` | Nenhuma | Tupla | Coleta dados |
| `processar_maioridade()` | 2 valores | String | Formata mensagem |
| `exibir_contador()` | 1 inteiro | Nenhuma | Exibe contador |
| `main()` | Nenhuma | Nenhuma | Coordena tudo |

---

## CONCEITOS IMPORTANTES DEMONSTRADOS

### 1. **Type Hints**
```python
def funcao(parametro: tipo_entrada) -> tipo_saida:
```

### 2. **Docstrings**
```python
"""Documentação da função"""
```

### 3. **Try/Except**
```python
try:
    operacao_arriscada()
except ErroEspecifico:
    tratar_erro()
```

### 4. **F-strings**
```python
f"Valor: {variavel}"
```

### 5. **Parâmetros com Padrão**
```python
def funcao(parametro: tipo = valor_padrao):
```

### 6. **Desempacotamento de Tupla**
```python
a, b = funcao_que_retorna_tupla()
```

### 7. **Loops**
```python
for item in colecao:
    processar(item)

while condicao:
    continuar()
```

### 8. **Condicionais**
```python
if condicao:
    executar_a()
else:
    executar_b()
```

### 9. **Main Guard**
```python
if __name__ == "__main__":
    main()
```

---

## QUESTÕES PARA REFLEXÃO

1. ❓ Por que usar `eh_maior_de_idade()` em vez de colocar a lógica diretamente em `processar_maioridade()`?
   - **Resposta:** Reutilização e separação de responsabilidades

2. ❓ O que acontece se o usuário digitar " João " (com espaços)?
   - **Resposta:** `.strip()` remove espaços, fica "João"

3. ❓ Como o loop em `obter_dados_usuario()` sabe quando parar?
   - **Resposta:** Quando `return` é executado

4. ❓ Qual é a diferença entre `except ValueError:` e `except Exception:`?
   - **Resposta:** ValueError é específico, Exception pega tudo

5. ❓ Por que `-> None` em algumas funções?
   - **Resposta:** Indicam que não retornam valor, apenas executam

---

## EXERCÍCIOS PRÁTICOS

### Exercício 1: Modificar Validação
Mude `eh_maior_de_idade()` para considerar 21 como maioridade (EUA)

### Exercício 2: Adicionar Função
Crie `eh_aposentavel(idade)` retornando True se idade >= 65

### Exercício 3: Expandir
Adicione coleta de CPF em `obter_dados_usuario()`

### Exercício 4: Tratamento
Faça `calcular_valor_final()` aceitar floats também

### Exercício 5: Análise
Explique por que `obter_dados_usuario()` usa `while True` em vez de `while False`

---

## CONCLUSÃO

Este código refatorado demonstra:
✅ Boas práticas de Python  
✅ Separação de responsabilidades  
✅ Type hints e documentação  
✅ Tratamento de erros  
✅ Funções pequenas e reutilizáveis  
✅ Código legível e manutenível  

**Lição principal:** Não é apenas "código que funciona", mas "código bem escrito"!
