def reemplazar(lista, actual, nuevo):
    for i in range(len(lista)):
        if lista[i] in [actual, actual + 1]:
            lista[i] = nuevo
    return lista


lista = [3, 2, 3, 4, 5, 3]
modificada = reemplazar(lista, 3, 2)
print(modificada)

lista2 = [3, 4, 3, 4, 2, 4, 5, 6]
mod = reemplazar(lista2, 3, 2)
print(mod)
