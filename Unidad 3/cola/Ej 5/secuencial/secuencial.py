import numpy as np

class colaSecuencial:
    __cant: int
    __pr: int
    __ult: int
    __max: int
    __items: object
    
    def __init__(self, max=5):
        self.__cant=0
        self.__pr=0
        self.__ult=0
        self.__max=max
        self.__items = np.empty(self.__max, dtype=object)
        
    def vacia(self):
        return self.__cant == 0
    
    def insertar(self, x):
        if self.__cant < self.__max:
            self.__items[self.__ult] = x
            self.__ult = (self.__ult + 1) % self.__max
            self.__cant += 1
            return(x)
        else:
            return(0)
        
    def suprimir(self):
        if self.vacia():
            print("cola vacia")
        else:
            x = self.__items[self.__pr]
            self.__pr = int((self.__pr + 1) % self.__max)
            self.__cant -= 1
            return x
        
"""    def mostrar(self):
        # Muestra todos los elementos de la cola en el orden correcto
        if self.vacia():
            print("Cola vacía")
        else:
            i = self.__pr
            for _ in range(self.__cant):
                print(self.__items[i], end=' ')
                i = (i + 1) % self.__max  # Mueve de forma circular
            print()"""
            
            
            
"""
if __name__ == "__main__":
    cola = colaSecuencial(5)
    cola.insertar(10)
    cola.insertar(20)
    cola.mostrar()
    print(cola.suprimir())
    cola.mostrar()"""

if __name__ =="__main__":
    c=colaSecuencial()
    b=True
    
    while b:
        print ("1. insertar\n 2. suprimir\n 3.mostrar cola ")
        op=int(input("Ingrese opcion: "))
        
        if op==1:
            elem=int(input("ingrese elemento: "))
            c.insertar(elem)
            #c.mostrar()
        elif op==2:
            c.suprimir()
            #c.mostrar()
        elif op== 3:
            while not c.vacia():
                print(c.suprimir())
            print("Cola terminada---")
            