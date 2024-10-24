import numpy as np
import random
from classNodo import Nodo

        
class Encadenamiento:
    __tamaño:int
    __tabla:list
    __cabeza:None
    
    def __init__(self, clave):
        self.__claves=clave
        self.__tamaño=self.__claves
        self.__tabla= [[] for _ in range(self.__tamaño)]
        

    def mostrar(self):
        print (self.__tabla)
        
        
    def division(self, clave):
        return int(clave % self.__tamaño)
        
        
    def insertar(self, clave):
        indice=self.division(clave)
        self.__tabla[indice].append(clave)
        print(f"Se ingreso {clave} en {indice}")
        
        
        
    def buscar(self, clave):
        indice= self.division(clave)
        i=0
        try:
            while self.__tabla[indice][i]!= clave:
                i+=1
            if self.__tabla[indice][i]== clave:
                print(f"Se encontró {clave} en la posicion {indice} de la tabla y posicion {i} de esa lista")
        except IndexError:
                print(f"---No se encontró la clave {clave}---")
        
        
        
    def generarclaves(self):
        return random.randint(0,500)
        
        
        
if __name__=="__main__":
    e=Encadenamiento(50)
    
    for _ in range(100):
        e.insertar(e.generarclaves())
    e.mostrar()
    
    busq=int(input("Ingrese la clave a buscar: "))
    e.buscar(busq)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    """contador=0
        print(len(self.__tabla[indice]))
        if len(self.__tabla[indice])>2:
            contador+=1
            indice=(indice+1)%self.__tamaño
            self.__tabla[indice].append(clave)
        else:
            self.__tabla[indice].append(clave)
        print(f"Se ingresó {clave} en {indice}")
        """
        #Que pasa con la cantidad de claves por listas?
        #Hay entradas con 4 claves y entradas con 0, tiene que ser equitativa cada lista de entradas?
        #En la teoria sale [ cant de claves / cant de entradas ]
        #En este caso teniendo 100 claves y 50 entradas , debería tener 2 claves por entrada