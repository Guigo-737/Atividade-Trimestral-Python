import time
import random



def lucro():
    while True:
        lucro = random.uniform(1000, 5000)      

        
        mês = random.randint(1, 12)

        print("")
        print(f"O lucro do mês {mês} foi de R${lucro:.2f} ao todo.")

        time.sleep(5)