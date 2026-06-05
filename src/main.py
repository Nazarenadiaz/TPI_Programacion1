from csv_utils import cargar_paises, agregar_pais
from busquedas import buscar_pais
from filtros import (
    filtrar_por_continente,
    filtrar_por_poblacion,
    filtrar_por_superficie
)


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


def main():
    """
    Carga los datos y controla el menu principal.
    """

    print("Cargando datos...")

    paises = cargar_paises()

    if not paises:
        print(
            "ADVERTENCIA: No se cargaron paises. "
            "Verifica el archivo paises.csv."
        )

    while True:

        mostrar_menu()

        opcion = input("Elegi una opcion: ").strip()

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
            print("\nMODULO PENDIENTE,Actualizar pais.")

        elif opcion == "7":
            print("\nMODULO PENDIENTE, Ordenar paises.")

        elif opcion == "8":
            print("\nMODULO PENDIENTE, Ver estadisticas.")

        elif opcion == "0":
            print("\nPrograma finalizado.")
            break

        else:
            print("ERROR,Opcion invalida.")


if __name__ == "__main__":
    main()
