from nodoconcursor import Nodo

class ListaEncadenada:
    def __init__(self):
        self.__cabeza = None
        self.__cont = 0

    def vacia(self):
        return self.__cont == 0

    def insertar(self, dato, posicion):
        nuevoNodo = Nodo(dato)                                              #1
        if posicion >= 0 and posicion <= self.__cont:                      #1+1=2
            if posicion == 0:                                               #1
                nuevoNodo.set_siguiente(self.__cabeza)                      #1
                self.__cabeza = nuevoNodo                                   #1
            else:
                actual = self.__cabeza                                      #1
                for _ in range(posicion - 1):                               
                    actual = actual.get_siguiente()                          #1 x n  
                nuevoNodo.set_siguiente(actual.get_siguiente())                #1    
                actual.set_siguiente(nuevoNodo)                               #1      
                
            self.__cont += 1                                                    #1
        else:
            print("Índice fuera de rango")                                  #total= n+10

    def suprimir(self, posicion):
        if self.vacia():
            print("La lista se encuentra vacía")
            return None
        elif posicion < 0 or posicion >= self.__cont:
            print("Índice fuera de rango")
            return None

        if posicion == 0:
            elemento = self.__cabeza.get_dato()
            self.__cabeza = self.__cabeza.get_siguiente()
        else:
            anterior = self.__cabeza
            actual = anterior.get_siguiente()
            for _ in range(1, posicion):
                anterior = actual
                actual = actual.get_siguiente()

            elemento = actual.get_dato()
            anterior.set_siguiente(actual.get_siguiente())

        self.__cont -= 1
        return elemento
    
    def insertarPorContenido(self, dato):
        nuevoNodo = Nodo(dato)
        if self.vacia():
            # Si la lista está vacía, simplemente se agrega como cabeza
            self.__cabeza = nuevoNodo
        else:
            # Caso cuando hay que insertar en la posición correcta
            actual = self.__cabeza
            anterior = None
            # Recorrer hasta encontrar la posición correcta para insertar
            while actual is not None and actual.get_dato() < dato:
                anterior = actual
                actual = actual.get_siguiente()
            
            if anterior is None:
                # Insertar al principio si es el menor elemento
                nuevoNodo.set_siguiente(self.__cabeza)
                self.__cabeza = nuevoNodo
            else:
                # Insertar en la posición encontrada
                nuevoNodo.set_siguiente(actual)
                anterior.set_siguiente(nuevoNodo)
        
        self.__cont += 1
        print(f"Elemento insertado: {dato}")

    def suprimirPorContenido(self, dato):
        if self.vacia():
            print("Lista vacía")
            return False
        
        actual = self.__cabeza
        anterior = None
        
        # Buscar el nodo con el dato
        while actual is not None and actual.get_dato() != dato:
            anterior = actual
            actual = actual.get_siguiente()
        
        # Si el nodo fue encontrado
        if actual is not None:
            if anterior is None:
                # Si el nodo a eliminar es el primero
                self.__cabeza = actual.get_siguiente()
            else:
                # Si el nodo a eliminar no es el primero
                anterior.set_siguiente(actual.get_siguiente())
            
            self.__cont -= 1
            print(f"Elemento eliminado: {dato}")
            return True
        else:
            print(f"El elemento {dato} no se encuentra en la lista")
            return False
    
    def mostrar(self):
        actual = self.__cabeza
        while actual is not None:
            print(f"{actual.get_dato()}", end="->")
            actual = actual.get_siguiente()
        print("None")

    def buscar(self, dato):
        aux = self.__cabeza
        pos = 0
        while aux is not None:
            if aux.get_dato() == dato:
                return pos
            aux = aux.get_siguiente()
            pos += 1
        print(f"El elemento {dato} no se encuentra en la lista")
        return -1

    def primerElemento(self):
        if self.__cabeza is not None:
            return self.__cabeza.get_dato()
        else:
            print("La lista está vacía")
            return None

    def ultimoElemento(self):
        aux = self.__cabeza
        if aux is None:
            print("La lista está vacía")
            return None
        
        while aux.get_siguiente() is not None:
            aux = aux.get_siguiente()
        return aux.get_dato()
    
    def anterior(self, pos):
        if pos <= 0 or pos >= self.__cont:
            print("El índice ingresado no es válido o es el primero (no tiene anterior).")
            return None
        
        aux = self.__cabeza
        for _ in range(pos - 1):
            aux = aux.get_siguiente()
        
        return aux.get_dato()
    
    def siguiente(self, pos):
        if pos < 0 or pos >= self.__cont - 1:
            print("El índice ingresado no es válido o es el último (no tiene siguiente).")
            return None
        
        aux = self.__cabeza
        for _ in range(pos + 1):
            aux = aux.get_siguiente()
        
        return aux.get_dato()

    def recuperar(self, pos):
        if pos < 0 or pos >= self.__cont:
            print("Índice fuera de rango")
            return None

        aux = self.__cabeza
        for _ in range(pos):
            aux = aux.get_siguiente()
        
        return aux.get_dato()


if __name__ == "__main__":
    lista = ListaEncadenada()
    lista.insertar(10, 0)
    lista.insertar(5, 1)
    lista.insertar(15, 2)
    lista.insertar(7, 3)
    lista.mostrar()
    lista.insertar(15, 0)
    lista.insertar(7, 1)
    lista.mostrar()
    print(f"El primer elemento es: {lista.primerElemento()}")
    print(f"El último elemento es: {lista.ultimoElemento()}")
    print(f"Se elimina el {lista.suprimir(0)}")
    lista.mostrar()
    print(f"El elemento 10 está en la posición {lista.buscar(10)}")
    print(f"En la posición 2 se encuentra el elemento {lista.recuperar(2)}")
    print(f"El elemento siguiente a la posición 2 es el {lista.siguiente(2)}")
    print(f"El elemento anterior a la posición 1 es el {lista.anterior(1)}")
