import numpy as np
import random

class Buckets:
    __tamaño:int
    __claves: int
    __areaprimaria:np.ndarray
    __overflow: int
    __buckets:int
    __areaoverflow:np.ndarray
    
    def __init__(self, claves,buckets, over):
        self.__claves=claves
        self.__buckets=buckets
        
        self.__tamaño= int(self.__claves/self.__buckets)
        self.__overflow=int((over/100)*(self.__tamaño))
        
        self.__areaprimaria=np.zeros((self.__tamaño,self.__buckets))
        self.__areaoverflow=np.zeros((self.__overflow,self.__buckets))
        
    def mostrar(self):
        print(f"Area primaria \n {self.__areaprimaria}\n")
        print(f"Area de Overflow \n {self.__areaoverflow}\n")
        
        
    def division(self, clave):
        return int(clave % self.__tamaño)
    
    
    def insertar(self, clave, bucket):
        indice=self.division(clave)
        contador=0
        if self.__areaprimaria[indice][bucket] == 0:
            self.__areaprimaria[indice][bucket]=clave
            print (f"Se agregó la clave {clave} en la dirección {indice}, en la posicion {bucket} del bucket")
        else:
            while self.__areaprimaria[indice][bucket] != 0 and bucket<3:
                bucket+=1
                if bucket>3:
                    raise Exception("Bucket lleno")
        
        
            
    def generarclave(self):
        return random.randint(0,1000)
    
    def generarbucket(self):
        return random.randint(0,3)
        
if __name__=="__main__":
    buck=Buckets(100, 4,20)
    
    for _ in range(120):
        buck.insertar(buck.generarclave(),buck.generarbucket())
   
    buck.mostrar()