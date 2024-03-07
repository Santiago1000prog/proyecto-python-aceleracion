lista = [3, 2, 3, 4, 5, 3]
valor_a_reemplazar = 3
valor_nuevo = 2

for i in range(6):
    if lista[i] in [3, 4]:
        lista[i] = 2

print(lista)
