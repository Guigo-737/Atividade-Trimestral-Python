import time
import random
from datetime import datetime



linhas = {
   "amarela": "A",
   "vermelha": "V",
   "roxa": "R",
   "marrom": "M"
}



def horario_de_pico(hora):
   return (5 <= hora < 8) or (hora == 12) or (16 <= hora < 19)



while True:
   # Seleciona qualque uma linha
   linha_nome, letra_linha = random.choice(list(linhas.items()))


   
   numero_trem = random.randint(1, 10)
   codigo_trem = f"{numero_trem}{letra_linha}"


   
   estado = "FUNCIONAL" if random.random() < 0.8 else "MANUTENÇÃO"


#  ⬜⬜⬜⬛⬛⬛⬛⬛⬜⬜⬜
# ⬜⬜⬛⬜⬜⬜⬜⬜⬛⬜⬜
# ⬜⬛⬜⬜⬜⬜⬜⬜⬜⬛⬜
# ⬛⬜⬜⬛⬛⬜⬛⬛⬜⬜⬛
# ⬛⬜⬛⬛⬛⬜⬛⬛⬛⬜⬛
# ⬛⬜⬛⬛⬛⬜⬛⬛⬛⬜⬛
# ⬛⬜⬛⬛⬜⬜⬜⬛⬛⬜⬛
# ⬛⬜⬜⬜⬜⬛⬜⬜⬜⬜⬛
# ⬜⬛⬜⬜⬜⬜⬜⬜⬜⬛⬜
# ⬜⬜⬛⬜⬛⬜⬛⬜⬛⬜⬜
# ⬜⬜⬛⬜⬛⬜⬛⬜⬛⬜⬜
# ⬜⬜⬜⬛⬛⬛⬛⬛⬜⬜⬜
 
   agora = datetime.now()
   hora = agora.hour
   minuto = agora.minute


   
   if horario_de_pico(hora):
       qtd_pessoas = random.randint(1200, 1900)
   else:
       qtd_pessoas = random.randint(400, 1000)


   
   print("------------------------------------------------------------------")
   print(f"LINHA: {linha_nome}/Horário: {hora:02d}h{minuto:02d}m")
   print(f"ESTADO DO TREM: {estado}")
   print(f"QTD: {qtd_pessoas}/N.° do Trem: {codigo_trem}")
   print("------------------------------------------------------------------\n")


   
   time.sleep(10)
