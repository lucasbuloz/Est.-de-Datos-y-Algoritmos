
class secuencial:
    __cant: int
    __tope:int
    __lista:list
    
    def __init__(self, xcant):
        self.__cant=xcant
        self.__tope=-1
        self.__lista=[0]*self.__cant
        
        
    def vacia(self):
        return self.__tope==-1
    
    def insertar(self, dato):
        if self.__tope<self.__cant-1:
            self.__tope+=1
            self.__lista[self.__tope]=dato
            print (f"Se agregó el elemento {dato}")
        else: 
            print("---lista completa---")

        
    def suprimir(self):
        if self.vacia():
            print("Lista vacia")
        else: 
            x=self.__lista[self.__tope]
            self.__tope-=1
            print (f"{x}")
    
    
    
    
if __name__=="__main__":
    cant=int(input("Tamaño de lista: "))
    p=secuencial(cant)
    b=True
    while b:
        print("1.Insertar \n 2.Suprimir\n 3. Mostrar pila")
        op=int (input("Ingrese opcion: "))
        if op==1:
            dato=input("Introduce dato a ingresar en la lista: ")
            p.insertar(dato)
        elif op==2:
            p.suprimir()
        elif op==3:
            while not p.vacia():
                p.suprimir()
            print("Se vació la lista\n")