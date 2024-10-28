import numpy as np
from collections import deque


class Secuencial:
    __cvertices: int
    __matrizaydacencia: np.ndarray

    
    def __init__(self, vertices): 
        self.__cvertices=vertices    
        self.__matrizaydacencia=np.zeros((vertices, vertices),dtype=int)

        
    def mostrar(self):  
        print(self.__matrizaydacencia)
        
    def agregar_arista(self, origen, destino, peso=1 ):
        if origen >= self.__cvertices or destino >= self.__cvertices:
            raise ValueError("Los vértices deben estar dentro del rango de la matriz")
        self.__matrizaydacencia[origen][destino] = peso
        self.__matrizaydacencia[destino][origen] = peso

    def nodos_adyacentes(self, nodo):
        if nodo>=self.__cvertices:
            raise ValueError ("No existe ese vertice, prueba con uno menor")
        else:
            ady=[]
            rango=self.__cvertices
            for i in range(rango):
                if self.__matrizaydacencia[nodo][i]!=0:
                    ady.append(i)
            
            
            print(f"Los nodos adyacentes de {nodo}, son: " , end=""  ) 
            for j in range(len(ady)):
                print(f"{ady[j]}", end=" "  )
           
    def grado(self, nodo):
        if nodo<=self.__cvertices:
            print(f"\n El grado del nodo {nodo}, es: {np.sum(self.__matrizaydacencia[nodo])}")
        else:
            raise IndexError ("El vertice no pertenece al grafo")


    def camino(self, inicio, fin):
        visitados = [False] * self.__cvertices
        #print(f"Visitados: {visitados}")
        pila = [(inicio, [inicio])]
        while pila:
           nodoactual, camino= pila.pop()
           #print(f"Nodo actual {nodoactual} y camino {camino} ")
           if nodoactual== fin:
               return camino
           if not visitados[nodoactual]:
               visitados[nodoactual]=True
               for vecino in range(self.__cvertices):
                   if self.__matrizaydacencia[nodoactual][vecino]==1 and not visitados[vecino]:
                       pila.append((vecino, camino + [vecino]))
            
            
    """ def conexo(self):
        visitados=[False]*self.__cvertices
        pila=[0]
        print (visitados)
        print(pila)
        while pila:
            print( visitados)
            print(pila)
            vertice=pila.pop()
            if not visitados[vertice]:
                print(f"vertice {vertice}")
                visitados[vertice]=True
                print (visitados)
                for i in range(self.__cvertices):
                    print(f" i: {i}")
                    
                    if self.__matrizaydacencia[vertice][i]==1 and not visitados[i]:
                        pila.append(i)
                        print(pila)

        return all(visitados)"""
    
    def conexo(self):
        visitados=[False]*self.__cvertices
        pila=[0]
        while pila:
            vertice=pila.pop()
            if not visitados[vertice]:
                visitados[vertice]=True
                for i in range(self.__cvertices):
                    
                    if self.__matrizaydacencia[vertice][i]==1 and not visitados[i]:
                        pila.append(i)
        return all(visitados)
    def aciclico(self):
        visitados=[False]*self.__cvertices
        pila =[(0,-1)]
            
        while pila:
            vertice, padre=pila.pop()
            if not visitados[vertice]:
                visitados[vertice]=True
                for i in range(self.__cvertices):
                    if self.__matrizaydacencia[vertice][i]==1 and not visitados[vertice]:
                        pila.append(i, vertice)
                    elif self.__matrizaydacencia[vertice][i]==1 and i!=padre:
                        return False
        return True     
    
    def BEP(self, nodo):
        visitados=[False]*self.__cvertices
        pila=[nodo]
        while pila:
            vertice=pila.pop()
            if not visitados[vertice]:
                visitados[vertice]=True
                for i in range(self.__cvertices):
                    
                    if self.__matrizaydacencia[vertice][i]==1 and not visitados[i]:
                        pila.append(i)

        return all(visitados)
    
    def BEA(self, nodo):
        visitados=[False]*self.__cvertices
        pila=[nodo]
        while pila:
            vertice=pila.pop(0)
            if not visitados[vertice]:
                visitados[vertice]=True
                for i in range(self.__cvertices):
                    
                    if self.__matrizaydacencia[vertice][i]==1 and not visitados[i]:
                        pila.append(i)

        return all(visitados)
        
    
if __name__ == "__main__":
    s = Secuencial(5)
    
    
    s.agregar_arista(0,1)
    s.agregar_arista(0,2)
    s.agregar_arista(0,3)
    
    s.agregar_arista(1,3)
    s.agregar_arista(1,4)
    s.agregar_arista(2,3)
    s.agregar_arista(3,4)

   
    s.mostrar()
    s.nodos_adyacentes(1)
    
    s.grado(1)
    
    print (f"camino: {s.camino(0,4)}")
    print (f"camino: {s.camino(1,2)}")
    
    if s.conexo():
        print ("El grafo es conexo")
    else:  print ("El grafo no es conexo")
    
    if s.aciclico():
        print ("El grafo es acíclico")
    else:  print ("El grafo no es acíclico")
    
    a=int(input("Ingrese un vertice para empezar la busqueda en profundidad:"))
    if s.BEP( a)!=False:
        print ("Todos los vertices visitados")
    else:  print ("No todos los vertices fueron visitados")
    
    b=int(input("Ingrese un vertice para empezar la busqueda en amplitud:"))
    if s.BEA( b)!=False:
        print ("Todos los vertices visitados")
    else:  print ("No todos los vertices fueron visitados")