def buscar_pais(paises):
    """
    Busca países cuyo nombre contenga el texto ingresado
    por el usuario, sin distinguir mayúsculas y minúsculas.
    """

    print("\n-Buscar país por nombre-")

    termino = input("Ingresá el nombre o parte del nombre: ").strip()

    if not termino:
        print("[ERROR] Debés ingresar al menos un carácter.")
        return

    resultados = []

    for pais in paises:
        if termino.lower() in pais["nombre"].lower():
            resultados.append(pais)

    if not resultados:
        print(f"\nNo se encontraron países que coincidan con '{termino}'.")
        return

    print(f"\nSe encontraron {len(resultados)} resultado(s):")
    mostrar_paises(resultados)


def mostrar_paises(lista):
    """
    Muestra una lista de países en formato de tabla.
    """

    if not lista:
        print("\nNo hay países para mostrar.")
        return

    print(
        f"\n{'Nombre':<20}"
        f"{'Población':>15}"
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
