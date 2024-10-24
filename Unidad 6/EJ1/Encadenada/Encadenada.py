from classNodo import Nodo
import numpy as np

class encadenada:
    __arreglo:np.ndarray
    __cvertices:int
    
    def __init__(self, v):
        self.__cvertices=v
        self.__arreglo= [None for _ in range(self.__cvertices)]
        print(f"Se creó el grafo con {v} vertices\n de 0 a {v-1}\n  ")
        
    
    
    def mostrar(self):
        for i, nodo in enumerate(self.__arreglo):
            print(f" {i}:", end=" ")
            actual = nodo
            while actual!=None:
                print(actual, end=" -> ")
                actual = actual.getSig()
            print("None")  # Indica el final de la lista
        
    def insertar(self, origen, destino):
        if destino>self.__cvertices or origen>self.__cvertices:
            raise IndexError("Vertices incorrectos, estan fuera del rango")
        else:
            o=Nodo(origen) 
            d=Nodo(destino)
            
            d.setSig(self.__arreglo[origen])
            self.__arreglo[origen]= d
            
            o.setSig(self.__arreglo[destino])
            self.__arreglo[destino]= o
            
            print(f"Se agregó arista entre {origen} y {destino}")
        
        
    def adyacentes(self, nodo):
        if nodo>=self.__cvertices:
            raise IndexError("Nodo incorrecto, esta fuera del rango")
        else:
            actual=self.__arreglo[nodo]
            print(f"Los adyacentes de {nodo} son: " , end="")
            while actual!=None:
                print(actual, end="->")
                actual=actual.getSig()
    
    def grado(self, nodo):
        if nodo>=self.__cvertices:
            raise IndexError("Nodo incorrecto, esta fuera del rango")
        else:
            actual=self.__arreglo[nodo]
            contador=0
            while actual!=None:
                contador+=1
                actual=actual.getSig()
            print(f"\n El vertice {nodo} es de grado {contador}")
                
                
   #Camino comentado con los prints, para ver que pasa
    """def camino(self, inicio, fin): 
        #Pueden eliminarse los print, los uso como guías
        if inicio>=self.__cvertices or fin>=self.__cvertices:
            raise IndexError("Vertices incorrectos, estan fuera del rango")
        else:
            visitados = [False] * self.__cvertices
            pila = [(inicio, [inicio])]  # Pila con tuplas: (nodo_actual, camino_recorrido)

            while pila:
                nodo_actual, camino = pila.pop()
                print(f"Visitando nodo {nodo_actual} con camino {camino}")

                if nodo_actual == fin:
                    return camino

                if not visitados[nodo_actual]!= False: #Es lo mismo decir if visitados[vertice]==False, si ese vertice no está visitado(False), entra
                    visitados[nodo_actual] = True
                    actual = self.__arreglo[nodo_actual]
                    print(f"visitados: {visitados}")
                    print(f"actual: {actual}")

                    while actual!=None:
                        vecino = actual.getDato()
                        print(f"vecino: {vecino}")
                        if not visitados[vecino]!= False:
                            pila.append((vecino, camino + [vecino]))
                            print (pila)
                        actual = actual.getSig()

            return None  # Si no se encuentra un camino"""
        
    #Camino sin prints
    
    def camino(self, inicio, fin):
        if inicio>=self.__cvertices or fin>=self.__cvertices:
            raise IndexError("Vertices incorrectos, estan fuera del rango")
        else:
            visitados = [False] * self.__cvertices
            pila = [(inicio, [inicio])]  # Pila con tuplas: (nodo_actual, camino_recorrido)

            while pila:
                nodo_actual, camino = pila.pop()

                if nodo_actual == fin:
                    return camino

                if not visitados[nodo_actual]!= False: #Es lo mismo decir if visitados[vertice]==False, si ese vertice no está visitado(False), entra
                    visitados[nodo_actual] = True
                    actual = self.__arreglo[nodo_actual]

                    while actual!=None:
                        vecino = actual.getDato()
                        if not visitados[vecino]!= False:
                            pila.append((vecino, camino + [vecino]))
                        actual = actual.getSig()

            return (f"No hay camino entre los vertices {inicio} y {fin}")  # Si no se encuentra un camino
   
    
    
    def conexo(self):
        visitados = [False] * self.__cvertices
        pila=[0]
        
        while pila: #Es lo mismo decir while len(pila)>0, pregunta si está vacía o no
            vertice=pila.pop()
            if not visitados[vertice]!=False: #Es lo mismo decir if visitados[vertice]==False, si ese vertice no está visitado(False), entra
                visitados[vertice]=True
                actual = self.__arreglo[vertice]
                
                while actual!=None:
                    vecino = actual.getDato()
                    if not visitados[vecino]!=False:
                        pila.append(vecino)
                    actual = actual.getSig()
        return all(visitados)
       
            
        
        
    
if __name__== "__main__":
    e=encadenada(5)
    
    e.insertar(0,1)
    e.insertar(0,2)
    e.insertar(0,3)
    
    e.insertar(1,3)
    e.insertar(1,4)
    
    e.insertar(2,3)
    
    e.insertar(3,4)

    
    e.mostrar()
    
    e.adyacentes(4)
    
    e.grado(1)
    
    print(f" Camino final: {e.camino(1,4)}")
    
    if e.conexo()!=False:
        print ("El grafo es conexo")
    else:  print ("El grafo no es conexo")