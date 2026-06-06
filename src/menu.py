from paises import agregar_pais, actualizar_pais
from busquedas import buscar_pais
from filtros import (
    filtrar_por_continente,
    filtrar_por_poblacion,
    filtrar_por_superficie
)
from ordenamientos import flujo_ordenar


def mostrar_menu():
    """
    Muestra el menu principal del sistema.
    """

    print("\n" + "=" * 45)
    print("      GESTION DE DATOS DE PAISES")
    print("=" * 45)
    print("1. Agregar pais")
    print("2. Buscar pais por nombre")
    print("3. Filtrar por continente")
    print("4. Filtrar por rango de poblacion")
    print("5. Filtrar por rango de superficie")
    print("6. Actualizar pais")
    print("7. Ordenar paises")
    print("8. Ver estadisticas")
    print("0. Salir")
    print("=" * 45)


def leer_opcion():
    """
    Pide al usuario que elija una opcion del menu.
    """

    return input("Elegi una opcion: ").strip()


def ejecutar_opcion(opcion, paises):
    """
    Ejecuta la accion correspondiente a la opcion elegida.
    Devuelve la lista de paises (posiblemente actualizada)
    y un booleano que indica si se debe continuar el menu.
    """

    if opcion == "1":
        paises = agregar_pais(paises)

    elif opcion == "2":
        buscar_pais(paises)

    elif opcion == "3":
        filtrar_por_continente(paises)

    elif opcion == "4":
        filtrar_por_poblacion(paises)

    elif opcion == "5":
        filtrar_por_superficie(paises)

    elif opcion == "6":
        paises = actualizar_pais(paises)

    elif opcion == "7":
        flujo_ordenar(paises)

    elif opcion == "8":
        print("\nMODULO PENDIENTE, Ver estadisticas.")

    elif opcion == "0":
        print("\nPrograma finalizado.")
        return paises, False

    else:
        print("ERROR,Opcion invalida.")

    return paises, True


def ejecutar_menu(paises):
    """
    Ciclo principal del menu: muestra opciones, lee la
    eleccion del usuario y ejecuta la accion asociada
    hasta que el usuario decida salir.
    """

    continuar = True

    while continuar:
        mostrar_menu()
        opcion = leer_opcion()
        paises, continuar = ejecutar_opcion(opcion, paises)
