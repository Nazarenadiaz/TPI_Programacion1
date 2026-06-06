from paises import mostrar_paises
from validaciones import (
    pedir_entero,
    pedir_texto_no_vacio,
    validar_rango
)


def filtrar_por_continente(paises):
    """
    Muestra los paises pertenecientes al continente ingresado.
    """

    print("\n-Filtrar por continente-")

    continente = pedir_texto_no_vacio("Ingresa el continente: ")

    if continente is None:
        return

    resultados = []

    for pais in paises:
        if pais["continente"].lower() == continente.lower():
            resultados.append(pais)

    if not resultados:
        print(f"\nNo se encontraron países en '{continente}'.")
        return

    print(f"\nPaíses en {continente} ({len(resultados)} resultado/s):")
    mostrar_paises(resultados)


def filtrar_por_poblacion(paises):
    """
    Filtra paises segun un rango de poblacion.
    """

    print("\n-Filtrar por rango de población-")

    minimo = pedir_entero("Población mínima: ")

    if minimo is None:
        return

    maximo = pedir_entero("Población máxima: ")

    if maximo is None:
        return

    if not validar_rango(minimo, maximo):
        return

    resultados = []

    for pais in paises:
        if minimo <= pais["poblacion"] <= maximo:
            resultados.append(pais)

    if not resultados:
        print(
            f"\nNo hay países con población entre "
            f"{minimo:,} y {maximo:,}."
        )
        return

    print(
        f"\nPaíses con población entre "
        f"{minimo:,} y {maximo:,}:"
    )

    mostrar_paises(resultados)


def filtrar_por_superficie(paises):
    """
    Filtra paises segun un rango de superficie.
    """

    print("\n-Filtrar por rango de superficie-")

    minimo = pedir_entero("Superficie mínima (km²): ")

    if minimo is None:
        return

    maximo = pedir_entero("Superficie máxima (km²): ")

    if maximo is None:
        return

    if not validar_rango(minimo, maximo):
        return

    resultados = []

    for pais in paises:
        if minimo <= pais["superficie"] <= maximo:
            resultados.append(pais)

    if not resultados:
        print(
            f"\nNo hay países con superficie entre "
            f"{minimo:,} y {maximo:,} km²."
        )
        return

    print(
        f"\nPaíses con superficie entre "
        f"{minimo:,} y {maximo:,} km²:"
    )

    mostrar_paises(resultados)
