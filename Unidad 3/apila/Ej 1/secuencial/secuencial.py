class Pila:
    def __init__(self, xcant=0):
        self.cant = xcant
        self.tope = -1
        self.lista = [0] * self.cant

    def vacia(self):
        return self.tope == -1

    def insertar(self, x):
        if self.tope < self.cant - 1:
            self.tope += 1
            self.lista[self.tope] = x
            return x
        else:
            return 0

    def suprimir(self):
        if self.vacia():
            print("Pila vacía")
            return 0
        else:
            x = self.lista[self.tope]
            self.tope -= 1
            return x

    def mostrar(self):
        if not self.vacia():
            for i in range(self.tope, -1, -1):
                print(self.lista[i])


if __name__ == "__main__":
    Pila()