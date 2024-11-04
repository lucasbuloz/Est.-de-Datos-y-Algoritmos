import numpy as np
import random

class Buckets:
    __tamaño:int
    __claves: int
    __tabla:np.ndarray
    __buckets:int
    __areaprimaria:int
    __indiceoverflow:int
    __arregloaux:np.ndarray
    
    def __init__(self, claves,buckets):
        self.__claves=claves
        self.__buckets=buckets
        self.__tamaño= int((self.__claves/self.__buckets)*1.2)
        self.__areaprimaria=int(self.__tamaño*0.8)
        self.__tabla=np.zeros((self.__tamaño,self.__buckets))
        self.__indiceoverflow=self.__areaprimaria
        self.__arregloaux=np.zeros(self.__tamaño)
        
    def mostrar(self):
        
        print("area primaria")
        for bucket in self.__tabla[:self.__areaprimaria]:
            print(bucket)
        print(f"area overflow ")
        for bucket in self.__tabla[self.__areaprimaria:]:
            print(bucket)
        
        
    def division(self, clave):
        return int(clave % self.__areaprimaria)
    
    
    def insertar(self, clave):
        indice=self.division(clave)
        if self.__arregloaux[indice]<self.__buckets:
                    j=self.__arregloaux[indice]
                    self.__tabla[indice][j]=clave
                    self.__arregloaux[indice]+=1
                    print(f"Se agregó la clave {clave} en la dirección {indice},   bucket {i} ")
        else:
            j=self.__indiceoverflow
            while self.__arregloaux[j] >= self.__buckets:
                j+=1
            if j<self.__tamaño:
                self.__tabla[j][self.__arregloaux[j]] = clave
                print(f"Se agregó la clave {clave} en overflow en la dirección {j},   bucket {self.__arregloaux[j]} ")
            
            
    def buscar(self,clave):
        indice=self.division(clave)
        i=0
        
        while i<self.__buckets:
            if self.__tabla[indice][i]==clave:
                return print(f"clave {clave} encontrada en el area primaria indice {indice}")
            i+=1
        
        while self.__indiceoverflow<self.__tamaño:
            i=0
            while i<self.__buckets:
                if self.__tabla[self.__indiceoverflow][i]==clave:
                    return print(f"clave {clave} encontrada en el area overflow indice {self.__indiceoverflow}")
                i+=1
            self.__indiceoverflow+=1
        
        
            
    def generarclave(self):
        return random.randint(0,1000)
    
        
if __name__=="__main__":
    buck=Buckets(100, 4)
    
    for _ in range(50):
       buck.insertar(buck.generarclave())
   
    buck.mostrar()
    
    buscar = int(input("Clave a buscar: "))
    buck.buscar(buscar)