from paises import mostrar_paises


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
