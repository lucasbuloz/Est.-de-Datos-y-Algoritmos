class Nodo:
    def __init__(self, dato=None):
        self.dato = dato
        self.sig = None

    def obtener_dato(self):
        return self.dato

    def obtener_sig(self):
        return self.sig

    def cargar_sig(self, sig):
        self.sig = sig




