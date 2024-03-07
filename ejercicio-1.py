lista = [1, 2, 3, 4, 5, 3]  # len(lista) = 6
valor_a_reemplazar = 3
valor_nuevo = 2

for i in range(6):
    if lista[i] in [3, 4]:  # equivalente a lista[i] == 3 or lista[i] == 4
        lista[i] = 2  # Si es 3 o 4, lo reemplazo por un 2

print(lista)  # [1, 2, 2, 2, 5, 2]
