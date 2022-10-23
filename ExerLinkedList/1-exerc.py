class Nodo:
    def __init__(self, value=0, nextValue=None):
        self.value = value
        self.next = nextValue

    def __repr__(self):
        return f"{self.value}, {self.next}"

class ListaEncadeada:
    def __init__(self):
        self.head = None

    def __repr__(self):
        return "[" + str(self.head) + "]"

    def append(self, lista, newValue):
        newValue = Nodo(newValue)
        newValue.next = lista.head
        lista.head = newValue

lista = ListaEncadeada()
lista.append(lista, 3)
lista.append(lista, 6)
lista.append(lista, 9)
lista.append(lista, 12)

print(lista)
