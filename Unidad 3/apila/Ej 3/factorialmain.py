from classpila import Pila

def factorial(Pila, num):
    while num > 0:
        Pila.insertar(num)
        num -= 1
    resultado = 1
    while not Pila.vacia():
        valor = Pila.suprimir()
        resultado *= valor
    return resultado    

def main():
    b=True
    p=Pila()
    while b:
        n = int(input("Ingrese un número: "))
        resultado_factorial = factorial(p,n)
        print(f"El factorial de {n} es: {resultado_factorial}")

if __name__ == "__main__":
    main()
