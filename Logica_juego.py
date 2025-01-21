import random

# Función para crear una baraja estándar
def crear_baraja():
    valores = list(range(2, 15))  # 2-10, J (11), Q (12), K (13), A (14)
    palos = ['Corazones', 'Diamantes', 'Tréboles', 'Picas']
    return [(valor, palo) for valor in valores for palo in palos]

# Función para calcular el spread
def calcular_spread(carta1, carta2):
    return abs(carta1 - carta2) - 1

def repartir_cartas(baraja):
    return baraja.pop(), baraja.pop()

#funcion para salir


# Función principal del juego
def jugar_red_dog():
    baraja = crear_baraja()
    random.shuffle(baraja)

    print("¡Bienvenido a Red Dog!")
    saldo = 100  # Saldo inicial del jugador
    
    if saldo < 1:
        print("No tienes saldo suficiente para jugar")
        return

    while saldo > 0:
            print(f"Saldo: ${saldo}")
            apuesta = int(input("Ingresa tu apuesta: "))
            if apuesta > saldo:
                print("No puedes apostar más de lo que tienes.")
                continue
            if apuesta < 1:
                print("La apuesta minima es de $1")
                continue

            # Repartir dos cartas
            carta1, carta2 = repartir_cartas(baraja)
            print(f"Cartas iniciales: {carta1[0]} y {carta2[0]}")

            # Caso de empate automático
            if abs(carta1[0] - carta2[0]) == 1:
                print("Las cartas son consecutivas. Empate.")
                continue
            if carta1[0] == carta2[0]:
                print("¡Las cartas son iguales!")
                tercera_carta = baraja.pop()
                if tercera_carta[0] == carta1[0]:
                    print(f"¡Triple! Ganaste 11:1. Carta: {tercera_carta[0]}")
                    saldo += apuesta * 11
                else:
                    print(f"Desempate perdido. Carta: {tercera_carta[0]}")
                continue

            # Calcular el spread
            spread = calcular_spread(carta1[0], carta2[0])
            print(f"Spread: {spread}")

            # Ofrecer al jugador doblar la apuesta
            if apuesta > saldo/2:
                print("No tienes saldo para doblar tu apuesta")
            else: 
                decision = input("¿Quieres doblar tu apuesta? (sí/no): ").lower()
                if decision == "sí":
                    apuesta *= 2

            # Repartir la tercera carta
            tercera_carta = baraja.pop()
            print(f"Tercera carta: {tercera_carta[0]}")

            # Verificar si gana
            rango_min = min(carta1[0], carta2[0])
            rango_max = max(carta1[0], carta2[0])
            if rango_min < tercera_carta[0] < rango_max:
                print("¡Ganaste!")
                if spread == 1:
                    saldo += apuesta * 5
                elif spread == 2:
                    saldo += apuesta * 4
                elif spread == 3:
                    saldo += apuesta * 2
                else:
                    saldo += apuesta
            else:
                print("Perdiste.")
                saldo -= apuesta
                
            if saldo < 1:
                print("¡Te has quedado sin saldo! Fin del juego.")
                break
            
           
            print(f"\nSaldo: ${saldo}")
            opcion = input("¿Quieres seguir jugando o salir? (jugar/salir): ").lower()
    
            if opcion == "salir":
                break
            
    
    print("Gracias por jugar. ¡Hasta la próxima!")


   
jugar_red_dog()


