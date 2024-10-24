from classnodo import Nodo

class Pila:
    __tope=None
    __cant:int
    
    def __init__(self):
        self.__tope=None
        self.__cant=0
        
    def vacio(self):
        return self.__tope is None
    
    def insertar(self, x):
        nuevo=Nodo(x)
        nuevo.cargar_sig(self.__tope)#apunto el nuevo al ultimo nodo, que era el marcado por tope
        self.__tope=nuevo #apunto el tope al nuevo
        self.__cant+=1    
        
            
    def suprimir(self):
        if self.vacio():
            print("pila vacia")
            return 0
        else: 
            #dato = self.__tope.obtener_dato()   #obtener el dato del ultimo elemento
            self.__tope = self.__tope.obtener_sig() #el siguiente del ultimo elemento es el tope
            self.__cant -= 1
            return dato
    
    def mostrar(self):
        if not self.vacio():
            actual=self.__tope
            while actual is not None:
                print (actual.obtener_dato(), end='->')
                actual=actual.obtener_sig()
            print("")
            
        else: print("Lista vacia")

if __name__=="__main__":
    #cant=int(input("Tamaño de lista: "))
    p=Pila()
    b=True
    while b:
        print("\n1.Insertar \n 2.Suprimir\n")
        op=int (input("Ingrese opcion: "))
        if op==1:
            dato=input("Introduce dato a ingresar en la lista: ")
            p.insertar(dato)
            p.mostrar()
        elif op==2:
            p.suprimir()
            p.mostrar()