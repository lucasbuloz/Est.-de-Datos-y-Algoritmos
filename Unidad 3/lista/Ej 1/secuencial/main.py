from lista_secuencial import Lista
from seclu import secuencial
if __name__ == "__main__":
        t=int(input("ingrese tamaño: "))
        s=secuencial(t)
        b=True
        while b:
                print("1. insertar\n 2. Suprimir\n 3. Buscar\n")
                op=int(input("Ingrese opcion: "))
                
                if op==1:
                        dato=int(input("ingrese dato: "))
                        pos=int(input("Ingrese posicion: "))
                        s.insertar(dato, pos)
                        s.Recorrer()
               
                elif op ==2:
                        s.suprimir(pos)
                elif op ==3:
                        ele=int(input("Ingrese elemento a buscar"))
                        s.buscar(ele)
                
"""        l=Lista()
        b= True
        
        while b:
                print("Opciones: \n1. Insertar ")
                opcion=int(input("Opcion: "))
                if opcion==1:
                        dato=input("Introduce dato a ingresar en la lista: ")
                        l.insertar(dato)
                else:
                        print("Opcion invalida")"""