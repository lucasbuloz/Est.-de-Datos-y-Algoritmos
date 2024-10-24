from cola import Cola
import random


def main():

    c=Cola()
    fre=int (input("Frecuencia: "))
    tms=int (input("Tiempo maximo de simulacion: "))
    tac=int (input("Tiempo de atencion al cliente: "))
    
    acum=0
    reloj=0
    cant=0
    lista=[]
    SA=0
    variante=0
    
    while reloj<tms:
        a=random.random()
        if a<=(1/fre):
            c.insertar(reloj)
        if variante==0 and not c.vacia():
            dato=int(c.suprimir())
            acum +=dato
            cant+=1
            variante=tac
            lista.append(dato)
            
        else:
            SA+=1
        reloj +=1
        
    if cant>0:
        TE=acum/cant
    
    print(f"Sin atender {SA}")
    print(f"Tiempo de espera: {TE}")
    print(f"Tiempo acumulado: {acum}")
    print(f"Cantidad de trabajos: {cant}")
    print(f"lista de atendidos: {lista}")

if __name__ == "__main__":
    main()