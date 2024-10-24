class Nodo:
    def __init__(self):
        self.__dato = None
        self.siguiente = -2  # Equivale a null

    def set_dato(self, x):
        self.__dato = x

    def get_dato(self):
        return self.__dato

    def set_siguiente(self, xp):
        self.siguiente = xp

    def get_siguiente(self):
        return self.siguiente

