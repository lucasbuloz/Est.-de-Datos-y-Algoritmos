class Nodo:
    def __init__(self, dato = None):
        self.dato = dato
        self.siguiente = None
        
    def getDato(self):
        return self.dato
    
    def getSiguiente(self):
        return self.siguiente
    
    def setSiguiente(self, siguiente):
        self.siguiente = siguiente