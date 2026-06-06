"""
Helpers de validacion de entradas del usuario.

Estas funciones envuelven input() y devuelven None cuando la
entrada es invalida. Quien llama decide que hacer en ese caso.
"""


def pedir_texto_no_vacio(mensaje):
    """
    Pide un texto al usuario y lo devuelve sin espacios al inicio
    o al final. Devuelve None si la entrada queda vacia.
    """

    texto = input(mensaje).strip()

    if not texto:
        print("ERROR: El valor no puede estar vacio.")
        return None

    return texto


def pedir_entero(mensaje):
    """
    Pide un numero entero al usuario.
    Devuelve el entero o None si la entrada no es un numero valido.
    """

    entrada = input(mensaje).strip()

    try:
        return int(entrada)
    except ValueError:
        print("ERROR: Debes ingresar un numero entero.")
        return None


def pedir_entero_no_negativo(mensaje):
    """
    Pide un numero entero mayor o igual a cero.
    Devuelve el entero o None si es invalido o negativo.
    """

    valor = pedir_entero(mensaje)

    if valor is None:
        return None

    if valor < 0:
        print("ERROR: El valor no puede ser negativo.")
        return None

    return valor


def validar_rango(minimo, maximo):
    """
    Valida que minimo y maximo sean enteros no negativos
    y que minimo <= maximo. Devuelve True o False.
    """

    if minimo is None or maximo is None:
        return False

    if minimo < 0 or maximo < 0:
        print("ERROR: Los valores del rango no pueden ser negativos.")
        return False

    if minimo > maximo:
        print("ERROR: El valor minimo no puede ser mayor al maximo.")
        return False

    return True
