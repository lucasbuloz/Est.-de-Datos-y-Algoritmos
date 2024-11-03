class hash:    
    def hash_extraccion(self, clave):
        clavestr = str(clave)
        ultimos = int(clavestr[-2]) + int(clavestr[-1]) if len(clavestr) >=2 else int(clavestr)
        return ultimos % self.size

    def hash_plegado(self, clave):
        # Método de Plegado (suma partes de 2 dígitos)
        clavestr = str(clave)
        acum= 0
        i = 0
        while i < len(clavestr):
            if i + 1 < len(clavestr):
                part = int(clavestr[i]) * 10 + int(clavestr[i + 1])  # Agrupa en pares
            else:
                part = int(clavestr[i])  # Si queda un solo dígito al final
            acum+= part
            i += 2
        return acum% self.size

    def hash_cuadrado_medio(self, key):
        # Método del Cuadrado Medio
        square = key ** 2
        square_str = str(square)
        mid_index = len(square_str) // 2
        # Toma dos dígitos centrales
        if len(square_str) % 2 == 0:
            extracted = int(square_str[mid_index - 1]) * 10 + int(square_str[mid_index])
        else:
            extracted = int(square_str[mid_index])
        return extracted % self.size

    def hash_alfanumerico(self, key):
        # Función hash para claves alfanuméricas (suma valores ASCII)
        total = 0
        for char in key:
            total += ord(char)  # Suma los valores ASCII de los caracteres
        return total % self.size