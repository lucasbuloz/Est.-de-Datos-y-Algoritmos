import random
from collections import defaultdict

class TablaHashBuckets:

    def __init__(self, tamaño, tamaño_bucket):
        self.tamaño = tamaño  # Número total de buckets
        self.tamaño_bucket = tamaño_bucket  # Capacidad de cada bucket
        self.tabla = defaultdict(list)  # Cada índice de la tabla tiene una lista (Bucket)
    
    # Función hash utilizando el método de extracción
    def metodo_extraccion(self, clave):
        clave_str = str(clave)
        # Extraer los 2 últimos dígitos como método de extracción
        extraido = clave_str[-2:]  # Extraemos los últimos 2 dígitos
        return int(extraido) % self.tamaño

    # Insertar una clave en la tabla hash
    def insertar(self, clave):
        indice = self.metodo_extraccion(clave)  # Usamos el método de extracción para calcular el índice
        if len(self.tabla[indice]) < self.tamaño_bucket:  # Si el bucket no está lleno
            self.tabla[indice].append(clave)  # Insertamos la clave en el bucket correspondiente

    # Generar claves aleatorias
    def generar_claves_aleatorias(self, cantidad, limite_superior=10000):
        return [random.randint(0, limite_superior) for _ in range(cantidad)]

    # Contar buckets desbordados
    def contar_buckets_desbordados(self):
        desbordados = 0
        for bucket in self.tabla.values():
            if len(bucket) == self.tamaño_bucket:  # Si el bucket está completamente lleno
                desbordados += 1
        return desbordados

    # Contar buckets subocupados (menos de la tercera parte ocupada)
    def contar_buckets_subocupados(self):
        subocupados = 0
        limite_subocupado = self.tamaño_bucket // 3  # Un tercio de la capacidad del bucket
        for bucket in self.tabla.values():
            if len(bucket) < limite_subocupado:  # Si el bucket tiene menos de un tercio de ocupación
                subocupados += 1
        return subocupados

# Proceso principal
if __name__ == "__main__":
    tamaño_tabla = 100  # Número de buckets
    tamaño_bucket = 15  # Cada bucket puede almacenar hasta 10 claves
    tabla_hash = TablaHashBuckets(tamaño_tabla, tamaño_bucket)

    # Generar 1000 claves aleatorias
    claves = tabla_hash.generar_claves_aleatorias(1000)

    # Insertar las claves en la tabla hash
    for clave in claves:
        tabla_hash.insertar(clave)

    # Informar la cantidad de buckets desbordados
    desbordados = tabla_hash.contar_buckets_desbordados()
    print(f"Cantidad de buckets desbordados (completamente ocupados): {desbordados}")

    # Informar la cantidad de buckets subocupados
    subocupados = tabla_hash.contar_buckets_subocupados()
    print(f"Cantidad de buckets subocupados (menos de un tercio ocupados): {subocupados}")
