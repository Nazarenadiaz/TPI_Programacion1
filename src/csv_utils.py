import csv
import os

# La ruta del CSV se calcula a partir de la ubicacion de este archivo
# para que el programa funcione sin depender del directorio de trabajo.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RUTA_CSV = os.path.join(BASE_DIR, "data", "paises.csv")


def cargar_paises(ruta=RUTA_CSV):
    """
    Lee el archivo CSV y devuelve una lista de paises.
    Cada pais se representa como un diccionario.
    """

    paises = []

    if not os.path.exists(ruta):
        print(f"ERROR, No se encontro el archivo '{ruta}'.")
        return paises

    try:
        with open(ruta, encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)

            for fila in lector:
                if (
                    not fila.get("nombre")
                    or not fila.get("poblacion")
                    or not fila.get("superficie")
                    or not fila.get("continente")
                ):
                    print(f"ADVERTENCIA, Fila incompleta ignorada: {dict(fila)}")
                    continue

                try:
                    pais = {
                        "nombre": fila["nombre"].strip(),
                        "poblacion": int(fila["poblacion"].strip()),
                        "superficie": int(fila["superficie"].strip()),
                        "continente": fila["continente"].strip()
                    }

                    paises.append(pais)

                except ValueError:
                    print(
                        f"ADVERTENCIA, Datos numericos invalidos: {dict(fila)}"
                    )

    except Exception as e:
        print(f"ERROR, Al leer el archivo CSV: {e}")

    return paises


def guardar_paises(paises, ruta=RUTA_CSV):
    """
    Guarda la lista de paises en el archivo CSV.
    """

    try:
        with open(ruta, "w", encoding="utf-8", newline="") as archivo:

            campos = [
                "nombre",
                "poblacion",
                "superficie",
                "continente"
            ]

            escritor = csv.DictWriter(
                archivo,
                fieldnames=campos
            )

            escritor.writeheader()
            escritor.writerows(paises)

        print("OK, Datos guardados correctamente.")

    except Exception as e:
        print(f"ERROR, Al guardar el archivo CSV: {e}")


def agregar_pais(paises, ruta=RUTA_CSV):
    """
    Solicita un nuevo pais, valida los datos y lo agrega
    a la lista si es correcto.
    """

    print("\n-Agregar nuevo pais-")

    nombre = input("Nombre del pais: ").strip()

    if not nombre:
        print("ERROR, El nombre no puede estar vacio.")
        return paises

    for pais in paises:
        if pais["nombre"].lower() == nombre.lower():
            print(f"ERROR, Ya existe un pais llamado '{nombre}'.")
            return paises

    try:
        poblacion = int(input("Poblacion: ").strip())

        if poblacion < 0:
            print("ERROR, La poblacion no puede ser negativa.")
            return paises

    except ValueError:
        print("ERROR, La poblacion debe ser un numero entero.")
        return paises

    try:
        superficie = int(input("Superficie en km²: ").strip())

        if superficie <= 0:
            print("ERROR, La superficie debe ser mayor a cero.")
            return paises

    except ValueError:
        print("ERROR, La superficie debe ser un numero entero.")
        return paises

    continente = input("Continente: ").strip()

    if not continente:
        print("ERROR, El continente no puede estar vacio.")
        return paises

    nuevo_pais = {
        "nombre": nombre,
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": continente
    }

    paises.append(nuevo_pais)

    guardar_paises(paises, ruta)

    print(f"OK, Pais '{nombre}' agregado correctamente.")

    return paises
