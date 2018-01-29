def mas_largo(primero, segundo, tercero):
    if primero >= (segundo and tercero):
        return primero
    elif segundo >= (primero and tercero):
        return segundo
    elif tercero >= (primero and segundo):
        return tercero


print(mas_largo(1, 2, 3))
