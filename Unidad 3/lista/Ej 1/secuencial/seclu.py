import numpy as np

class secuencial:
    __tamaño: int
    __ult: int
    __arreglo:np.ndarray
    __cant: int
    
    def __init__(self, tamaño):
        self.__tamaño=tamaño
        self.__ult=-1
        self.__cant=0
        self.__arreglo=np.empty(self.__tamaño, dtype=int)
        
    def vacio(self):
        return self.__cant==0
    
    def lleno(self):
        return self.__cant==self.__tamaño
    
    def insertar(self, x, pos):
        if not self.lleno():
            if pos>=0 and pos<=self.__tamaño:
                i=self.__ult+1
                while i>pos:
                    self.__arreglo[i]=self.__arreglo[i-1]
                    i-=1
                self.__arreglo[i]=x
                self.__cant+=1
                self.__ult+=1
                print(f"Se insertó el elemento {self.__arreglo[i]}")
            else: print(f"La posicion no es valida. El tamaño de la lista es {self.__tamaño}")
        else: print("No hay mas espacio para insertar mas elementos")
        
    def insertarporcontenido(self, dato):
        if not self.lleno():
            if self.vacio():
                self.__ult+=1
                self.__arreglo[self.__ult]=dato
                self.__cant+=1
                print(f"El elemento insertado fue {dato}")
            else:
                i=0
                while i<=self.__ult and self.__arreglo[i]<dato:
                    i+=1
                for j in range(self.__ult+1, i-1, -1):
                    self.__arreglo[j] = self.__arreglo[j-1]
                self.__ult += 1
                self.__arreglo[i] = dato
                self.__cant += 1
                print(f"El elemento insertado fue {dato}")
                
        else: print("No hay mas espacio para insertar mas elementos")
        
    def Recorrer(self):
        i = 0
        if not self.vacio():
            while i <= self.__ult:
                print("El elemento {}, posicion {}".format(self.__arreglo[i], i))
                i += 1
        else:
            print("La lista esta vacia, no se muestra ningun elemento")
                
    def suprimir (self, pos):
        if not self.vacio():
            if pos>=0 and pos<=self.__ult:
                i=self.__ult
                eliminado=self.__arreglo[pos]
                while pos<i:
                    self.__arreglo[pos]=self.__arreglo[pos-1]
                    pos+=1
                self.__cant-=1
                self.__ult-=1
                print(f"Se eliminó el elemento {eliminado}")
            else: print("No se puede eliminar, posicion fuera de rango.")
        else: print("---Lista vacia---")

    def buscar(self, elemento):
        if not self.vacio():
            i=0
            while elemento !=self.__arreglo[i] and i<=self.__ult:
                i+=1
            if elemento==self.__arreglo[i]:
                print (f"El elemento {self.__arreglo[i]} se encontró en la posicion {i}")
            else: print(f"El elemento no se encontró en la lista")
            