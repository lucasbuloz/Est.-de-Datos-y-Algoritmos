from enlazada import Cola
import random
def main():
    c=Cola()
    frecuencia=10 #int(input("Ingrese frecuencia de llegada de cliente: ")) #10 minutos
    tms=120 #int(input("Ingrese el tiempo maximo de simulación: ")) #Tiempo maximo de simulación, 5 horas
    tac=15 #int(input("Ingrese el tiempo de atencion: ")) #15 minutos


    reloj=0
    acum=0
    cant=0
    sinatender=0
    lista=[]
    ipv=0
    
    while reloj <= tms:
        aleatorio=random.random()
        if aleatorio<=(1/frecuencia):
            c.insertar(reloj)
            
            
        if ipv ==0 and not c.vacia():
            dato= int(c.suprimir())
            acum+=dato
            cant+=1
            ipv=tac
            lista.append(dato)
        else:
            sinatender+=1
            
        reloj+=1
        
        if ipv>0:
            ipv-=1
            
    if cant > 0:
        tiempoespera = acum / cant
    else:
        tiempoespera = 0
    print(f"trabajos sin atender: {sinatender}")
    print(f"tiempo de espera: {tiempoespera}")
    print(f"cantidad de trabajos atendidos: {cant}")
    print(f"lista de tiempos de espera: {lista}")
    print(f"tiempo: {acum}")
if __name__ == "__main__":
    main()