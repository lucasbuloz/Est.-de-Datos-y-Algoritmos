from classnodo import Nodo

class Pila:  
    def __init__(self):
        self.__tope = None  
        self.__cant = 0  # Contador de elementos en la pila

    def vacia(self):
        return self.__tope is None

    def insertar(self, valor):
        nuevo_nodo = Nodo(valor)  # Creamos un nuevo nodo con el valor dado
        nuevo_nodo.cargar_sig(self.__tope)  # El siguiente del nuevo nodo es el actual __tope de la pila
        self.__tope = nuevo_nodo  # Ahora, el nuevo nodo es el __tope de la pila
        self.__cant += 1

    def suprimir(self):
        if self.vacia():
            print("La pila está vacía")
            return None
        else:
            valor = self.__tope.obtener_dato()  # Obtenemos el valor del nodo en el __tope
            self.__tope = self.__tope.obtener_sig()  # El __tope ahora pasa a ser el siguiente nodo
            self.__cant -= 1
            return valor

    