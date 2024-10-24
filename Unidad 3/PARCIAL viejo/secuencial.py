import numpy as np

class parcial:
    __ult: int
    __cant:int
    __pr:int
    __max=int
    __arreglo:object
    
    def __init__(self):
        self.__ult=0
        self.__pr=0
        self.__max=0
        self.__cant=0
        self.__arreglo=np.empty(self.__max,dtype=object)
        
    def vacio(self):
        return self.__cant==0
    
    def insertar(self, x):
        if self.__cant<self.__max:
            self.__arreglo[self.__ult]=x
            self.__ult= (self.__ult + 1) % self.__max
            self.__cant+=1
        else:
            print("Cola completa")
            
    def suprimir(self):
        if self.vacio():
            print("COla vacia")
        else:
            x=self.__arreglo[self.__pr]
            self.__pr=(self.__pr+1)%self.__max
            self.__cant -=1
            print (f"Se eliminó{x}")
    
    def mostrar(self):
        if self.vacio():
            print("COla vacia")
        else:
            i=self.__pr
            for _ in range(self.__cant):
                print(self.__arreglo[i], end='')
                i=(i+1)% self.__max 
            print ()