import b_validate

def get_int(mensaje: str, mensaje_error: str, minimo: int, maximo: int, reintentos: int) -> int | None:
    print(f"Por favor, ingrese un número entero entre {minimo} y {maximo}:")
    contador = 0
    salida = None

    while contador < reintentos:
        entrada = input("Número: ")  
        resultado = b_validate.validate_number_int(entrada, minimo, maximo)
        if resultado is not False and resultado != "range_error":
            salida = resultado
            break
        else:
            print("Error: debe ingresar un número entero válido.") if resultado is False else print(f"Error: el número debe estar entre {minimo} y {maximo}.")
        contador += 1

    if salida is None:
        print("Se agotaron los intentos. No se ingresó un número válido.")
    return salida

def get_float(mensaje: str, mensaje_error: str, minimo: float, maximo: float, reintentos: float) -> float | None:
    print(f"Por favor, ingrese un número decimal entre {minimo} y {maximo}:")
    contador = 0
    salida = None

    while contador < reintentos:
        entrada = input("Número: ")  
        resultado = b_validate.validate_number_float(entrada, minimo, maximo)
        if resultado is not False and resultado != "range_error":
            salida = resultado
            break
        else:
            print("Error: debe ingresar un número decimal válido.") if resultado is False else print(f"Error: el número debe estar entre {minimo} y {maximo}.")
        contador += 1

    if salida is None:
        print("Se agotaron los intentos. No se ingresó un número válido.")
    return salida

def get_string(longitud: int) -> str | None:
    contador = 0
    reintentos = 3
    salida = None
    print(f"Por favor, ingrese los caracteres pedidos ({longitud}): ")

    while contador < reintentos:
        mensaje = input("Ingrese su respuesta: ") 
        resultado = b_validate.validate_length(mensaje, longitud)
        if len(mensaje) == longitud:
            salida = mensaje
            break
        else:
            print(f"Error: la respuesta debe contener la cantidad de ({longitud}) caracteres.")
            contador += 1

    if salida is None:
        print("Se agotaron los intentos. No se ingresó un texto válido.")
    return salida