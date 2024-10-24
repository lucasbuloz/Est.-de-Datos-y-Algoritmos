from classnodo import Nodo

class Lista:
    __cabeza : int
    
    def __init__(self):
        self.__cabeza = None

    def vacia(self):
        return self.__cabeza is None

    def insertar_al_final(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.vacia():
            self.__cabeza = nuevo_nodo
        else:
            actual = self.__cabeza
            while actual.obtener_sig() is not None:
                actual = actual.obtener_sig()
            actual.cargar_sig(nuevo_nodo)


    def suprimir_al_inicio(self):
        if self.vacia():
            print("La lista está vacía")
            return None
        else:
            dato = self.__cabeza.obtener_dato()
            self.__cabeza = self.__cabeza.obtener_sig()
            return dato


    def mostrar(self):
        if self.vacia():
            print("La lista está vacía")
        else:
            actual = self.__cabeza
            while actual is not None:
                print(actual.obtener_dato(), end=" -> ")
                actual = actual.obtener_sig()
            
    """def suprimir_al_final(self):
        if self.vacia():
            print("La lista está vacía")
            return None
        elif self.__cabeza.obtener_sig() is None:  # Si hay un solo elemento
            dato = self.__cabeza.obtener_dato()
            self.__cabeza = None
            return dato
        else:
            actual = self.__cabeza
            while actual.obtener_sig().obtener_sig() is not None:
                actual = actual.obtener_sig()
            dato = actual.obtener_sig().obtener_dato()
            actual.cargar_sig(None)
            return dato"""
            
            
            
    """ def insertar_al_inicio(self, dato):
        nuevo_nodo = Nodo(dato)
        nuevo_nodo.cargar_sig(self.__cabeza)
        self.__cabeza = nuevo_nodo"""