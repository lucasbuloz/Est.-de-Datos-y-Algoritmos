from nodoconcursor import Nodo

class Lista:
    def __init__(self, xmax):
        self.max = xmax
        self.cab = 0
        self.cantidad = 0
        self.espacio = [Nodo() for _ in range(xmax)]
        self.disponible = 0

    def vacia(self):
        return self.cantidad == 0

    def get_disponible(self):
        for i in range(self.max):
            if self.espacio[i].get_siguiente() == -2:
                self.disponible = i
                return True
        self.disponible = -2
        return False

    def free_disponible(self, disp):
        if 0 <= disp < self.max:
            self.espacio[disp].set_siguiente(-2)
            return True
        return False

    def insertar_por_posicion(self, x, xp):
        if self.cantidad < self.max and 0 <= xp <= self.cantidad and self.get_disponible():
            self.espacio[self.disponible].set_dato(x)
            ant = self.cab
            cabeza = self.cab
            i = 0

            while i < xp:
                i += 1
                ant = cabeza
                cabeza = self.espacio[cabeza].get_siguiente()

            if cabeza == self.cab:  # Insertar al inicio
                if self.cantidad == 0:
                    self.espacio[self.cab].set_siguiente(-1)
                else:
                    self.espacio[self.disponible].set_siguiente(self.cab)
                self.cab = self.disponible
            elif cabeza == -1:  # Insertar al final
                self.espacio[self.disponible].set_siguiente(-1)
                self.espacio[ant].set_siguiente(self.disponible)
            else:
                self.espacio[self.disponible].set_siguiente(cabeza)
                self.espacio[ant].set_siguiente(self.disponible)

            self.cantidad += 1
            return True
        else:
            print("Espacio lleno o posición incorrecta.")
            return False

    def insertar_por_contenido(self, x):
        if self.cantidad < self.max and self.get_disponible():
            ant = self.cab
            cabeza = self.cab
            i = 0
            self.espacio[self.disponible].set_dato(x)

            while i < self.cantidad and cabeza != -1 and self.espacio[cabeza].get_dato() < x:
                i += 1
                ant = cabeza
                cabeza = self.espacio[cabeza].get_siguiente()

            if cabeza == self.cab:  # Insertar al inicio
                if self.cantidad == 0:
                    self.espacio[self.cab].set_siguiente(-1)
                else:
                    self.espacio[self.disponible].set_siguiente(self.cab)
                self.cab = self.disponible
            elif cabeza == -1:  # Insertar al final
                self.espacio[self.disponible].set_siguiente(-1)
                self.espacio[ant].set_siguiente(self.disponible)
            else:
                self.espacio[self.disponible].set_siguiente(cabeza)
                self.espacio[ant].set_siguiente(self.disponible)

            self.cantidad += 1
            return True
        else:
            print("Espacio lleno.")
            return False

    def suprimir(self, xp):
        if self.cantidad != 0 and 0 <= xp < self.cantidad:
            ant = self.cab
            cabeza = self.cab
            i = 0

            while i < xp and cabeza != -1:
                i += 1
                ant = cabeza
                cabeza = self.espacio[cabeza].get_siguiente()

            if cabeza == self.cab:
                if self.cantidad == 1:
                    self.cab = 0
                else:
                    self.cab = self.espacio[ant].get_siguiente()
            else:
                self.espacio[ant].set_siguiente(self.espacio[cabeza].get_siguiente())

            x = self.espacio[cabeza].get_dato()
            self.disponible = cabeza
            self.free_disponible(self.disponible)
            self.cantidad -= 1
            return x
        else:
            print("Lista vacía o posición incorrecta.")
            return None

    def recuperar(self, xp):
        if self.cantidad != 0 and 0 <= xp < self.cantidad:
            cabeza = self.cab
            i = 0

            while cabeza != -1 and i < xp:
                i += 1
                cabeza = self.espacio[cabeza].get_siguiente()

            return self.espacio[cabeza].get_dato()
        else:
            print("Lista vacía o posición incorrecta.")
            return None

    def recorrer(self):
        if self.cantidad != 0:
            cabeza = self.cab
            print("Lista:", end=" ")
            while cabeza != -1:
                print(self.espacio[cabeza].get_dato(), end=" ")
                cabeza = self.espacio[cabeza].get_siguiente()
            print()
        else:
            print("Lista vacía.")
