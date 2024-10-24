import numpy as np
import random

class Buckets:
    __tamaño:int
    __claves: int
    __areaprimaria:list
    __overflow: int
    __buckets:int
    __areaoverflow:list
    
    def __init__(self, claves,buckets, over):
        self.__claves=claves
        self.__buckets=buckets
        
        self.__tamaño= int(self.__claves/self.__buckets)
        self.__overflow=int((over/100)*(self.__tamaño))
        
        self.__areaprimaria=[[] for _ in range(self.__tamaño)]
        self.__areaoverflow=[[] for _ in range(self.__overflow)]
        
    def mostrar(self):
        print(f"\n Area primaria ")
        for i, bucket in enumerate(self.__areaprimaria):
            print(f"Bucket {i}: {bucket}")
        
        print(f"\n Area de Overflow ")
        for i, bucket in enumerate(self.__areaoverflow):
            print(f"Bucket {i}: {bucket}")
        
        
    def division(self, clave):
        return int(clave % self.__tamaño)
    
    def divisionoverflow(self, clave):
        return int(clave % self.__overflow)
    
    
    def insertar(self, clave):
        indice=self.division(clave)
        
        if len(self.__areaprimaria[indice])<self.__buckets:
            self.__areaprimaria[indice].append(clave)
            print (f"Se agregó la clave {clave} en la dirección {indice}, del area primaria")
        else:
            print(f"Bucket {indice} lleno, agrego en overflow")
            i=self.divisionoverflow(clave)
            if len(self.__areaoverflow[i])<self.__buckets:
                self.__areaoverflow[i].append(clave)
                print (f"Se agregó la clave {clave} en la dirección {indice}, del overflow")
    

    def buscar(self, clave):
        indice=self.division(clave)
        i=0
        try:
            while self.__areaprimaria[indice][i]!= clave:
                i+=1
            if self.__areaprimaria[indice][i]== clave:
                print(f"Se encontró {clave} en el bucket {indice} del area primaria y posicion {i} del bucket")
        except:
                print(f"---No se encontró la clave {clave} en el área primaria---")
                o=self.divisionoverflow(clave)
                j=0
                try:
                    while self.__areaoverflow[o][j]!= clave:
                        j+=1
                    if self.__areaoverflow[o][j]== clave: 
                        print(f"Se encontró {clave} en el bucket {o} del area overflow y posicion {j} del bucket")
                except:
                    print(f"---No se encontró la clave {clave} en ningún área---")
                    
            
        
            
    def generarclave(self):
        return random.randint(0,1000)
    
    
        
if __name__=="__main__":
    buck=Buckets(100, 4,20)
    
    for _ in range(70):
       buck.insertar(buck.generarclave())
   
    buck.mostrar()
    
    b=int(input("Ingrese la clave a buscar: "))
    buck.buscar(b)