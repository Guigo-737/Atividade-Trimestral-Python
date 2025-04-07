import time
import random
from datetime import datetime

# Dicionário com as linhas e as letras correspondentes
linhas = {
    "amarela": "A",
    "vermelha": "V",
    "roxa": "R",
    "marrom": "M"
}

# Função para verificar se está em horário de pico
def horario_de_pico(hora):
    return (5 <= hora < 8) or (hora == 12) or (16 <= hora < 19)

# Loop infinito do sistema de monitoramento
while True:
    # Seleciona aleatoriamente uma linha
    linha_nome, letra_linha = random.choice(list(linhas.items()))

    # Gera um número de trem entre 1 e 10
    numero_trem = random.randint(1, 10)
    codigo_trem = f"{numero_trem}{letra_linha}"

    # Determina estado do trem: 80% de chance de estar funcional
    estado = "FUNCIONAL" if random.random() < 0.8 else "MANUTENÇÃO"

    # Pega o horário atual
