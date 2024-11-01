import numpy as np
import random


class DireccionamientoAbierto:
    __tamaño:int
    __claves:int
    __tabla:np.array
    __facCarga:float
    
    def __init__(self, claves, facCarga):
        self.__claves = claves
        self.__facCarga = facCarga
        self.__tamaño = int(self.__claves/self.__facCarga)
        self.__tabla = np.zeros(self.__tamaño)
        
    def division(self, clave):
        
        return int(clave % self.__tamaño)
  
    def generarclaves(self):
        return random.randint(0,1000) 
    
    
    def insertar(self, clave):
        indice= self.division(clave)
        contador=0
        
        if self.__tabla[indice]==0:
            self.__tabla[indice] = clave
            print(f"Se ingresó el {clave} en la posición {indice}")
        else:
            while self.__tabla[indice] != 0 and contador<self.__tamaño:
                contador+=1
                indice = (indice + 1) % self.__tamaño
            if self.__tabla[indice] ==0:
                self.__tabla[indice]=clave
                print(f"Se ingresó el {clave} en la posición {indice}, despues de {contador} intentos")
            else:
                raise Exception("Tabla llena")
    
    def buscar(self, clave):
        indice = self.division(clave)
        contador=0
        
        if self.__tabla[indice]==clave:
            print(f"Se encontró {clave} en la posición {indice}")
        else:
            while self.__tabla[indice] != clave and contador<self.__tamaño:
                contador+=1
                indice = (indice + 1) % self.__tamaño
            if self.__tabla[indice]==clave:
                print(f"Se encontró {clave} en la posición {indice}, despues de {contador} intentos")
            else:
                print(f"Tabla recorrida, no se encontró {clave}")
            return self.__tabla
    
    def mostrar(self):
        print(self.__tabla)
        
if __name__ == "__main__":
    dir = DireccionamientoAbierto(100,0.7 )
    
    dir.generarclaves()
    
    for _ in range(70):
        dir.insertar(dir.generarclaves())
    #dir.mostrar()
    busq=int(input("Ingrese clave a buscar: "))
    dir.buscar(busq)
    
    
    
    