import time
import random

def simular_lucro(qtd_meses=12):
    for mes in range(1, qtd_meses + 1):
        valor_lucro = random.uniform(-1000, 5000)
        print("———————————————————————————————————————————————————")
        print(f"O lucro do mês {mes} foi de R${valor_lucro:.2f} ao todo.")
        print("———————————————————————————————————————————————————")
        time.sleep(5)
