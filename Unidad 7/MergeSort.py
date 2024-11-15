def mergesort(lista):
    if len(lista) <= 1:
        return lista


    # División de la lista en dos mitades
    mitad = len(lista) // 2
    lista1 = mergesort(lista[:mitad])
    lista2 = mergesort(lista[mitad:])


    # Fusión de lista1 y lista2 
    i, j = 0, 0
    resultado = []


    # Comparación de elementos entre lista1 y lista2
    while i < len(lista1) and j < len(lista2):
        if lista1[i] < lista2[j]:
            resultado.append(lista1[i])
            i += 1
        else:
            resultado.append(lista2[j])
            j += 1


    # Agregar los elementos restantes de lista1
    while i < len(lista1):
        resultado.append(lista1[i])
        i += 1


    # Agregar los elementos restantes de lista2
    while j < len(lista2):
        resultado.append(lista2[j])
        j += 1


    return resultado
if __name__ == '__main__':
    lista = [5,3,8,2,1]
    print(f"El arreglo original es: {lista}")
    print(f"El arreglo ordenado es: {mergesort(lista)}")
    
    