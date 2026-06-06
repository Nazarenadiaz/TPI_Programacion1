from paises import agregar_pais, actualizar_pais
from busquedas import buscar_pais
from filtros import (
    filtrar_por_continente,
    filtrar_por_poblacion,
    filtrar_por_superficie
)
from ordenamientos import flujo_ordenar
from estadisticas import mostrar_estadisticas


def mostrar_menu():
    """
    Muestra el menu principal del sistema.
    """

    print("\n" + "=" * 45)
    print("      GESTIÓN DE DATOS DE PAÍSES")
    print("=" * 45)
    print("1. Agregar país")
    print("2. Buscar país por nombre")
    print("3. Filtrar por continente")
    print("4. Filtrar por rango de población")
    print("5. Filtrar por rango de superficie")
    print("6. Actualizar país")
    print("7. Ordenar países")
    print("8. Ver estadísticas")
    print("0. Salir")
    print("=" * 45)


def leer_opcion():
    """
    Pide al usuario que elija una opcion del menu.
    """

    return input("Elegí una opción: ").strip()


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
        mostrar_estadisticas(paises)

    elif opcion == "0":
        print("\nPrograma finalizado.")
        return paises, False

    else:
        print("ERROR: Opción inválida.")

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
