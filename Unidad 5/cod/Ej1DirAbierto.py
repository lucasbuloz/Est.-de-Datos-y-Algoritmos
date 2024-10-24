import random
class hash:
    
    # Función hash usando el método de la división
    def hash_division(self,clave, tamaño):
        return clave % tamaño

    # Insertar claves con manejo de colisiones usando prueba lineal
    def insertar(self,tabla, clave):
        tamaño = len(tabla)
        indice = h.hash_division(clave, tamaño)
        secuencia = 0
        while tabla[indice] is not None:  # Si ya está ocupado, buscamos el siguiente
            secuencia += 1
            if secuencia>=tamaño:
                raise Exception("Tabla llena")
            indice = (indice + 1) % tamaño  # Prueba lineal
        tabla[indice] = clave
        return secuencia  # Devolvemos la longitud de la secuencia de prueba

    # Buscar una clave con manejo de colisiones
    def buscar(self,tabla, clave):
        tamaño = len(tabla)
        indice = h.hash_division(clave, tamaño)
        secuencia = 0
        while tabla[indice] is not None:  # Buscar en la tabla hash
            secuencia += 1
            if tabla[indice] == clave:
                return secuencia  # Devuelve la longitud de la secuencia de prueba
            else: indice = (indice + 1) % tamaño
        return -1  # Si no lo encontramos

    # Función para generar claves aleatorias
    def claves_aleat(self,n, lim=1000):
        return [random.randint(0,1000) for _ in range(n)]

    # Probar con un tamaño no primo
    def simu_tabla_hash(self,tamaño):
        tabla = [None] * tamaño
        claves = h.claves_aleat(1000)
        total_pruebas = 0
        for clave in claves:
            total_pruebas += h.insertar(tabla, clave)
        return total_pruebas / len(claves)  # Promedio de la longitud de la secuencia de prueba



if __name__ == "__main__":
    h=hash()
    
    tamaño_noprimo = 1000  
    tamaño_primo = 1009  # Es primo cercano a 1000

    #Se guardan resultados
    no_primo= h.simu_tabla_hash(tamaño_noprimo)
    primo = h.simu_tabla_hash(tamaño_primo)
    
    print(f"Promedio de longitud de secuencia en tabla no prima: {no_primo}")
    print(f"Promedio de longitud de secuencia en tabla prima: {primo}")



"""
Explicación:

hash_function: Calcula el índice para una clave dada usando el módulo.

insert_key: Inserta una clave en la tabla hash, manejando colisiones con prueba lineal. Devuelve la longitud de la secuencia de prueba (es decir, cuántos intentos se hicieron hasta encontrar un espacio).

search_key: Busca una clave en la tabla, devolviendo la longitud de la secuencia.

generate_random_keys: Genera 1000 claves numéricas aleatorias.

hash_table_simulation: Simula la inserción de las claves en la tabla y calcula el promedio de la longitud de las secuencias de prueba.


Análisis Comparativo:
En general, cuando el tamaño de la tabla es un número primo, tiende a haber menos colisiones y una menor longitud de secuencias de prueba, ya que los números primos reducen las posibilidades de colisiones sistemáticas.
Usar un tamaño no primo aumenta la probabilidad de que varias claves diferentes mapeen al mismo índice, causando más colisiones y más intentos de prueba.



"""