class Nodo:
    def __init__(self):
        self.dato = None
        self.siguiente = -2  # Equivale a null

    def set_dato(self, x):
        self.dato = x

    def get_dato(self):
        return self.dato

    def set_siguiente(self, xp):
        self.siguiente = xp

    def get_siguiente(self):
        return self.siguiente

