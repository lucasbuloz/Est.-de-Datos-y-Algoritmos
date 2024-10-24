import random
class hash:
    
    # Función hash usando el método de la división
    def metodo_division(self,clave, tamaño):
        return clave % tamaño
    
    """VERIFICAR porque extrae los digitos centrales y no los que más varian"""
    def metodo_extraccion(self,clave, tamaño):
        clave_str = str(clave)
        # Extracción de los 2 dígitos centrales
        mitad = len(clave_str) // 2
        extraido = clave_str[mitad-1:mitad+1]  # Dos dígitos centrales
        return int(extraido) % tamaño

    """VERIFICAR"""
    def metodo_plegado(self,clave, tamaño):
        clave_str = str(clave)
        suma = 0
        # Tomar grupos de 2 dígitos y sumarlos
        for i in range(0, len(clave_str), 2):
            suma += int(clave_str[i:i+2])  # Tomamos de 2 en 2
        return suma % tamaño
    
    def metodo_cuadrado_medio(self,clave, tamaño):
        cuadrado = clave ** 2
        cuadrado_str = str(cuadrado)
        # Extraemos los dígitos centrales del cuadrado
        mitad = len(cuadrado_str) // 2
        extraido = cuadrado_str[mitad-1:mitad+1]  # Dos dígitos centrales
        return int(extraido) % tamaño

    def metodo_clave_alfanumerica(self,clave, tamaño):
        suma_ascii = sum(ord(c) for c in clave)  # Convertimos cada carácter en su valor ASCII y sumamos
        return suma_ascii % tamaño
    
    
    # Insertar claves con manejo de colisiones usando prueba lineal
    def insertar(self,tabla, clave, estrategia):
        tamaño = len(tabla)
        indice = estrategia(clave, tamaño)
        secuencia = 0
        while tabla[indice] is not None:  # Si ya está ocupado, buscamos el siguiente
            secuencia += 1
            indice = (indice + 1) % tamaño  # Prueba lineal
        tabla[indice] = clave
        return secuencia  # Devolvemos la longitud de la secuencia de prueba

    # Buscar una clave con manejo de colisiones
    def buscar(self,tabla, clave):
        tamaño = len(tabla)
        indice = h.elegir(clave,tamaño)
        secuencia = 0
        while tabla[indice] is not None:  # Buscar en la tabla hash
            secuencia += 1
            if tabla[indice] == clave:
                return secuencia  # Devuelve la longitud de la secuencia de prueba
            else: indice = (indice + 1) % tamaño
        return -1  # Si no lo encontramos

    def elegir(self,clave, tamaño):
        print ("--Métodos de hash-- \n1. División \n2. Extracción \n3. Plegado \n4. Cuadrado medio \n5. Alfanumérica")
        op=int(input("Elegir metodo hash: "))
        if  op== 1:
            return h.metodo_division
        elif op == 2:
            return h.metodo_extraccion
        elif op == 3:
            return h.metodo_plegado
        elif op == 4:
            return h.metodo_cuadrado_medio
        elif op ==5:
            return h.metodo_clave_alfanumerica
        else:
            raise ValueError("Estrategia no válida")

    
    # Función para generar claves aleatorias
    def claves_aleat(self,n, lim=1000):
        return [random.randint(0,1000) for _ in range(n)]

    # Probar con un tamaño no primo
    def simu_tabla_hash(self,tamaño):
        tabla = [None] * tamaño
        claves = h.claves_aleat(1000)
        total_pruebas = 0
        estrategia=h.elegir(claves,tamaño)
        for clave in claves:
            total_pruebas += h.insertar(tabla, clave, estrategia)
        return total_pruebas / len(claves)  # Promedio de la longitud de la secuencia de prueba



if __name__ == "__main__":
    h=hash()
    
    tamaño_noprimo = 1000  
    tamaño_primo = 1009  # Es primo cercano a 1000

    #Se guardan resultados
    print("-----Con numero no primo-----")
    
    no_primo= h.simu_tabla_hash(tamaño_noprimo)
    print("-----Con numero primo-----")
    primo = h.simu_tabla_hash(tamaño_primo)
    
    print(f"Promedio de longitud de secuencia en tabla no prima: {no_primo}")
    print(f"Promedio de longitud de secuencia en tabla prima: {primo}")
