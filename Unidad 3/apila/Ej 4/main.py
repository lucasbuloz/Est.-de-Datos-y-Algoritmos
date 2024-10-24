from classpila import Pila

def mostrarTorres(t1, t2, t3):
    print("Torre 1:", t1.mostrarContenido())
    print("Torre 2:", t2.mostrarContenido())
    print("Torre 3:", t3.mostrarContenido())
    print()

def esMovimientoValido(origen, destino):
    if origen.vacia():
        return False, "La torre de origen está vacía."
    if not destino.vacia() and origen.verTope() > destino.verTope():
        return False, "No puedes mover un disco más grande sobre uno más pequeño."
    return True, ""

def moverDisco(origen, destino):
    disco = origen.eliminar()
    destino.insertar(disco)

def main():
    torre1 = Pila()
    torre2 = Pila()
    torre3 = Pila()
    
    piezas = int(input("Ingrese el número de piezas: "))
    
    # Colocar las piezas en la torre 1
    for i in range(piezas, 0, -1):
        torre1.insertar(i)
    
    # Mostrar el estado inicial del juego
    mostrarTorres(torre1, torre2, torre3)
    
    movimientos = 0
    while not torre1.vacia() or not torre2.vacia():
        origen = int(input("Ingrese la torre de origen (1, 2 o 3): "))
        destino = int(input("Ingrese la torre de destino (1, 2 o 3): "))
        
        if origen == 1:
            torre_origen = torre1
        elif origen == 2:
            torre_origen = torre2
        elif origen == 3:
            torre_origen = torre3
        else:
            print("Torre de origen inválida.")
            continue
        
        if destino == 1:
            torre_destino = torre1
        elif destino == 2:
            torre_destino = torre2
        elif destino == 3:
            torre_destino = torre3
        else:
            print("Torre de destino inválida.")
            continue
        
        valido, mensaje = esMovimientoValido(torre_origen, torre_destino)
        if valido:
            moverDisco(torre_origen, torre_destino)
            movimientos += 1
        else:
            print(mensaje)
        
        mostrarTorres(torre1, torre2, torre3)
    
    print(f"Juego terminado en {movimientos} movimientos.")
    print(f"El número mínimo de movimientos posibles es {2**piezas - 1}.")

if __name__ == "__main__":
    main()