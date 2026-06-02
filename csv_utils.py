import csv
import os

RUTA_CSV = "paises.csv"


def cargar_paises(ruta=RUTA_CSV):
    """
    Lee el archivo CSV y devuelve una lista de países.
    Cada país se representa como un diccionario.
    """

    paises = []

    if not os.path.exists(ruta):
        print(f"[ERROR] No se encontró el archivo '{ruta}'.")
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
                    print(f"[ADVERTENCIA] Fila incompleta ignorada: {dict(fila)}")
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
                        f"[ADVERTENCIA] Datos numéricos inválidos: {dict(fila)}"
                    )

    except Exception as e:
        print(f"[ERROR] Al leer el archivo CSV: {e}")

    return paises


def guardar_paises(paises, ruta=RUTA_CSV):
    """
    Guarda la lista de países en el archivo CSV.
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

        print("[OK] Datos guardados correctamente.")

    except Exception as e:
        print(f"[ERROR] Al guardar el archivo CSV: {e}")


def agregar_pais(paises, ruta=RUTA_CSV):
    """
    Solicita un nuevo país, valida los datos y lo agrega
    a la lista si es correcto.
    """

    print("\n--- Agregar nuevo país ---")

    nombre = input("Nombre del país: ").strip()

    if not nombre:
        print("[ERROR] El nombre no puede estar vacío.")
        return paises

    for pais in paises:
        if pais["nombre"].lower() == nombre.lower():
            print(f"[ERROR] Ya existe un país llamado '{nombre}'.")
            return paises

    try:
        poblacion = int(input("Población: ").strip())

        if poblacion < 0:
            print("[ERROR] La población no puede ser negativa.")
            return paises

    except ValueError:
        print("[ERROR] La población debe ser un número entero.")
        return paises

    try:
        superficie = int(input("Superficie en km²: ").strip())

        if superficie <= 0:
            print("[ERROR] La superficie debe ser mayor a cero.")
            return paises

    except ValueError:
        print("[ERROR] La superficie debe ser un número entero.")
        return paises

    continente = input("Continente: ").strip()

    if not continente:
        print("[ERROR] El continente no puede estar vacío.")
        return paises

    nuevo_pais = {
        "nombre": nombre,
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": continente
    }

    paises.append(nuevo_pais)

    guardar_paises(paises, ruta)

    print(f"[OK] País '{nombre}' agregado correctamente.")

    return paises
