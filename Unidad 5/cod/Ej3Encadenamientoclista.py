import random
from collections import defaultdict

class TablaHashEncadenada:

    def __init__(self, tamaño):
        self.tamaño = tamaño
        self.tabla = defaultdict(list)  # Usamos defaultdict para crear listas automáticamente
    
    # Función hash utilizando el método de plegado
    def metodo_plegado(self, clave):
        clave_str = str(clave)
        suma = 0
        # Tomar grupos de 2 dígitos y sumarlos
        for i in range(0, len(clave_str), 2):
            suma += int(clave_str[i:i+2])  # Tomamos de 2 en 2
        return suma % self.tamaño

    # Insertar una clave en la tabla hash
    def insertar(self, clave):
        indice = self.metodo_plegado(clave)  # Usamos el método de plegado para calcular el índice
        self.tabla[indice].append(clave)  # Insertamos la clave en la lista correspondiente

    # Generar claves aleatorias
    def generar_claves_aleatorias(self, cantidad, limite_superior=10000):
        return [random.randint(0, limite_superior) for _ in range(cantidad)]

    # Calcular las longitudes de las listas de sinónimos
    def longitudes_listas(self):
        longitudes = {indice: len(lista) for indice, lista in self.tabla.items()}
        return longitudes

    # Calcular el promedio de las longitudes
    def promedio_longitudes(self, longitudes):
        return sum(longitudes.values()) / len(longitudes)

    # Informar sobre las listas cuya longitud varía en hasta 3 unidades respecto al promedio
    def listas_en_rango(self, longitudes, promedio):
        en_rango = 0
        for longitud in longitudes.values():
            if abs(longitud - promedio) <= 3:
                en_rango += 1
        return en_rango

# Proceso principal
if __name__ == "__main__":
    tamaño_tabla = 200  # Tamaño de la tabla hash
    tabla_hash = TablaHashEncadenada(tamaño_tabla)

    # Generar 1000 claves aleatorias
    claves = tabla_hash.generar_claves_aleatorias(1000)

    # Insertar las claves en la tabla hash
    for clave in claves:
        tabla_hash.insertar(clave)

    # Obtener las longitudes de las listas de sinónimos
    longitudes = tabla_hash.longitudes_listas()

    # Calcular el promedio de las longitudes
    promedio = tabla_hash.promedio_longitudes(longitudes)

    # Informar las longitudes de cada lista
    print("Longitudes de las listas de sinónimos:")
    for indice, longitud in longitudes.items():
        print(f"Índice {indice}: {longitud} elementos")

    # Informar cuántas listas están dentro del rango de ±3 respecto al promedio
    listas_en_rango = tabla_hash.listas_en_rango(longitudes, promedio)
    print(f"\nCantidad de listas con longitud dentro de ±3 unidades respecto al promedio ({promedio:.2f}): {listas_en_rango}")
