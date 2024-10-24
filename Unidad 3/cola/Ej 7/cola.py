from nodo import Nodo
class Cola:
    def __init__(self):
        self.frente = None
        self.final = None

    def insertar(self, elemento):
        nuevo_nodo = Nodo(elemento)
        if self.final:
            self.final.getSiguiente(nuevo_nodo) 
        self.final = nuevo_nodo
        if not self.frente:
            self.frente = nuevo_nodo

    def suprimir(self):
        if not self.vacia():
            valor = self.frente.getDato()
            self.frente = self.frente.getSiguiente()
            if not self.frente:
                self.final = None
            return valor
        else:
            return None

    def vacia(self):
        return self.frente is None

    def Frente(self):
        if not self.vacia():
            return self.frente.getDato()
        else:
            return None
    def tamanio(self):
        actual = self.frente
        contador = 0
        while actual:
            contador += 1
            actual = actual.getSiguiente()
        return contador