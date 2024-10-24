from cola import Cola
import random

def main():
    c=Cola()
    frecuencia = int(input("Ingrese la frecuencia de llegada de trabajos: "))
    tac = int(input("Ingrese el tiempo de atencion de la impresora: "))
    tms = int(input("Ingrese el tiempo maximo de simulacion: "))
    
    acum=0
    lista=[]
    cant=0
    SA=0
    reloj=0
    variante=0
    
    
    while reloj<=tms:
        a=random.random()
        if a<=(1/frecuencia):
            c.insertar(reloj)
        if variante==0 and not c.vacia():
            dato=int(c.suprimir())
            acum+=dato
            cant+=1
            lista.append(dato)
            variante =tac
        else:
            SA+=1
        reloj+=1
        
        if variante >0:
            variante-=1
            
    if cant>=0:
        te=acum/cant

    print(f"acum: {acum}")
    print(f"cant: {cant}")
    print(f"lista: {lista}")
    print(f"Sin atender: {SA}")
    print (f"Tiempo espera: {te}")
    
    


if __name__=="__main__":
    main()