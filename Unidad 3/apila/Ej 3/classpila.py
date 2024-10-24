from classnodo import Nodo
class Pila:
    __cabeza = None
    
    def _init_(self):
        self.__cabeza = None

    def vacia(self):
        return self.__cabeza is None

    def insertar(self, dato):
        nuevo_nodo = Nodo(dato)
        nuevo_nodo.cargar_sig(self.__cabeza)
        self.__cabeza = nuevo_nodo

    def suprimir(self):
        if self.vacia():
            print("La lista está vacía")
            return None
        else:
            dato = self.__cabeza.obtener_dato()
            self.__cabeza = self.__cabeza.obtener_sig()
            return dato

