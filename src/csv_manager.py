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
