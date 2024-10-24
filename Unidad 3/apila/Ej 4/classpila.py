from classnodo import Nodo

class Pila:
    def __init__(self):
        self.__cabeza = None
        
    def vacia(self):
        return self.__cabeza == None
    
    def insertar(self, dato):
        nuevo = Nodo(dato)
        nuevo.setSiguiente(self.__cabeza)
        self.__cabeza = nuevo
        
    def eliminar(self):
        if self.vacia():
            raise Exception("La pila esta vacia")
        else:
            dato = self.__cabeza.getDato()
            self.__cabeza = self.__cabeza.getSiguiente()
            return dato
        
    def mostrarContenido(self):
        contenido = []
        actual = self.__cabeza
        while actual is not None:
            contenido.append(actual.getDato())
            actual = actual.getSiguiente()
        return contenido[::-1]  # invertir para mostrar de base a tope
    
    def verTope(self):
        if self.vacia():
            raise Exception("La pila está vacía")
        return self.__cabeza.getDato()  # Devuelve el dato del nodo en la cima