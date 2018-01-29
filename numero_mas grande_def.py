def mas_largo(primero, segundo, tercero):

    while not primero.isdigit():
        primero = input("Introduce el primer numero: ")
    while not segundo.isdigit():
        segundo = input("Introduce el segundo numero: ")
    while not tercero.isdigit():
        tercero = input("Introduce el tercer numero: ")
    if primero >= (segundo and tercero):
        return primero
    elif segundo >= (primero and tercero):
        return segundo
    elif tercero >= (primero and segundo):
        return tercero

numero = mas_largo("", "", "")
print("El numero mas grande es {}".format(numero))
