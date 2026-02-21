#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
MOTOR Z9 ULTRA v10.2 - MONTE CARLO CONVERGÊNCIA
Criado por: hackerstarclay & Gemini
"""

import os, sys, time, math, re, random, hashlib, itertools
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from typing import List, Dict, Tuple, Set, Optional

# CONFIGURAÇÕES
CHAVE_MESTRA = "hackerstarclay"
ARQUIVO_DADOS = 'DEZENAS.txt'
[span_1](start_span)MC_ITERACOES_JOGO = 10000[span_1](end_span)

@dataclass
class JogoGerado:
    letra: str
    dezenas: List[int]
    precisao: float
    [span_2](start_span)status_detalhado: List[str] = field(default_factory=list)[span_2](end_span)

def calcular_raiz(n: int) -> int:
    [span_3](start_span)return (n - 1) % 9 + 1 if n > 0 else 0[span_3](end_span)

class MotorDados:
    def __init__(self):
        self.dados = []
    def carregar(self):
        if not os.path.exists(ARQUIVO_DADOS): return False
        with open(ARQUIVO_DADOS, 'r') as f:
            for l in f:
                nums = re.findall(r'\d+', l)
                if len(nums) >= 6:
                    [span_4](start_span)d = [int(x) for x in nums[-6:]][span_4](end_span)
                    [span_5](start_span)self.dados.append({'reais': d, 'raizes': [calcular_raiz(x) for x in d]})[span_5](end_span)
        return True

def main():
    [span_6](start_span)print("ESCRITÓRIO Z9 - SCANNER NEURAL ULTRA v10.2")[span_6](end_span)
    chave = input("DIGITE A KEY: ").strip()
    if chave != CHAVE_MESTRA: return
    motor = MotorDados()
    if motor.carregar():
        [span_7](start_span)print(f"✓ {len(motor.dados)} concursos carregados. Analisando inércia...")[span_7](end_span)

if __name__ == "__main__":
    main()
