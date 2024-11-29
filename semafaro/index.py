import time
import random

def semaforo_inteligente():
    while True:
        # Simulamos a detecção de tráfego com um número aleatório (sensor)
        carros_detectados = random.randint(0, 100)  # Número de carros detectados (de 0 a 100)
        
        print(f"Carros detectados: {carros_detectados} carros")
        
        if carros_detectados > 50:
            # Se houver mais de 50 carros, o semáforo fica verde por mais tempo
            print("VERDE: Siga, muito tráfego")
            time.sleep(15)  # O semáforo fica verde por 10 segundos
        else:
            # Se houver menos de 50 carros, o semáforo fica verde por menos tempo
            print("VERDE: Siga, pouco tráfego")
            time.sleep(5)  # O semáforo fica verde por 5 segundos
        
        print("AMARELO: Atenção")
        time.sleep(3)  # O semáforo fica amarelo por 2 segundos
        
        print("VERMELHO: Pare")
        time.sleep(5)  # O semáforo fica vermelho por 5 segundos

# Chama a função para executar.
semaforo_inteligente()
