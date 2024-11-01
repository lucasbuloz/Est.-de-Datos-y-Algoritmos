import numpy as np
import random

class Buckets:
    __tamaño:int
    __claves: int
    __tabla:np.ndarray
    __buckets:int
    
    def __init__(self, claves,buckets):
        self.__claves=claves
        self.__buckets=buckets
        
        self.__tamaño= int((self.__claves/self.__buckets)*1.2)
        self.__tabla=np.zeros((self.__tamaño,self.__buckets))
        
    def mostrar(self):
        tamano = int(self.__tamaño * 0.8)
        print("area primaria")
        for bucket in self.__tabla[:tamano]:
            print(bucket)
        print(f"area overflow ")
        for bucket in self.__tabla[tamano:]:
            print(bucket)
        
        
    def division(self, clave):
        return int(clave % self.__tamaño)
    
    
    def insertar(self, clave,c):
        indice=self.division(clave)
        tamaño=int (self.__tamaño*0.8)
        i=0
        
        if indice<tamaño:
            while i<self.__buckets:
                if self.__tabla[indice][i]==0:
                    self.__tabla[indice][i]=clave
                    c+=1
                    print(f"Se agregó la clave {clave} en la dirección {indice},   bucket {i} ")
                    return c
                i+=1
                
                
        indiceoverflow=tamaño
        while indiceoverflow<self.__tamaño:
            i=0
            while i<self.__buckets:
                if self.__tabla[indiceoverflow][i]==0:
                    self.__tabla[indiceoverflow][i]=clave
                    c+=1
                    print(f"Area primaria llena. Se agregó en overflow {clave} en la dirección {indiceoverflow},   bucket {i} ")
                    return c
                i+=1
            indiceoverflow+=1
        
        print("Tabla llena, no se pudo insertar la clave")
        return c
            
    def buscar(self,clave):
        indice=self.division(clave)
        tamaño=int (self.__tamaño*0.8)
        i=0
        indiceoverflow=tamaño
        
        while i<self.__buckets:
            if self.__tabla[indice][i]==clave:
                return print(f"clave {clave} encontrada en el area primaria indice {indice}")
            i+=1
        
        while indiceoverflow<self.__tamaño:
            i=0
            while i<self.__buckets:
                if self.__tabla[indiceoverflow][i]==clave:
                    return print(f"clave {clave} encontrada en el area overflow indice {indiceoverflow}")
                i+=1
            indiceoverflow+=1
        
        
            
    def generarclave(self):
        return random.randint(0,1000)
    
        
if __name__=="__main__":
    buck=Buckets(100, 4)
    
    c=0
    for _ in range(50):
       c= buck.insertar(buck.generarclave(),c)
   
    buck.mostrar()
    
    buscar = int(input("Clave a buscar: "))
    buck.buscar(buscar)