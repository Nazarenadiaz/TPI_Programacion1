from paises import mostrar_paises
from validaciones import pedir_texto_no_vacio


def buscar_pais(paises):
    """
    Busca paises cuyo nombre contenga el texto ingresado
    por el usuario, sin distinguir mayusculas y minusculas.
    """

    print("\n-Buscar país por nombre-")

    termino = pedir_texto_no_vacio("Ingresa el nombre o parte del nombre: ")

    if termino is None:
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
