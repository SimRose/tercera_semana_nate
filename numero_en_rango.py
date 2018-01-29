def numero_en_rango(numero, rango1, rango2):
    if rango1 <= numero <= rango2:
        return True
    else:
        return False

print(numero_en_rango(0, 1, 10))
print(numero_en_rango(4, 1, 100))
