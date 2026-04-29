# PRÁTICA 3 - DEBUG COM IA

## Guia Completo de Identificação e Correção de Erros

---

## 📋 Índice dos Erros

1. [Erro de Sintaxe: Parênteses não fechado](#erro-1)
2. [Erro de Indentação](#erro-2)
3. [NameError: Variável não definida](#erro-3)
4. [TypeError: Tipos incompatíveis](#erro-4)
5. [IndexError: Índice fora do intervalo](#erro-5)
6. [KeyError: Chave não existe](#erro-6)
7. [AttributeError: Método inexistente](#erro-7)
8. [ValueError: Conversão inválida](#erro-8)
9. [UnboundLocalError: Variável não atribuída](#erro-9)
10. [TypeError: Argumentos faltando](#erro-10)
11. [Indentação em Classe](#erro-11)
12. [Loop Infinito](#erro-12)
13. [SyntaxError: Operador errado](#erro-13)
14. [Ordem de Operações](#erro-14)
15. [SyntaxError: Palavra-chave reservada](#erro-15)

---

## ❌ ERRO 1: Parênteses Não Fechado
### Tipo: `SyntaxError`

### ❌ Código com Erro:
```python
def calcular_media(notas
    """Calcula a média das notas."""
    return sum(notas) / len(notas)
```

### 🔍 Causa:
- Parêntese aberto `(` em `notas` não foi fechado com `)`
- Python espera mais código ou fechamento de parêntese

### ✅ Código Corrigido:
```python
def calcular_media(notas):
    """Calcula a média das notas."""
    return sum(notas) / len(notas)
```

### 💡 Dica:
- Sempre verifique se há parênteses, colchetes e chaves balanceados
- Editores com syntax highlighting ajudam a identificar

---

## ❌ ERRO 2: Indentação Incorreta
### Tipo: `IndentationError`

### ❌ Código com Erro:
```python
def validar_idade(idade):
    if idade >= 18:
    print("Maior de idade")  # Falta indentação!
    else:
        print("Menor de idade")
```

### 🔍 Causa:
- O `print()` dentro do `if` não está indentado
- Python usa indentação para definir blocos de código
- Toda linha dentro de um bloco `if`, `for`, `while` etc. deve estar indentada

### ✅ Código Corrigido:
```python
def validar_idade(idade):
    if idade >= 18:
        print("Maior de idade")  # Indentado corretamente
    else:
        print("Menor de idade")
```

### 💡 Dica:
- Use 4 espaços para cada nível de indentação
- Evite misturar tabs e espaços

---

## ❌ ERRO 3: NameError - Variável Não Definida
### Tipo: `NameError`

### ❌ Código com Erro:
```python
def processar_dados(lista):
    total = 0
    for item in lista:
        total += item
    return media  # ❌ 'media' não existe!
```

### 🔍 Causa:
- Variável `media` foi referenciada mas nunca foi definida
- O código definiu `total`, não `media`
- Typo/erro do programador

### ✅ Código Corrigido:
```python
def processar_dados(lista):
    total = 0
    for item in lista:
        total += item
    media = total / len(lista)  # Definir a variável
    return media
```

### 💡 Dica:
- Use um linter (pylint, flake8) para detectar variáveis não definidas
- VS Code pode destacar variáveis que não existem

---

## ❌ ERRO 4: TypeError - Tipos Incompatíveis
### Tipo: `TypeError`

### ❌ Código com Erro:
```python
def concatenar_strings(texto1, texto2):
    resultado = texto1 + texto2 + 10  # ❌ str + str + int
    return resultado
```

### 🔍 Causa:
- Tentando somar string com inteiro: `"texto" + 10`
- O operador `+` funciona diferente para tipos diferentes
- Strings: concatenação
- Números: adição matemática

### ✅ Código Corrigido:
```python
def concatenar_strings(texto1, texto2):
    resultado = texto1 + texto2 + str(10)  # Converter inteiro para string
    return resultado

# Ou, se quer somar números:
def somar_numeros(num1, num2, num3):
    return num1 + num2 + num3
```

### 💡 Dica:
- Type hints ajudam: `def func(texto: str, numero: int) -> str:`
- Use `str()`, `int()`, `float()` para conversão de tipos

---

## ❌ ERRO 5: IndexError - Índice Fora do Intervalo
### Tipo: `IndexError`

### ❌ Código com Erro:
```python
def acessar_primeiro_elemento(lista):
    return lista[10]  # ❌ Lista não tem 10 elementos!
```

### 🔍 Causa:
- Tentando acessar índice 10 de uma lista que pode ter só 3 elementos
- Índices começam do 0
- Lista com 3 elementos: índices 0, 1, 2 (não existe índice 3+)

### ✅ Código Corrigido:
```python
def acessar_primeiro_elemento(lista):
    if len(lista) > 10:
        return lista[10]
    else:
        return None  # Ou lançar um erro informativo

# Ou mais simples:
def acessar_primeiro_elemento(lista):
    if lista:  # Verifica se lista não está vazia
        return lista[0]  # Primeiro elemento
```

### 💡 Dica:
- Sempre verifique o tamanho da lista antes de acessar
- Use `lista[-1]` para último elemento (seguro se lista existe)
- Considere usar `.get()` para dicionários (não lança erro)

---

## ❌ ERRO 6: KeyError - Chave Não Existe
### Tipo: `KeyError`

### ❌ Código com Erro:
```python
def acessar_dicionario():
    dados = {"nome": "João", "idade": 25}
    return dados["email"]  # ❌ Chave "email" não existe!
```

### 🔍 Causa:
- Tentando acessar chave "email" que não existe no dicionário
- Dicionário só tem "nome" e "idade"

### ✅ Código Corrigido:
```python
def acessar_dicionario():
    dados = {"nome": "João", "idade": 25}
    
    # Opção 1: Usar .get() (seguro)
    return dados.get("email", "Email não fornecido")
    
    # Opção 2: Verificar antes
    # if "email" in dados:
    #     return dados["email"]
    # else:
    #     return "Email não fornecido"
```

### 💡 Dica:
- Use `.get()` para evitar KeyError: `dicionario.get(chave, valor_padrao)`
- Verifique existência: `if chave in dicionario:`

---

## ❌ ERRO 7: AttributeError - Método Inexistente
### Tipo: `AttributeError`

### ❌ Código com Erro:
```python
def manipular_string(texto):
    return texto.maiuscula()  # ❌ Método 'maiuscula' não existe!
```

### 🔍 Causa:
- String não tem método `.maiuscula()`
- Método correto é `.upper()`
- Programador pode estar pensando em outra linguagem

### ✅ Código Corrigido:
```python
def manipular_string(texto):
    return texto.upper()  # Correto!
```

### 💡 Métodos Comuns de String:
```python
texto = "Python"
texto.upper()      # "PYTHON"
texto.lower()      # "python"
texto.capitalize() # "Python"
texto.replace("P", "J")  # "Jython"
texto.split()      # ["Python"]
```

---

## ❌ ERRO 8: ValueError - Conversão Inválida
### Tipo: `ValueError`

### ❌ Código com Erro:
```python
def converter_para_inteiro():
    numero_texto = "123abc"
    return int(numero_texto)  # ❌ Não pode converter "123abc" para inteiro!
```

### 🔍 Causa:
- Não pode converter string "123abc" para inteiro
- Inteiros só podem ter dígitos (e sinais)

### ✅ Código Corrigido:
```python
def converter_para_inteiro():
    numero_texto = "123"
    return int(numero_texto)  # ✓ Funciona!

# Ou com tratamento de erro:
def converter_com_validacao(numero_texto):
    try:
        return int(numero_texto)
    except ValueError:
        print(f"Erro: '{numero_texto}' não é um número válido")
        return None
```

### 💡 Dica:
- Sempre trate conversões com try/except
- Valide entrada do usuário antes de converter

---

## ❌ ERRO 9: UnboundLocalError - Variável Não Atribuída
### Tipo: `UnboundLocalError`

### ❌ Código com Erro:
```python
def calcular_resultado(x, y):
    resultado = x + y
    print(temporario)  # ❌ 'temporario' não existe!
    temporario = resultado * 2
    return temporario
```

### 🔍 Causa:
- `temporario` é referenciado antes de ser atribuído
- A atribuição ocorre na linha DEPOIS do print

### ✅ Código Corrigido:
```python
def calcular_resultado(x, y):
    resultado = x + y
    temporario = resultado * 2  # Definir ANTES de usar
    print(temporario)
    return temporario
```

---

## ❌ ERRO 10: TypeError - Argumentos Faltando
### Tipo: `TypeError`

### ❌ Código com Erro:
```python
def saudar(nome, sobrenome):
    return f"Olá, {nome} {sobrenome}!"

mensagem = saudar("João")  # ❌ Faltou 'sobrenome'!
```

### 🔍 Causa:
- Função espera 2 argumentos: `nome` e `sobrenome`
- Apenas 1 argumento foi fornecido: `"João"`

### ✅ Código Corrigido:
```python
def saudar(nome, sobrenome):
    return f"Olá, {nome} {sobrenome}!"

mensagem = saudar("João", "Silva")  # ✓ Correto!

# Ou com argumentos opcionais:
def saudar(nome, sobrenome=""):
    if sobrenome:
        return f"Olá, {nome} {sobrenome}!"
    return f"Olá, {nome}!"

mensagem = saudar("João")  # ✓ Funciona!
```

---

## ❌ ERRO 11: Indentação em Classe
### Tipo: `IndentationError`

### ❌ Código com Erro:
```python
class Pessoa:
    def __init__(self, nome):
    self.nome = nome  # ❌ Indentação errada!

    def apresentar(self):
        return f"Meu nome é {self.nome}"
```

### 🔍 Causa:
- Corpo do método `__init__` não está indentado
- Deve estar um nível abaixo da definição do método

### ✅ Código Corrigido:
```python
class Pessoa:
    def __init__(self, nome):
        self.nome = nome  # ✓ Indentado corretamente
    
    def apresentar(self):
        return f"Meu nome é {self.nome}"
```

---

## ❌ ERRO 12: Loop Infinito
### Tipo: `Lógico` (não causa erro imediato)

### ❌ Código com Erro:
```python
def buscar_numero():
    numeros = [1, 2, 3, 4, 5]
    while True:
        print("Procurando...")
        # ❌ Loop infinito! Nunca sai!
```

### 🔍 Causa:
- `while True` é sempre verdadeiro
- Não há `break` para sair do loop

### ✅ Código Corrigido:
```python
def buscar_numero():
    numeros = [1, 2, 3, 4, 5]
    for numero in numeros:
        print(f"Procurando {numero}...")
    
# Ou com while:
def buscar_numero():
    numeros = [1, 2, 3, 4, 5]
    indice = 0
    while indice < len(numeros):
        print(f"Procurando {numeros[indice]}...")
        indice += 1
```

---

## ❌ ERRO 13: Operador Errado (Atribuição vs Comparação)
### Tipo: `SyntaxError`

### ❌ Código com Erro:
```python
def comparar_valores(a, b):
    if a = b:  # ❌ '=' é atribuição, não comparação!
        return "Iguais"
    return "Diferentes"
```

### 🔍 Causa:
- Usar `=` (atribuição) em vez de `==` (comparação)
- Em `if`, você precisa de comparação, não atribuição

### ✅ Código Corrigido:
```python
def comparar_valores(a, b):
    if a == b:  # ✓ '==' para comparação
        return "Iguais"
    return "Diferentes"

# Outros operadores de comparação:
a == b   # Igual
a != b   # Diferente
a > b    # Maior
a < b    # Menor
a >= b   # Maior ou igual
a <= b   # Menor ou igual
```

---

## ❌ ERRO 14: Ordem de Operações
### Tipo: `Lógico` (não é erro, mas pode parecer)

### ❌ Código com Erro:
```python
def calcular_expressao():
    resultado = 2 + 3 * 4  # Esperava 20? Errado!
    return resultado
```

### 🔍 Explicação:
- Resultado é **14**, não 20
- Multiplicação tem precedência sobre adição
- Python segue ordem matemática: `*` e `/` antes de `+` e `-`

### ✅ Código Corrigido:
```python
def calcular_expressao():
    # Se quer 20: fazer adição primeiro com parênteses
    resultado = (2 + 3) * 4  # (2 + 3) * 4 = 5 * 4 = 20
    return resultado

# Ordem de precedência (do maior para o menor):
# 1. () Parênteses
# 2. ** Exponenciação
# 3. *, /, //, % Multiplicação, divisão, etc.
# 4. +, - Adição, subtração
```

### 💡 Dica:
- Use parênteses quando tiver dúvida
- Deixa o código mais legível

---

## ❌ ERRO 15: Palavra-chave Reservada como Nome de Variável
### Tipo: `SyntaxError`

### ❌ Código com Erro:
```python
def function():
    class = "Python"  # ❌ 'class' é palavra-chave!
    return class
```

### 🔍 Causa:
- `class` é uma palavra-chave reservada do Python
- Não pode ser usada como nome de variável

### ✅ Código Corrigido:
```python
def function():
    classe = "Python"  # ✓ 'classe' não é palavra-chave
    return classe

# Ou outro nome:
def function():
    class_name = "Python"
    return class_name
```

### 📌 Palavras-Chave Reservadas:
```
and, as, assert, async, await, break, class, continue, def, del, 
elif, else, except, finally, for, from, global, if, import, in, 
is, lambda, nonlocal, not, or, pass, raise, return, try, while, 
with, yield, True, False, None
```

---

## 🧠 Estratégia de Debug

### 1️⃣ **Leia a Mensagem de Erro**
```
Traceback (most recent call last):
  File "programa.py", line 10, in <module>
    resultado = lista[10]
IndexError: list index out of range
```

- **Tipo**: `IndexError`
- **Linha**: 10
- **Problema**: Índice fora do intervalo

### 2️⃣ **Identifique o Tipo de Erro**
- `SyntaxError`: Erro de escrita/sintaxe
- `NameError`: Variável não existe
- `TypeError`: Tipos incompatíveis
- `IndexError`: Índice inválido
- `KeyError`: Chave não existe
- `AttributeError`: Método/atributo não existe
- `ValueError`: Valor inválido
- `ZeroDivisionError`: Divisão por zero

### 3️⃣ **Verifique a Linha Indicada**
- Não é sempre a linha do erro
- Pode ser antes (faltou fechar parêntese)

### 4️⃣ **Use Print para Debug**
```python
def funcao(x, y):
    print(f"x = {x}, y = {y}, tipo x = {type(x)}")
    resultado = x + y
    print(f"Resultado = {resultado}")
    return resultado
```

### 5️⃣ **Use um Debugger**
```python
import pdb
pdb.set_trace()  # Pausa e permite inspeção
```

### 6️⃣ **Leia Documentação**
- VS Code com Pylance
- Docstrings das funções
- Stack Overflow

---

## 📋 Checklist para Evitar Erros

- [ ] Parênteses, colchetes e chaves balanceados?
- [ ] Indentação consistente (4 espaços)?
- [ ] Variáveis definidas antes de usar?
- [ ] Tipos compatíveis nas operações?
- [ ] Índices dentro do intervalo?
- [ ] Chaves existem no dicionário?
- [ ] Métodos têm nome correto?
- [ ] Argumentos suficientes na função?
- [ ] Conversões de tipo válidas?
- [ ] Loops têm condição de parada?

---

## 🎯 Próximas Práticas

1. **Teste seu código** antes de entregar
2. **Use type hints** para evitar erros de tipo
3. **Escreva testes** para cada função
4. **Use linters** (pylint, flake8)
5. **Pratique debugging** regularmente
