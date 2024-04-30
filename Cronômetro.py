import time

def cronometro(tempo_segundos):
    for segundos_restantes in range(tempo_segundos, 0, -1):
        print(f"Tempo restante: {segundos_restantes} segundos")
        time.sleep(1)

    print("Tempo esgotado!")

# Exemplo de uso por 5 segundos
cronometro(5)
