def inverte(vet):
    if len(vet) == 1:
        return vet
    print(vet[0])
    return inverte(vet[1:]) + [vet[0],]

lista = []
for i in range(100):
    lista.append(i)

print(inverte(lista))