"""
PRÁTICA 4 - VALIDAÇÃO DE COMPREENSÃO

Teste seu entendimento do código refatorado respondendo às questões!
"""

print("""
╔════════════════════════════════════════════════════════════════════╗
║        PRÁTICA 4 - VALIDAÇÃO DE COMPREENSÃO DO CÓDIGO             ║
║                                                                    ║
║  Instruções:                                                       ║
║  1. Leia cada pergunta cuidadosamente                             ║
║  2. Tente responder sem olhar as respostas                        ║
║  3. Compare sua resposta com a correta                            ║
║  4. Entenda por que estava certo ou errado                        ║
╚════════════════════════════════════════════════════════════════════╝
""")

# ============================================================================
# SEÇÃO 1: ENTENDIMENTO DE FUNÇÕES
# ============================================================================

print("\\n" + "=" * 70)
print("SEÇÃO 1: ENTENDIMENTO DE FUNÇÕES")
print("=" * 70)

questoes_secao1 = [
    {
        "numero": 1,
        "pergunta": "O que a função calcular_operacao(10, 20) retorna?",
        "opcoes": [
            "a) 30 (soma)",
            "b) 10 (diferença)",
            "c) -10 (diferença reversa)",
            "d) 200 (multiplicação)"
        ],
        "resposta": "a) 30 (soma)",
        "explicacao": """
        Como 10 < 20 é VERDADEIRO, a função retorna 10 + 20 = 30
        Se fosse calcular_operacao(30, 20), seria 30 - 20 = 10
        """
    },
    {
        "numero": 2,
        "pergunta": "Qual é a saída de calcular_valor_final('50')?",
        "opcoes": [
            "a) 50",
            "b) 55",
            "c) 500",
            "d) Erro ValueError"
        ],
        "resposta": "b) 55",
        "explicacao": """
        A função converte '50' para 50 (inteiro)
        Depois adiciona 5: 50 + 5 = 55
        Só daria erro se a string não fosse um número válido
        """
    },
    {
        "numero": 3,
        "pergunta": "O que eh_maior_de_idade(18) retorna?",
        "opcoes": [
            "a) True",
            "b) False",
            "c) 18",
            "d) None"
        ],
        "resposta": "a) True",
        "explicacao": """
        A função verifica: 18 >= 18
        Como é VERDADEIRO, retorna True
        Note: >= inclui igualdade, então 18 é considerado maior de idade
        """
    },
    {
        "numero": 4,
        "pergunta": "Qual é a diferença entre 'return' e 'print'?",
        "opcoes": [
            "a) Não há diferença",
            "b) print exibe, return encerra a função",
            "c) return exibe, print encerra",
            "d) print é melhor que return"
        ],
        "resposta": "b) print exibe, return encerra a função",
        "explicacao": """
        - print() → Exibe valor na tela, função continua
        - return → Encerra função e devolve valor
        
        Em main():
        calcular_operacao(10, 20)  # Sem print, valor é descartado
        print(calcular_operacao(10, 20))  # Exibe o resultado
        """
    }
]

for q in questoes_secao1:
    print(f"\\nQUESTÃO {q['numero']}: {q['pergunta']}")
    print("─" * 70)
    for opcao in q['opcoes']:
        print(f"  {opcao}")
    print(f"\\n✓ RESPOSTA: {q['resposta']}")
    print(f"📚 EXPLICAÇÃO:{q['explicacao']}")


# ============================================================================
# SEÇÃO 2: TYPE HINTS E TIPOS
# ============================================================================

print("\\n" + "=" * 70)
print("SEÇÃO 2: TYPE HINTS E TIPOS")
print("=" * 70)

questoes_secao2 = [
    {
        "numero": 5,
        "pergunta": "O que significa 'def funcao(nome: str) -> int:'?",
        "opcoes": [
            "a) Função recebe string, retorna string",
            "b) Função recebe string, retorna inteiro",
            "c) Função recebe inteiro, retorna string",
            "d) Função não retorna nada"
        ],
        "resposta": "b) Função recebe string, retorna inteiro",
        "explicacao": """
        Type hints indicam tipos esperados:
        - 'nome: str' → Parâmetro é string
        - '-> int' → Retorna inteiro
        """
    },
    {
        "numero": 6,
        "pergunta": "O que Tuple[str, int] significa?",
        "opcoes": [
            "a) Uma tupla contendo 1 string e 1 inteiro",
            "b) Uma tupla contendo 2 strings",
            "c) Uma tupla contendo 2 inteiros",
            "d) Uma tupla desorganizada"
        ],
        "resposta": "a) Uma tupla contendo 1 string e 1 inteiro",
        "explicacao": """
        Tuple[str, int] → Tupla com exatamente 2 elementos:
        - 1º elemento: str (string)
        - 2º elemento: int (inteiro)
        
        Exemplo: ("João", 25) ✓
        Exemplo: ("João", "25") ✗ (segundo deveria ser int)
        """
    },
    {
        "numero": 7,
        "pergunta": "O que '-> None' significa?",
        "opcoes": [
            "a) Função não recebe parâmetros",
            "b) Função retorna nada (só executa)",
            "c) Função retorna um valor None",
            "d) Função é desnecessária"
        ],
        "resposta": "b) Função retorna nada (só executa)",
        "explicacao": """
        '-> None' indica que a função não retorna valor:
        - Usa-se para funções que só executam/exibem
        
        Exemplo:
        def exibir() -> None:
            print("Olá")  # Só exibe, não retorna
        
        Não faz: return exibir()
        Faz: exibir()
        """
    }
]

for q in questoes_secao2:
    print(f"\\nQUESTÃO {q['numero']}: {q['pergunta']}")
    print("─" * 70)
    for opcao in q['opcoes']:
        print(f"  {opcao}")
    print(f"\\n✓ RESPOSTA: {q['resposta']}")
    print(f"📚 EXPLICAÇÃO:{q['explicacao']}")


# ============================================================================
# SEÇÃO 3: FLUXO DE CONTROLE
# ============================================================================

print("\\n" + "=" * 70)
print("SEÇÃO 3: FLUXO DE CONTROLE (if/while/for)")
print("=" * 70)

questoes_secao3 = [
    {
        "numero": 8,
        "pergunta": "Quantas vezes o loop 'for numero in range(3):' executa?",
        "opcoes": [
            "a) 1 vez",
            "b) 2 vezes",
            "c) 3 vezes",
            "d) Infinitamente"
        ],
        "resposta": "c) 3 vezes",
        "explicacao": """
        range(3) → [0, 1, 2] → 3 elementos
        
        Iterações:
        1ª: numero = 0
        2ª: numero = 1
        3ª: numero = 2
        
        Depois o loop encerra
        """
    },
    {
        "numero": 9,
        "pergunta": "Por que usar 'while True' em obter_dados_usuario()?",
        "opcoes": [
            "a) Porque True sempre é verdadeiro",
            "b) Para solicitar entrada repetidamente até ser válida",
            "c) Porque não há outra forma de fazer loop",
            "d) Não deveria usar"
        ],
        "resposta": "b) Para solicitar entrada repetidamente até ser válida",
        "explicacao": """
        while True cria loop infinito que:
        - Pede idade do usuário
        - Se inválida: continue → pede novamente
        - Se válida: return → sai do loop
        
        Garante que só sai com entrada válida
        """
    },
    {
        "numero": 10,
        "pergunta": "O que 'continue' faz?",
        "opcoes": [
            "a) Encerra o programa",
            "b) Encerra o loop",
            "c) Pula para a próxima iteração do loop",
            "d) Retorna o valor"
        ],
        "resposta": "c) Pula para a próxima iteração do loop",
        "explicacao": """
        'continue' → Volta ao início do loop, ignora resto do código
        
        Exemplo:
        while True:
            entrada = input()
            if entrada == "abc":
                print("Inválido!")
                continue  ← Volta ao while, pede novamente
            return entrada  ← Só executa se não foi continue
        """
    }
]

for q in questoes_secao3:
    print(f"\\nQUESTÃO {q['numero']}: {q['pergunta']}")
    print("─" * 70)
    for opcao in q['opcoes']:
        print(f"  {opcao}")
    print(f"\\n✓ RESPOSTA: {q['resposta']}")
    print(f"📚 EXPLICAÇÃO:{q['explicacao']}")


# ============================================================================
# SEÇÃO 4: TRATAMENTO DE ERROS
# ============================================================================

print("\\n" + "=" * 70)
print("SEÇÃO 4: TRATAMENTO DE ERROS (try/except)")
print("=" * 70)

questoes_secao4 = [
    {
        "numero": 11,
        "pergunta": "O que acontece quando calcular_valor_final('abc') é chamada?",
        "opcoes": [
            "a) Retorna 'abc'",
            "b) Retorna 'abc' + 5",
            "c) Lança ValueError com mensagem de erro",
            "d) Retorna None"
        ],
        "resposta": "c) Lança ValueError com mensagem de erro",
        "explicacao": """
        try:
            int('abc')  ← Falha! int() não pode converter
        except ValueError:
            raise ValueError(...)  ← Lança erro customizado
        
        Se não capturar com try/except, o programa quebra
        """
    },
    {
        "numero": 12,
        "pergunta": "Qual é a diferença entre 'raise' e 'except'?",
        "opcoes": [
            "a) São a mesma coisa",
            "b) raise lança erro, except captura erro",
            "c) except lança, raise captura",
            "d) Ambas exibem erro"
        ],
        "resposta": "b) raise lança erro, except captura erro",
        "explicacao": """
        raise → Lança/dispara uma exceção
        except → Captura/trata uma exceção
        
        Exemplo:
        try:
            raise ValueError("Erro!")  ← Lança
        except ValueError:
            print("Tratado!")  ← Captura
        """
    },
    {
        "numero": 13,
        "pergunta": "O que 'except ValueError:' captura?",
        "opcoes": [
            "a) Todos os erros",
            "b) Apenas erros ValueError",
            "c) Apenas erros de sintaxe",
            "d) Nenhum erro"
        ],
        "resposta": "b) Apenas erros ValueError",
        "explicacao": """
        except especifica o tipo de erro a capturar:
        
        - except ValueError: ← Captura ValueError
        - except TypeError: ← Captura TypeError
        - except Exception: ← Captura qualquer erro
        
        Se usar ValueError, TypeError não é capturado
        """
    }
]

for q in questoes_secao4:
    print(f"\\nQUESTÃO {q['numero']}: {q['pergunta']}")
    print("─" * 70)
    for opcao in q['opcoes']:
        print(f"  {opcao}")
    print(f"\\n✓ RESPOSTA: {q['resposta']}")
    print(f"📚 EXPLICAÇÃO:{q['explicacao']}")


# ============================================================================
# SEÇÃO 5: DESEMPACOTAMENTO E TUPLAS
# ============================================================================

print("\\n" + "=" * 70)
print("SEÇÃO 5: DESEMPACOTAMENTO E TUPLAS")
print("=" * 70)

questoes_secao5 = [
    {
        "numero": 14,
        "pergunta": "O que 'nome, idade = (\"João\", 25)' faz?",
        "opcoes": [
            "a) Cria uma lista com 2 elementos",
            "b) Desempacota tupla em 2 variáveis",
            "c) Cria variável chamada 'nome, idade'",
            "d) Compara nome com idade"
        ],
        "resposta": "b) Desempacota tupla em 2 variáveis",
        "explicacao": """
        Desempacotamento → Separa elementos de tupla em variáveis
        
        ("João", 25)
           ↓       ↓
        nome   idade
        
        Agora:
        nome = "João"
        idade = 25
        """
    },
    {
        "numero": 15,
        "pergunta": "Por que obter_dados_usuario() retorna uma tupla?",
        "opcoes": [
            "a) Para retornar dois valores",
            "b) Porque é mais rápido",
            "c) Porque é obrigatório",
            "d) Tuplas não existem"
        ],
        "resposta": "a) Para retornar dois valores",
        "explicacao": """
        Função retorna: (nome, idade)
        
        Se usasse lista ou dicionário:
        - Funciona, mas tupla é melhor para retornos fixos
        - Tupla = imutável (segura)
        - Permite desempacotamento elegante
        """
    }
]

for q in questoes_secao5:
    print(f"\\nQUESTÃO {q['numero']}: {q['pergunta']}")
    print("─" * 70)
    for opcao in q['opcoes']:
        print(f"  {opcao}")
    print(f"\\n✓ RESPOSTA: {q['resposta']}")
    print(f"📚 EXPLICAÇÃO:{q['explicacao']}")


# ============================================================================
# SEÇÃO 6: ANÁLISE DE CÓDIGO
# ============================================================================

print("\\n" + "=" * 70)
print("SEÇÃO 6: ANÁLISE DE CÓDIGO")
print("=" * 70)

questoes_secao6 = [
    {
        "numero": 16,
        "pergunta": """
Observe este código:
    def processar_maioridade(nome, idade):
        if eh_maior_de_idade(idade):
            return f"✓ {nome} é maior"
        else:
            return f"✗ {nome} é menor"

Por que eh_maior_de_idade() é chamada aqui?
        """,
        "opcoes": [
            "a) Porque é obrigatório",
            "b) Para reutilizar a lógica de verificação",
            "c) Porque não há outra forma",
            "d) Para piorar o código"
        ],
        "resposta": "b) Para reutilizar a lógica de verificação",
        "explicacao": """
        Boas práticas:
        - Se você já tem eh_maior_de_idade(), use!
        - Não repita código (DRY)
        - Uma mudança em um lugar afeta todas as chamadas
        
        Comparar:
        ❌ Ruim: duplicar 'idade >= 18' em vários lugares
        ✓ Bom: chamar eh_maior_de_idade()
        """
    },
    {
        "numero": 17,
        "pergunta": "Por que usar .strip() depois de input()?",
        "opcoes": [
            "a) Para corrigir erros",
            "b) Para remover espaços em branco",
            "c) Porque é obrigatório",
            "d) Não deveria usar"
        ],
        "resposta": "b) Para remover espaços em branco",
        "explicacao": """
        input() coleta o que o usuário digita:
        - Entrada: "  João  "
        - Com input(): "  João  " (com espaços)
        - Com input().strip(): "João" (limpo!)
        
        .strip() remove:
        - Espaços em branco no início
        - Espaços em branco no final
        - Caracteres de nova linha
        """
    }
]

for q in questoes_secao6:
    print(f"\\nQUESTÃO {q['numero']}: {q['pergunta']}")
    print("─" * 70)
    for opcao in q['opcoes']:
        print(f"  {opcao}")
    print(f"\\n✓ RESPOSTA: {q['resposta']}")
    print(f"📚 EXPLICAÇÃO:{q['explicacao']}")


# ============================================================================
# RESUMO
# ============================================================================

print("\\n" + "=" * 70)
print("RESUMO DAS QUESTÕES")
print("=" * 70)

print("""
Categorias cobertas:

✓ Entendimento de Funções (4 questões)
  - O que cada função retorna
  - Diferenças entre return e print
  - Fluxo de execução

✓ Type Hints e Tipos (3 questões)
  - Interpretação de type hints
  - Tuplas e tipos compostos
  - None como retorno

✓ Fluxo de Controle (3 questões)
  - Loops (for, while)
  - Continue
  - Lógica de repetição

✓ Tratamento de Erros (3 questões)
  - Try/except
  - Raise
  - Captura específica de erros

✓ Desempacotamento (2 questões)
  - Tuplas
  - Retorno múltiplo

✓ Análise de Código (2 questões)
  - Reutilização
  - Boas práticas

═══════════════════════════════════════════════════════════════════

Próximos passos:

1. Revise questões que errou
2. Estude a explicação novamente
3. Faça seus próprios exemplos
4. Explique o código para alguém
5. Teste modificações no código

Lembre: Compreender é melhor que memorizar! 🧠
""")

print("=" * 70)
print("✅ VALIDAÇÃO DE COMPREENSÃO CONCLUÍDA")
print("=" * 70)
