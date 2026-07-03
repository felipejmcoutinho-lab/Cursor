# -*- coding: utf-8 -*-
"""Conteúdo técnico do Manual TIA Portal - BLBW."""

MANUAL_META = {
    "title": "MANUAL TÉCNICO AVANÇADO DE INSTRUÇÕES E LÓGICA DE CONTROLE",
    "subtitle": "Referência Rápida e Aplicações Práticas - Siemens TIA Portal / Step 7 (LAD/STL)",
    "version": "Corporativa 1.0",
    "audience": "Engenharia de Automação e Manutenção Industrial (Nível Especialista)",
    "platform": "CLP Siemens (S7-1200, S7-1500, S7-300/400)",
    "company": "BLBW - Be Life, Be Water",
    "classification": "Documento Técnico Interno - Uso Restrito",
}

INDEX = [
    ("CAPÍTULO 1: Bit Logic Operations", [
        "1.1 Contatos de Alta Performance e Bobinas de Atribuição",
        "1.2 Memorização de Estado e Flip-Flops (SR / RS)",
        "1.3 Operações de Detecção de Borda (P_TRIG / N_TRIG / R_TRIG / F_TRIG)",
    ]),
    ("CAPÍTULO 2: Timer Operations (IEC Timers)", [
        "2.1 TON (Timer On-Delay)",
        "2.2 TOF (Timer Off-Delay)",
        "2.3 TP (Timer Pulse)",
        "2.4 TONR (Time Accumulator)",
    ]),
    ("CAPÍTULO 3: Counter Operations (IEC Counters)", [
        "3.1 CTU (Count Up)",
        "3.2 CTD (Count Down)",
        "3.3 CTUD (Count Up/Down)",
    ]),
    ("CAPÍTULO 4: Comparator Operations", [
        "4.1 Operações Matemáticas Relacionais (==, <>, >=, <=, >, <)",
        "4.2 Checagem de Limites (IN_Range / OUT_Range)",
    ]),
    ("CAPÍTULO 5: Math Functions", [
        "5.1 Cálculos Aritméticos Básicos (ADD, SUB, MUL, DIV)",
        "5.2 Seleção de Extremos e Limitação (MIN, MAX, LIMIT)",
        "5.3 Funções Trigonométricas e Exponenciais Avançadas",
    ]),
    ("CAPÍTULO 6: Move Operations", [
        "6.1 Transferência de Bloco Escalar (MOVE)",
        "6.2 Manipulação em Lote e Serialização (MOVE_BLK, FILL_BLK, SWAP)",
    ]),
    ("CAPÍTULO 7: Conversion Operations", [
        "7.1 Conversão Explícita de Cast (CONVERT)",
        "7.2 Arredondamento e Truncamento (ROUND, CEIL, FLOOR, TRUNC)",
        "7.3 Escalonamento de Sinais Analógicos (SCALE_X, NORM_X)",
    ]),
    ("CAPÍTULO 8: Program Control Operations", [
        "8.1 Saltos e Roteamento Lógico (JMP, JMPN, LABEL, SWTCH)",
        "8.2 Finalização de Bloco (RET)",
    ]),
    ("CAPÍTULO 9: Word Logic Operations", [
        "9.1 Mascaramento a Nível de Palavra (AND, OR, XOR)",
        "9.2 Manipulação Estrutural (ENCO, DECO, SEL, MUX, DEMUX)",
    ]),
    ("CAPÍTULO 10: Shift and Rotate Operations", [
        "10.1 Deslocamento de Bits (SHR, SHL)",
        "10.2 Rotação de Registradores (ROR, ROL)",
    ]),
]

# Each section: title, instructions list
# Each instruction: name, objective, when_use, syntax, lad, stl, icon_placeholder

CHAPTERS = [
    {
        "title": "CAPÍTULO 1: Bit Logic Operations",
        "sections": [
            {
                "title": "1.1 Contatos de Alta Performance e Bobinas de Atribuição",
                "instructions": [
                    {
                        "name": "Contato Normalmente Aberto (NA) — | |",
                        "objective": "Elemento de entrada que conduz corrente lógica (RLO = 1) quando o operando associado está em estado TRUE. Base de toda lógica combinacional em LAD.",
                        "when_use": "Leitura de sensores digitais (proximidade, pressostato, botoeira), habilitação de cadeias lógicas e condicionamento de blocos IEC. Em S7-1500, prefira tags otimizadas (%I, %Q) para acesso direto sem overhead de DB.",
                        "syntax": "Operando (BOOL): Tag de entrada, memória M, bit de DB ou entrada física %I. O contato avalia o estado binário no início do ciclo de scan (process image input). Não possui pinos EN/ENO — é elemento de contato puro.",
                        "lad": """[INSERIR IMAGEM DO ÍCONE DA FUNÇÃO Contato NA AQUI]

   Sens_Partida
------| |------+-----( ) Cmd_Motor
               |
   Emerg_OK
------| |------+""",
                        "stl": """// Contato NA: instrução A (AND) / O (OR) conforme posição na rede
A     "Sens_Partida"
A     "Emerg_OK"
=     "Cmd_Motor"
""",
                    },
                    {
                        "name": "Contato Normalmente Fechado (NF) — |/|",
                        "objective": "Elemento de entrada que conduz quando o operando está em FALSE. Inversão lógica de sinal de campo ou condição de segurança.",
                        "when_use": "Intertravamentos de parada de emergência (NF em série), detecção de falta de sinal, lógica de alarme por perda de comunicação. Em STL, equivalente a AN (AND NOT).",
                        "syntax": "Operando (BOOL): Mesmas regras do contato NA. A avaliação ocorre no ciclo atual; não há debounce nativo — implemente TON externo se necessário.",
                        "lad": """[INSERIR IMAGEM DO ÍCONE DA FUNÇÃO Contato NF AQUI]

   Emerg_NC
------|/|------+-----( ) Linha_Habilitada
               |
   Porta_Fech
------| |------+""",
                        "stl": """AN    "Emerg_NC"      // AND NOT — contato NF
A     "Porta_Fech"
=     "Linha_Habilitada"
""",
                    },
                    {
                        "name": "Bobina de Atribuição — ( )",
                        "objective": "Escreve o RLO atual no operando de saída a cada ciclo de scan. Comportamento volátil: se a condição de entrada cair, a saída retorna a FALSE imediatamente.",
                        "when_use": "Comandos momentâneos, sinalização de estados transitórios, saídas que devem espelhar condição lógica sem memorização. Não utilizar para partida de motor sem intertravamento SR/RS.",
                        "syntax": "Operando (BOOL): Saída %Q, memória M ou bit de DB. Em S7-1200/1500, bobinas em OBs de alta prioridade podem sobrepor saídas de OB1 — respeite hierarquia de OBs.",
                        "lad": """[INSERIR IMAGEM DO ÍCONE DA FUNÇÃO Bobina AQUI]

   Condicao_OK
------| |---------------------( ) Lamp_Ready
""",
                        "stl": """A     "Condicao_OK"
=     "Lamp_Ready"
""",
                    },
                    {
                        "name": "Set (S) e Reset (R) — Bobinas de Memorização",
                        "objective": "Instruções de coil que alteram o estado do operando para TRUE (S) ou FALSE (R) quando o RLO = 1, mantendo o estado entre ciclos. Ordem de varredura define prioridade em conflito.",
                        "when_use": "Sequências simples, alarmes latched, reset de falhas. Em STL clássico S7-300/400, S e R na mesma rede: o último processado vence. Para prioridade explícita, use blocos RS/SR.",
                        "syntax": "Operando (BOOL): Bit a memorizar. S: set dominante se escrito por último. R: reset dominante se escrito por último. Não usar S/R no mesmo operando em redes paralelas sem análise de prioridade.",
                        "lad": """[INSERIR IMAGEM DO ÍCONE DA FUNÇÃO Set/Reset AQUI]

   Btn_Start
------| |---------------------(S) Motor_Run

   Btn_Stop
------| |---------------------(R) Motor_Run
""",
                        "stl": """// Reset dominante: R após S
A     "Btn_Start"
S     "Motor_Run"
A     "Btn_Stop"
R     "Motor_Run"
""",
                    },
                ],
            },
            {
                "title": "1.2 Memorização de Estado e Flip-Flops (SR / RS)",
                "instructions": [
                    {
                        "name": "SR (Set Dominant) e RS (Reset Dominant)",
                        "objective": "Blocos de flip-flop para memorização de estado lógico. SR prioriza Set quando S1 e R estão simultaneamente TRUE (Q = 1). RS prioriza Reset (Q = 0). Garantem comportamento determinístico em comando concorrente.",
                        "when_use": "Partida/parada de motores, válvulas ON/OFF, intertravamentos de processo. RS obrigatório quando parada de emergência ou condição de segurança não pode ser sobreposta por partida. SR apenas quando Set deve prevalecer em conflito (ex.: modo automático forçado).",
                        "syntax": "S1/S (BOOL): Condição de Set. R/R1 (BOOL): Condição de Reset. Q (BOOL): Estado memorizado. Instanciar como multi-instância em FB ou DB dedicado tipo SR/RS.",
                        "lad": """[INSERIR IMAGEM DO ÍCONE DA FUNÇÃO RS AQUI]

                  +-------+
   Btn_Start     |  RS   |
------| |--------|S     Q|-----------------( ) Blower_Cmd
                  |       |
   Press_High    |       |
------| |--------|R1     |
                  +-------+""",
                        "stl": """// Reset dominante via ordem STL
A     "Btn_Start"
S     "Blower_Cmd"
A     "Press_High"
R     "Blower_Cmd"

// Ou via CALL do bloco IEC
CALL  "RS_Blower", "DB_RS_Blower"
   SET := "Btn_Start"
   RESET1 := "Press_High"
   Q := "Blower_Cmd"
""",
                    },
                ],
            },
            {
                "title": "1.3 Operações de Detecção de Borda (P_TRIG / N_TRIG / R_TRIG / F_TRIG)",
                "instructions": [
                    {
                        "name": "P_TRIG (Positive Trigger) / FP em STL",
                        "objective": "Emite pulso TRUE por exatamente 1 ciclo de scan na transição 0→1 do sinal monitorado. R_TRIG é variante em bloco com saída Q e entrada CLK.",
                        "when_use": "Disparo único de requisições (REQ em GET/PUT), incremento de contadores de evento, registro de alarmes sem repetição cíclica, handshake de comunicação Profinet.",
                        "syntax": "CLK (BOOL): Sinal monitorado. M_BIT (BOOL): Memória de borda — exclusiva, estática em FB. Q (BOOL): Pulso de 1 scan. Em STL: FP \"Edge_Mem\" após A do sinal.",
                        "lad": """[INSERIR IMAGEM DO ÍCONE DA FUNÇÃO P_TRIG AQUI]

   Inv_Fault                    +--------+
------| |-----------------------| P_TRIG |---------------------( ) Log_Trigger
                               |        |
"Inst_DB".Edge_Mem_InvFault----| M_BIT  |
                               +--------+""",
                        "stl": """A     "Inv_Fault"
FP    "Inst_DB".Edge_Mem_InvFault
=     "Log_Trigger"
""",
                    },
                    {
                        "name": "N_TRIG (Negative Trigger) / FN em STL",
                        "objective": "Pulso de 1 ciclo na transição 1→0. F_TRIG é equivalente em bloco.",
                        "when_use": "Detecção de fim de ciclo, liberação de intertravamento após retorno de sensor, contagem de peças na saída da zona de detecção.",
                        "syntax": "Mesmos parâmetros do P_TRIG. FN em STL requer memória de borda dedicada.",
                        "lad": """[INSERIR IMAGEM DO ÍCONE DA FUNÇÃO N_TRIG AQUI]

   Sens_Peca                    +--------+
------| |-----------------------| N_TRIG |---------------------( ) Peca_Saida
                               |        |
"DB_Prod".Edge_Mem_Sens--------| M_BIT  |
                               +--------+""",
                        "stl": """A     "Sens_Peca"
FN    "DB_Prod".Edge_Mem_Sens
=     "Peca_Saida"
""",
                    },
                    {
                        "name": "R_TRIG / F_TRIG (Blocos IEC)",
                        "objective": "Blocos encapsulados de detecção de borda positiva (R_TRIG) e negativa (F_TRIG) com interface padronizada EN/CLK/Q.",
                        "when_use": "FBs reutilizáveis, bibliotecas corporativas BLBW, padronização de código em equipes multidisciplinares.",
                        "syntax": "CLK (BOOL): Entrada. Q (BOOL): Saída pulsada. Memória interna no DB de instância — não expor M_BIT externamente.",
                        "lad": """[INSERIR IMAGEM DO ÍCONE DA FUNÇÃO R_TRIG AQUI]

                  +---------+
   Start_Pulse    | R_TRIG  |
------| |--------|CLK     Q|-----------------( ) Step_Advance
                  +---------+""",
                        "stl": """CALL  "R_TRIG_Step", "DB_R_TRIG_Step"
   CLK := "Start_Pulse"
   Q   := "Step_Advance"
""",
                    },
                ],
            },
        ],
    },
    {
        "title": "CAPÍTULO 2: Timer Operations (IEC Timers)",
        "sections": [
            {
                "title": "2.1 TON (Timer On-Delay)",
                "instructions": [
                    {
                        "name": "TON — Generate On-Delay",
                        "objective": "Temporizador IEC com retardo na ativação. Q = TRUE somente após IN permanecer TRUE durante PT. Perda de IN zera ET e Q imediatamente.",
                        "when_use": "Debounce de sensores, sequenciamento de partidas escalonadas, retardo pós-rearme de emergência, confirmação de presença de peça.",
                        "syntax": "IN (BOOL): Habilitação. PT (TIME): Preset T#250ms, T#5s, etc. Q (BOOL): Saída temporizada. ET (TIME): Tempo decorrido. DB: IEC_TIMER ou instância em FB.",
                        "lad": """[INSERIR IMAGEM DO ÍCONE DA FUNÇÃO TON AQUI]

                  +---------+
   Sens_Part      |   TON   |
------| |--------|IN      Q|-----------------( ) Part_Confirmed
                  |         |
  T#250ms --------|PT     ET|- "DB_Prod".Part_ET
                  +---------+""",
                        "stl": """CALL  "TON_Part_Instance"
   IN := "Sens_Part"
   PT := T#250MS
   Q  := "Part_Confirmed"
   ET := "DB_Prod".Part_ET
""",
                    },
                ],
            },
            {
                "title": "2.2 TOF (Timer Off-Delay)",
                "instructions": [
                    {
                        "name": "TOF — Generate Off-Delay",
                        "objective": "Q assume TRUE instantaneamente com IN = TRUE. Ao cair IN, inicia contagem de PT antes de Q = FALSE. Retorno de IN durante contagem cancela e reinicia.",
                        "when_use": "Ventilação pós-processo, lubrificação residual, extração de fumos após solda, despressurização com dreno temporizado.",
                        "syntax": "IN, PT, Q, ET — idênticos ao TON. Tipo de timer: IEC_TIMER.",
                        "lad": """[INSERIR IMAGEM DO ÍCONE DA FUNÇÃO TOF AQUI]

                  +---------+
   Weld_Arc       |   TOF   |
------| |--------|IN      Q|-----------------( ) Exhaust_Cmd
                  |         |
  T#30s ----------|PT     ET|- "DB_Maint".Exhaust_ET
                  +---------+""",
                        "stl": """CALL  "TOF_Exhaust_Instance"
   IN := "Weld_Arc"
   PT := T#30S
   Q  := "Exhaust_Cmd"
   ET := "DB_Maint".Exhaust_ET
""",
                    },
                ],
            },
            {
                "title": "2.3 TP (Timer Pulse)",
                "instructions": [
                    {
                        "name": "TP — Generate Pulse",
                        "objective": "Gera pulso de duração fixa PT na borda de subida de IN. Q permanece TRUE por PT independente do estado de IN após disparo. Nova borda só é aceita após término do pulso.",
                        "when_use": "Impulso de válvula proporcional, blink de alarme, pulso de reset remoto, temporização de acionamento de relé monostável.",
                        "syntax": "IN (BOOL): Flanco de disparo. PT (TIME): Duração do pulso. Q (BOOL): Saída pulsada. ET: tempo restante do pulso.",
                        "lad": """[INSERIR IMAGEM DO ÍCONE DA FUNÇÃO TP AQUI]

                  +---------+
   Cmd_Pulse      |   TP    |
------| |--------|IN      Q|-----------------( ) Valve_Pulse
                  |         |
  T#2s -----------|PT     ET|- "DB_Valve".Pulse_ET
                  +---------+""",
                        "stl": """CALL  "TP_Valve_Instance"
   IN := "Cmd_Pulse"
   PT := T#2S
   Q  := "Valve_Pulse"
   ET := "DB_Valve".Pulse_ET
""",
                    },
                ],
            },
            {
                "title": "2.4 TONR (Time Accumulator)",
                "instructions": [
                    {
                        "name": "TONR — Time Accumulator",
                        "objective": "Acumula tempo de IN = TRUE entre ciclos. R (BOOL) zera ET e Q. Diferente do TON, perda momentânea de IN preserva tempo acumulado.",
                        "when_use": "Horímetro de equipamento, manutenção preventiva por tempo de operação, controle de tempo máximo de ciclo acumulado, billing de tempo de bomba.",
                        "syntax": "IN (BOOL): Contagem ativa. PT (TIME): Tempo alvo acumulado. R (BOOL): Reset. Q (BOOL): TRUE quando ET >= PT. ET (TIME): Tempo total acumulado.",
                        "lad": """[INSERIR IMAGEM DO ÍCONE DA FUNÇÃO TONR AQUI]

                  +---------+
   Pump_Run       |  TONR   |
------| |--------|IN      Q|-----------------( ) Maint_Due
                  |         |
  T#500h ---------|PT     ET|- "DB_Maint".Pump_Hours
                  |         |
   Reset_Hours    |       R |
------| |--------|         |
                  +---------+""",
                        "stl": """CALL  "TONR_Pump_Hours"
   IN := "Pump_Run"
   PT := T#500H
   R  := "Reset_Hours"
   Q  := "Maint_Due"
   ET := "DB_Maint".Pump_Hours
""",
                    },
                ],
            },
        ],
    },
    {
        "title": "CAPÍTULO 3: Counter Operations (IEC Counters)",
        "sections": [
            {
                "title": "3.1 CTU (Count Up)",
                "instructions": [
                    {
                        "name": "CTU — Count Up",
                        "objective": "Contador incremental IEC. Incrementa CV em borda de subida de CU quando R = FALSE. Q = TRUE quando CV >= PV.",
                        "when_use": "Contagem de peças produzidas, batching, limite de ciclos para manutenção, controle de paletização.",
                        "syntax": "CU (BOOL): Count Up — borda de subida. R (BOOL): Reset CV para 0. PV (INT/DINT): Preset. CV (INT/DINT): Valor atual. Q (BOOL): CV >= PV.",
                        "lad": """[INSERIR IMAGEM DO ÍCONE DA FUNÇÃO CTU AQUI]

                  +---------+
   Sens_Peca      |   CTU   |
------|P|--------|CU      Q|-----------------( ) Batch_Complete
                  |         |
   Reset_Batch    |       R |
------| |--------|         |
       100 -------|PV     CV|- "DB_Prod".Batch_Count
                  +---------+""",
                        "stl": """CALL  "CTU_Batch"
   CU := "Sens_Peca"
   R  := "Reset_Batch"
   PV := 100
   Q  := "Batch_Complete"
   CV := "DB_Prod".Batch_Count
""",
                    },
                ],
            },
            {
                "title": "3.2 CTD (Count Down)",
                "instructions": [
                    {
                        "name": "CTD — Count Down",
                        "objective": "Contador decremental. CD em borda de subida decrementa CV. LD carrega PV em CV. Q = TRUE quando CV <= 0.",
                        "when_use": "Contagem regressiva de etapas, dispensação de N doses, sequenciador com número fixo de passos restantes.",
                        "syntax": "CD (BOOL): Count Down. LD (BOOL): Load — carrega PV em CV. PV, CV, Q conforme CTU. Q ativo em CV = 0.",
                        "lad": """[INSERIR IMAGEM DO ÍCONE DA FUNÇÃO CTD AQUI]

                  +---------+
   Step_Done      |   CTD   |
------|P|--------|CD      Q|-----------------( ) Seq_End
                  |         |
   Load_Steps     |      LD |
------| |--------|         |
        10 -------|PV     CV|- "DB_Seq".Steps_Left
                  +---------+""",
                        "stl": """CALL  "CTD_Sequence"
   CD := "Step_Done"
   LD := "Load_Steps"
   PV := 10
   Q  := "Seq_End"
   CV := "DB_Seq".Steps_Left
""",
                    },
                ],
            },
            {
                "title": "3.3 CTUD (Count Up/Down)",
                "instructions": [
                    {
                        "name": "CTUD — Count Up/Down",
                        "objective": "Contador bidirecional. CU incrementa, CD decrementa. QU e QD indicam CV >= PV e CV <= 0 respectivamente. R zera CV.",
                        "when_use": "Controle de estoque em silos, posicionamento incremental, filas de buffer com entrada/saída simultânea.",
                        "syntax": "CU, CD, R, LD, PV, CV, QU, QD. Prioridade de CU e CD simultâneos: conforme manual IEC — verificar versão de firmware.",
                        "lad": """[INSERIR IMAGEM DO ÍCONE DA FUNÇÃO CTUD AQUI]

                  +----------+
   Entry_Sens     |  CTUD    |
------|P|--------|CU      QU|--------------( ) Silo_Full
                  |          |
   Exit_Sens      |          |
------|P|--------|CD      QD|--------------( ) Silo_Empty
                  |          |
   Reset_Level    |        R |
------| |--------|          |
      1000 -------|PV      CV|- "DB_Silo".Level
                  +----------+""",
                        "stl": """CALL  "CTUD_Silo_Level"
   CU := "Entry_Sens"
   CD := " Exit_Sens"
   R  := "Reset_Level"
   PV := 1000
   QU := "Silo_Full"
   QD := "Silo_Empty"
   CV := "DB_Silo".Level
""",
                    },
                ],
            },
        ],
    },
    {
        "title": "CAPÍTULO 4: Comparator Operations",
        "sections": [
            {
                "title": "4.1 Operações Matemáticas Relacionais (==, <>, >=, <=, >, <)",
                "instructions": [
                    {
                        "name": "CMP == / CMP <> / CMP >= / CMP <= / CMP > / CMP <",
                        "objective": "Comparação aritmética entre dois operandos do mesmo tipo numérico ou tempo. Resultado BOOL na saída do box ou como condição de contato em LAD.",
                        "when_use": "Setpoint de temperatura, comparação de posição encoder, verificação de receita, intertravamento por faixa de velocidade.",
                        "syntax": "IN1, IN2: Operandos comparáveis (INT, DINT, REAL, TIME). Tipos devem coincidir ou usar CONVERT prévio. Saída BOOL integrada ao RLO em LAD.",
                        "lad": """[INSERIR IMAGEM DO ÍCONE DA FUNÇÃO CMP >= AQUI]

                  +----------+
"AI_Temp".Scaled--|          |
                  |  CMP >=  |---------------------( ) Temp_OK
      75.0 --------|          |
                  +----------+""",
                        "stl": """L     "AI_Temp".Scaled
>=R   75.0
=     "Temp_OK"
""",
                    },
                ],
            },
            {
                "title": "4.2 Checagem de Limites (IN_Range / OUT_Range)",
                "instructions": [
                    {
                        "name": "IN_Range / OUT_Range",
                        "objective": "IN_Range: TRUE se MIN <= IN <= MAX. OUT_Range: TRUE se IN < MIN ou IN > MAX. Simplifica faixas sem dupla comparação.",
                        "when_use": "Validação de sinal analógico dentro de faixa operacional, detecção de sensor quebrado (4-20mA), tolerância de processo em estação SanBox BLBW.",
                        "syntax": "IN (numeric): Valor avaliado. MIN, MAX: Limites inclusivos (IN_Range). Tipos homogêneos REAL recomendado para analógicos.",
                        "lad": """[INSERIR IMAGEM DO ÍCONE DA FUNÇÃO IN_Range AQUI]

                  +-----------+
"AI_Press".Value-|           |
                  | IN_Range  |---------------------( ) Press_Valid
      2.0 ---------|           |
     10.0 ---------|           |
                  +-----------+""",
                        "stl": """CALL  "IN_Range_Press"
   IN  := "AI_Press".Value
   MIN := 2.0
   MAX := 10.0
   OUT := "Press_Valid"
""",
                    },
                ],
            },
        ],
    },
    {
        "title": "CAPÍTULO 5: Math Functions",
        "sections": [
            {
                "title": "5.1 Cálculos Aritméticos Básicos (ADD, SUB, MUL, DIV)",
                "instructions": [
                    {
                        "name": "ADD / SUB / MUL / DIV",
                        "objective": "Operações aritméticas IEC com EN/ENO. DIV com proteção: ENO = FALSE em divisão por zero — sempre monitorar ENO em cálculos críticos.",
                        "when_use": "Cálculo de vazão, balanço massa, offset de setpoint, conversão de unidades em runtime.",
                        "syntax": "EN (BOOL): Habilitação. IN1, IN2: Operandos. OUT: Resultado. ENO (BOOL): Sem erro. Tipos: INT, DINT, REAL — resultado conforme tipo maior.",
                        "lad": """[INSERIR IMAGEM DO ÍCONE DA FUNÇÃO ADD AQUI]

                  +---------+
   Calc_Enable    |   ADD   |
------| |--------|EN      ENO|-----------------( ) Calc_OK
"Flow_A".Value----|         |
"Flow_B".Value----|IN1     OUT|-- "Total_Flow".Value
                  |IN2      |
                  +---------+""",
                        "stl": """A     "Calc_Enable"
CALL  "ADD_Flow"
   IN1 := "Flow_A".Value
   IN2 := "Flow_B".Value
   OUT := "Total_Flow".Value
   ENO => "Calc_OK"
""",
                    },
                ],
            },
            {
                "title": "5.2 Seleção de Extremos e Limitação (MIN, MAX, LIMIT)",
                "instructions": [
                    {
                        "name": "MIN / MAX / LIMIT",
                        "objective": "MIN: menor de IN1/IN2. MAX: maior. LIMIT: restringe IN entre MN e MX (MN se IN<MN, MX se IN>MX, senão IN).",
                        "when_use": "Saturação de comando analógico, seleção de menor pressão entre redundância, clamping de PID output, proteção de atuador.",
                        "syntax": "IN1, IN2 (MIN/MAX). IN, MN, MX (LIMIT). OUT: resultado. Tipos REAL para analógicos.",
                        "lad": """[INSERIR IMAGEM DO ÍCONE DA FUNÇÃO LIMIT AQUI]

                  +----------+
"PID_Out".Value--|          |
                  |  LIMIT   |-- "AO_Valve".Cmd
       0.0 --------|          |
     100.0 --------|          |
                  +----------+""",
                        "stl": """CALL  "LIMIT_Valve"
   IN := "PID_Out".Value
   MN := 0.0
   MX := 100.0
   OUT := "AO_Valve".Cmd
""",
                    },
                ],
            },
            {
                "title": "5.3 Funções Trigonométricas e Exponenciais Avançadas",
                "instructions": [
                    {
                        "name": "SIN / COS / TAN / SQRT / EXPT / LN / EXP",
                        "objective": "Funções matemáticas em REAL. Entrada e saída em radianos para trigonométricas. SQRT de valor negativo gera ENO = FALSE.",
                        "when_use": "Cinemática de braço robótico, cálculo de coordenadas em esteira circular, escalonamento não linear, dosing exponencial.",
                        "syntax": "IN (REAL): Operando. OUT (REAL): Resultado. ENO: status. CALCULATE disponível para expressões compostas.",
                        "lad": """[INSERIR IMAGEM DO ÍCONE DA FUNÇÃO SQRT AQUI]

                  +---------+
"Tank_Vol".m3-----|  SQRT   |-- "Level_Est".m
                  +---------+""",
                        "stl": """CALL  "SQRT_Level"
   IN  := "Tank_Vol".m3
   OUT := "Level_Est".m
""",
                    },
                ],
            },
        ],
    },
    {
        "title": "CAPÍTULO 6: Move Operations",
        "sections": [
            {
                "title": "6.1 Transferência de Bloco Escalar (MOVE)",
                "instructions": [
                    {
                        "name": "MOVE — Move Value",
                        "objective": "Cópia de valor entre tags de tipos compatíveis. Suporta BOOL até estruturas e VARIANT conforme versão. Substituto moderno de BLK MOV e transferências STL.",
                        "when_use": "Cópia de setpoint recebido via comunicação, transferência de estrutura de receita, inicialização de parâmetros de FB.",
                        "syntax": "EN, ENO. IN: origem. OUT: destino. Tipos devem ser atribuíveis — usar CONVERT se necessário.",
                        "lad": """[INSERIR IMAGEM DO ÍCONE DA FUNÇÃO MOVE AQUI]

                  +---------+
   Update_Recipe  |  MOVE   |
------| |--------|EN      ENO|
"HMI".Setpoint----|IN      OUT|-- "DB_Recipe".Setpoint
                  +---------+""",
                        "stl": """A     "Update_Recipe"
CALL  "MOVE_Setpoint"
   IN  := "HMI".Setpoint
   OUT := "DB_Recipe".Setpoint
""",
                    },
                ],
            },
            {
                "title": "6.2 Manipulação em Lote e Serialização (MOVE_BLK, FILL_BLK, SWAP)",
                "instructions": [
                    {
                        "name": "MOVE_BLK / FILL_BLK / SWAP",
                        "objective": "MOVE_BLK: copia N elementos de array. FILL_BLK: preenche array com valor constante. SWAP: inverte ordem de bytes (endianness) em WORD/DWORD.",
                        "when_use": "Buffer de comunicação, cópia de zona de DB, inicialização de arrays de tendência, conversão Modbus RTU (byte swap).",
                        "syntax": "MOVE_BLK: SRC, DST, COUNT, INDEX. FILL_BLK: SRC (valor), DST, COUNT. SWAP: IN/OUT WORD/DWORD.",
                        "lad": """[INSERIR IMAGEM DO ÍCONE DA FUNÇÃO MOVE_BLK AQUI]

                  +-----------+
   Copy_Enable    | MOVE_BLK  |
------| |--------|EN         ENO|
"Src_Array"-------|           |
"Dst_Array"-------|           |
       20 ---------| COUNT     |
                  +-----------+""",
                        "stl": """CALL  "MOVE_BLK_Data"
   SRC_ARRAY := "Src_Array"
   DST_ARRAY := "Dst_Array"
   COUNT     := 20
""",
                    },
                    {
                        "name": "Serialize / Deserialize",
                        "objective": "Serializa estrutura tipada em array de BYTE para transmissão. Deserialize reconstrói estrutura a partir do buffer.",
                        "when_use": "Telemetria SanBox BLBW, envio de struct via PUT/GET, logging compacto em CPU sem cartão SD.",
                        "syntax": "SRC/DST: VARIANT ou struct. POS: offset no buffer. BUFFER: ARRAY OF BYTE.",
                        "lad": """[INSERIR IMAGEM DO ÍCONE DA FUNÇÃO Serialize AQUI]

                  +------------+
   Tx_Enable      | Serialize  |
------| |--------|EN          ENO|
"DB_Telemetry"----|            |
"Tx_Buffer"-------|            |
                  +------------+""",
                        "stl": """CALL  "Serialize_Telemetry"
   SRC    := "DB_Telemetry"
   BUFFER := "Tx_Buffer"
   POS    := 0
""",
                    },
                ],
            },
        ],
    },
    {
        "title": "CAPÍTULO 7: Conversion Operations",
        "sections": [
            {
                "title": "7.1 Conversão Explícita de Cast (CONVERT)",
                "instructions": [
                    {
                        "name": "CONVERT",
                        "objective": "Conversão tipada explícita entre tipos numéricos (INT↔REAL↔DINT↔DWORD). Overflow gera ENO = FALSE em alguns casos — validar.",
                        "when_use": "Processamento de AI (INT para REAL), preparação de operandos para CMP e math, integração com drives (DWORD).",
                        "syntax": "IN: tipo origem. OUT: tipo destino declarado no box. ENO: status.",
                        "lad": """[INSERIR IMAGEM DO ÍCONE DA FUNÇÃO CONVERT AQUI]

                  +-----------+
"AI_Raw".Int------|  CONVERT  |-- "AI_Raw".Real
                  +-----------+""",
                        "stl": """CALL  "CONVERT_AI"
   IN  := "AI_Raw".Int
   OUT := "AI_Raw".Real
""",
                    },
                ],
            },
            {
                "title": "7.2 Arredondamento e Truncamento (ROUND, CEIL, FLOOR, TRUNC)",
                "instructions": [
                    {
                        "name": "ROUND / CEIL / FLOOR / TRUNC",
                        "objective": "ROUND: arredondamento matemático para inteiro. CEIL: próximo inteiro superior. FLOOR: próximo inferior. TRUNC: descarta parte fracionária.",
                        "when_use": "Exibição em IHM sem decimal, cálculo de quantidade inteira de embalagens, indexação de array por REAL.",
                        "syntax": "IN (REAL/LREAL). OUT (INT/DINT conforme bloco).",
                        "lad": """[INSERIR IMAGEM DO ÍCONE DA FUNÇÃO ROUND AQUI]

                  +---------+
"Dose_Kg".Real----|  ROUND  |-- "Dose_Kg".Int
                  +---------+""",
                        "stl": """CALL  "ROUND_Dose"
   IN  := "Dose_Kg".Real
   OUT := "Dose_Kg".Int
""",
                    },
                ],
            },
            {
                "title": "7.3 Escalonamento de Sinais Analógicos (SCALE_X, NORM_X)",
                "instructions": [
                    {
                        "name": "SCALE_X / NORM_X",
                        "objective": "NORM_X: normaliza entrada de faixa RAW (ex. 0-27648) para 0.0-1.0. SCALE_X: aplica ganho e offset de 0-1 para engenharia (0-10 bar). Par inverso para escrita em AO.",
                        "when_use": "Padronização de tratamento AI/AO em biblioteca BLBW, eliminação de fórmulas manuais em cada tag analógica.",
                        "syntax": "NORM_X: MIN, VALUE, MAX → OUT 0..1. SCALE_X: MIN, VALUE(0..1), MAX → engenharia.",
                        "lad": """[INSERIR IMAGEM DO ÍCONE DA FUNÇÃO SCALE_X AQUI]

                  +----------+
"AI_Raw".Value----|  NORM_X  |-- "AI_Norm".Pct
       0 ----------|          |
   27648 ----------|          |
                  +----------+

                  +----------+
"AI_Norm".Pct-----| SCALE_X  |-- "AI_Press".Bar
     0.0 ----------|          |
    10.0 ----------|          |
                  +----------+""",
                        "stl": """CALL  "NORM_X_AI"
   MIN   := 0
   VALUE := "AI_Raw".Value
   MAX   := 27648
   OUT   := "AI_Norm".Pct

CALL  "SCALE_X_Press"
   MIN   := 0.0
   VALUE := "AI_Norm".Pct
   MAX   := 10.0
   OUT   := "AI_Press".Bar
""",
                    },
                ],
            },
        ],
    },
    {
        "title": "CAPÍTULO 8: Program Control Operations",
        "sections": [
            {
                "title": "8.1 Saltos e Roteamento Lógico (JMP, JMPN, LABEL, SWTCH)",
                "instructions": [
                    {
                        "name": "JMP / JMPN / LABEL",
                        "objective": "JMP: salta para LABEL se RLO=1. JMPN: salta se RLO=0. LABEL: destino do salto. Código entre JMP e LABEL não é processado quando salto ativo.",
                        "when_use": "Otimização de scan em OB1 extensa, bypass de diagnóstico, desabilitação condicional de redes STL. Usar com moderação — prejudica rastreabilidade.",
                        "syntax": "LABEL: identificador único na rede. JMP/JMPN: coil-style em LAD. Apenas dentro do mesmo OB/FC.",
                        "lad": """[INSERIR IMAGEM DO ÍCONE DA FUNÇÃO JMP AQUI]

   Skip_Diag
------| |---------------------(JMP) Label_Prod

   // Redes de diagnóstico omitidas quando Skip_Diag = TRUE

                  LABEL
   Label_Prod:
   Process_Run
------| |---------------------( ) Line_Run
""",
                        "stl": """A     "Skip_Diag"
JMP   Label_Prod
// ... diagnóstico ...
Label_Prod: A     "Process_Run"
=     "Line_Run"
""",
                    },
                    {
                        "name": "SWTCH (Jump Distributor)",
                        "objective": "Distribuidor de salto indexado. K (INT) seleciona qual saída CASE é ativada, roteando fluxo para múltiplos LABELs.",
                        "when_use": "Sequenciadores em STL puro, máquinas de estados em FC sem GRAPH, seleção de rotina por código de receita.",
                        "syntax": "K (INT): índice 1..n. Entradas CASE1..CASEn com LABEL associado.",
                        "lad": """[INSERIR IMAGEM DO ÍCONE DA FUNÇÃO SWTCH AQUI]

                  +---------+
"Recipe".ID-------|  SWTCH  |
                  | K:=ID   |
                  | CASE1   |---> Label_R1
                  | CASE2   |---> Label_R2
                  +---------+""",
                        "stl": """L     "Recipe".ID
SWTCH
CASE1 Label_R1
CASE2 Label_R2
""",
                    },
                ],
            },
            {
                "title": "8.2 Finalização de Bloco (RET)",
                "instructions": [
                    {
                        "name": "RET — Return",
                        "objective": "Encerra execução do OB/FC/Fb atual imediatamente. Redes subsequentes não são processadas neste ciclo.",
                        "when_use": "FC de comunicação com abort em erro, proteção contra execução sem habilitação, saída antecipada em diagnóstico.",
                        "syntax": "RET como coil quando RLO=1. Em STL: RET condicionado ou incondicional.",
                        "lad": """[INSERIR IMAGEM DO ÍCONE DA FUNÇÃO RET AQUI]

   Comm_Error
------| |---------------------(RET)
""",
                        "stl": """A     "Comm_Error"
RET
""",
                    },
                ],
            },
        ],
    },
    {
        "title": "CAPÍTULO 9: Word Logic Operations",
        "sections": [
            {
                "title": "9.1 Mascaramento a Nível de Palavra (AND, OR, XOR)",
                "instructions": [
                    {
                        "name": "AND / OR / XOR (Word)",
                        "objective": "Operação bit a bit entre WORD/DWORD. AND: máscara de bits ativos. OR: união. XOR: comparação e toggle.",
                        "when_use": "Máscara de status de drive em DWORD, extração de nibble, diagnóstico de palavra de falha Profinet, reset seletivo de bits.",
                        "syntax": "IN1, IN2 (WORD/DWORD). OUT: resultado mesma largura.",
                        "lad": """[INSERIR IMAGEM DO ÍCONE DA FUNÇÃO AND Word AQUI]

                  +---------+
"Drive".Status----|   AND   |-- "Drive".Masked
16#00FF -----------|         |
                  +---------+""",
                        "stl": """L     "Drive".Status
L     16#00FF
AND
T     "Drive".Masked
""",
                    },
                ],
            },
            {
                "title": "9.2 Manipulação Estrutural (ENCO, DECO, SEL, MUX, DEMUX)",
                "instructions": [
                    {
                        "name": "ENCO / DECO",
                        "objective": "ENCO: converte posição de bit TRUE em INT (encoder one-hot). DECO: converte INT em word com bit correspondente em TRUE.",
                        "when_use": "Seleção de canal ativo, decodificador de posição em matriz de válvulas, interface com hardware one-hot.",
                        "syntax": "ENCO: IN (WORD), OUT (INT bit position). DECO: IN (INT), OUT (WORD).",
                        "lad": """[INSERIR IMAGEM DO ÍCONE DA FUNÇÃO ENCO AQUI]

                  +---------+
"Valve_Mask".Word-|  ENCO   |-- "Valve_Active".Idx
                  +---------+""",
                        "stl": """CALL  "ENCO_Valve"
   IN  := "Valve_Mask".Word
   OUT := "Valve_Active".Idx
""",
                    },
                    {
                        "name": "SEL / MUX / DEMUX",
                        "objective": "SEL: se G=0 OUT=IN0, se G=1 OUT=IN1. MUX: seleciona entre N entradas por índice K. DEMUX: distribui entrada para uma de N saídas por K.",
                        "when_use": "Seletor manual/auto de setpoint, multiplexação de sensores redundantes, roteamento de comando para um de vários atuadores.",
                        "syntax": "SEL: G, IN0, IN1. MUX: K (INT), IN0..INn. DEMUX: K, IN, OUT0..OUTn.",
                        "lad": """[INSERIR IMAGEM DO ÍCONE DA FUNÇÃO MUX AQUI]

                  +---------+
"Mode".Manual-----|   MUX   |-- "Setpoint".Active
"HMI".SP_Man------|         |
"DCS".SP_Auto-----|         |
"Mode".SelIdx-----| K       |
                  +---------+""",
                        "stl": """CALL  "MUX_Setpoint"
   K    := "Mode".SelIdx
   IN0  := "HMI".SP_Man
   IN1  := "DCS".SP_Auto
   OUT  := "Setpoint".Active
""",
                    },
                ],
            },
        ],
    },
    {
        "title": "CAPÍTULO 10: Shift and Rotate Operations",
        "sections": [
            {
                "title": "10.1 Deslocamento de Bits (SHR, SHL)",
                "instructions": [
                    {
                        "name": "SHR / SHL",
                        "objective": "SHR: desloca bits para direita, bits baixos perdem, entrada N define quantidade. SHL: desloca à esquerda. Útil para divisão/multiplicação por potência de 2.",
                        "when_use": "Serialização manual de bits, conversão de formato de encoder, alinhamento de dados em buffer, otimização aritmética em INT.",
                        "syntax": "IN (WORD/DWORD). N (INT): posições. OUT: resultado.",
                        "lad": """[INSERIR IMAGEM DO ÍCONE DA FUNÇÃO SHR AQUI]

                  +---------+
"Reg".Data--------|   SHR   |-- "Reg".Shifted
       2 ------------| N       |
                  +---------+""",
                        "stl": """CALL  "SHR_Reg"
   IN  := "Reg".Data
   N   := 2
   OUT := "Reg".Shifted
""",
                    },
                ],
            },
            {
                "title": "10.2 Rotação de Registradores (ROR, ROL)",
                "instructions": [
                    {
                        "name": "ROR / ROL",
                        "objective": "Rotação circular de bits — bits que saem reentram do lado oposto. Preserva todos os bits sem perda.",
                        "when_use": "CRC bit-a-bit, criptografia leve de token, simulação de registrador de deslocamento em hardware, algoritmos de hash industrial.",
                        "syntax": "IN (WORD/DWORD). N (INT): posições de rotação. OUT: resultado.",
                        "lad": """[INSERIR IMAGEM DO ÍCONE DA FUNÇÃO ROR AQUI]

                  +---------+
"Token".Word------|   ROR   |-- "Token".Rotated
       1 ------------| N       |
                  +---------+""",
                        "stl": """CALL  "ROR_Token"
   IN  := "Token".Word
   N   := 1
   OUT := "Token".Rotated
""",
                    },
                ],
            },
        ],
    },
]
