import numpy as np
class ListaSecuencial:
    __tamanio: int
    __ultimo: int
    __arreglo: np.ndarray
    __cantidad: int
    
    def __init__(self, tamanio = 5):
        self.__tamanio = tamanio
        self.__ultimo = -1
        self.__cantidad = 0
        self.__arreglo = np.empty(self.__tamanio,dtype=int)
        
    def Vacio(self):
        return (self.__cantidad == 0)
    
    def Lleno(self):
        return self.__cantidad == self.__tamanio
    
    def Insertar(self, L,posicion):
        if not self.Lleno():
            if (posicion>=0) and (posicion<=self.__ultimo+1):
                i = self.__ultimo + 1
                while i > posicion:
                    self.__arreglo[i] = self.__arreglo[i-1]
                    i -= 1
                self.__arreglo[i] = L
                self.__cantidad += 1
                self.__ultimo += 1
            else:
                print("La posicion no es valida. La ultima posicion valida es {}".format(self.__ultimo+1))
        else:
            print("No hay mas espacio para insertar mas elementos")
            
    def InsertarPorContenido(self,dato):
        if not self.Lleno():
            if self.Vacio():
                self.__ultimo += 1
                self.__arreglo[self.__ultimo] = dato
                self.__cantidad += 1
                print(f"El elemento insertado fue {dato}")
            else:
                i = 0
                while i <= self.__ultimo and self.__arreglo[i] < dato:
                    i += 1
                for j in range(self.__ultimo+1, i-1, -1):
                    self.__arreglo[j] = self.__arreglo[j-1]
                self.__ultimo += 1
                self.__arreglo[i] = dato
                self.__cantidad += 1

    def Recorrer(self):
        i = 0
        if not self.Vacio():
            while i <= self.__ultimo:
                print("El elemento {}, posicion {}".format(self.__arreglo[i], i))
                i += 1
        else:
            print("La lista esta vacia, no se muestra ningun elemento")
            
    def SuprimirPorContenido(self,dato):
        print("Se ingresa al suprimir por contenido")
        i = 0
        if not self.Vacio():
            while i <= self.__ultimo and dato != self.__arreglo[i]:
                i += 1
                print("Estoy en el while i=",i)
            if i <= self.__ultimo:
                for j in range(i,self.__ultimo):
                    print("J en For vale",j)
                    self.__arreglo[j] = self.__arreglo[j+1]
            print("Se elimino el elemento ",dato,"de la posicion",i)
            self.__ultimo -= 1
            self.__cantidad -= 1
                
                
                
    def Suprimir(self,posicion):
        if not self.Vacio():
            if posicion>=0 and posicion<=self.__ultimo:
                i = self.__ultimo
                eliminado = self.__arreglo[posicion]
                while posicion<i:
                    self.__arreglo[posicion] = self.__arreglo[posicion+1]
                    posicion += 1
                self.__cantidad -= 1
                self.__ultimo -= 1
                print("Se elimino el elemento {}".format(eliminado))
            else:
                print("No se puede eliminar, posicion invalida")
        else:
            print("La lista esta vacia, no se puede eliminar ningun elemento")
            
    def Buscar(self,buscado):
        if not self.Vacio():
            i = 0
            while buscado != self.__arreglo[i] and i < self.__ultimo:
                i += 1
            if buscado == self.__arreglo[i]:
                print("El elemento {} esta en la posicion {}".format(buscado,i))
            else:
                print("El elemento {} no esta en la lista".format(buscado))
                
    def PrimerElemento(self):
        if not self.Vacio():
            return self.__arreglo[0]
        
    def UltimoElemento(self):
        if not self.Vacio():
            return self.__arreglo[self.__ultimo]
        
    def Siguiente(self,posicion):
        if not self.Vacio():
            if posicion == self.__ultimo:
                print("En esa posicion esta el ultimo elemento, no tiene siguiente")
            else:
                if posicion >= 0 and posicion < self.__ultimo:
                    print("El siguiente es: {}".format(self.__arreglo[posicion + 1])) 
            
    def Anterior(self,posicion):
        if not self.Vacio():
            if posicion == 0:
                print("En esa posicion se encuentra el primer elemento, no tiene anterior")
            else:
                if posicion > 0 and posicion <= self.__ultimo:
                    print("El anterior es: {}".format(self.__arreglo[posicion - 1])) 
        
        
if __name__ == "__main__":
    L = ListaSecuencial()
    print("INSERTA EN LA CABEZA")
    L.InsertarPorContenido(3)
    L.InsertarPorContenido(5)
    L.InsertarPorContenido(1)
    L.InsertarPorContenido(4)
    L.InsertarPorContenido(2)
    L.Recorrer()
    print("-------------------------")
    L.SuprimirPorContenido(4)
    print("-------------------------")
    L.Recorrer()
    #L.Insertar(1,0) 
    #L.Insertar(2,1)
    #L.Insertar(3,0)
    #L.Insertar(4,2)
    #L.Insertar(5,1)
    
    #3-5-1-4-2
    print("-----------------------------")
    #L.Suprimir(2)
    #L.Recorrer()
    print("------------------------")
    
    '''L.Buscar(4)
    L.Buscar(5)
    print("El primer elemento es {}.".format(L.PrimerElemento()))
    print("El ultimo elemento es {}.".format(L.UltimoElemento()))
    L.Siguiente(2)
    L.Anterior(3)'''
            