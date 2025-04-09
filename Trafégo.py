import random
import os
import time
from datetime import datetime

# Lista das ruas
ruas = [
    "Rua das Palmeiras Douradas",
    "Avenida do Sol Nascente",
    "Rua do Lago Azul",
    "Praça das Magnólias",
    "Rua do Horizonte Claro",
    "Avenida das Acácias",
    "Rua do Encanto Verde",
    "Rua das Orquídeas",
    "Alameda do Bosque Secreto",
    "Rua do Vento Suave"
]

# Lista de status
status_opcoes = ["Livre", "Movimentado", "Cheio"]

try:
    while True:
        # Embaralha as ruas para não repetir dentro do mesmo ciclo
        ruas_embaralhadas = ruas.copy()
        random.shuffle(ruas_embaralhadas)

        for rua in ruas_embaralhadas:
            # Limpa a tela
            os.system('cls' if os.name == 'nt' else 'clear')

            # Pega o horário atual (HH:MM)
            agora = datetime.now()
            horario_formatado = agora.strftime("%H:%M")

            # Escolhe status aleatoriamente (pode repetir)
            status = random.choice(status_opcoes)

            # Exibe informações
            print(f"Horário: {horario_formatado}")
            print(f"Rua: {rua}")
            print(f"Status: {status}")

            # Espera 3 segundos antes de mostrar a próxima
            time.sleep(10)

# ░░░░░░░░░░░█▀▀░░█░░░░░░
# ░░░░░░▄▀▀▀▀░░░░░█▄▄░░░░
# ░░░░░░█░█░░░░░░░░░░▐░░░
# ░░░░░░▐▐░░░░░░░░░▄░▐░░░
# ░░░░░░█░░░░░░░░▄▀▀░▐░░░
# ░░░░▄▀░░░░░░░░▐░▄▄▀░░░░
# ░░▄▀░░░▐░░░░░█▄▀░▐░░░░░
# ░░█░░░▐░░░░░░░░▄░█░░░░░
# ░░░█▄░░▀▄░░░░▄▀▐░█░░░░░
# ░░░█▐▀▀▀░▀▀▀▀░░▐░█░░░░░
# ░░▐█▐▄░░▀░░░░░░▐░█▄▄░░
# ░░░▀▀░▄███▄▄░░░▐▄▄▄▀░░░ 