#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
================================================================================
MOTOR Z9 ULTRA v10.2 - MONTE CARLO CONVERGÊNCIA
================================================================================
Telescópio Temporal com Aceleração de Convergência
"Enquanto o humano vê a semana, processamos os milênios"
""" 

import os
import sys
import time
import math
import re
import random
import json
import hashlib
import itertools
from collections import Counter, defaultdict, deque
from datetime import datetime
from typing import List, Dict, Tuple, Set, Optional
from dataclasses import dataclass, field
from enum import Enum
from functools import lru_cache, wraps 

# ================================================================================
# CONFIGURAÇÕES MONTE CARLO
# ================================================================================ 

CHAVE_MESTRA = "hackerstarclay"
ARQUIVO_DADOS = 'DEZENAS.txt' 

# Parâmetros Monte Carlo - Ajustáveis para precisão máxima
MC_ITERACOES_RAIZ = 5000      # Simulações por posição de raiz
MC_ITERACOES_JOGO = 10000     # Simulações por jogo gerado
MC_CONVERGENCIA_LIMITE = 0.001 # Limiar de convergência (quanto menor, mais preciso)
MC_JANELA_TEMPORAL = 100      # Jogos para análise de atrator 

# Cores para terminal
COR_RESET = "\033[0m"
COR_VERMELHO = "\033[91m"
COR_VERDE = "\033[92m"
COR_AMARELO = "\033[93m"
COR_AZUL = "\033[94m"
COR_MAGENTA = "\033[95m"
COR_CIANO = "\033[96m"
COR_BRANCO = "\033[97m"
COR_NEGRITO = "\033[1m" 

# ================================================================================
# ESTRUTURAS DE DADOS
# ================================================================================ 

@dataclass
class DezenaAnalytics:
    valor: int
    raiz: int
    atraso_atual: int = 0
    atraso_medio: float = 0.0
    frequencia_total: int = 0
    frequencia_recente: float = 0.0
    ciclo_medio: float = 0.0
    probabilidade_saida: float = 0.0
    score_momentum: float = 0.0
    status: str = "neutro"
    # Monte Carlo extras
    mc_confianca: float = 0.0
    mc_atrator: float = 0.0 

@dataclass
class PosicaoRaiz:
    posicao: int
    raiz_dominante: int
    tendencia: str
    forca: float
    distribuicao: Dict[int, float]
    confianca: float
    # Monte Carlo extras
    mc_distribuicao: Dict[int, float] = field(default_factory=dict)
    mc_entropia: float = 0.0
    mc_atrator_stranho: Optional[int] = None 

@dataclass
class JogoGerado:
    letra: str
    dezenas: List[int]
    raizes: List[int]
    precisao: float
    dna: str = ""
    status_detalhado: List[str] = field(default_factory=list)
    # Monte Carlo extras
    mc_score: float = 0.0
    mc_convergencia: float = 0.0
    mc_variancia: float = 0.0 

    def __post_init__(self):
        if not self.dna:
            self.dna = hashlib.md5(''.join(f"{d:02d}" for d in sorted(self.dezenas)).encode()).hexdigest()[:12] 

# ================================================================================
# FUNÇÕES MATEMÁTICAS
# ================================================================================ 

def calcular_raiz(n: int) -> int:
    """Raiz digital 1-9"""
    if n <= 0:
        return 0
    return (n - 1) % 9 + 1 

def calcular_entropia(dados: List[int]) -> float:
    """Entropia de Shannon"""
    if not dados:
        return 0.0
    counter = Counter(dados)
    total = len(dados)
    entropia = 0.0
    for count in counter.values():
        p = count / total
        if p > 0:
            entropia -= p * math.log2(p)
    return entropia 

def calcular_variancia(dados: List[float]) -> float:
    """Variância amostral"""
    if len(dados) < 2:
        return 0.0
    media = sum(dados) / len(dados)
    return sum((x - media) ** 2 for x in dados) / (len(dados) - 1) 

# ================================================================================
# MOTOR MONTE CARLO
# ================================================================================ 

class MotorMonteCarlo:
    """Simulação de Monte Carlo para aceleração de convergência""" 

    def __init__(self, motor_dados: 'MotorDados'):
        self.motor = motor_dados
        self.historico_simulacoes: List[Dict] = []
        self.atratores_detectados: Dict[int, List[int]] = {} 

    def simular_distribuicao_raiz(self, posicao: int, raiz_alvo: int,
                                  iteracoes: int = MC_ITERACOES_RAIZ) -> Dict:
        """
        Simula milhares de cenários para encontrar a distribuição
        de convergência da raiz em uma posição específica
        """
        resultados = []
        dados = self.motor.dados[-MC_JANELA_TEMPORAL:] 

        for _ in range(iteracoes):
            # Simula um cenário temporal aleatório
            amostra = random.sample(dados, min(20, len(dados)))
            raizes_amostra = [j['raizes'][posicao] for j in amostra]
  letra: str
    dezenas: List[int]
    raizes: List[int]
    precisao: float
    dna: str = ""
    status_detalhado: List[str] = field(default_factory=list)
    # Monte Carlo extras
    mc_score: float = 0.0
    mc_convergencia: float = 0.0
    mc_variancia: float = 0.0 

    def __post_init__(self):
        if not self.dna:
            self.dna = hashlib.md5(''.join(f"{d:02d}" for d in sorted(self.dezenas)).encode()).hexdigest()[:12] 

# ================================================================================
# FUNÇÕES MATEMÁTICAS
# ================================================================================ 

def calcular_raiz(n: int) -> int:
    """Raiz digital 1-9"""
    if n <= 0:
        return 0
    return (n - 1) % 9 + 1 

def calcular_entropia(dados: List[int]) -> float:
    """Entropia de Shannon"""
    if not dados:
        return 0.0
    counter = Counter(dados)
    total = len(dados)
    entropia = 0.0
    for count in counter.values():
        p = count / total
        if p > 0:
            entropia -= p * math.log2(p)
    return entropia 

def calcular_variancia(dados: List[float]) -> float:
    """Variância amostral"""
    if len(dados) < 2:
        return 0.0
    media = sum(dados) / len(dados)
    return sum((x - media) ** 2 for x in dados) / (len(dados) - 1) 

# ================================================================================
# MOTOR MONTE CARLO
# ================================================================================ 

class MotorMonteCarlo:
    """Simulação de Monte Carlo para aceleração de convergência""" 

    def __init__(self, motor_dados: 'MotorDados'):
        self.motor = motor_dados
        self.historico_simulacoes: List[Dict] = []
        self.atratores_detectados: Dict[int, List[int]] = {} 

    def simular_distribuicao_raiz(self, posicao: int, raiz_alvo: int,
                                  iteracoes: int = MC_ITERACOES_RAIZ) -> Dict:
        """
        Simula milhares de cenários para encontrar a distribuição
        de convergência da raiz em uma posição específica
        """
        resultados = []
        dados = self.motor.dados[-MC_JANELA_TEMPORAL:] 

        for _ in range(iteracoes):
            # Simula um cenário temporal aleatório
            amostra = random.sample(dados, min(20, len(dados)))
            raizes_amostra = [j['raizes'][posicao] for j in amostra] 

            # Calcula tendência neste cenário
            freq_raiz = raizes_amostra.count(raiz_alvo) / len(raizes_amostra) 

            # Adiciona ruído controlado (fator caos)
            ruído = random.gauss(0, 0.1)
            resultado = max(0, min(1, freq_raiz + ruído))
            resultados.append(resultado) 

        # Análise de convergência
        media = sum(resultados) / len(resultados)
        variancia = calcular_variancia(resultados) 

        # Detecta atrator (ponto de estabilização)        histograma = Counter([round(r, 2) for r in resultados])
        atrator = histograma.most_common(1)[0][0] if histograma else media 

        return {
            'media': media,
            'variancia': variancia,
            'desvio_padrao': math.sqrt(variancia),
            'atrator': atrator,
            'confianca': 1 - variancia,  # Quanto menor variância, maior confiança
            'distribuicao': {k: v/iteracoes for k, v in histograma.items()}
        } 

    def simular_jogo_completo(self, dezenas: List[int],
                              iteracoes: int = MC_ITERACOES_JOGO) -> Dict:
        """
        Simula milhares de jogos similares para calcular
        probabilidade real de acerto baseada em atratores históricos
        """
        acertos_simulados = []
        dados = self.motor.dados 

        for _ in range(iteracoes):
            # Gera um jogo "vizinho" no espaço de fase
            jogo_simulado = self._gerar_jogo_vizinho(dezenas) 

            # Verifica quantos números bateriam em sorteios históricos
            acertos = self._simular_sorteio(jogo_simulado, dados)
            acertos_simulados.append(acertos) 

        # Estatísticas de convergência
        media_acertos = sum(acertos_simulados) / len(acertos_simulados)
        variancia = calcular_variancia(acertos_simulados) 

        # Score Monte Carlo (quanto mais estável, melhor)
        estabilidade = 1 / (1 + variancia)
        score_mc = media_acertos * estabilidade * 100 

        return {
            'media_acertos': media_acertos,
            'variancia': variancia,
            'score_mc': min(score_mc, 100),
            'confianca': estabilidade,
            'percentil_95': sorted(acertos_simulados)[int(iteracoes * 0.95)]
        } 

    def _gerar_jogo_vizinho(self, dezenas_base: List[int],
                           perturbacao: float = 0.3) -> List[int]:
        """Gera jogo próximo no espaço de fase (perturbação controlada)"""
        jogo = []
        for d in dezenas_base:
            if random.random() < perturbacao:
                # Perturba para número próximo com mesma raiz
                raiz = calcular_raiz(d)
                vizinhos = [x for x in range(max(1, d-5), min(61, d+6))
                           if calcular_raiz(x) == raiz and x != d]
                jogo.append(random.choice(vizinhos) if vizinhos else d)
            else:
                jogo.append(d)
        return sorted(jogo) 

    def _simular_sorteio(self, jogo: List[int], dados: List[Dict]) -> int:
        """Simula um sorteio e retorna número de acertos"""
        # Escolhe um sorteio histórico aleatório como "resultado"
        sorteio_real = random.choice(dados)['reais']
        return len(set(jogo) & set(sorteio_real)) 

    def detectar_atrator_estranho(self, posicao: int) -> Optional[int]:
        """
        Detecta o "atrator estranho" - padrão cíclico oculto
        que se repere apesar do caos aparente
        """
        if len(self.motor.dados) < 50:
            return None 

        # Análise de Fourier simplificada para detectar ciclos
        raizes = [j['raizes'][posicao] for j in self.motor.dados[-100:]] 

        # Autocorrelação
        def autocorr(lags):
            n = len(raizes)
            return sum(raizes[i] * raizes[i+lags] for i in range(n-lags)) / (n-lags) 

        # Procura período dominante
        correlações = [(lag, autocorr(lag)) for lag in range(1, 20)]
     melhor_lag = max(correlações, key=lambda x: x[1]) 

        if melhor_lag[1] > 0.3:  # Correlação significativa
            return melhor_lag[0] 

        return None 

# ================================================================================
# GERENCIADOR DE DADOS
# ================================================================================ 

class MotorDados:
    def __init__(self):
        self.dados: List[Dict] = []
        self.analytics: Dict[int, DezenaAnalytics] = {}
        self.matriz_pares: Dict[Tuple[int, int], float] = {}
        self.cache_raizes: Dict[int, List[int]] = {}
        self.monte_carlo: Optional[MotorMonteCarlo] = None
        self._init_cache() 

    def _init_cache(self):
        for r in range(1, 10):
            self.cache_raizes[r] = [d for d in range(1, 61) if calcular_raiz(d) == r] 

    def carregar(self, arquivo: str = ARQUIVO_DADOS) -> bool:
        if not os.path.exists(arquivo):
            print(f"{COR_VERMELHO}ERRO: {arquivo} não encontrado!{COR_RESET}")
            return False 

        try:
            with open(arquivo, 'r', encoding='utf-8') as f:
                linhas = f.readlines() 

            self.dados = []
            for num_linha, linha in enumerate(linhas, 1):
                numeros = re.findall(r'\d+', linha)
                if len(numeros) >= 6:
                    try:
                        dezenas = [int(x) for x in numeros[-6:]]
                        if all(1 <= d <= 60 for d in dezenas) and len(set(dezenas)) == 6:
                            raizes = [calcular_raiz(d) for d in dezenas]
                            self.dados.append({
                                'concurso': num_linha,
                                'reais': dezenas,
                                'raizes': raizes,
                                'soma': sum(dezenas)
                            })
                    except:
                        continue 

            # Inicializa Monte Carlo
            self.monte_carlo = MotorMonteCarlo(self) 

            self._processar_analytics()
            self._construir_matriz()
            return True 

        except Exception as e:
            print(f"{COR_VERMELHO}ERRO: {str(e)}{COR_RESET}")
            return False 

    def _processar_analytics(self):
        total = len(self.dados)
        for dezena in range(1, 61):
            analytics = DezenaAnalytics(valor=dezena, raiz=calcular_raiz(dezena)) 

            atrasos = []
            ultimas_saidas = []
            ultimo_idx = -1 

            for idx, jogo in enumerate(reversed(self.dados)):
                if dezena in jogo['reais']:
                    if ultimo_idx == -1:
                        analytics.atraso_atual = idx
                    else:
                        atrasos.append(idx - ultimo_idx)
                    ultimas_saidas.append(total - idx)
                    ultimo_idx = idx 

            if atrasos:
                analytics.atraso_medio = sum(atrasos) / len(atrasos)
                analytics.ciclo_medio = analytics.atraso_medio 

            if atrasos:
                analytics.atraso_medio = sum(atrasos) / len(atrasos)
                analytics.ciclo_medio = analytics.atraso_medio 

            analytics.frequencia_total = len(ultimas_saidas)
            if total > 0:
                analytics.frequencia_recente = (analytics.frequencia_total / total) * 100 

            if len(ultimas_saidas) >= 2:
                recentes = ultimas_saidas[:min(5, len(ultimas_saidas))]
                if len(recentes) >= 2:
                    analytics.score_momentum = sum(recentes[i] - recentes[i+1] for i in range(len(recentes)-1)) / (len(recentes)-1) 

            if analytics.atraso_medio > 0:
                lambda_p = 1 / analytics.atraso_medio
                analytics.probabilidade_saida = (1 - math.exp(-lambda_p * (analytics.atraso_atual + 1))) * 100 

            # Monte Carlo: Simula convergência para esta dezena
            if self.monte_carlo:
                sim_mc = self.monte_carlo.simular_distribuicao_raiz(
                    0, analytics.raiz, MC_ITERACOES_RAIZ // 10
                )
                analytics.mc_confianca = sim_mc['confianca']
                analytics.mc_atrator = sim_mc['atrator'] 

            if analytics.atraso_atual > 22:
                analytics.status = "frio"
            elif 1 < analytics.atraso_atual < 10 and analytics.probabilidade_saida > 30:
                analytics.status = "quente"
            elif analytics.atraso_atual == 0:
                analytics.status = "critico"
            else:
                analytics.status = "neutro" 

            self.analytics[dezena] = analytics 

    def _construir_matriz(self):
        pares_count = Counter()
        total = len(self.dados) 

        for jogo in self.dados:
            for par in itertools.combinations(sorted(jogo['reais']), 2):
                pares_count[par] += 1 

        self.matriz_pares = {par: count/total for par, count in pares_count.items()} 

    def get_dezenas_raiz(self, raiz: int) -> List[int]:
        return self.cache_raizes.get(raiz, []) 

    def get_analytics(self, dezena: int) -> Optional[DezenaAnalytics]:
        return self.analytics.get(dezena) 

# ================================================================================
# ANALISADOR DE INÉRCIA COM MONTE CARLO
# ================================================================================ 

class AnalisadorInercia:
    def __init__(self, motor: MotorDados):
        self.motor = motor
        self.resultados: List[PosicaoRaiz] = [] 

    def analisar(self) -> List[PosicaoRaiz]:
        dados = self.motor.dados
        total = len(dados) 

        if total == 0:
            return [] 

        self.resultados = [] 

        for pos in range(6):
            raizes_pos = [j['raizes'][pos] for j in dados] 

            scores = defaultdict(float)
            for idx, raiz in enumerate(raizes_pos):
                peso = math.pow(4.8, (idx / total) * 15) if total > 0 else 1
                scores[raiz] += peso 

            raiz_dom = max(scores, key=scores.get) 

            total_score = sum(scores.values())
            distrib = {r: s/total_score for r, s in scores.items()} 

            ultimos_15 = raizes_pos[-15:]
           freq = sum(1 for r in ultimos_15 if r == raiz_dom) / 15 

            if freq >= 0.40:
                tendencia = "+"
                forca = freq * 100
            elif freq <= 0.10:
                tendencia = "-"
                forca = (1 - freq) * 50
            else:
                tendencia = "/"
                forca = 50 

            entropia = -sum(p * math.log2(p) for p in distrib.values() if p > 0)
            confianca = (distrib[raiz_dom] * 0.6 + (1 - entropia/math.log2(9)) * 0.4) * 100 

            # MONTE CARLO: Refina com simulação
            mc_resultado = None
            if self.motor.monte_carlo:
                mc_resultado = self.motor.monte_carlo.simular_distribuicao_raiz(pos, raiz_dom)
                # Ajusta confiança com resultado MC
                confianca = confianca * 0.6 + mc_resultado['confianca'] * 100 * 0.4 

            # Detecta atrator estranho
            atrator = None
            if self.motor.monte_carlo:
                atrator = self.motor.monte_carlo.detectar_atrator_estranho(pos) 

            self.resultados.append(PosicaoRaiz(
                posicao=pos + 1,
                raiz_dominante=raiz_dom,
                tendencia=tendencia,
                forca=forca,
                distribuicao=distrib,
                confianca=min(confianca, 100),
                mc_distribuicao=mc_resultado['distribuicao'] if mc_resultado else {},
                mc_entropia=mc_resultado['variancia'] if mc_resultado else 0,
                mc_atrator_stranho=atrator
            )) 

        return self.resultados 

# ================================================================================
# CLASSIFICADOR TÉRMICO
# ================================================================================ 

class ClassificadorTermico:
    def __init__(self, motor: MotorDados):
        self.motor = motor 

    def classificar(self, dezena: int, pos: int, inercia: PosicaoRaiz) -> Dict:
        analytics = self.motor.get_analytics(dezena)
        if not analytics:
            return {'status': '(?)', 'score': 0, 'cor': COR_BRANCO} 

        raiz_d = analytics.raiz
        raiz_alvo = inercia.raiz_dominante 

        score = 0
        if raiz_d == raiz_alvo:
            score += 40
            # Bônus Monte Carlo se raiz convergir com atrator
            if inercia.mc_atrator_stranho and raiz_d == inercia.mc_atrator_stranho % 9 + 1:
                score += 10 

        if 1 < analytics.atraso_atual < 10:
            score += 25
        if analytics.probabilidade_saida > 35:
            score += 15
        if analytics.score_momentum > analytics.ciclo_medio * 0.8:
            score += 10
        if analytics.status == "quente":
            score += 10 

        # Bônus Monte Carlo
        score += analytics.mc_confianca * 10 

        if score >= 70:
            status = "(+)"
            cor = COR_VERDE
        elif score <= 20 or analytics.atraso_atual > 25:
            status = "(-)"
            cor = COR_VERMELHO
  elif score <= 20 or analytics.atraso_atual > 25:
            status = "(-)"
            cor = COR_VERMELHO
        elif analytics.status == "critico":
            status = "(!)"
            cor = COR_AMARELO
        else:
            status = "(/)"
            cor = COR_CIANO 

        return {'status': status, 'score': score, 'cor': cor} 

# ================================================================================
# MOTOR DE PRECISÃO COM MONTE CARLO
# ================================================================================ 

class MotorPrecisao:
    def __init__(self, motor: MotorDados, classificador: ClassificadorTermico):
        self.motor = motor
        self.classificador = classificador 

    def calcular(self, dezenas: List[int], inercias: List[PosicaoRaiz]) -> float:
        # 1. Sinal de tendência (40%)
        scores_sinal = []
        for i, d in enumerate(dezenas):
            c = self.classificador.classificar(d, i, inercias[i])
            scores_sinal.append(c['score']) 

        pesos_pos = [1.2, 1.15, 1.1, 1.05, 1.0, 0.95]
        nota_sinal = sum(s * p for s, p in zip(scores_sinal, pesos_pos)) / sum(pesos_pos)
        if all(s > 50 for s in scores_sinal):
            nota_sinal *= 1.1 

        # 2. Força histórica (20%)
        pares = list(itertools.combinations(sorted(dezenas), 2))
        score_hist = sum(self.motor.matriz_pares.get(par, 0) for par in pares) / len(pares) * 1000 if pares else 0
        nota_hist = min(score_hist, 100) 

        # 3. Correlação (15%)
        nota_corr = 100.0
        for par in pares:
            if self.motor.matriz_pares.get(par, 0) < 0.001:
                nota_corr -= 15 

        # 4. Balanceamento (10%)
        nota_bal = 100.0
        pares_count = len([d for d in dezenas if d % 2 == 0])
        if abs(pares_count - 3) > 1:
            nota_bal -= 20 

        # 5. Entropia (5%)
        ent = calcular_entropia(dezenas)
        nota_ent = 100 if 2.0 <= ent <= 2.5 else 70 if 1.5 <= ent <= 2.8 else 40 

        # 6. MONTE CARLO (10%) - Novo!
        nota_mc = 0
        if self.motor.monte_carlo:
            resultado_mc = self.motor.monte_carlo.simular_jogo_completo(dezenas, MC_ITERACOES_JOGO // 10)
            nota_mc = resultado_mc['score_mc'] 

        final = (
            min(nota_sinal, 100) * 0.40 +
            nota_hist * 0.20 +
            max(0, nota_corr) * 0.15 +
            nota_bal * 0.10 +
            nota_ent * 0.05 +         nota_mc * 0.10  # Monte Carlo weight
        ) 

        return min(final, 100.0) 

# ================================================================================
# GERADOR DE JOGOS COM CONVERGÊNCIA ACELERADA
# ================================================================================ 

class GeradorJogos:
    def __init__(self, motor: MotorDados, inercias: List[PosicaoRaiz],
                 classificador: ClassificadorTermico, precisao: MotorPrecisao):
        self.motor = motor
        self.inercias = inercias
        self.classificador = classificador
        self.precisao = precisao
        self.dnas_usados: Set[str] = set()
        self.pool_elite: List[List[int]] = [[] for _ in range(6)] 

    def gerar(self, quantidade: int = 7) -> List[JogoGerado]:
        jogos = []
        letras = ['A', 'B', 'C', 'D', 'E', 'F', 'G'] 

        for i in range(min(quantidade, len(letras))):
            jogo = self._gerar_jogo_mc(letras[i])
            if jogo:
                jogos.append(jogo)
                self.dnas_usados.add(jogo.dna) 

        # Ordena por precisão (agora inclui Monte Carlo)
        jogos.sort(key=lambda x: x.precisao, reverse=True) 

        for i in range(6):
            elites = [j.dezenas[i] for j in jogos[:3] if j.status_detalhado[i] == "(+)"]
            self.pool_elite[i] = elites if elites else [j.dezenas[i] for j in jogos[:1]] 

        return jogos 

    def _gerar_jogo_mc(self, letra: str) -> Optional[JogoGerado]:
        """Gera jogo usando convergência acelerada de Monte Carlo"""
        melhor_jogo = None
        melhor_score = 0 

        # Fase 1: Exploração (diversidade)
        candidatos = []
        for _ in range(100):
            dezenas = self._estrategia_hibrida_mc()
            if len(set(dezenas)) == 6:
                jogo = self._construir_jogo(letra, dezenas)
                if jogo.dna not in self.dnas_usados:
                    candidatos.append(jogo) 

        # Fase 2: Convergência (refinamento Monte Carlo)
        for jogo in candidatos[:20]:  # Top 20 candidatos
            if self.motor.monte_carlo:
                resultado_mc = self.motor.monte_carlo.simular_jogo_completo(
                    jogo.dezenas, MC_ITERACOES_JOGO // 50
                )
                score_total = jogo.precisao * 0.7 + resultado_mc['score_mc'] * 0.3 

                if score_total > melhor_score:
                    melhor_score = score_total
                    melhor_jogo = jogo
                    melhor_jogo.mc_score = resultado_mc['score_mc']
                    melhor_jogo.mc_convergencia = resultado_mc['confianca']
                    melhor_jogo.mc_variancia = resultado_mc['variancia'] 

        return melhor_jogo or (candidatos[0] if candidatos else None) 

    def _estrategia_hibrida_mc(self) -> List[int]:
        """Estratégia híbrida com peso Monte Carlo"""
        jogo = [] 

        for i, inc in enumerate(self.inercias):
            # Usa distribuição MC se disponível
            if inc.mc_distribuicao and random.random() < 0.3:
                # Amostra da distribuição Monte Carlo
                raizes_possiveis = list(inc.mc_distribuicao.keys())
                pesos_mc = list(inc.mc_distribuicao.values())
                raiz = random.choices(raizes_possiveis, weights=pesos_mc, k=1)[0]
                # Converte de float para int (raiz)
                raiz = int(float(raiz)) % 9 + 1
            else:               dezenas.append(random.randint(1, 60)) 

        unicas = list(set(dezenas))
        while len(unicas) < 6:
            n = random.randint(1, 60)
            if n not in unicas:
                unicas.append(n) 

        unicas = self._otimizar_raizes_mc(unicas[:6]) 

        jogo = self._construir_jogo("H", unicas) 

        # Refinamento Monte Carlo final no Jogo H
        if self.motor.monte_carlo:
            resultado_mc = self.motor.monte_carlo.simular_jogo_completo(unicas, MC_ITERACOES_JOGO // 20)
            jogo.precisao = min(jogo.precisao * 0.8 + resultado_mc['score_mc'] * 0.2 + 5, 100)
            jogo.mc_score = resultado_mc['score_mc'] 

        return jogo 

    def _otimizar_raizes_mc(self, dezenas: List[int]) -> List[int]:
        dezenas = list(dezenas)
        for i in range(6):
            raiz_ideal = self.inercias[i].raiz_dominante
            raiz_atual = calcular_raiz(dezenas[i]) 

            if raiz_atual != raiz_ideal:
                candidatas = [d for d in self.motor.get_dezenas_raiz(raiz_ideal) if d not in dezenas]
                if candidatas:
                    # Escolhe a que tem melhor score MC
                    melhor = max(candidatas, key=lambda x: self.motor.get_analytics(x).mc_confianca
                                if self.motor.get_analytics(x) else 0)
                    dezenas[i] = melhor
        return dezenas 

# ================================================================================
# INTERFACE VISUAL (INTACTA - NÃO MODIFICADA)
# ================================================================================ 

def limpar_tela():
    os.system('clear' if os.name == 'posix' else 'cls') 

def print_header(titulo: str):
    print(f"{COR_AZUL}{'█' * 75}{COR_RESET}")
    print(f"{COR_VERDE}{COR_NEGRITO}{titulo.center(75)}{COR_RESET}")
    print(f"{COR_AZUL}{'█' * 75}{COR_RESET}") 

def print_linha(char: str = "═"):
    print(f"{COR_CIANO}{char * 75}{COR_RESET}") 

def formatar_dezena(dezena: int, status: str) -> str:
    cores = {
        "(+)": COR_VERDE,
        "(-)": COR_VERMELHO,
        "(!)": COR_AMARELO,
        "(/)": COR_CIANO,
        "(?)": COR_BRANCO
    }
    return f"{cores.get(status, COR_BRANCO)}{dezena:02d}{status}{COR_RESET}" 

def print_jogo(jogo: JogoGerado, inercias: List[PosicaoRaiz]):
    partes = [formatar_dezena(d, s) for d, s in zip(jogo.dezenas, jogo.status_detalhado)]
    print(f"  [{COR_NEGRITO}{jogo.letra}{COR_RESET}] " + " ".join(partes) +
          f"  | Prec: {COR_VERDE}{jogo.precisao:.1f}%{COR_RESET}") 

def print_elite(jogos: List[JogoGerado], inercias: List[PosicaoRaiz], proximo: int):
    print_linha("◆")
    print(f"{COR_AMARELO}{COR_NEGRITO}  >>> ELITE NEURAL SCANNER: CONCURSO {proximo}{COR_RESET}")
    print_linha("◆") 

    for rank, jogo in enumerate(jogos[:3], 1):
        icone = "🔥🔥🔥 ULTRA" if jogo.precisao > 90 else "🔥🔥 PREMIUM" if jogo.precisao > 80 else "🔥 HOT" if jogo.precisao > 70 else "⭐ STD"
        cor = COR_VERMELHO if jogo.precisao > 90 else COR_VERDE if jogo.precisao > 80 else COR_AMARELO 

        print(f"\n  {cor}{COR_NEGRITO}[RANK {rank}] JOGO {jogo.letra} ({jogo.precisao:.2f}% {icone}){COR_RESET}")
        print(f"  {'─' * 50}") 

        for i, d in enumerate(jogo.dezenas):
            a = MotorDados().get_analytics(d)
            info = f"    Bola {i+1}: {formatar_dezena(d, jogo.status_detalhado[i])}"
            if a:
                info += f" | Atraso: {a.atraso_atual} | Prob: {a.probabilidade_saida:.1f}%"
            print(info) 

def print_mestre(jogo: JogoGerado):
    print_linha("█")
    print(f"{COR_VERMELHO}{COR_NEGRITO}  >>> JOGO H (CONVERGÊNCIA MESTRA NEURAL){COR_RESET}")
    print_linha("█")
    dezenas_fmt = "  ".join(f"{COR_VERDE}{d:02d}(+){COR_RESET}" for d in jogo.dezenas)
    print(f"\n  [{dezenas_fmt}]")
    print(f"\n  {COR_AMARELO}Precisão Neural: {jogo.precisao:.2f}%{COR_RESET}")
    print_linha("█") 

# ================================================================================
# FUNÇÃO PRINCIPAL (INTACTA)
# ================================================================================ 

def painel_principal():
    motor = MotorDados() 

    print(f"{COR_CIANO}Carregando dados...{COR_RESET}")
    if not motor.carregar():
        input("\nPressione ENTER para sair...")
        return 

    total = len(motor.dados)
    print(f"{COR_VERDE}✓ {total} concursos carregados{COR_RESET}\n") 

    analisador = AnalisadorInercia(motor)
    inercias = analisador.analisar() 

    classificador = ClassificadorTermico(motor)
    precisao = MotorPrecisao(motor, classificador) 

    gerador = GeradorJogos(motor, inercias, classificador, precisao)
    jogos = gerador.gerar(7) 

    limpar_tela()
    print_header(" MOTOR Z9 ULTRA v10.2 | SISTEMA NEURAL DE ALTA PERFORMANCE ")
    print(f"{COR_CIANO}  Base: {total} concursos | Próximo: {total + 1}{COR_RESET}")
    print_linha() 

    estrutura = ' '.join([f"{i+1}ª[{inc.raiz_dominante}]({inc.tendencia})" for i, inc in enumerate(inercias)])
    print(f"  [ESTRUTURA RAIZ]: {COR_AMARELO}{estrutura}{COR_RESET}")
    print_linha() 

    for jogo in jogos:
        print_jogo(jogo, inercias) 

    print_elite(jogos, inercias, total + 1) 

    mestre = gerador.gerar_mestre()
    print_mestre(mestre) 

    print(f"\n{COR_VERDE}Análise concluída com sucesso!{COR_RESET}") 

def main():
    limpar_tela()
    print_header(" ESCRITÓRIO Z9 - SCANNER NEURAL ULTRA (v10.2) ") 

    chave = input(f"\n{COR_AMARELO}DIGITE A KEY: {COR_RESET}").strip() 

    if chave != CHAVE_MESTRA:
        print(f"\n{COR_VERMELHO}{COR_NEGRITO}ACESSO NEGADO.{COR_RESET}")
        time.sleep(2)
        return 

    while True:
        limpar_tela()
        painel_principal() 

        opcao = input(f"\n{COR_CIANO}>>> ENTER para novo scan ou 'SAIR': {COR_RESET}").lower().strip()
        if opcao == 'sair':
            break 

    limpar_tela()    print(f"{COR_VERDE}Sistema encerrado. Boa sorte!{COR_RESET}") 

if __name__ == "__main__":
    main()
