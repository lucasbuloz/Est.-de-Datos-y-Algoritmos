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
            if Nodo.get_dato()<xraiz.get_dato():
                if xraiz.getizq()==None:
                    xraiz.setizq(Nodo)
                else: self.insertar(xraiz.getizq(), Nodo)
            elif Nodo.get_dato()>xraiz.get_dato():
                if xraiz.getder()==None:
                    xraiz.setder(Nodo)
                else: self.insertar(xraiz.getder(), Nodo)
                
    
    def buscar(self,xraiz, valor):
        if xraiz == None:
            return None
        elif xraiz.get_dato() == valor:
            return xraiz
        elif valor < xraiz.get_dato():
            return self.buscar(xraiz.getizq(), valor)
        else:
            return self.buscar(xraiz.getder(), valor)
        
        
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
            nodo.setdato(sucesor.get_dato()) #reemplaza el nodo eliminado por el sucesor inorden
            nodo.getder() == self.eliminar(nodo,sucesor.get_dato()) #elimina el sucesor inorden
        return nodo
    
    def encontrarMin(self, xraiz):
        actual = xraiz
        while actual.getizq() != None:
            actual = actual.getizq()
        return actual
    
    def nivel(self, xraiz, valor, nivel):
        if xraiz == None:
            return -1
        if xraiz.get_dato() == valor:
            return nivel
        elif valor < xraiz.get_dato():
            return self.nivel(xraiz.getizq(), valor, nivel+1)
        else:
            return self.nivel(xraiz.getder(), valor, nivel +1)
        
    def hoja(self, valor):
        nodo = self.buscar(self.__raiz, valor)
        if nodo == None:
           return False
        return nodo.getizq() == None and nodo.getder() == None
    
    def hijo(self, padre, hijo):
        xpadre = self.buscar(self.__raiz, padre)
        if xpadre != None:
            if xpadre.getizq() != None and xpadre.getizq().get_dato() == hijo:
                return True
            elif xpadre.getder() != None and xpadre.getder().get_dato() == hijo:
                return True
        return False
    
    def padre(self, xraiz, hijo, padre):
        if xraiz == None:
            return False
        elif xraiz.get_dato() == hijo:
            return padre.get_dato() if padre != None else None 
        elif hijo < xraiz.get_dato():
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
    

    
    def mostrarfrontera(self,nodo):
        if nodo!=None:
            self.mostrarfrontera(nodo.getizq())
            if nodo.grado()==0:
                print(nodo.get_dato())
            self.mostrarfrontera(nodo.getder())
            
    def hermanos(self,nodo):
        if nodo!=None:
            self.hermanos(nodo.getizq())
            if nodo.grado()==2:
                print(nodo.getizq().get_dato(),      nodo.getder().get_dato())
            self.hermanos(nodo.getder())
        
        
    def unhijo(self,nodo):
        if nodo!=None:
            self.unhijo(nodo.getizq())
            if nodo.grado()==1:
                if nodo.getizq()!=None:
                   print(nodo.getizq().get_dato())
                else:
                     print(nodo.getder().get_dato())
            self.unhijo(nodo.getder())
    
    
    
    def nodointerior(self,nodo):
        if nodo is not None:
            self.nodointerior(nodo.getizq())
            if nodo.grado()>0 and nodo !=self.__raiz:
                print(nodo.get_dato())
            self.nodointerior(nodo.getder())
        


if __name__=="__main__":
    arbol = ArbolBinarioBusqueda()
    nuevo=Nodo(20)
    arbol.insertar(arbol.getraiz(), nuevo)
    nuevo=Nodo(10)
    arbol.insertar(arbol.getraiz(), nuevo)
    nuevo=Nodo(15)
    arbol.insertar(arbol.getraiz(), nuevo)
    nuevo=Nodo(30)
    arbol.insertar(arbol.getraiz(), nuevo)
    nuevo=Nodo(25)
    arbol.insertar(arbol.getraiz(), nuevo)
    nuevo=Nodo(60)
    arbol.insertar(arbol.getraiz(), nuevo)
    nuevo=Nodo(9)
    arbol.insertar(arbol.getraiz(), nuevo)
    nuevo=Nodo(14)
    arbol.insertar(arbol.getraiz(), nuevo)
    
   
   
    arbol.inorden(arbol.getraiz())
    """print (f"El 9 es hoja: {arbol.hoja(9)}")
    print (f"El 20 es hoja: {arbol.hoja(20)}")
    
    
    print (f"El 9 es hijo de 10: {arbol.hijo(10, 9)}")
    print (f"El padre de 9 es: {arbol.padre(arbol.getraiz(),9, None)}")"""
    
    print ("--------")
    arbol.mostrarfrontera(arbol.getraiz())
    print ("--------")
    arbol.nodointerior(arbol.getraiz())
    print ("--------")
    arbol.hermanos(arbol.getraiz())
    print ("--------")
    arbol.unhijo(arbol.getraiz())
    