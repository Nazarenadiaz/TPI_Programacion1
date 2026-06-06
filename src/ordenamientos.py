"""
Ordenamiento de paises por distintos criterios.
Usa sorted() y devuelve una lista nueva sin modificar
la original.
"""

from paises import mostrar_paises


def obtener_nombre(pais):
    """
    Devuelve el nombre del pais en minusculas.
    Se usa como clave para ordenar por nombre sin
    distinguir mayusculas y minusculas.
    """

    return pais["nombre"].lower()


def obtener_poblacion(pais):
    """
    Devuelve la poblacion del pais.
    Se usa como clave para ordenar por poblacion.
    """

    return pais["poblacion"]


def obtener_superficie(pais):
    """
    Devuelve la superficie del pais.
    Se usa como clave para ordenar por superficie.
    """

    return pais["superficie"]


def ordenar_paises(paises, criterio, ascendente):
    """
    Devuelve una nueva lista ordenada por el criterio dado.
    Criterios validos: 'nombre', 'poblacion', 'superficie'.
    El orden por nombre es insensible a mayusculas.
    Si el criterio no es valido, devuelve una copia de la lista.
    """

    if criterio == "nombre":
        clave = obtener_nombre

    elif criterio == "poblacion":
        clave = obtener_poblacion

    elif criterio == "superficie":
        clave = obtener_superficie

    else:
        return list(paises)

    return sorted(paises, key=clave, reverse=not ascendente)


def pedir_criterio_orden():
    """
    Muestra el submenu de criterio y devuelve el nombre del
    criterio elegido o None si la opcion es invalida.
    """

    print("\nOrdenar por:")
    print("1. Nombre")
    print("2. Poblacion")
    print("3. Superficie")

    opcion = input("Elegi un criterio: ").strip()

    if opcion == "1":
        return "nombre"

    if opcion == "2":
        return "poblacion"

    if opcion == "3":
        return "superficie"

    print("ERROR, Opcion de criterio invalida.")
    return None


def pedir_direccion():
    """
    Muestra el submenu de direccion y devuelve True si el
    usuario elige ascendente, False si elige descendente,
    o None si la opcion es invalida.
    """

    print("\nDireccion:")
    print("1. Ascendente")
    print("2. Descendente")

    opcion = input("Elegi una direccion: ").strip()

    if opcion == "1":
        return True

    if opcion == "2":
        return False

    print("ERROR, Direccion invalida.")
    return None


def flujo_ordenar(paises):
    """
    Orquesta el submenu de ordenamiento: pide criterio y
    direccion, ordena la lista y muestra el resultado.
    """

    print("\n-Ordenar paises-")

    if not paises:
        print("\nNo hay paises para ordenar.")
        return

    criterio = pedir_criterio_orden()

    if criterio is None:
        return

    ascendente = pedir_direccion()

    if ascendente is None:
        return

    resultado = ordenar_paises(paises, criterio, ascendente)

    direccion_txt = "ascendente" if ascendente else "descendente"

    print(
        f"\nPaises ordenados por {criterio} ({direccion_txt}):"
    )

    mostrar_paises(resultado)
