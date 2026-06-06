"""
Estadisticas sobre la lista de paises.
Funciones puras que calculan totales y agrupaciones, mas
una funcion orquestadora que muestra los resultados en consola.
"""


def pais_mayor_poblacion(paises):
    """
    Devuelve el pais con mayor poblacion.
    Si la lista esta vacia devuelve None.
    """

    if not paises:
        return None

    mayor = paises[0]

    for pais in paises[1:]:
        if pais["poblacion"] > mayor["poblacion"]:
            mayor = pais

    return mayor


def pais_menor_poblacion(paises):
    """
    Devuelve el pais con menor poblacion.
    Si la lista esta vacia devuelve None.
    """

    if not paises:
        return None

    menor = paises[0]

    for pais in paises[1:]:
        if pais["poblacion"] < menor["poblacion"]:
            menor = pais

    return menor


def promedio_poblacion(paises):
    """
    Devuelve el promedio de poblacion como float.
    Si la lista esta vacia devuelve 0 para evitar division por cero.
    """

    if not paises:
        return 0

    total = 0

    for pais in paises:
        total = total + pais["poblacion"]

    return total / len(paises)


def promedio_superficie(paises):
    """
    Devuelve el promedio de superficie como float.
    Si la lista esta vacia devuelve 0 para evitar division por cero.
    """

    if not paises:
        return 0

    total = 0

    for pais in paises:
        total = total + pais["superficie"]

    return total / len(paises)


def cantidad_por_continente(paises):
    """
    Devuelve un diccionario con la cantidad de paises por
    continente. El diccionario se arma manualmente recorriendo
    la lista con un for.
    """

    conteo = {}

    for pais in paises:
        continente = pais["continente"]

        if continente in conteo:
            conteo[continente] = conteo[continente] + 1
        else:
            conteo[continente] = 1

    return conteo


def mostrar_estadisticas(paises):
    """
    Calcula y muestra todas las estadisticas en consola.
    Si la lista esta vacia, avisa al usuario y vuelve.
    """

    print("\n-Estadísticas-")

    if not paises:
        print("\nNo hay países cargados. No se pueden calcular estadísticas.")
        return

    mayor = pais_mayor_poblacion(paises)
    menor = pais_menor_poblacion(paises)
    prom_pob = promedio_poblacion(paises)
    prom_sup = promedio_superficie(paises)
    conteo = cantidad_por_continente(paises)

    print(f"\nTotal de países: {len(paises)}")

    print(
        f"\nPaís con mayor población: "
        f"{mayor['nombre']} ({mayor['poblacion']:,} habitantes)"
    )

    print(
        f"País con menor población: "
        f"{menor['nombre']} ({menor['poblacion']:,} habitantes)"
    )

    print(f"\nPromedio de población:  {prom_pob:,.2f} habitantes")
    print(f"Promedio de superficie: {prom_sup:,.2f} km²")

    print("\nCantidad de países por continente:")

    for continente in conteo:
        print(f"  {continente:<12} {conteo[continente]}")

    print()
