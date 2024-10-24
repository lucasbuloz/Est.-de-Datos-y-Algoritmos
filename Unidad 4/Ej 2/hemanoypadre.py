from classnodo import Nodo

class ArbolBinarioBusqueda:
    __raiz:Nodo
    
    def __init__(self):
        self.__raiz = None

    def getraiz(self):
        return self.__raiz
    
    def insertar (self,xraiz, Nodo):
        if xraiz is None:
            self.__raiz=Nodo
        else:
            if int(Nodo.get_dato())<xraiz.get_dato():
                if xraiz.getizq()==None:
                    xraiz.setizq(Nodo)
                else: self.insertar(xraiz.getizq(), Nodo)
            elif int(Nodo.get_dato())>xraiz.get_dato():
                if xraiz.getder()==None:
                    xraiz.setder(Nodo)
                else: self.insertar(xraiz.getder(), Nodo)
                
    
    def buscar(self,nodo, valor):
        if self.__raiz == None:
            return None
        elif nodo.get_dato() == valor:
            return nodo
        elif valor < nodo.get_dato():
            return self.buscar(nodo.getizq(), valor)
        else:
            return self.buscar(nodo.getder(), valor)
        
        
    def eliminar(self, nodo, valor):
        if self.__raiz == None:
            return
        if valor < nodo.get_dato():
            nodo.setizq(self.eliminar(nodo.getizq(), valor))
        elif valor > nodo.get_dato():
            nodo.setder(self.eliminar(nodo.getder(), valor))
        else:
            #caso 1: simplemente elimino el nodo
            if nodo.getizq() == None and nodo.getder() == None:
                return None
            #caso 2: el nodo se elimina y su hijo ocupa el lugar vacio
            if nodo.getizq() == None:
                return nodo.getder()
            elif nodo.getder() == None:
                return nodo.getizq()
            #caso 3: se encuentra el sucesor inorden(el nodo mas pequeno en el subarbol derecho) o el predecesor inorden (el nodo mas grande en ek subarbol izquierdo) para reemplazar el nodo eliminado
            sucesor = self.encontrarMin(nodo.getder()) #encuentra el sucesor inorden
            nodo.set_dato(sucesor.get_dato()) #reemplaza el nodo eliminado por el sucesor inorden
            nodo.setder(self.eliminar(nodo.getder(), sucesor.get_dato())) #elimina el sucesor inorden

        return nodo
    
    def encontrarMin(self, nodo):
        actual = nodo
        while actual.getizq() != None:
            actual = actual.getizq()
        return actual
    
    def nivel(self, nodo, valor, nivel):
        if nodo == None:
            return -1 #si no encuentra el nodo
        if nodo.get_dato() == valor:
            return nivel
        elif valor < nodo.get_dato():
            return self.nivel(nodo.getizq(), valor, nivel+1)
        else:
            return self.nivel(nodo.getder(), valor, nivel +1)
        
    def hoja(self, valor):
        nodo = self.buscar(self.__raiz, valor)
        if nodo == None:
           return False
        return nodo.getizq() == None and nodo.getder() == None
    
    def hijo(self, padre, hijo):
        padre = self.buscar(self.__raiz, padre)
        if padre != None:
            if padre.getizq() != None and padre.getizq().get_dato() == hijo:
                return True
            elif padre.getder() != None and padre.getder().get_dato() == hijo:
                return True
        return False
    
    def padre(self, xraiz, hijo, padre=None):
        if xraiz is None:
            return None
        elif xraiz.get_dato() == hijo:
            return padre
        elif int(hijo) < int(xraiz.get_dato()):
            return self.padre(xraiz.getizq(), hijo, xraiz)
        else:
            return self.padre(xraiz.getder(), hijo, xraiz)
        
    def camino(self,valor):
        camino = []
        self.caminoAux(self.__raiz, valor, camino)
        return camino
    
    def caminoAux(self, xraiz, valor, camino):
        if xraiz == None:
            return False
        camino.append(xraiz.get_dato())
        if xraiz.get_dato() == valor:
            return True
        elif valor < xraiz.get_dato():
            return self.caminoAux(xraiz.getizq(), valor, camino)
        else:
            return self.caminoAux(xraiz.getder(), valor, camino)
        
    def altura(self, xraiz):
        if xraiz == None:
            return 0
        else:
            alturaIzquierda = self.altura(xraiz.getizq())
            alturaDerecha = self.altura(xraiz.getder())
            return max(alturaIzquierda, alturaDerecha) + 1
            
    def inorden(self,nodo):
        if nodo is not None:
            self.inorden(nodo.getizq())
            print(nodo.get_dato())
            self.inorden(nodo.getder())
    
    def preorden(self, nodo):
        if nodo != None:
            print(nodo.get_dato())
            self.preorden(nodo.getizq())
            self.preorden(nodo.getder())
            
    def postorden(self, nodo):
        if nodo != None:
            self.postorden(nodo.getizq())
            self.postorden(nodo.getder())
            print(nodo.get_dato())
    

if __name__=="__main__":
    arbol = ArbolBinarioBusqueda()
    valores = [20, 10, 30, 5, 15, 25, 35]
    for v in valores:
        arbol.insertar(arbol.getraiz(), Nodo(v))
    
    nuevo = Nodo(int(input("Ingrese un valor: ")))
    arbol.insertar(arbol.getraiz(), nuevo)

    # Busco el padre del nuevo nodo ingresado
    padre = arbol.padre(arbol.getraiz(), nuevo.get_dato())
    if padre is not None:
        #Verifico los hermanos
        if padre.getizq() != None and padre.getizq().get_dato() == nuevo.get_dato():  #Si el hijo por izquierda del padre es el nuevo, envío a su hermano de la derecha
            hermano = padre.getder()
        elif padre.getder() != None and padre.getder().get_dato() == nuevo.get_dato():    #Si el hijo por derecha del padre es el nuevo, envío a su hermano de la izquierda
            hermano = padre.getizq()  
        if hermano is not None:
            print(f"El hermano es {hermano.get_dato()}")
        else:
            print("El nodo no tiene hermano.")
    else:print("El nodo ingresado es la raíz, no tiene padre ni hermano.")
    
    arbol.inorden(arbol.getraiz())
    print ("FFIIINNNN")