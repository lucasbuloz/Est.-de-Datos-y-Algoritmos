class Nodo:
    __dato:None
    __sig:None
    
    def __init__(self, dato):
        self.__dato=dato
        self.__sig=None

    def setSig(self, sig):
        self.__sig=sig
        
    def getSig(self):
        return self.__sig
    
    def setDato(self, dato):
        self.__dato=dato
        
    def getDato(self):
        return self.__dato
    
    def __str__(self):
        return str(self.__dato)