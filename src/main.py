from csv_manager import cargar_paises
from menu import ejecutar_menu


def main():
    """
    Carga los datos y delega el control al menu principal.
    """

    print("Cargando datos...")

    paises = cargar_paises()

    if not paises:
        print(
            "ADVERTENCIA: No se cargaron países. "
            "Verificá el archivo paises.csv."
        )

    ejecutar_menu(paises)


if __name__ == "__main__":
    main()
