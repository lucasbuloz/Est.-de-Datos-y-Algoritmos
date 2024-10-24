import numpy as np

class secola:
    __pr:int
    __ult:int
    __cant:int
    __max: int
    __arreglo: object
    
    def __init__(self, max=5):
        self.__pr=0
        self.__ult=0
        self.__cant=0
        self.__max=max
        self.__arreglo=np.empty(self.__max, dtype=object)
        
    def vacio(self):
        return self.__cant==0
    
    def insertar(self, x):
        if self.__cant<self.__max:
            self.__arreglo[self.__ult]=x
            self.__ult= (self.__ult+1)%self.__max
            self.__cant+=1
            
        else:print("Cola llena")
        
    def lleno(self):
        return not self.__cant <self.__max
    
    def suprimir(self):
        if not self.vacio():
            x=self.__arreglo[self.__pr]
            self.__pr=(self.__pr+1)%self.__max
            self.__cant-=1
        else:print("Cola vacia")
        
    def mostrar(self):
        if self.vacio():
            print("Cola vacia")
        else: 
            i=self.__pr
            for _ in range(self.__cant):
                print(self.__arreglo[i], end='')
                i= (i+1)%self.__max
            print()
        
if __name__=="__main__":
    c=secola()
    b=True
    
    while b:
        op=int (input("\nInserte: ")) 
        
        if op==1:
            x=int(input("Ingrese a insertar: "))
            c.insertar(x) 
            c.mostrar()
        if op==2:
            c.suprimir()
            c.mostrar()
