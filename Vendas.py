import time
import random



def lucro():
    while True:
        lucro = random.uniform(1000, 2500, 3900, 5200)
        print(f"o lucro do mês {mês:.2f}")
        print("foi de {lucro:.2f} ao todo")      
        mês = random.uniform(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)

        time.sleep(5)