"""
PRÁTICA 4 - DIAGRAMA DE FLUXO E MAPA MENTAL

Este arquivo visualiza como o código refatorado funciona
através de diagramas ASCII e mapas mentais.
"""

print("""
╔══════════════════════════════════════════════════════════════════════╗
║            PRÁTICA 4 - FLUXO DE EXECUÇÃO DO PROGRAMA               ║
╚══════════════════════════════════════════════════════════════════════╝

┌──────────────────────────────────────────────────────────────────────┐
│  DIAGRAMA 1: FLUXO PRINCIPAL (main)                                  │
└──────────────────────────────────────────────────────────────────────┘

                              START
                                │
                                ▼
                    ┌─────────────────────┐
                    │   EXIBIR CABEÇALHO  │
                    └──────────┬──────────┘
                               │
                ┌──────────────┼──────────────┐
                │              │              │
                ▼              ▼              ▼
            SEÇÃO 1        SEÇÃO 2       SEÇÃO 3
         Matemática      Conversão      Contador
            (10,20)       ("123")          (3)
                │              │              │
                │              │              │
                ▼              ▼              ▼
        calcular_operacao  calcular_valor  exibir_contador
           (10, 20)        final("123")         (3)
                │              │              │
                │              │              │
            Retorna:        Retorna:       Exibe:
             30               128         1, 2, 3
                │              │          + Fim
                │              │              │
                └──────────────┼──────────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │    SEÇÃO 4          │
                    │  INTERAÇÃO USUÁRIO  │
                    └──────────┬──────────┘
                               │
                    ┌──────────▼──────────┐
                    │ obter_dados_usuario │
                    │   Input: (nome,     │
                    │    idade)           │
                    └──────────┬──────────┘
                               │
                    ┌──────────▼──────────┐
                    │processar_maioridade │
                    │  Output: mensagem   │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ EXIBIR RODAPÉ       │
                    └──────────┬──────────┘
                               │
                               ▼
                              END


┌──────────────────────────────────────────────────────────────────────┐
│  DIAGRAMA 2: FUNÇÃO obter_dados_usuario()                            │
└──────────────────────────────────────────────────────────────────────┘

                            INÍCIO
                              │
                    ┌─────────▼─────────┐
                    │ Coleta NOME       │
                    │ input + strip()   │
                    └────────┬──────────┘
                             │
                   ┌─────────▼─────────┐
                   │ LOOP: while True  │
                   └────────┬──────────┘
                            │
            ┌───────────────┼───────────────┐
            │               │               │
            ▼               ▼               ▼
         INPUT           TRY:            EXCEPT:
        idade_input   int(idade_input)   ValueError
            │               │               │
            └───────┬───────┘               │
                    │                       │
            Conversão bem-sucedida?         │
                    │                       │
        ┌───────────┴───────────┐          │
        │ SIM                   │ NÃO      │
        │                       │          │
        ▼                       │          ▼
    Validação             Exceção    Exibir erro
    idade < 0?            lançada     Volta loop
        │                             │
    ┌───┴───┐                 ▼
    │       │            (continua)
   NÃO     SIM
    │       │
    │       ▼
    │    Erro exibido
    │    Volta loop
    │
    ▼
  Retorna
(nome, idade)


┌──────────────────────────────────────────────────────────────────────┐
│  DIAGRAMA 3: FUNÇÃO processar_maioridade()                           │
└──────────────────────────────────────────────────────────────────────┘

          INPUT: (nome, idade)
                 │
         ┌───────▼───────┐
         │ eh_maior_de   │
         │ idade(idade)? │
         └───────┬───────┘
                 │
        ┌────────┴────────┐
        │                 │
      TRUE              FALSE
        │                 │
        ▼                 ▼
    Retorna:          Retorna:
  "✓ João (25)      "✗ Ana (16)
   é maior de        é menor de
   idade"            idade"
        │                 │
        └────────┬────────┘
                 │
              OUTPUT
           (mensagem formatada)


┌──────────────────────────────────────────────────────────────────────┐
│  DIAGRAMA 4: CHAMADAS DE FUNÇÃO                                      │
└──────────────────────────────────────────────────────────────────────┘

main()
  │
  ├─ calcular_operacao(10, 20)
  │  └─ Lógica: if 10 < 20: return 10+20
  │     └─ RETORNA: 30
  │
  ├─ calcular_valor_final("123")
  │  └─ Lógica: try: int("123") + 5
  │     └─ RETORNA: 128
  │
  ├─ exibir_contador(3)
  │  └─ Lógica: for i in range(3)
  │     └─ IMPRIME: Iteração 1, 2, 3 + Fim
  │
  ├─ obter_dados_usuario()
  │  └─ Lógica: while True + try/except
  │     └─ RETORNA: (nome, idade)
  │
  ├─ processar_maioridade(nome, idade)
  │  ├─ Chama: eh_maior_de_idade(idade)
  │  │  └─ RETORNA: bool
  │  └─ RETORNA: string formatada
  │
  └─ Exibir resultado


┌──────────────────────────────────────────────────────────────────────┐
│  DIAGRAMA 5: TIPOS DE DADOS (Type Hints)                             │
└──────────────────────────────────────────────────────────────────────┘

calcular_operacao
   ↓
(int, int) ──→ Função ──→ int
   ↓                       ↓
(10, 20) ──→ calcular_operacao ──→ 30


calcular_valor_final
   ↓
(str) ──→ Função ──→ int
   ↓                  ↓
"123" ──→ calcular_valor_final ──→ 128


eh_maior_de_idade
   ↓
(int) ──→ Função ──→ bool
   ↓                  ↓
25 ──→ eh_maior_de_idade ──→ True


obter_dados_usuario
   ↓
(None) ──→ Função ──→ Tuple[str, int]
   ↓                  ↓
(input) ──→ obter_dados_usuario ──→ ("João", 25)
                                     ↓       ↓
                                    str     int


processar_maioridade
   ↓
(str, int) ──→ Função ──→ str
   ↓                        ↓
("João", 25) ──→ processar_maioridade ──→ "✓ João é maior..."


exibir_contador
   ↓
(int) ──→ Função ──→ None
   ↓                 ↓
3 ──→ exibir_contador ──→ (imprime)


┌──────────────────────────────────────────────────────────────────────┐
│  DIAGRAMA 6: ESTRUTURA DE DECISÃO (if/else)                          │
└──────────────────────────────────────────────────────────────────────┘

FUNÇÃO: calcular_operacao

         entrada: numero_a, numero_b

              ┌─────────────┐
              │ numero_a   │
              │   < numero_b?
              └──────┬──────┘
                     │
         ┌───────────┴───────────┐
         │                       │
        SIM                     NÃO
         │                       │
         ▼                       ▼
     return              return
    a + b              a - b


FUNÇÃO: eh_maior_de_idade

         entrada: idade

              ┌──────────┐
              │ idade   │
              │ >= 18?   │
              └────┬─────┘
                   │
         ┌─────────┴─────────┐
         │                   │
        SIM                 NÃO
         │                   │
         ▼                   ▼
       True                False


┌──────────────────────────────────────────────────────────────────────┐
│  DIAGRAMA 7: LOOP (for/while)                                        │
└──────────────────────────────────────────────────────────────────────┘

FUNÇÃO: exibir_contador (iteracoes=3)

        for numero in range(3):
            print(f"Iteração {numero + 1}")
            if numero == 2:
                print("Fim")

Execução:
┌────────────────────────────────┐
│ Iteração 1 do loop             │
│ numero = 0                     │
│ print("Iteração 1")            │
│ 0 == 2? NÃO → não imprime fim  │
└────────────┬───────────────────┘
             ▼
┌────────────────────────────────┐
│ Iteração 2 do loop             │
│ numero = 1                     │
│ print("Iteração 2")            │
│ 1 == 2? NÃO → não imprime fim  │
└────────────┬───────────────────┘
             ▼
┌────────────────────────────────┐
│ Iteração 3 do loop             │
│ numero = 2                     │
│ print("Iteração 3")            │
│ 2 == 2? SIM → print("Fim")     │
└────────────┬───────────────────┘
             ▼
        Loop encerra


FUNÇÃO: obter_dados_usuario

        while True:
            try: ... (linha 1)
            except ValueError: (linha 2)

Fluxo:
┌──────────────────────────────────┐
│ Iteração 1: while True           │
│ Tenta: int(input_ruim)           │
│ ERRO → except → mensagem         │
│ continue → volta ao while        │
└────────────┬─────────────────────┘
             ▼
┌──────────────────────────────────┐
│ Iteração 2: while True           │
│ Tenta: int(input_bom)            │
│ SUCESSO → validações OK          │
│ return → sai do while            │
└────────────┬─────────────────────┘
             ▼
        Loop encerra + retorna


┌──────────────────────────────────────────────────────────────────────┐
│  DIAGRAMA 8: TRATAMENTO DE ERROS (try/except)                        │
└──────────────────────────────────────────────────────────────────────┘

try:
    int("123")     ← Sucesso ✓
except ValueError:
    # Nunca chega aqui

           ▼
       ✓ Função retorna 128


try:
    int("abc")     ← Erro! ValueError ✗
except ValueError:
    # Chega aqui!
    raise ValueError(...)

           ▼
       ✗ Exceção lançada


┌──────────────────────────────────────────────────────────────────────┐
│  DIAGRAMA 9: DESEMPACOTAMENTO DE TUPLA                               │
└──────────────────────────────────────────────────────────────────────┘

obter_dados_usuario() retorna:
("João", 25)
   ↓       ↓
 nome    idade


nome_usuario, idade_usuario = obter_dados_usuario()
     ↓                                    ↓
   "João"                         ("João", 25)
     ↑
  atribuído


nome_usuario = "João"
idade_usuario = 25


┌──────────────────────────────────────────────────────────────────────┐
│  DIAGRAMA 10: MAIN GUARD                                             │
└──────────────────────────────────────────────────────────────────────┘

Cenário 1: Executar arquivo
$ python pratica2_refatorado.py

  if __name__ == "__main__":  ← Verdadeiro
      main()                  ← Executa


Cenário 2: Importar em outro arquivo
from pratica2_refatorado import calcular_operacao

  if __name__ == "__main__":  ← Falso!
      main()                  ← NÃO executa
  
  Mas calcular_operacao está disponível para usar!


┌──────────────────────────────────────────────────────────────────────┐
│  MAPA MENTAL: CONCEITOS PRINCIPAIS                                   │
└──────────────────────────────────────────────────────────────────────┘

                         CÓDIGO
                           │
            ┌──────────────┼──────────────┐
            │              │              │
        FUNÇÕES        ESTRUTURAS     TIPOS
            │              │              │
        ┌───┴────────┐    ├─ if/else    ├─ int
        │            │    ├─ for        ├─ str
        │      ┌─────┴──┐ ├─ while      ├─ bool
        │      │        │ ├─ try/except ├─ Tuple
        │      │        │ │             ├─ None
        │   Reutilizar  │ │             │
        │   Simples     │ │  Controle   │
        │   Testável    │ │  de fluxo   │
        │   Documentada │ │             │
        └───────────────┘ └─────────────┘


╔══════════════════════════════════════════════════════════════════════╗
║                     FIM DOS DIAGRAMAS                               ║
║                                                                      ║
║  Use estes diagramas para:                                          ║
║  ✓ Entender o fluxo do programa                                    ║
║  ✓ Visualizar como funções se conectam                             ║
║  ✓ Rastrear valores através das chamadas                           ║
║  ✓ Aprender estruturas de controle                                 ║
║  ✓ Praticar explicação de código                                   ║
╚══════════════════════════════════════════════════════════════════════╝
""")
