from nodo import Nodo

class encola:
    __cant:int
    __pr:Nodo
    __ult: Nodo
    

    def __init__(self):
        self.__cant=0
        self.__pr=None
        self.__ult=None
    
    def vacio(self):
        return self.__cant==0
    
    def insertar(self, x):
        nuevo=Nodo(x)
        if self.vacio():
            nuevo.setSiguiente(None)
            self.__pr=nuevo
            self.__ult=nuevo
        else:
            self.__ult.setSiguiente(nuevo)
            self.__ult=nuevo
            self.__ult.setSiguiente(None)
        self.__cant+=1
        
    def suprimir(self):
        if self.vacio():
            print("Cola vacia")
        else: 
            x=self.__pr.getDato()
            self.__pr=self.__pr.getSiguiente()
            self.__cant-=1
        
    def mostrar(self):
        actual=self.__pr
        while actual is not None:
            print(actual.getDato())
            actual =actual.getSiguiente()
        print()
        
if __name__=="__main__":
    c=encola()
    b=True 
    
    while b:
        print ("1. insertar\n 2. suprimir \n")
        op=int(input("Ingrese opcion: "))
        
        if op==1:
            ele=int (input("Ingrese elemento: "))
            c.insertar(ele)
            c.mostrar()
        elif op==2:
            c.suprimir()
            c.mostrar()