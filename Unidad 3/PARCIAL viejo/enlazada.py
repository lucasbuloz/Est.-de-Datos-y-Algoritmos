from nodo import Nodo

class Cola:
    cant: int
    pr: Nodo
    ult: Nodo

    def __init__(self):
        self.cant = 0
        self.pr = None
        self.ult = None

    def vacia(self):
        return self.cant == 0

    def insertar(self, x):
        nuevo = Nodo(x)
        if self.vacia():
            nuevo.setSiguiente(None)
            self.pr = nuevo
            self.ult = nuevo
        else:
            self.ult.setSiguiente(nuevo)
            self.ult = nuevo
            self.ult.setSiguiente(None)
        self.cant += 1

    def suprimir(self):
        if self.vacia():
            print("cola vacia")
            return 0
        else:
            x = self.pr.getDato()
            self.pr = self.pr.getSiguiente()
            self.cant -= 1
            return x

    def mostrar(self, primero):
        if primero != None:
            print(primero.getDato())
            self.mostrar(primero.getSiguiente())