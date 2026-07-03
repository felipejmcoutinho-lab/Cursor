# -*- coding: utf-8 -*-
"""Conteúdo estendido — Parte 2 do Manual TIA Portal BLBW."""

EXTENDED_INDEX = [
    ("CAPÍTULO 1 (continuação): Bit Logic Operations", [
        "1.4 Inversão de RLO, Bobinas Especiais e Contatos de Borda",
        "1.5 Operações em Campo de Bits (SET_BF / RESET_BF)",
    ]),
    ("CAPÍTULO 2 (continuação): Timer Operations", [
        "2.5 Instruções Coil de Temporizador (-(TON)-, -(RT)-, -(PT)-)",
        "2.6 Controle de Runtime (RE_TRIGR, RUNTIME)",
    ]),
    ("CAPÍTULO 4 (continuação): Comparator Operations", [
        "4.3 Comparadores Variant e Ponteiros (EQ_Type, IS_NULL, IS_ARRAY)",
        "4.4 Validação de Integridade (|OK| / |NOT_OK|)",
    ]),
    ("CAPÍTULO 5 (continuação): Math Functions", [
        "5.4 Operações Modulares e Incrementais (MOD, INC, DEC, NEG, ABS)",
        "5.5 Bloco CALCULATE — Expressões Compostas",
    ]),
    ("CAPÍTULO 6 (continuação): Move Operations", [
        "6.3 Operações Ininterruptas e Bit Packing (UMOVE_BLK, SCATTER, GATHER)",
        "6.4 Variant e Limites de Array (VariantGet, LOWER_BOUND, UPPER_BOUND)",
    ]),
    ("CAPÍTULO 8 (continuação): Program Control", [
        "8.3 Lista de Saltos (JMP_LIST) e Diagnóstico Local (GET_ERROR)",
        "8.4 Controle de Execução (STP, ENDIS_PW)",
    ]),
    ("APÊNDICE A: Arquitetura de Execução e Ciclo de Scan", [
        "A.1 Hierarquia de OBs e Prioridade de Saídas",
        "A.2 Process Image vs Acesso Direto (%I / %Q / PEEK / POKE)",
    ]),
    ("APÊNDICE B: Referência Rápida LAD ↔ STL", [
        "B.1 Tabela de Equivalência de Instruções",
        "B.2 Convenções de Nomenclatura BLBW",
    ]),
]

EXTENDED_CHAPTERS = [
    {
        "title": "CAPÍTULO 1 (continuação): Bit Logic Operations",
        "sections": [
            {
                "title": "1.4 Inversão de RLO, Bobinas Especiais e Contatos de Borda",
                "instructions": [
                    {
                        "name": "Invert RLO — |NOT|",
                        "objective": "Inverte o Result of Logic Operation (RLO) atual sem alterar o operando de entrada. O estado do bit monitorado permanece intacto; apenas a corrente lógica é negada.",
                        "when_use": "Inversão de cadeia lógica sem criar contato NF adicional, simplificação de redes com múltiplas negações, preparação de condição para bloco que requer RLO invertido.",
                        "syntax": "Sem operando associado. Atua sobre o RLO acumulado na rede. Em STL: NOT após A/AN. Em LAD: elemento |NOT| em série.",
                        "lad": """[INSERIR IMAGEM DO ÍCONE DA FUNÇÃO Invert RLO AQUI]

   Cond_A
------| |------|NOT|------+-----( ) Output_Inv
                           |
   Cond_B
------| |------------------+""",
                        "stl": """A     "Cond_A"
NOT
A     "Cond_B"
=     "Output_Inv"
""",
                    },
                    {
                        "name": "Bobina Negada — -(/)-",
                        "objective": "Atribui o complemento do RLO ao operando: Q = NOT(RLO). Quando a cadeia lógica conduz, o operando é resetado; quando não conduz, o operando é setado.",
                        "when_use": "Sinalização invertida de estado (lâmpada de 'não pronto'), interface com hardware active-low, lógica de falha silenciosa onde ausência de condição = alarme.",
                        "syntax": "Operando (BOOL): Saída ou memória. Comportamento oposto à bobina -( )-.",
                        "lad": """[INSERIR IMAGEM DO ÍCONE DA FUNÇÃO Bobina Negada AQUI]

   System_Fault
------| |---------------------(/) Lamp_OK
""",
                        "stl": """A     "System_Fault"
NOT
=     "Lamp_OK"
""",
                    },
                    {
                        "name": "Contato de Borda Positiva — |P| e Bobina P — -(P)-",
                        "objective": "|P|: conduz por 1 scan na transição 0→1 do operando. -(P)-: seta o operando por 1 scan na borda de subida do RLO. Equivalente funcional a P_TRIG/FP sem bloco dedicado.",
                        "when_use": "Incremento de contador em rede única, latch momentâneo de comando, alternativa compacta quando não há FB disponível.",
                        "syntax": "|P|: operando monitorado com memória interna implícita no compilador. -(P)-: operando de saída pulsada. Preferir R_TRIG em código reutilizável.",
                        "lad": """[INSERIR IMAGEM DO ÍCONE DA FUNÇÃO Contato P AQUI]

   Btn_Count
------|P|-------------------------( ) Count_Pulse
""",
                        "stl": """A     "Btn_Count"
FP    "DB_Edge".Btn_Mem
=     "Count_Pulse"
""",
                    },
                    {
                        "name": "Contato de Borda Negativa — |N| e Bobina N — -(N)-",
                        "objective": "|N|: conduz por 1 scan na transição 1→0. -(N)-: reset pulsado na borda de descida do RLO.",
                        "when_use": "Detecção de desacionamento de sensor, contagem de retirada de peça, trigger de log ao desligar equipamento.",
                        "syntax": "Equivalente a FN/F_TRIG. Memória de borda obrigatória em STL.",
                        "lad": """[INSERIR IMAGEM DO ÍCONE DA FUNÇÃO Contato N AQUI]

   Sens_Out
------|N|-------------------------( ) Piece_Left_Zone
""",
                        "stl": """A     "Sens_Out"
FN    "DB_Edge".Sens_Mem
=     "Piece_Left_Zone"
""",
                    },
                ],
            },
            {
                "title": "1.5 Operações em Campo de Bits (SET_BF / RESET_BF)",
                "instructions": [
                    {
                        "name": "SET_BF — Set Bit Field",
                        "objective": "Seta um campo contínuo de N bits a partir de uma posição inicial (INDEX) em um operando BYTE/WORD/DWORD. Operação atômica em uma instrução.",
                        "when_use": "Inicialização de palavra de comando para múltiplas válvulas, set de máscara de habilitação de eixos, reset parcial de word de status.",
                        "syntax": "OUT: operando de destino (BYTE/WORD/DWORD). INDEX: bit inicial (0-based). LEN: quantidade de bits a setar.",
                        "lad": """[INSERIR IMAGEM DO ÍCONE DA FUNÇÃO SET_BF AQUI]

                  +----------+
   Init_Valves    |  SET_BF  |
------| |--------|          |
"Valve_Cmd".Word--| OUT      |
       0 ----------| INDEX    |
       4 ----------| LEN      |
                  +----------+""",
                        "stl": """A     "Init_Valves"
L     4
L     0
SET_BF "Valve_Cmd".Word
""",
                    },
                    {
                        "name": "RESET_BF — Reset Bit Field",
                        "objective": "Reseta (zera) campo contínuo de N bits a partir de INDEX. Complemento do SET_BF para limpeza seletiva de word de comando.",
                        "when_use": "Parada de grupo de válvulas, limpeza de byte de diagnóstico, desabilitação de faixa de saídas digitais em word consolidada.",
                        "syntax": "OUT, INDEX, LEN — idênticos ao SET_BF.",
                        "lad": """[INSERIR IMAGEM DO ÍCONE DA FUNÇÃO RESET_BF AQUI]

                  +-----------+
   Stop_Group     | RESET_BF  |
------| |--------|           |
"Valve_Cmd".Word--| OUT       |
       0 ----------| INDEX     |
       4 ----------| LEN       |
                  +-----------+""",
                        "stl": """A     "Stop_Group"
L     4
L     0
RESET_BF "Valve_Cmd".Word
""",
                    },
                ],
            },
        ],
    },
    {
        "title": "CAPÍTULO 2 (continuação): Timer Operations",
        "sections": [
            {
                "title": "2.5 Instruções Coil de Temporizador (-(TON)-, -(RT)-, -(PT)-)",
                "instructions": [
                    {
                        "name": "-(TON)- / -(TOF)- / -(TP)- / -(TONR)- — Coil Timer",
                        "objective": "Variantes coil-style dos temporizadores IEC. Integram disparo e instância de timer na mesma rede LAD. O timer referenciado deve ter DB de instância associado via propriedade da coil.",
                        "when_use": "Redes compactas em LAD sem bloco box, código legado S7-300 migrado, sequências visuais em documentação de manutenção.",
                        "syntax": "Coil -(TON)-: parâmetros TV (TIME) e bi/timer instance. Saída Q refletida na coil ou em contato posterior. -(PT)-: carrega preset sem iniciar contagem.",
                        "lad": """[INSERIR IMAGEM DO ÍCONE DA FUNÇÃO -(TON)- AQUI]

   Start_Delay
------| |---------------------(TON)
                              TV := T#5s
                              Instance := "DB_TON_Start"

   "DB_TON_Start".Q
------| |---------------------( ) Motor_Allowed
""",
                        "stl": """// Coil timers são exclusivos LAD; equivalente STL:
CALL  "TON", "DB_TON_Start"
   IN := "Start_Delay"
   PT := T#5S
A     "DB_TON_Start".Q
=     "Motor_Allowed"
""",
                    },
                    {
                        "name": "-(RT)- — Reset Timer / -(PT)- — Load Preset",
                        "objective": "-(RT)-: zera ET e Q do timer instanciado. -(PT)-: carrega novo PT sem resetar estado de execução — uso avançado em HMI para ajuste de tempo em runtime.",
                        "when_use": "Reset manual de temporizador via IHM, abort de sequência, retargeting de preset em receita sem reiniciar máquina.",
                        "syntax": "-(RT)-: associado ao DB de instância do timer. -(PT)-: TV := novo valor TIME.",
                        "lad": """[INSERIR IMAGEM DO ÍCONE DA FUNÇÃO -(RT)- AQUI]

   HMI_Reset
------| |---------------------(RT)
                              Instance := "DB_TON_Start"

   HMI_NewTime
------| |---------------------(PT)
                              TV := "HMI".Delay_SP
                              Instance := "DB_TON_Start"
""",
                        "stl": """// Reset via CALL com R em TONR ou reinício por IN:=FALSE
A     "HMI_Reset"
R     "DB_TON_Start".IN_Instance_Flag  // conforme instância
""",
                    },
                ],
            },
            {
                "title": "2.6 Controle de Runtime (RE_TRIGR, RUNTIME)",
                "instructions": [
                    {
                        "name": "RE_TRIGR — Restart Cycle Monitoring Time",
                        "objective": "Reinicia o tempo de ciclo máximo (cycle monitoring timeout) da CPU. Evita erro OB80 por overrun quando bloco de inicialização ou download estende o scan.",
                        "when_use": "Após download parcial, inicialização de arrays grandes, primeiro scan pós-power-on com carga pesada, testes de comissionamento.",
                        "syntax": "Sem parâmetros. Chamada incondicional. Executar pontualmente — não deixar em OB1 cíclico.",
                        "lad": """[INSERIR IMAGEM DO ÍCONE DA FUNÇÃO RE_TRIGR AQUI]

   First_Scan
------| |--------------------+---------+
                               |RE_TRIGR |
                               +---------+""",
                        "stl": """A     "First_Scan"
CALL  RE_TRIGR
""",
                    },
                    {
                        "name": "RUNTIME — Measure Program Runtime",
                        "objective": "Mede tempo de execução em microssegundos de um trecho de código delimitado por duas chamadas RUNTIME consecutivas.",
                        "when_use": "Profiling de OB/FC crítico, diagnóstico de overrun intermitente, validação de otimização de código em S7-1500.",
                        "syntax": "MEM (RET_VAL): DINT acumulador. Primeira chamada: inicia medição. Segunda: retorna delta em µs.",
                        "lad": """[INSERIR IMAGEM DO ÍCONE DA FUNÇÃO RUNTIME AQUI]

                  +---------+
                  | RUNTIME |-- "DB_Diag".T_Start
                  +---------+
        // ... código medido ...
                  +---------+
                  | RUNTIME |-- "DB_Diag".T_Delta
                  +---------+""",
                        "stl": """CALL  RUNTIME, "DB_Diag".T_Start
// ... código ...
CALL  RUNTIME, "DB_Diag".T_Delta
""",
                    },
                ],
            },
        ],
    },
    {
        "title": "CAPÍTULO 4 (continuação): Comparator Operations",
        "sections": [
            {
                "title": "4.3 Comparadores Variant e Ponteiros (EQ_Type, IS_NULL, IS_ARRAY)",
                "instructions": [
                    {
                        "name": "EQ_Type / NE_Type — Comparação de Tipo",
                        "objective": "Compara o tipo de dado de um operando VARIANT ou tag genérica com outro tipo referência. Retorna TRUE se tipos coincidem (EQ) ou diferem (NE).",
                        "when_use": "Bibliotecas genéricas de comunicação, FC único para múltiplos tipos de receita, validação de VARIANT recebido via PUT/GET antes de processar.",
                        "syntax": "IN1: VARIANT ou tag tipada. IN2: tipo referência (ex. \"REAL\", struct name). OUT: BOOL.",
                        "lad": """[INSERIR IMAGEM DO ÍCONE DA FUNÇÃO EQ_Type AQUI]

                  +----------+
"Rx_Data".Variant-|          |
                  | EQ_Type  |---------------------( ) Type_Real_OK
      "REAL" ------|          |
                  +----------+""",
                        "stl": """CALL  "EQ_Type_Check"
   IN1  := "Rx_Data".Variant
   IN2  := "REAL"
   OUT  := "Type_Real_OK"
""",
                    },
                    {
                        "name": "IS_NULL / NOT_NULL — Verificação de Ponteiro",
                        "objective": "IS_NULL: TRUE se ponteiro/VARIANT não referencia dado válido. NOT_NULL: inverso. Essencial antes de dereferenciar VARIANT em runtime.",
                        "when_use": "Receitas opcionais, parâmetros de FB não configurados, proteção contra acesso a DB inexistente em endereçamento dinâmico.",
                        "syntax": "IN: VARIANT ou Pointer. OUT: BOOL.",
                        "lad": """[INSERIR IMAGEM DO ÍCONE DA FUNÇÃO IS_NULL AQUI]

                  +----------+
"Param".Variant---|          |
                  | IS_NULL  |---------------------( ) Param_Missing
                  +----------+""",
                        "stl": """CALL  "IS_NULL_Check"
   IN  := "Param".Variant
   OUT := "Param_Missing"
""",
                    },
                    {
                        "name": "IS_ARRAY / EQ_ElemType — Verificação de Array",
                        "objective": "IS_ARRAY confirma se operando é array. EQ_ElemType compara tipo dos elementos do array com tipo referência.",
                        "when_use": "Iteração dinâmica com CountOfElements, validação de buffer recebido de SCADA, UDFC genérico para tendências.",
                        "syntax": "IN: VARIANT ou array. OUT: BOOL. EQ_ElemType requer IN2 como tipo elemento.",
                        "lad": """[INSERIR IMAGEM DO ÍCONE DA FUNÇÃO IS_ARRAY AQUI]

                  +----------+
"Trend".Variant---|          |
                  | IS_ARRAY |---------------------( ) Trend_IsArray
                  +----------+""",
                        "stl": """CALL  "IS_ARRAY_Check"
   IN  := "Trend".Variant
   OUT := "Trend_IsArray"
""",
                    },
                ],
            },
            {
                "title": "4.4 Validação de Integridade (|OK| / |NOT_OK|)",
                "instructions": [
                    {
                        "name": "|OK| / |NOT_OK| — Check Validity",
                        "objective": "Contatos de validação para tags com status de qualidade (S7-1500, tags de comunicación). |OK|: conduz se tag válida. |NOT_OK|: conduz se inválida ou substituída.",
                        "when_use": "Integração com tags OPC/Profinet com quality code, tratamento de valor substituto (substitute value) em falha de sensor, intertravamento em perda de link.",
                        "syntax": "Operando: tag com atributo de validade habilitado. Disponível em CPUs com suporte a qualidade de tag.",
                        "lad": """[INSERIR IMAGEM DO ÍCONE DA FUNÇÃO OK AQUI]

"AI_Flow".Value
------|OK|------+-----( ) Flow_Control_En
                 |
"Comm_Link"
------| |-------+""",
                        "stl": """// Verificar validade via bloco de sistema ou qualidade explícita
A     "AI_Flow".Valid
A     "Comm_Link"
=     "Flow_Control_En"
""",
                    },
                ],
            },
        ],
    },
    {
        "title": "CAPÍTULO 5 (continuação): Math Functions",
        "sections": [
            {
                "title": "5.4 Operações Modulares e Incrementais (MOD, INC, DEC, NEG, ABS)",
                "instructions": [
                    {
                        "name": "MOD — Return Remainder of Division",
                        "objective": "Retorna resto da divisão inteira IN1 / IN2. ENO = FALSE se IN2 = 0.",
                        "when_use": "Cálculo de posição em ciclo (índice módulo N), rotação de estação de trabalho, divisão de pacotes em buffer circular.",
                        "syntax": "IN1, IN2: INT/DINT. OUT: resto. ENO: status.",
                        "lad": """[INSERIR IMAGEM DO ÍCONE DA FUNÇÃO MOD AQUI]

                  +---------+
"Station".Idx-----|   MOD   |-- "Station".Pos
       8 ----------|         |
                  +---------+""",
                        "stl": """CALL  "MOD_Station"
   IN1 := "Station".Idx
   IN2 := 8
   OUT := "Station".Pos
""",
                    },
                    {
                        "name": "INC / DEC — Increment / Decrement",
                        "objective": "Incrementa (INC) ou decrementa (DEC) o valor de IN em 1 e escreve em OUT. Equivalente a ADD/OUT com constante 1, otimizado.",
                        "when_use": "Índice de array, contador manual em HMI, passo de sequência em FC leve.",
                        "syntax": "IN/OUT: INT ou DINT. OUT pode ser mesma tag que IN (in-place).",
                        "lad": """[INSERIR IMAGEM DO ÍCONE DA FUNÇÃO INC AQUI]

   Step_Advance
------| |--------+---------+
                  |   INC   |-- "Seq".StepIdx
"Seq".StepIdx-----|         |
                  +---------+""",
                        "stl": """A     "Step_Advance"
L     "Seq".StepIdx
INC
T     "Seq".StepIdx
""",
                    },
                    {
                        "name": "NEG / ABS — Negation / Absolute Value",
                        "objective": "NEG: complemento de dois (negativo). ABS: valor absoluto. ABS de INT_MIN pode overflow — usar DINT intermediário.",
                        "when_use": "Cálculo de erro bidirecional (ABS setpoint - PV), inversão de comando, tratamento de delta em posicionamento.",
                        "syntax": "IN: INT/DINT/REAL. OUT: mesmo tipo.",
                        "lad": """[INSERIR IMAGEM DO ÍCONE DA FUNÇÃO ABS AQUI]

                  +---------+
"Error".Value-----|   ABS   |-- "Error".Magnitude
                  +---------+""",
                        "stl": """CALL  "ABS_Error"
   IN  := "Error".Value
   OUT := "Error".Magnitude
""",
                    },
                ],
            },
            {
                "title": "5.5 Bloco CALCULATE — Expressões Compostas",
                "instructions": [
                    {
                        "name": "CALCULATE — Expressão Matemática Configurável",
                        "objective": "Bloco com editor de expressão para fórmulas compostas (ex: (IN1+IN2)*0.5/SQRT(IN3)). Reduz cascata de blocos ADD/MUL/DIV.",
                        "when_use": "Engenharia de processo com fórmulas complexas, linearização de curva, cálculo de entalpia ou vazão compensada — documentar expressão no comentário do bloco.",
                        "syntax": "EN, ENO. Operandos IN1..INn conforme expressão. OUT: tipo definido na configuração. Erro de domínio (sqrt negativo) → ENO=FALSE.",
                        "lad": """[INSERIR IMAGEM DO ÍCONE DA FUNÇÃO CALCULATE AQUI]

                  +-----------+
   Calc_En        | CALCULATE |
------| |--------|EN        ENO|-----------------( ) Calc_Valid
"Flow".Temp-------|           |
"Flow".Press------|  OUT:     |-- "Flow".Compensated
                  | (IN1+IN2)*0.5
                  +-----------+""",
                        "stl": """// CALCULATE é primariamente LAD/FBD; em STL usar CALL com parâmetros
A     "Calc_En"
CALL  "CALC_FlowComp"
   IN1 := "Flow".Temp
   IN2 := "Flow".Press
   OUT := "Flow".Compensated
   ENO => "Calc_Valid"
""",
                    },
                ],
            },
        ],
    },
    {
        "title": "CAPÍTULO 6 (continuação): Move Operations",
        "sections": [
            {
                "title": "6.3 Operações Ininterruptas e Bit Packing (UMOVE_BLK, SCATTER, GATHER)",
                "instructions": [
                    {
                        "name": "UMOVE_BLK / UFILL_BLK — Uninterruptible Move/Fill",
                        "objective": "Variantes atômicas de MOVE_BLK e FILL_BLK. Garantem que cópia não seja interrompida por evento assíncrono — consistência de dados em leitura concorrente.",
                        "when_use": "Buffer compartilhado entre OB1 e OB35, cópia de trending para IHM durante scan, dados de segurança em transição.",
                        "syntax": "Mesmos parâmetros de MOVE_BLK/FILL_BLK. Maior tempo de bloqueio de CPU — usar apenas quando necessário.",
                        "lad": """[INSERIR IMAGEM DO ÍCONE DA FUNÇÃO UMOVE_BLK AQUI]

                  +------------+
   Snapshot       | UMOVE_BLK  |
------| |--------|EN          ENO|
"Live_Data"-------|            |
"Snap_Data"-------|            |
      100 ---------| COUNT      |
                  +------------+""",
                        "stl": """CALL  "UMOVE_BLK_Snap"
   SRC_ARRAY := "Live_Data"
   DST_ARRAY := "Snap_Data"
   COUNT     := 100
""",
                    },
                    {
                        "name": "SCATTER / GATHER — Bit Sequence Pack/Unpack",
                        "objective": "SCATTER: decompõe sequência de bits de IN em array de BOOL. GATHER: compacta array de BOOL em word/dword de saída.",
                        "when_use": "Interface com word Modbus de status, conversão de 16 alarmes em word para HMI, packing de DI em DWORD para transmissão.",
                        "syntax": "SCATTER: IN (bit sequence), OUT (array of BOOL), COUNT. GATHER: inverso.",
                        "lad": """[INSERIR IMAGEM DO ÍCONE DA FUNÇÃO SCATTER AQUI]

                  +-----------+
"Alarm".Word------|  SCATTER  |
"Alarm".Bits[]---|           |
      16 ----------| COUNT     |
                  +-----------+""",
                        "stl": """CALL  "SCATTER_Alarms"
   IN    := "Alarm".Word
   OUT   := "Alarm".Bits
   COUNT := 16
""",
                    },
                ],
            },
            {
                "title": "6.4 Variant e Limites de Array (VariantGet, LOWER_BOUND, UPPER_BOUND)",
                "instructions": [
                    {
                        "name": "VariantGet / VariantPut",
                        "objective": "VariantGet: lê valor apontado por VARIANT para tag tipada. VariantPut: escreve valor em destino VARIANT.",
                        "when_use": "FC genérico de cópia, logging polimórfico, receita com campos de tipos variados.",
                        "syntax": "VARIANT: ponteiro genérico. VALUE: tag com tipo concreto. ENO=FALSE se tipo incompatível.",
                        "lad": """[INSERIR IMAGEM DO ÍCONE DA FUNÇÃO VariantGet AQUI]

                  +------------+
"Src".Variant-----| VariantGet |
"Dst".Real--------|            |
                  +------------+""",
                        "stl": """CALL  "VariantGet_Real"
   VARIANT := "Src".Variant
   VALUE   := "Dst".Real
""",
                    },
                    {
                        "name": "LOWER_BOUND / UPPER_BOUND / CountOfElements",
                        "objective": "Retornam índice inferior, superior e quantidade de elementos de ARRAY[*] dinâmico ou VARIANT array.",
                        "when_use": "Loop FOR com limite dinâmico, validação de bounds antes de acesso, UDFC para processamento de buffer de tamanho variável.",
                        "syntax": "ARR: ARRAY[*] ou VARIANT. OUT: DINT. ENO=FALSE se não for array.",
                        "lad": """[INSERIR IMAGEM DO ÍCONE DA FUNÇÃO LOWER_BOUND AQUI]

                  +--------------+
"Buf".Array[]-----| LOWER_BOUND  |-- "Loop".Idx_Min
                  +--------------+

                  +--------------+
"Buf".Array[]-----| UPPER_BOUND  |-- "Loop".Idx_Max
                  +--------------+""",
                        "stl": """CALL  "LOWER_BOUND_Buf"
   ARR := "Buf".Array
   OUT := "Loop".Idx_Min

CALL  "UPPER_BOUND_Buf"
   ARR := "Buf".Array
   OUT := "Loop".Idx_Max
""",
                    },
                ],
            },
        ],
    },
    {
        "title": "CAPÍTULO 8 (continuação): Program Control",
        "sections": [
            {
                "title": "8.3 Lista de Saltos (JMP_LIST) e Diagnóstico Local (GET_ERROR)",
                "instructions": [
                    {
                        "name": "JMP_LIST — Define Jump List",
                        "objective": "Define lista de destinos LABEL para distribuição de salto por índice K. Alternativa estruturada ao SWTCH em projetos grandes.",
                        "when_use": "Sequenciador com >8 ramos, tabela de saltos documentada, máquina de estados tabular.",
                        "syntax": "K: INT índice. Lista de pares (valor, LABEL).",
                        "lad": """[INSERIR IMAGEM DO ÍCONE DA FUNÇÃO JMP_LIST AQUI]

                  +----------+
"State".Idx-------| JMP_LIST |
                  | K        |
                  | 1: St_10  |
                  | 2: St_20  |
                  | 3: St_30  |
                  +----------+""",
                        "stl": """L     "State".Idx
JMP_LIST
1  St_10
2  St_20
3  St_30
""",
                    },
                    {
                        "name": "GET_ERROR / GET_ERR_ID — Local Error Capture",
                        "objective": "Captura erro local (último ENO=FALSE em bloco) sem depender de OB80/OB82. GET_ERR_ID retorna código numérico do erro.",
                        "when_use": "Diagnóstico em FC de comunicação, log de falha de CONVERT/MOVE sem parar CPU, IHM de manutenção com último erro.",
                        "syntax": "REQ: BOOL trigger. ERR_STRUCT: UDT de erro. DONE/ERROR: status.",
                        "lad": """[INSERIR IMAGEM DO ÍCONE DA FUNÇÃO GET_ERROR AQUI]

   Diag_Req
------| |--------+-----------+
                  | GET_ERROR |
                  |           |
"Diag".ErrStruct--| ERR       |
                  +-----------+""",
                        "stl": """A     "Diag_Req"
CALL  "GET_ERROR"
   REQ        := TRUE
   ERR_STRUCT := "Diag".ErrStruct
""",
                    },
                ],
            },
            {
                "title": "8.4 Controle de Execução (STP, ENDIS_PW)",
                "instructions": [
                    {
                        "name": "STP — Exit Program",
                        "objective": "Transiciona CPU para STOP mode a partir do programa. Irreversível sem intervenção externa (online, cartão, PG).",
                        "when_use": "Condição de catástrofe com dano mecânico iminente, teste de falha controlado em bancada — nunca em produção sem análise de risco.",
                        "syntax": "Chamada incondicional ou condicionada. Sem parâmetros.",
                        "lad": """[INSERIR IMAGEM DO ÍCONE DA FUNÇÃO STP AQUI]

   Catastrophic
------| |--------------------+-----+
                               | STP |
                               +-----+""",
                        "stl": """A     "Catastrophic"
CALL  STP
""",
                    },
                    {
                        "name": "ENDIS_PW — Limit and Enable Password Legitimation",
                        "objective": "Habilita/desabilita proteção por senha de níveis de acesso. LIMIT restringe tentativas; ENABLE ativa legitimação.",
                        "when_use": "Comissionamento: desabilitar proteção temporariamente; produção: reabilitar. Documentar em procedimento BLBW de entrega.",
                        "syntax": "REQ, PASSWORD (conforme versão). Consultar manual de proteção CPU.",
                        "lad": """[INSERIR IMAGEM DO ÍCONE DA FUNÇÃO ENDIS_PW AQUI]

   Comm_Enable
------| |--------------------+--------+
                               |ENDIS_PW|
                               +--------+""",
                        "stl": """// Procedimento sensível — executar apenas em startup controlado
CALL  "ENDIS_PW_Enable"
   REQ := "Comm_Enable"
""",
                    },
                ],
            },
        ],
    },
    {
        "title": "APÊNDICE A: Arquitetura de Execução e Ciclo de Scan",
        "sections": [
            {
                "title": "A.1 Hierarquia de OBs e Prioridade de Saídas",
                "instructions": [
                    {
                        "name": "Modelo de Prioridade OB — Referência BLBW",
                        "objective": "OB1 (cyclic) executa após eventos de maior prioridade. OB35/OB30 (cyclic interrupts) preemptam OB1. OBs de erro (OB80-OB87) e startup (OB100) têm prioridade definida por classe.",
                        "when_use": "Dimensionamento de scan time, decisão de alocar PID em OB30 vs OB1, diagnóstico de jitter em contagem de alta velocidade.",
                        "syntax": "N/A — conceito arquitetural. Saídas escritas em OB de maior prioridade sobrescrevem OB1 no mesmo ciclo até próxima atualização.",
                        "lad": """// Estrutura recomendada BLBW:
// OB100  — Startup, inicialização DB, RE_TRIGR
// OB35   — PID, contagem rápida, filtros
// OB1    — Sequência, lógica, comunicação
// OB82   — Diagnóstico de módulo (template BLBW_Diag)""",
                        "stl": """// OB35 — exemplo de prioridade sobre OB1
ORGANIZATION_BLOCK OB35
BEGIN
    CALL  "FC_PID_Fast"
    CALL  "FC_Counter_HSC"
END_ORGANIZATION_BLOCK
""",
                    },
                ],
            },
            {
                "title": "A.2 Process Image vs Acesso Direto",
                "instructions": [
                    {
                        "name": "%I / %Q / PEEK / POKE — Acesso a Periféricos",
                        "objective": "Process Image: entrada lida no início do ciclo, saída escrita no fim — consistente mas com 1 ciclo de latência. Acesso directo (%I, %Q ou PEEK/POKE): imediato, risco de inconsistência intra-scan.",
                        "when_use": "PEEK/POKE: diagnóstico, leitura pontual fora do image. %I/%Q: otimização S7-1500. Não misturar image e direct no mesmo bit sem documentar.",
                        "syntax": "%I0.0, %Q0.0 — sintaxe absoluta. PEEK/POKE: área, DB, offset, bit.",
                        "lad": """// Leitura otimizada S7-1500
   %I10.0
------| |---------------------( ) %Q10.0""",
                        "stl": """A     %I10.0
=     %Q10.0

// PEEK — leitura imediata de entrada
L     PEEK_BOOL
    AREA := 16#82    // Inputs
    DBNO := 0
    BYTE := 10
    BIT  := 0
T     "Diag".In_Immediate
""",
                    },
                ],
            },
        ],
    },
    {
        "title": "APÊNDICE B: Referência Rápida LAD ↔ STL",
        "sections": [
            {
                "title": "B.1 Tabela de Equivalência de Instruções",
                "instructions": [
                    {
                        "name": "Equivalência LAD ↔ STL — Principais Instruções",
                        "objective": "Tabela de referência cruzada para conversão manual entre LAD e STL em manutenção de campo sem TIA Portal disponível.",
                        "when_use": "Análise de print de programa em papel, suporte remoto, auditoria de código legado S7-300.",
                        "syntax": "Ver tabela abaixo nos exemplos LAD/STL.",
                        "lad": """| LAD Elemento    | STL        | Observação                    |
|-----------------|------------|-------------------------------|
| | |  (NA)         | A          | AND com RLO anterior          |
| |/| (NF)         | AN         | AND NOT                       |
| NOT |           | NOT        | Inverte RLO                   |
| ( )             | =          | Atribuição                    |
| (S)             | S          | Set                           |
| (R)             | R          | Reset                         |
| |P|             | FP Mem     | Borda subida                  |
| |N|             | FN Mem     | Borda descida                 |
| CMP >=          | >=I >=D >=R| Sufixo por tipo               |
| TON box         | CALL TON   | DB instância obrigatório      |""",
                        "stl": """// Exemplo de conversão rede LAD → STL
// LAD: |Emerg|--+--( ) Run
//      |Start|--+
A     "Emerg"
A     "Start"
=     "Run"
""",
                    },
                ],
            },
            {
                "title": "B.2 Convenções de Nomenclatura BLBW",
                "instructions": [
                    {
                        "name": "Padrão de Tags BLBW — SanBox / Industrial",
                        "objective": "Convenção corporativa BLBW para nomenclatura de tags, garantindo legibilidade entre projetos SanBox, painéis e estações de bombeamento.",
                        "when_use": "Todo novo projeto BLBW. Migração de código legado deve mapear tags antigas para padrão na primeira intervenção.",
                        "syntax": "Estrutura: [Área]_[Equipamento]_[Função]_[Modificador]. Ex: PU_01_Run_Cmd, TK_02_Level_PV, AL_Flow_HiHi.",
                        "lad": """// Exemplos de tags BLBW em rede LAD:
   PU_01_Run_FB
------| |------+-----( ) PU_01_Run_Cmd
               |
   PU_01_Fault
------|/|------+

   TK_02_Level_LL
------| |---------------------(S) AL_TK02_Level_LL""",
                        "stl": """// Prefixos BLBW padrão:
// PU = Bomba (Pump)    TK = Tanque (Tank)
// XV = Válvula ON/OFF  CV = Controle (válvula modulante)
// AL = Alarme          AI/AO = Analógico
// FB = Feedback campo  Cmd = Comando

A     "PU_01_Run_FB"
AN    "PU_01_Fault"
=     "PU_01_Run_Cmd"
""",
                    },
                ],
            },
        ],
    },
]

# Instruções adicionais para seções existentes (inseridas via merge)
SECTION_ADDITIONS = {
    "1.2 Memorização de Estado e Flip-Flops (SR / RS)": [
        {
            "name": "SR — Set Dominant Flip-Flop",
            "objective": "Variante com prioridade Set: se S1 e R simultâneos, Q = 1. Utilizar apenas quando partida/comando ON deve prevalecer sobre parada em conflito de sinais.",
            "when_use": "Modo automático forçado por supervisório, partida prioritária em processo contínuo onde parada momentânea de R é aceitável ser ignorada — raro; documentar FMEA.",
            "syntax": "S1 (BOOL): Set. R (BOOL): Reset. Q (BOOL): Saída. Bloco SR em paleta Bit logic.",
            "lad": """[INSERIR IMAGEM DO ÍCONE DA FUNÇÃO SR AQUI]

                  +-------+
   Auto_Force     |  SR   |
------| |--------|S1    Q|-----------------( ) Process_On
                  |       |
   Oper_Stop      |       |
------| |--------|R      |
                  +-------+""",
            "stl": """CALL  "SR_Process", "DB_SR_Process"
   S1 := "Auto_Force"
   R  := "Oper_Stop"
   Q  := "Process_On"
""",
        },
    ],
    "4.1 Operações Matemáticas Relacionais (==, <>, >=, <=, >, <)": [
        {
            "name": "CMP == (Equal) e CMP <> (Not Equal)",
            "objective": "Igualdade (==) ou diferença (<>) exata entre operandos. Cuidado com REAL: comparar com tolerância via IN_Range em vez de == direto.",
            "when_use": "Verificação de código de receita, estado discreto numérico, comparação de posição em passo fixo.",
            "syntax": "IN1, IN2: tipos homogêneos. Para REAL use ABS(IN1-IN2) < Epsilon via CALCULATE.",
            "lad": """[INSERIR IMAGEM DO ÍCONE DA FUNÇÃO CMP == AQUI]

                  +----------+
"Recipe".Code-----|          |
                  |  CMP ==  |---------------------( ) Recipe_Match
      1001 --------|          |
                  +----------+""",
            "stl": """L     "Recipe".Code
==I   1001
=     "Recipe_Match"
""",
        },
    ],
    "5.1 Cálculos Aritméticos Básicos (ADD, SUB, MUL, DIV)": [
        {
            "name": "DIV — Divide (com monitoramento ENO)",
            "objective": "Divisão com detecção de divisor zero. ENO=FALSE interrompe cadeia EN/ENO — downstream não executa.",
            "when_use": "Cálculo de média, razão de vazões, conversão de unidade. Sempre inserir ramo de fallback quando ENO=FALSE.",
            "syntax": "IN1/IN2/OUT. Tipos REAL recomendados para analógicos. INT division trunca — usar REAL.",
            "lad": """[INSERIR IMAGEM DO ÍCONE DA FUNÇÃO DIV AQUI]

                  +---------+
   Calc_En        |   DIV   |
------| |--------|EN      ENO|----+-----( ) Div_OK
"Flow".Total------|         |    |
"Flow".Hours------|IN1     OUT|---|-- "Flow".Avg
                  |IN2      |    |
                  +---------+    |
                               +-----( ) Div_Fault
""",
            "stl": """A     "Calc_En"
CALL  "DIV_AvgFlow"
   IN1 := "Flow".Total
   IN2 := "Flow".Hours
   OUT := "Flow".Avg
   ENO => "Div_OK"
AN    "Div_OK"
=     "Div_Fault"
""",
        },
    ],
    "7.2 Arredondamento e Truncamento (ROUND, CEIL, FLOOR, TRUNC)": [
        {
            "name": "CEIL / FLOOR — Limites Inteiros Superior/Inferior",
            "objective": "CEIL: menor inteiro >= IN. FLOOR: maior inteiro <= IN. Diferem de ROUND e TRUNC em valores negativos e .5 exatos.",
            "when_use": "Dimensionamento de lotes (CEIL para garantir cobertura), cálculo de capacidade mínima de recipientes.",
            "syntax": "IN: REAL/LREAL. OUT: INT/DINT.",
            "lad": """[INSERIR IMAGEM DO ÍCONE DA FUNÇÃO CEIL AQUI]

                  +---------+
"Batches".Real----|  CEIL   |-- "Batches".Count
                  +---------+""",
            "stl": """CALL  "CEIL_Batches"
   IN  := "Batches".Real
   OUT := "Batches".Count
""",
        },
    ],
    "9.1 Mascaramento a Nível de Palavra (AND, OR, XOR)": [
        {
            "name": "INVERT — Ones Complement (Word)",
            "objective": "Inverte todos os bits da palavra (complemento de um). OUT = NOT(IN) bit a bit.",
            "when_use": "Geração de máscara invertida, protocolo serial, teste de redundância XOR.",
            "syntax": "IN/OUT: WORD/DWORD.",
            "lad": """[INSERIR IMAGEM DO ÍCONE DA FUNÇÃO INVERT AQUI]

                  +---------+
"Mask".Template---| INVERT  |-- "Mask".Inverted
                  +---------+""",
            "stl": """L     "Mask".Template
INV_I
T     "Mask".Inverted
""",
        },
    ],
    "10.1 Deslocamento de Bits (SHR, SHL)": [
        {
            "name": "SHL — Shift Left",
            "objective": "Deslocamento à esquerda N posições. Bits altos perdem. Equivalente a multiplicação por 2^N para valores sem sinal.",
            "when_use": "Multiplicação rápida por potência de 2, montagem de word a partir de nibbles, endereçamento em word de comando.",
            "syntax": "IN (WORD/DWORD), N (INT), OUT.",
            "lad": """[INSERIR IMAGEM DO ÍCONE DA FUNÇÃO SHL AQUI]

                  +---------+
"Val".Word--------|   SHL   |-- "Val".X2
       1 ------------| N       |
                  +---------+""",
            "stl": """CALL  "SHL_Val"
   IN  := "Val".Word
   N   := 1
   OUT := "Val".X2
""",
        },
    ],
}
