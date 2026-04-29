# Prática 2: Refatoração com Boas Práticas

## 📋 Índice
1. [Problemas Identificados](#problemas-identificados)
2. [Melhorias Implementadas](#melhorias-implementadas)
3. [Comparação Lado a Lado](#comparação-lado-a-lado)
4. [Lições Aprendidas](#lições-aprendidas)

---

## ❌ Problemas Identificados

### 1. **Nomes de Variáveis Genéricos**

**Problema:** Letras isoladas (a, b, c, d, x, y, z) não indicam o propósito da variável.

```python
# ❌ ANTES (Ruim)
a = 10
b = 20
c = 0
x = "123"
y = int(x)
z = y + 5
```

**Impacto:**
- Impossível entender o significado sem ler todo o contexto
- Dificulta manutenção e debug
- Viola princípio de código autodocumentado

---

### 2. **Repetição Desnecessária de Código (DRY)**

**Problema:** Mesmo bloco de código repetido duas vezes.

```python
# ❌ ANTES (Violação de DRY)
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
```

**Impacto:**
- Se precisar mudar a lógica, alterações em um lugar são ignoradas no outro
- Aumenta chances de bugs
- Código fica difícil de manter

**Solução:** Extrair em função reutilizável
```python
# ✅ DEPOIS (Bom)
def calcular_operacao(numero_a: int, numero_b: int) -> int:
    if numero_a < numero_b:
        return numero_a + numero_b
    return numero_a - numero_b

resultado = calcular_operacao(a, b)
```

---

### 3. **Código Morto / Inútil**

**Problema:** Código que nunca será executado (condição impossível).

```python
# ❌ ANTES (Código Morto)
d = 100
if d < 50:  # d é 100, portanto NUNCA será < 50
    print("nunca vai acontecer")
```

**Impacto:**
- Confunde desenvolvedores
- Aumenta complexidade
- Cria débito técnico

**Solução:** Remover código morto
```python
# ✅ DEPOIS (Limpo)
# Código removido
```

---

### 4. **Falta de Documentação**

**Problema:** Nenhuma docstring ou comentário explicativo.

```python
# ❌ ANTES (Sem documentação)
def calcular_operacao(numero_a: int, numero_b: int) -> int:
    if numero_a < numero_b:
        return numero_a + numero_b
    return numero_a - numero_b
```

**Solução:** Adicionar docstrings claras
```python
# ✅ DEPOIS (Com documentação)
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
```

---

### 5. **Mistura de Responsabilidades**

**Problema:** Uma seção faz input, validação E output juntos sem separação clara.

```python
# ❌ ANTES (Responsabilidades Misturadas)
nome = input("digite seu nome: ")
idade = input("idade: ")

if idade == "18":  # Validação fraca: compara string, não inteiro
    print(nome + " é maior de idade")
else:
    print("não sei")  # Mensagem vaga
```

**Problemas:**
- Comparação de string "18" em vez de inteiro 18
- Pessoa com 19, 25, 30 anos seria considerada menor de idade!
- Mensagens genéricas
- Sem tratamento de erro
- Lógica + Input + Output misturados

**Solução:** Separar responsabilidades
```python
# ✅ DEPOIS (Responsabilidades Separadas)

def eh_maior_de_idade(idade: int) -> bool:
    """Verifica se é maior de idade."""
    return idade >= 18

def obter_dados_usuario() -> Tuple[str, int]:
    """Coleta dados do usuário com validação."""
    nome = input("Digite seu nome: ").strip()
    while True:
        try:
            idade = int(input("Digite sua idade: ").strip())
            if idade < 0:
                print("⚠️ Idade não pode ser negativa.")
                continue
            return nome, idade
        except ValueError:
            print("⚠️ Deve ser um número válido.")

def processar_maioridade(nome: str, idade: int) -> str:
    """Determina e retorna mensagem sobre maioridade."""
    if eh_maior_de_idade(idade):
        return f"✓ {nome} ({idade} anos) é maior de idade"
    return f"✗ {nome} ({idade} anos) é menor de idade"
```

---

### 6. **Sem Tratamento de Erros**

**Problema:** Input sem validação ou try/except.

```python
# ❌ ANTES (Sem tratamento de erros)
x = "123"
y = int(x)  # Se x não for número válido, programa quebra!

idade = input("idade: ")  # Se digitar "abc", int() vai falhar
```

**Solução:** Adicionar validação e try/except
```python
# ✅ DEPOIS (Com tratamento de erros)
def calcular_valor_final(valor_string: str) -> int:
    try:
        valor_numerico = int(valor_string)
        return valor_numerico + 5
    except ValueError:
        raise ValueError(f"Erro: '{valor_string}' não é um número válido")

def obter_dados_usuario() -> Tuple[str, int]:
    while True:
        try:
            idade = int(input("Digite sua idade: ").strip())
            if idade < 0:
                print("⚠️ Idade não pode ser negativa.")
                continue
            return nome, idade
        except ValueError:
            print("⚠️ Deve ser um número válido.")
```

---

### 7. **Loop Confuso Sem Necessidade Clara**

**Problema:** Loop que existe mas é confuso em propósito.

```python
# ❌ ANTES (Confuso)
for i in range(3):
    print("loop", i)
    if i == 2:
        print("fim do loop")
```

**Solução:** Esclarecer e organizar
```python
# ✅ DEPOIS (Claro)
def exibir_contador(iteracoes: int = 3) -> None:
    """Exibe um contador com lógica clara."""
    for numero in range(iteracoes):
        print(f"Iteração {numero + 1}")
        if numero == iteracoes - 1:
            print("✓ Fim das iterações")
```

---

## ✅ Melhorias Implementadas

| Melhoria | Benefício | Categoria |
|----------|-----------|-----------|
| **Nomes descritivos** | Código auto-explicativo | Legibilidade |
| **Funções com responsabilidade única** | Código reutilizável e testável | Arquitetura |
| **Docstrings** | Fácil entender propósito e uso | Documentação |
| **Type hints** | Maior segurança e IDE support | Tipagem |
| **DRY (Don't Repeat Yourself)** | Menos bugs, mais manutenível | Manutenibilidade |
| **Separação de responsabilidades** | Código modular | Arquitetura |
| **Tratamento de erros** | Programa robusto | Robustez |
| **Remover código morto** | Código limpo e focado | Qualidade |
| **Validação de entrada** | Dados confiáveis | Segurança |
| **Funções `main()`** | Execução controlada | Organização |

---

## 🔄 Comparação Lado a Lado

### Exemplo 1: Operação Matemática

```python
# ❌ ANTES
a = 10
b = 20
c = 0

if a < b:
    c = a + b
    print("resultado:", c)
else:
    c = a - b
    print("resultado:", c)

if a < b:
    c = a + b
    print("de novo:", c)
else:
    c = a - b
    print("de novo:", c)
```

```python
# ✅ DEPOIS
def calcular_operacao(numero_a: int, numero_b: int) -> int:
    """Calcula a soma se a < b, caso contrário calcula a diferença."""
    if numero_a < numero_b:
        return numero_a + numero_b
    return numero_a - numero_b

numero_a = 10
numero_b = 20
resultado = calcular_operacao(numero_a, numero_b)
print(f"Resultado: {resultado}")
```

**Diferenças:**
- Sem repetição (DRY)
- Nomes claros
- Reutilizável
- Função pura (sem efeitos colaterais)

---

### Exemplo 2: Conversão de Dados

```python
# ❌ ANTES
x = "123"
y = int(x)
z = y + 5
print("valor final:", z)
```

```python
# ✅ DEPOIS
def calcular_valor_final(valor_string: str) -> int:
    """Converte string para inteiro e adiciona 5."""
    try:
        valor_numerico = int(valor_string)
        return valor_numerico + 5
    except ValueError:
        raise ValueError(f"Erro: '{valor_string}' não é um número válido")

valor_final = calcular_valor_final("123")
print(f"Valor final: {valor_final}")
```

**Diferenças:**
- Nomes descritivos (x, y, z → valor_string, valor_numerico, resultado)
- Tratamento de erros
- Reutilizável
- Documentada

---

### Exemplo 3: Validação de Idade

```python
# ❌ ANTES
nome = input("digite seu nome: ")
idade = input("idade: ")

if idade == "18":  # BUG: Compara string, não inteiro!
    print(nome + " é maior de idade")
else:
    print("não sei")  # Mensagem vaga
```

```python
# ✅ DEPOIS
def eh_maior_de_idade(idade: int) -> bool:
    """Verifica se a pessoa é maior de idade."""
    return idade >= 18

def obter_dados_usuario() -> Tuple[str, int]:
    """Coleta nome e idade com validação."""
    nome = input("Digite seu nome: ").strip()
    while True:
        try:
            idade = int(input("Digite sua idade: ").strip())
            if idade < 0:
                print("⚠️ Idade não pode ser negativa.")
                continue
            return nome, idade
        except ValueError:
            print("⚠️ Deve ser um número válido.")

def processar_maioridade(nome: str, idade: int) -> str:
    """Formata mensagem sobre maioridade."""
    if eh_maior_de_idade(idade):
        return f"✓ {nome} ({idade} anos) é maior de idade"
    return f"✗ {nome} ({idade} anos) é menor de idade"

# Uso
nome, idade = obter_dados_usuario()
print(processar_maioridade(nome, idade))
```

**Diferenças:**
- Compara inteiro, não string (não mais >= 18)
- Validação robusta de entrada
- Mensagens claras
- Separação de responsabilidades

---

## 📚 Lições Aprendidas

### 1. **Use Nomes Descritivos**
```python
# ❌ Ruim
a, b, c = 10, 20, 0

# ✅ Bom
numero_a, numero_b, resultado = 10, 20, 0
```

### 2. **DRY: Don't Repeat Yourself**
```python
# ❌ Ruim - Repetir código
calc_a = a + b
print(calc_a)
calc_b = a + b
print(calc_b)

# ✅ Bom - Extrair função
def calcular(x, y):
    return x + y

resultado = calcular(a, b)
print(resultado)
print(resultado)
```

### 3. **Uma Função, Uma Responsabilidade**
```python
# ❌ Ruim - Múltiplas responsabilidades
def processar_usuario():
    nome = input()
    print("Input recebido")
    arquivo = open("users.txt", "w")
    arquivo.write(nome)
    arquivo.close()
    print("Salvo!")

# ✅ Bom - Responsabilidades separadas
def obter_nome() -> str:
    return input("Nome: ")

def salvar_nome(nome: str, arquivo: str) -> None:
    with open(arquivo, "w") as f:
        f.write(nome)

def exibir_confirmacao(nome: str) -> None:
    print(f"✓ {nome} foi salvo!")

nome = obter_nome()
salvar_nome(nome, "users.txt")
exibir_confirmacao(nome)
```

### 4. **Sempre Trate Erros**
```python
# ❌ Ruim
idade = int(input("Idade: "))

# ✅ Bom
try:
    idade = int(input("Idade: "))
except ValueError:
    print("Idade deve ser um número!")
```

### 5. **Use Type Hints**
```python
# ❌ Ruim
def somar(a, b):
    return a + b

# ✅ Bom
def somar(a: int, b: int) -> int:
    """Soma dois inteiros e retorna o resultado."""
    return a + b
```

### 6. **Documente Seu Código**
```python
# ❌ Ruim
def calc(x, y):
    if x < y:
        return x + y
    return x - y

# ✅ Bom
def calcular_operacao(numero_a: int, numero_b: int) -> int:
    """
    Calcula a soma se a < b, caso contrário a diferença.
    
    Args:
        numero_a: Primeiro número
        numero_b: Segundo número
    
    Returns:
        int: Resultado da operação
    """
    if numero_a < numero_b:
        return numero_a + numero_b
    return numero_a - numero_b
```

### 7. **Remova Código Morto**
```python
# ❌ Ruim
d = 100
if d < 50:  # Nunca vai ser verdade!
    print("Isso nunca vai rodar")

# ✅ Bom
# Código removido - mais limpo e claro
```

---

## 🎯 Checklist de Qualidade

Use este checklist ao refatorar:

- [ ] Variáveis têm nomes descritivos?
- [ ] Não há repetição de código (DRY)?
- [ ] Cada função tem uma responsabilidade?
- [ ] Há docstrings adequadas?
- [ ] Type hints estão presentes?
- [ ] Erros são tratados?
- [ ] Código morto foi removido?
- [ ] Código é testável?
- [ ] Nomenclatura é consistente?
- [ ] Há comentários apenas para "por quê", não "o quê"?

---

## 📌 Resumo

| Aspecto | Antes | Depois |
|---------|-------|--------|
| **Funções** | 0 | 6 |
| **Linhas** | 25 | 85 (+ documentação) |
| **Type hints** | 0% | 100% |
| **Docstrings** | 0% | 100% |
| **Repetição** | Sim | Não (DRY) |
| **Tratamento de erros** | Não | Sim |
| **Legibilidade** | ⭐⭐ | ⭐⭐⭐⭐⭐ |
| **Manutenibilidade** | ⭐ | ⭐⭐⭐⭐⭐ |
| **Testabilidade** | ⭐ | ⭐⭐⭐⭐⭐ |
