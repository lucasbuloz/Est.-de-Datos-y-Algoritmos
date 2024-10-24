from classnodo import Nodo

class AVL:
    __raiz: Nodo
    
    def __init__(self):
        self.__raiz = None
        
    def getraiz(self):
        return self.__raiz
    
    def altura(self, xraiz):
        if xraiz == None:
            return 0
        return max(self.altura(xraiz.getizq()), self.altura(xraiz.getder())) + 1

    def obtener_factor_balance(self, xraiz):
        if xraiz == None:
            return 0
        return  self.altura(xraiz.getder()) - self.altura(xraiz.getizq())
    
    def rotacion_derecha(self, y):
        print(f"Realizando rotación derecha sobre el nodo {y.get_dato()}")
        x = y.getizq()
        T2 = x.getder()
        
        # Realizar rotación
        x.setder(y)
        x.setizq(T2)
        
        return x

    def rotacion_izquierda(self, x):
        print(f"Realizando rotación izquierda sobre el nodo {x.get_dato()}")
        y = x.getder()
        T2 = y.getizq()
        
        # Realizar rotación0
        y.setizq(x)
        y.setder(T2)
        
        return y
    
    def insertar(self, xraiz, valor):
        if xraiz is None:
            print(f"Insertando el valor {valor.get_dato()} en el árbol")
            return valor  # Retorna el nuevo nodo
        
        # Inserción normal de árbol binario de búsqueda
        if valor.get_dato() < xraiz.get_dato():
            print(f"Insertando {valor.get_dato()} en el subárbol izquierdo de {xraiz.get_dato()}")
            xraiz.setizq=self.insertar(xraiz.getizq(),valor)
        else:
            print(f"Insertando {valor.get_dato()} en el subárbol derecho de {xraiz.get_dato()}")
            xraiz.setder=self.insertar(xraiz.getder(), valor)


        # Verificar el factor de balance
        balance = self.obtener_factor_balance(xraiz)
        print(f"El factor de balance del nodo {xraiz.get_dato()} es {balance}")
         
         # Caso 1 - Rotación derecha
        if balance > 1 and valor.get_dato() < xraiz.getizq().get_dato():
            print(f"Balance descompensado en el nodo {xraiz.get_dato()} hacia la izquierda")
            return self.rotacion_derecha(xraiz)
        
        # Caso 2 - Rotación izquierda
        if balance < -1 and xraiz.getder() and valor.get_dato() > xraiz.getder().get_dato():
            print(f"Balance descompensado en el nodo {xraiz.get_dato()} hacia la derecha")
            return self.rotacion_izquierda(xraiz)
        
        # Caso 3 - Rotación izquierda-derecha
        if balance > 1 and xraiz.getizq() and valor.get_dato() > xraiz.getizq().get_dato():
            print(f"Balance descompensado en el nodo {xraiz.get_dato()} hacia la izquierda-derecha")
            xraiz.setizq(self.rotacion_izquierda(xraiz.getizq()))
            return self.rotacion_derecha(xraiz)
        
        # Caso 4 - Rotación derecha-izquierda
        if balance < -1 and xraiz.getder() and valor.get_dato() < xraiz.getder().get_dato():
            print(f"Balance descompensado en el nodo {xraiz.get_dato()} hacia la derecha-izquierda")
            xraiz.setder(self.rotacion_derecha(xraiz.getder()))
            return self.rotacion_izquierda(xraiz)
        
        if balance >=1 or balance <=-1:
            print ("---entra aqui---")
        
        
    def insertar_raiz(self, valor):
        # Inserta y actualiza la raíz del árbol
        self.__raiz = self.insertar(self.__raiz, valor)


if __name__ == "__main__":
    a = AVL()
    
"""    valores = [7, 5, 2, 4, 3, 8, 1, 6, 11, 10, 9]
    for valor in valores:
        nuevo = Nodo(valor)  # Crea un nuevo Nodo
        a.__raiz = a.insertar(a.getraiz(), nuevo)
"""

nuevo=Nodo(20)
a.insertar_raiz(nuevo)
nuevo=Nodo(10)
a.insertar_raiz(nuevo)
nuevo=Nodo(5)
a.insertar_raiz(nuevo)
nuevo=Nodo(2)
a.insertar_raiz(nuevo)
nuevo=Nodo(7)
a.insertar_raiz(nuevo)
nuevo=Nodo(23)

a.insertar_raiz(nuevo)
nuevo=Nodo(25)
a.insertar_raiz(nuevo)
"""nuevo=Nodo(6)
a.insertar_raiz(nuevo)
nuevo=Nodo(11)
a.insertar_raiz(nuevo)
nuevo=Nodo(10)
a.insertar_raiz(nuevo)
nuevo=Nodo(9)
a.insertar_raiz(nuevo)"""
