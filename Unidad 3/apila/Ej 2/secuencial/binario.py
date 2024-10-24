class binariosec:
    __cant:int
    __tope:int
    __lista:list
    
    def __init__(self, xcant):
        self.__cant=xcant
        self.__tope=-1
        self.__lista=[0]*xcant
        
    def vacio(self):
        return self.__tope==-1
        
    def insertar(self,x):
        if self.__tope<self.__cant-1:
            self.__tope+=1
            self.__lista[self.__tope]=x
            
    def suprimir(self):
        if not self.vacio():
            
            print (f"{self.__lista[self.__tope]}")
            self.__tope-=1

        
    def binario(self, num):
        while num>=2:
            resto=num%2
            self.insertar(resto)
            num=num//2
        self.insertar(num)
        
        print ("El numero en binario es: ")
        while not self.vacio():
            self.suprimir()
        
if __name__=="__main__":
    p=binariosec(4)
    
    
    
    numero=int(input("Ingrese numero entero para pasar a binario: "))
    p.binario(numero)
    