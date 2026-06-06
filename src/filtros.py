from paises import mostrar_paises


def filtrar_por_continente(paises):
    """
    Muestra los paises pertenecientes al continente ingresado.
    """

    print("\n-Filtrar por continente-")

    continente = input("Ingresa el continente: ").strip()

    if not continente:
        print("ERROR, El continente no puede estar vacio.")
        return

    resultados = []

    for pais in paises:
        if pais["continente"].lower() == continente.lower():
            resultados.append(pais)

    if not resultados:
        print(f"\nNo se encontraron paises en '{continente}'.")
        return

    print(f"\nPaíses en {continente} ({len(resultados)} resultado/s):")
    mostrar_paises(resultados)


def filtrar_por_poblacion(paises):
    """
    Filtra paises segun un rango de poblacion.
    """

    print("\n-Filtrar por rango de poblacion-")

    try:
        minimo = int(input("Poblacion minima: ").strip())
        maximo = int(input("Poblacion maxima: ").strip())

    except ValueError:
        print("ERROR, Debes ingresar numeros enteros.")
        return

    if minimo > maximo:
        print("ERROR, El valor minimo no puede ser mayor al maximo.")
        return

    resultados = [
        pais
        for pais in paises
        if minimo <= pais["poblacion"] <= maximo
    ]

    if not resultados:
        print(
            f"\nNo hay paises con poblacion entre "
            f"{minimo:,} y {maximo:,}."
        )
        return

    print(
        f"\nPaises con poblacion entre "
        f"{minimo:,} y {maximo:,}:"
    )

    mostrar_paises(resultados)


def filtrar_por_superficie(paises):
    """
    Filtra paises segun un rango de superficie.
    """

    print("\n-Filtrar por rango de superficie-")

    try:
        minimo = int(input("Superficie minima (km²): ").strip())
        maximo = int(input("Superficie maxima (km²): ").strip())

    except ValueError:
        print("ERROR, Debes ingresar numeros enteros.")
        return

    if minimo > maximo:
        print("ERROR, El valor minimo no puede ser mayor al maximo.")
        return

    resultados = [
        pais
        for pais in paises
        if minimo <= pais["superficie"] <= maximo
    ]

    if not resultados:
        print(
            f"\nNo hay paises con superficie entre "
            f"{minimo:,} y {maximo:,} km²."
        )
        return

    print(
        f"\nPaises con superficie entre "
        f"{minimo:,} y {maximo:,} km²:"
    )

    mostrar_paises(resultados)
