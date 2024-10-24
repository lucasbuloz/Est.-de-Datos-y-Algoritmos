from cola import Cola
import random 

def main():
    c = Cola()
    frecuencia = int(input("Ingrese la frecuencia de llegada de trabajos: "))
    tac = int(input("Ingrese el tiempo de atencion de la impresora: "))
    tms = int(input("Ingrese el tiempo maximo de simulacion: "))
    
    cajero =0
    reloj = 0
    acum = 0
    cant = 0
    sinAtender = 0
    lista = []
    
    while reloj < tms:
        aleatorio = random.random()
        if aleatorio <= (1/frecuencia):
            c.insertar(reloj)
        if cajero == 0 and not c.vacia():
            dato = int(c.suprimir())
            acum += dato
            cant += 1
            cajero = tac
            lista.append(dato)
        else:
            sinAtender +=1
        reloj += 1
        if cajero > 0:
            cajero -= 1
            
    if cant>0:
        tiempoEspera = acum/cant
    
    print(f"trabajos sin atender: {sinAtender}")
    print(f"tiempo de espera: {tiempoEspera}")
    print(f"cantidad de trabajos: {cant}")
    print(f"lista de tiempos de espera: {lista}")
    print(f"tiempo: {acum}")
    
if __name__ == "__main__":
    main()