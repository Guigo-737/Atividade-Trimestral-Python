import random
import os
import time
from datetime import datetime


#▒▒▒▒▒▒▒▒▒▒▒▒
#▒▒▒▒▓▒▒▓▒▒▒▒
#▒▒▒▒▓▒▒▓▒▒▒▒
#▒▒▒▒▒▒▒▒▒▒▒▒
#▒▓▒▒▒▒▒▒▒▒▓▒
#▒▒▓▓▓▓▓▓▓▓▒▒
#▒▒▒▒▒▒▒▒▒▒▒▒
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

#─▄▀▀▀▄────▄▀█▀▀█▄
#▄▀─▀─▀▄▄▀█▄▀─▄▀─▄▀▄
#█▄▀█───█─█▄▄▀─▄▀─▄▀▄
#──█▄▄▀▀█▄─▀▀▀▀▀▀▀─▄█
#─────▄████▀▀▀▀████─▀▄
status_opcoes = ["Livre", "Movimentado", "Cheio"]

try:
    while True:

        ruas_embaralhadas = ruas.copy()
        random.shuffle(ruas_embaralhadas)

        for rua in ruas_embaralhadas:

            os.system('cls' if os.name == 'nt' else 'clear')

            agora = datetime.now()
            horario_formatado = agora.strftime("%H:%M")

            status = random.choice(status_opcoes)

# ░░░░░░███████ ]▄▄▄▄▄▄▄▄▃
#▂▄▅█████████▅▄▃▂
#I███████████████████].
#◥⊙▲⊙▲⊙▲⊙▲⊙▲⊙▲⊙◤


            print(f"Horário: {horario_formatado}")
            print(f"Rua: {rua}")
            print(f"Status: {status}")

# ───▄██▄─██▄───▄
#─▄██████████▄███▄
#─▌████████████▌
#▐▐█░█▌░▀████▀░░
#░▐▄▐▄░░░▐▄▐▄░░░░
            time.sleep(10)

except KeyboardInterrupt:
    print("\nExecução interrompida.")
