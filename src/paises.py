"""
Operaciones de dominio sobre la lista de paises:
mostrar, agregar y actualizar.
"""

from csv_manager import guardar_paises
from validaciones import (
    pedir_texto_no_vacio,
    pedir_entero_no_negativo
)


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


def agregar_pais(paises):
    """
    Solicita un nuevo pais, valida los datos y lo agrega
    a la lista si es correcto.
    """

    print("\n-Agregar nuevo pais-")

    nombre = pedir_texto_no_vacio("Nombre del pais: ")

    if nombre is None:
        return paises

    for pais in paises:
        if pais["nombre"].lower() == nombre.lower():
            print(f"ERROR, Ya existe un pais llamado '{nombre}'.")
            return paises

    poblacion = pedir_entero_no_negativo("Poblacion: ")

    if poblacion is None:
        return paises

    superficie = pedir_entero_no_negativo("Superficie en km²: ")

    if superficie is None:
        return paises

    if superficie == 0:
        print("ERROR, La superficie debe ser mayor a cero.")
        return paises

    continente = pedir_texto_no_vacio("Continente: ")

    if continente is None:
        return paises

    nuevo_pais = {
        "nombre": nombre,
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": continente
    }

    paises.append(nuevo_pais)

    guardar_paises(paises)

    print(f"OK, Pais '{nombre}' agregado correctamente.")

    return paises


def actualizar_pais(paises):
    """
    Busca un pais por nombre exacto (insensible a mayusculas)
    y permite actualizar su poblacion y superficie.
    """

    print("\n-Actualizar pais-")

    nombre = pedir_texto_no_vacio("Nombre del pais a actualizar: ")

    if nombre is None:
        return paises

    pais_encontrado = None

    for pais in paises:
        if pais["nombre"].lower() == nombre.lower():
            pais_encontrado = pais
            break

    if pais_encontrado is None:
        print(f"ERROR, No se encontro un pais llamado '{nombre}'.")
        return paises

    print(
        f"\nDatos actuales de '{pais_encontrado['nombre']}':"
    )
    print(f"  Poblacion:  {pais_encontrado['poblacion']:,}")
    print(f"  Superficie: {pais_encontrado['superficie']:,} km²")
    print()

    nueva_poblacion = pedir_entero_no_negativo("Nueva poblacion: ")

    if nueva_poblacion is None:
        return paises

    nueva_superficie = pedir_entero_no_negativo("Nueva superficie en km²: ")

    if nueva_superficie is None:
        return paises

    if nueva_superficie == 0:
        print("ERROR, La superficie debe ser mayor a cero.")
        return paises

    pais_encontrado["poblacion"] = nueva_poblacion
    pais_encontrado["superficie"] = nueva_superficie

    guardar_paises(paises)

    print(
        f"OK, Pais '{pais_encontrado['nombre']}' "
        f"actualizado correctamente."
    )

    return paises
