class Nodo:
    __dato: int
    __izquierdo:None
    __derecho:None  
        
    def __init__(self, dato):
        self.__dato = dato
        self.__izquierdo = None
        self.__derecho = None

    def get_dato(self):
        return self.__dato
    
    def setdato(self, xdato):
        self.__dato=xdato
    
    def getizq(self):
        return self.__izquierdo
    
    def setizq(self, nodo):
        self.__izquierdo=nodo
    
    def getder(self):
        return self.__derecho
    
    def setder(self, nodo):
        self.__derecho=nodo
    