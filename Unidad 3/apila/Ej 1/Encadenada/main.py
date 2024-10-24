from classlista import Lista

if __name__ == "__main__":
    lista = Lista()
    lista.insertar_al_inicio(10)
    lista.insertar_al_inicio(20)
    lista.insertar_al_final(30)
    lista.insertar_al_final(40)

    lista.mostrar()

    print(f"Elemento eliminado del inicio: {lista.suprimir_al_inicio()}")
    lista.mostrar()

    print(f"Elemento eliminado del final: {lista.suprimir_al_final()}")
    lista.mostrar()