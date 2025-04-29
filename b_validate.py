def validate_number_int(entrada, minimo, maximo):
    valido = True

    if entrada == "":
        valido = False

    for i, caracter in enumerate(entrada):
        if caracter == '-' and i == 0:  
            continue 
        if caracter < '0' or caracter > '9':
            valido = False

    if valido:
        entrada = int(entrada)
        if entrada >= minimo and entrada <= maximo:
            return entrada
        else:
            return "range_error"
    return False

def validate_number_float(entrada, minimo, maximo):
    valido = True
    punto = 0
    
    if entrada == "":
        valido = False

    for i, caracter in enumerate(entrada):
        if caracter == '.':
            punto += 1
        elif caracter == '-' and i == 0:  
            continue
        elif caracter < '0' or caracter > '9':
            valido = False

    if punto > 1:
        valido = False
    if punto != 1:  
        valido = False

    if valido:
        entrada = float(entrada)
        if entrada >= minimo and entrada <= maximo:
            return entrada
        else:
            return "range_error"
    return False

def validate_length(mensaje, longitud):
    if len(mensaje) == longitud:
        return mensaje
    return False