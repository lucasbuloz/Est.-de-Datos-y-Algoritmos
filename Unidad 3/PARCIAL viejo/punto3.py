class punto:
    __cab=None
    __cont:int
    
    def __init__(self):
        self.__cab=None
        self.__cont=0
        
        
    def buscar(self, dato):
        aux=self.__cab
        pos=0
        while aux is not None:
            if aux.getdato()==dato:
                return pos
            aux=aux.getsiguiente()
            pos+=1
        print("El elemento no está en la lista")
        