from classpila import Pila


def main():
    p = Pila()
    numero = int(input("Introduce un número decimal: "))
    num=numero
    while num >= 2:
        resto = num % 2
        p.insertar(resto)
        num = num // 2
    p.insertar(num)
    while not p.vacia():
            print(p.suprimir())
    

if __name__ == "__main__":
    main()
