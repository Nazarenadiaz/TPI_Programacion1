def buscar_pais(paises):
    """
    Busca paises cuyo nombre contenga el texto ingresado
    por el usuario, sin distinguir mayusculas y minusculas.
    """

    print("\n-Buscar pais por nombre-")

    termino = input("Ingrese el nombre o parte del nombre: ").strip()

    if not termino:
        print("ERROR, Debes ingresar al menos un caracter.")
        return

    resultados = []

    for pais in paises:
        if termino.lower() in pais["nombre"].lower():
            resultados.append(pais)

    if not resultados:
        print(f"\nNo se encontraron paises que coincidan con '{termino}'.")
        return

    print(f"\nSe encontraron {len(resultados)} resultado(s):")
    mostrar_paises(resultados)


def mostrar_paises(lista):
    """
    Muestra una lista de paises en formato de tabla.
    """

    if not lista:
        print("\nNo hay paises para mostrar.")
        return

    print(
        f"\n{'Nombre':<20}"
        f"{'Poblacion':>15}"
        f"{'Superficie (km²)':>18}"
        f"{'Continente':<15}"
    )

    print("-" * 72)

    for pais in lista:
        print(
            f"{pais['nombre']:<20}"
            f"{pais['poblacion']:>15,}"
            f"{pais['superficie']:>18,}"
            f"{pais['continente']:<15}"
        )

    print()
