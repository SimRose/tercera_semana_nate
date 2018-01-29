def devolver_pares(lista):
    pares = []
    for numero in lista:
        if numero % 2 == 0:
            pares.append(numero)
    return pares

print(devolver_pares([4, 5, 6, 7]))

